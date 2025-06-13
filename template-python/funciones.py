import subprocess

import paramiko
import os
import time
import re

import variable
import funciones

def ejecutar_comando(comando):
    """
    Ejecuta un comando de Linux y devuelve su salida.

    Args:
        comando: El comando de Linux que se va a ejecutar.

    Returns:
        La salida del comando.
    """
    print(f"\n---Ejecución de comando \"{comando}\"")
    resultado = subprocess.run(comando, shell=True, capture_output=True, text=True)  # shell=True para ejecutarlo como un script
    return resultado.stdout

def crear_security_user1(chan):
    userName        = variable.securityUserName
    userPassword    = variable.securityUserPassword
    userUID         = variable.securityUserUID
    userMaxDaysBetweenChange = variable.securityUserMaxDaysBetweenChange
    userWarnDaysBeforeExpire = variable.securityUserWarnDaysBeforeExpire

    #Esperar prompt
    buff = ''
    resp = ''
    msgPromptSysadmin = f"{variable.usuarioSys}@{variable.hostname}# "
    while msgPromptSysadmin not in buff:
        resp = chan.recv(9999)
        buff = f"{buff}{resp}"
        #print(resp.decode())

    cmd_crear_usuario = f"user add {userName}  password  {userPassword} uid {userUID} role security  max-days-between-change {userMaxDaysBetweenChange} warn-days-before-expire {userWarnDaysBeforeExpire} " 
    print(f"\n---Ejecución de comando \"{cmd_crear_usuario}\"")

    # Ssh and wait for the password prompt.
    time.sleep(1)
    chan.send(cmd_crear_usuario + '\n')

    buff = ''
    resp = ''
    while True:
         resp = chan.recv(9999)
         buff = f"{buff}{resp}"
         print(resp.decode())

         msgCreado = f"User \"{userName}\" added."
         msgExiste = f"**** User \"{userName}\" already exists."
         msgNoAuth = f"****  You are not authorized to add a user account with 'security' role"
         if msgCreado in buff:
              return("El usuario de seguridad ha sido creado correctamente.")
         elif msgExiste in buff:
              return("Ese usuario de seguridad ya existe, no ha sido creado o modificado.")
         elif msgNoAuth in buff:
              return("Un usuario de seguridad se debe crear desde otro usuario de seguridad si existe, que es el caso.")
          
def crear_security_users(userName, userPassword, userUID, chan):    
    #Esperar prompt
    buff = ''
    resp = ''
    msgPromptSecurityuser = f"{variable.securityUserName}@{variable.hostname}> "
    while msgPromptSecurityuser not in buff:
        resp = chan.recv(9999)
        buff = f"{buff}{resp}"
        #print(resp.decode())

    cmd_crear_usuario = f"user add {userName}  password  {userPassword} uid {userUID} role security" 
    print(f"\n---Ejecución de comando \"{cmd_crear_usuario}\"")
    
    # Enviar comando.
    time.sleep(1)
    chan.send(cmd_crear_usuario + '\n')

    buff = ''
    resp = ''
    while True:
         resp = chan.recv(9999)
         buff = f"{buff}{resp}"
         print(resp.decode())

         msgCreado = f"User \"{userName}\" added."
         msgExiste = f"**** User \"{userName}\" already exists."
         msgNoAuth = f"****  You are not authorized to add a user account with 'security' role"
         if msgCreado in buff:
              return("El usuario de seguridad ha sido creado correctamente.")
         elif msgExiste in buff:
              return("Ese usuario de seguridad ya existe, no ha sido creado o modificado.")         
         elif msgNoAuth in buff:
              return("Un usuario de seguridad se debe crear desde otro usuario de seguridad si existe, que es el caso.")

def crear_admin_users(userName, userPassword, userUID, chan):    
    #Esperar prompt
    buff = ''
    resp = ''
    msgPromptSysadmin = f"{variable.usuarioSys}@{variable.hostname}# "
    while msgPromptSysadmin not in buff:
        resp = chan.recv(9999)
        buff = f"{buff}{resp}"
        #print(resp.decode())

    cmd_crear_usuario = f"user add {userName}  password  {userPassword} uid {userUID} role admin" 
    print(f"\n---Ejecución de comando \"{cmd_crear_usuario}\"")
    
    # Enviar comando.
    time.sleep(1)
    chan.send(cmd_crear_usuario + '\n')

    buff = ''
    resp = ''
    while True:
         resp = chan.recv(9999)
         buff = f"{buff}{resp}"
         print(resp.decode())

         msgCreado = f"User \"{userName}\" added."
         msgExiste = f"**** User \"{userName}\" already exists."
         if msgCreado in buff:
              return(f"El usuario {userName} ha sido creado correctamente.")
         elif msgExiste in buff:
              return(f"El usuario {userName} ya existe, no ha sido creado o modificado.")      

def habilitar_security_officer(cmd_habilitar_security_officer, chan):
    buff = ''
    resp = ''
    msgPromptSecurityuser = f"{variable.securityUserName}@{variable.hostname}>"
    while msgPromptSecurityuser not in buff:
        resp = chan.recv(9999)
        buff = f"{buff}{resp}"
        #print(resp.decode())
   
    # Ssh and wait for the password prompt.
    time.sleep(1)
    chan.send(cmd_habilitar_security_officer + '\n')

    buff = ''
    resp = ''
    while True:
         resp = chan.recv(9999)
         buff = f"{buff}{resp}"
         print(resp.decode())

         msgHabilitado = f"Runtime authorization policy has been enabled."
         msgPreviamenteHabilitado = f"Runtime authorization policy is already enabled."
         if msgHabilitado in buff:
              return("OK")
         elif msgPreviamenteHabilitado in buff:
              return("OK")      

def establecer_passphrase(cmd,chan):
    buff = ''
    resp = ''
    msgPromptSysadmin = f"{variable.usuarioSys}@{variable.hostname}# "
    while msgPromptSysadmin not in buff:
        resp = chan.recv(9999)
        buff = f"{buff}{resp}"
        #print(resp.decode())

    cmd_establecer_passphrase = f"{cmd} " 
    
    # Ssh and wait for the password prompt.
    time.sleep(1)
    chan.send(cmd_establecer_passphrase + '\n')

    buff = ''
    resp = ''
    while True:
         resp = chan.recv(9999)
         buff = f"{buff}{resp}"
         print(resp.decode())
         
         msgExiste = f"The system passphrase is already set."
         if msgExiste in buff:
              return("No se ha podido establecer la passphrase, ya existía una.")

         msgPassphrase1 = f"Enter new passphrase: "
         if msgPassphrase1 in buff:
            # Send the password and wait for a prompt.
            time.sleep(1)
            chan.send(variable.passphraseClave + '\n')

            buff = ''
            resp = ''
            while True:
                resp = chan.recv(9999)
                buff = f"{buff}{resp}"
                print(resp.decode())
         
                msgPassphrase2 = f"Re-enter new passphrase: "
                if msgPassphrase2 in buff:
                    # Send the password and wait for a prompt.
                    time.sleep(1)
                    chan.send(variable.passphraseClave + '\n')

                    while True:
                        resp = chan.recv(9999)
                        buff = f"{buff}{resp}"
                        print(resp.decode())
         
                        msgPromptSysadmin = f"{variable.usuarioSys}@{variable.hostname}# "
                        if msgPromptSysadmin in buff:
                            return("La passphrase ha sido establecida correctamente.")

def conectar_a_data_domain(ipDD, usuario, contrasena, cliente):
    ### CONECTAR AL DATA DOMAIN A CONFIGURAR
    try:
        cliente.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        cliente.connect(hostname=ipDD, username=usuario, password=contrasena)
    except paramiko.ssh_exception.AuthenticationException:
        return(f"El usuario {usuario} no pudo conectarse al Data Domain.")
                
    ### Comprobar que estamos en el DD correcto.
    stand_input, stand_output, stand_error = cliente.exec_command('system show serialno')
    resultado = stand_output.read().decode()
    resultadoError = stand_error.read().decode()

    # Buscar el valor en la salida
    valor_a_buscar = variable.serialNumber
    if valor_a_buscar not in resultado:
        #  Realizar alguna acción basada en la búsqueda
        print(f"El DD sobre el que se quiere actuar '{variable.serialNumber}' no coincide con el indicado en el fichero de variables.")
        return(f"NOT OK")
    
    print(f"El usuario {usuario} se ha conectado correctamente al Data Domain.")
    return(f"OK")
    ### FIN CONECTAR AL DATA DOMAIN A CONFIGURAR
           
def licenciar_Data_Domain(chan):
    #Esperar prompt
    buff = ''
    resp = ''
    msgPromptSysadmin = f"{variable.usuarioSys}@{variable.hostname}# "
    while msgPromptSysadmin not in buff:
        resp = chan.recv(9999)
        buff = f"{buff}{resp}"
        #print(resp.decode())

    # Ejecución de comando.
    time.sleep(1)
    cmd = f"elicense update" 
    chan.send(cmd + '\n')

    #Esperar ejecución de comando
    buff = ''
    resp = ''
    while True:
         resp = chan.recv(9999)
         buff = f"{buff}{resp}"
         print(resp.decode())

         msgInicioLic = f"Enter the content of license file and then press Control-D, or press Control-C to cancel."
         if msgInicioLic in buff:
            #Enviar la licencia
            ruta_archivo = f"{variable.licenciaDD}"
            try:
                with open(ruta_archivo, "r") as archivo:
                    # Leer el contenido del archivo
                    contenido = archivo.read()
            except FileNotFoundError:
                print(f"Error: El archivo '{ruta_archivo}' no fue encontrado.")
                contenido = ""  # O cualquier valor que desees si no se encuentra el archivo

            # Enviar el contenido de la licencia.
            time.sleep(1)
            chan.send(contenido + '\n' + '\x04')

            buff = ''
            resp = ''
            while True:
                resp = chan.recv(9999)
                buff = f"{buff}{resp}"
                print(resp.decode())
         
                msgAceptarLic = f"Do you want to proceed? (yes|no) [yes]:"
                if msgAceptarLic in buff:
                    # Enviar "yes" para aceptar la licencia.
                    time.sleep(1)
                    chan.send("yes" + '\n')

                    while True:
                        resp = chan.recv(9999)
                        buff = f"{buff}{resp}"
                        print(resp.decode())
         
                        msgFinOK = f"eLicense(s) updated."
                        if msgFinOK in buff:
                            return("OK")
                        
def send_cmd_shell(cmd,chan):
    #Esperar prompt
    buff = ''
    resp = ''
    msgPromptSysadmin = f"{variable.usuarioSys}@{variable.hostname}# "
    while msgPromptSysadmin not in buff:
        resp = chan.recv(9999)
        buff = f"{buff}{resp}"
        #print(resp.decode())

    # Ejecución de comando.
    print(f"\n---Ejecución de comando \"{cmd}\"")
    time.sleep(1)
    chan.send(cmd + '\n')

    #Esperar ejecución de comando
    buff = ''
    resp = ''
    while True:
         resp = chan.recv(9999)
         buff = f"{buff}{resp}"
         print(resp.decode())

         #Fin de comando OK
         msgPromptSysadmin = f"{variable.usuarioSys}@{variable.hostname}# "
         if msgPromptSysadmin in buff:
              print(f"---Ejecución de comando \"{cmd}\": OK")
              return("OK")
         
         #Se requiere usuario de seguridad.
         msgUsuarioDeSeguridadNecesario = f"This command requires authorization by a user having a 'security' role."
         if msgUsuarioDeSeguridadNecesario in buff and "Username:" in buff:
            # Enviar usuario de seguridad.
            time.sleep(1)
            chan.send(variable.securityUserName + '\n')

            buff = ''
            resp = ''
            while True:
                resp = chan.recv(9999)
                buff = f"{buff}{resp}"
                print(resp.decode())
         
                msgUsuarioDeSeguridadPassword = f"Password:"
                if msgUsuarioDeSeguridadPassword in buff:
                    # Enviar password de seguridad.
                    time.sleep(1)
                    chan.send(variable.securityUserPassword + '\n')

                    buff = ''
                    resp = ''
                    while True:
                        resp = chan.recv(9999)
                        buff = f"{buff}{resp}"
                        print(resp.decode())
                
                        msgPromptSysadmin = f"{variable.usuarioSys}@{variable.hostname}# "
                        if msgPromptSysadmin in buff:
                            print(f"---Ejecución de comando \"{cmd}\": OK")
                            return("OK")
                
def establecer_hora(cmd,chan):
    #Esperar prompt
    buff = ''
    resp = ''
    msgPromptSysadmin = f"{variable.usuarioSys}@{variable.hostname}# "
    while msgPromptSysadmin not in buff:
        resp = chan.recv(9999)
        buff = f"{buff}{resp}"
        #print(resp.decode())

    # Ejecución de comando.
    time.sleep(1)
    chan.send(cmd + '\n')

    #Esperar ejecución de comando
    buff = ''
    resp = ''
    while True:
         resp = chan.recv(9999)
         buff = f"{buff}{resp}"
         print(resp.decode())

         #Fin de comando OK
         msgPromptSysadmin = f"{variable.usuarioSys}@{variable.hostname}# "
         if msgPromptSysadmin in buff:
              return("OK")
         
         #Cambio de hora significativa
         msgCambioSignificativo = f"System date will be adjusted by"
         msgSeguro = f"Are you sure? (yes|no) [no]:"
         if msgCambioSignificativo in buff and msgSeguro in buff:
            # Confirmar cambio horario.
            time.sleep(1)
            chan.send("yes" + '\n')

            buff = ''
            resp = ''
            while True:
                resp = chan.recv(9999)
                buff = f"{buff}{resp}"
                print(resp.decode())
         
                msgPromptSysadmin = f"{variable.usuarioSys}@{variable.hostname}# "
                if msgPromptSysadmin in buff:
                    return("OK")   

def crear_filesystem(chan):
    #Esperar prompt
    buff = ''
    resp = ''
    msgPromptSysadmin = f"{variable.usuarioSys}@{variable.hostname}# "
    while msgPromptSysadmin not in buff:
        resp = chan.recv(9999)
        buff = f"{buff}{resp}"
        #print(resp.decode())

    #Agregar discos a Active tier
    print("\n-Agregar discos a Active tier.")
    cmd_agregar_discos_tierActive = f"storage add tier active {variable.tierActive}"

    #Enviar comando
    time.sleep(1)
    chan.send(cmd_agregar_discos_tierActive + '\n')

    buff = ''
    resp = ''
    while True:
            resp = chan.recv(9999)
            buff = f"{buff}{resp}"
            print(resp.decode())

            msgAgregadoActiveTier = f"successfully added to the active tier"
            msgNoAgregadoActivetier = f"cannot be added"
            msgNoDiscosActivetier = f"does not exist"
            msgPromptSysadmin = f"{variable.usuarioSys}@{variable.hostname}# "
            if msgAgregadoActiveTier in buff and msgPromptSysadmin in buff:
                print(f"-Discos correctamente agregados a Active Tier {variable.tierActive}")
                break
            elif msgNoAgregadoActivetier in buff and msgPromptSysadmin in buff:
                print(f"-Algunos discos no han podido ser agregados a Active Tier")
                break
            elif msgNoDiscosActivetier in buff and msgPromptSysadmin in buff:
                print(f"-Algunos discos no existen y no han podido ser agregados a Active Tier")
                break

    #Agregar discos a Cache Tier
    print("\n-Agregar discos a Cache tier.")
    if variable.tierCache == "":
        print(f"-No hay discos indicados a agregar a Cache tier.")
    else:
        print(f"-Discos a Cache Tier agregados.")

    print("\n-Crear filesystem")
    #Enviar comando
    time.sleep(1)
    chan.send("filesys create" + '\n')

    buff = ''
    resp = ''
    while True:
            resp = chan.recv(9999)
            buff = f"{buff}{resp}"
            print(resp.decode())

            msgNoStorageForFS = f"There is no storage available for creation"
            msgCrearFS = f"Do you want to continue? (yes|no) [yes]:"
            msgFSExist = f"A filesystem already exists"
            msgPromptSysadmin = f"{variable.usuarioSys}@{variable.hostname}# "
            if msgNoStorageForFS in buff and msgPromptSysadmin in buff:
                print(f"-El filesystem no ha podido ser creado por no tener storage disponible para ello.")
                break
            elif msgCrearFS in buff:
                #Enviar "yes"
                time.sleep(1)
                chan.send("yes" + '\n')

                buff = ''
                resp = ''
                while True:
                        resp = chan.recv(9999)
                        buff = f"{buff}{resp}"
                        print(resp.decode())
                        msgPromptSysadmin = f"{variable.usuarioSys}@{variable.hostname}# "
                        if msgPromptSysadmin in buff:
                            print(f"-El filesystem ha sido creado.")
                            break
                break
            elif msgFSExist  in buff and msgPromptSysadmin in buff:
                print(f"-El filesystem ya estaba creado")
                break
    
    print("\n-Habilitar filesystem")
    #Enviar comando
    time.sleep(1)
    chan.send("filesys enable" + '\n')

    buff = ''
    resp = ''
    while True:
            resp = chan.recv(9999)
            buff = f"{buff}{resp}"
            print(resp.decode())

            msgNoExisteFS = f"The filesystem doesn't exist. Create the filesystem and try again"
            msgHabilitadoFS = f"The filesystem is now enabled"
            msgHabilitadoPreviamene = f"The filesystem is already enabled"
            msgPromptSysadmin = f"{variable.usuarioSys}@{variable.hostname}# "
            if msgNoExisteFS in buff and msgPromptSysadmin in buff:
                print(f"-El filesystem no existe y por ello no se ha habilitado.")
                return(f"NOT OK")
            elif msgHabilitadoFS in buff and msgPromptSysadmin in buff:
                print(f"-El filesystem se ha habilitado.")
                return(f"OK")
            elif msgHabilitadoPreviamene in buff and msgPromptSysadmin in buff:
                print(f"-El filesystem ya estaba habilitado.")
                return(f"OK")

def send_restart_filesystem(cmd,chan):
    #Esperar prompt
    buff = ''
    resp = ''
    msgPromptSysadmin = f"{variable.usuarioSys}@{variable.hostname}# "
    while msgPromptSysadmin not in buff:
        resp = chan.recv(9999)
        buff = f"{buff}{resp}"
        #print(resp.decode())

    # Ejecución de comando.
    print(f"\n---Ejecución de comando \"{cmd}\"")
    time.sleep(1)
    chan.send(cmd + '\n')

    #Esperar ejecución de comando
    buff = ''
    resp = ''
    while True:
         resp = chan.recv(9999)
         buff = f"{buff}{resp}"
         print(resp.decode())

         msgRestartFilesystem = f"This action will restart the file system"
         msgSeguroReinicioFS  =  f"Are you sure? (yes|no) [no]"
         if msgRestartFilesystem in buff and msgSeguroReinicioFS in buff:
            # Enviar "yes"
            time.sleep(1)
            chan.send(f"yes" + '\n')

            buff = ''
            resp = ''
            while True:
                resp = chan.recv(9999)
                buff = f"{buff}{resp}"
                print(resp.decode())
         
                msgRestartFilesystem = f"The filesystem is now enabled"
                msgPromptSysadmin    = f"{variable.usuarioSys}@{variable.hostname}# "
                if msgRestartFilesystem in buff and msgPromptSysadmin in buff:
                    # Enviar password de seguridad.
                    print(f"---Ejecución de comando \"{cmd}\": OK")
                    return("OK")
    
def send_encryption_apply_changes(cmd,chan):
    #Esperar prompt
    buff = ''
    resp = ''
    msgPromptSysadmin = f"{variable.usuarioSys}@{variable.hostname}# "
    while msgPromptSysadmin not in buff:
        resp = chan.recv(9999)
        buff = f"{buff}{resp}"
        #print(resp.decode())

    # Ejecución de comando.
    print(f"\n---Ejecución de comando \"{cmd}\"")
    time.sleep(1)
    chan.send(cmd + '\n')

    #Esperar ejecución de comando
    buff = ''
    resp = ''
    while True:
         resp = chan.recv(9999)
         buff = f"{buff}{resp}"
         print(resp.decode())

         msgAplicarCambios = f"This command will apply current encryption configuration to all data"
         msgSeguroAplicarCambios  =  f"Do you want to proceed? (yes|no) [no]"
         if msgAplicarCambios in buff and msgSeguroAplicarCambios in buff:
            #Enviar "yes"
            time.sleep(1)
            chan.send(f"yes" + '\n')

            buff = ''
            resp = ''
            while True:
                resp = chan.recv(9999)
                buff = f"{buff}{resp}"
                print(resp.decode())
                         
                msgPromptSysadmin = f"{variable.usuarioSys}@{variable.hostname}# "
                if msgPromptSysadmin in buff:
                    #Cambios aplicados.
                    print(f"---Ejecución de comando \"{cmd}\": OK")
                    return("OK")
    
def send_encryption_keys_export(cmd,chan):
    #Esperar prompt
    buff = ''
    resp = ''
    msgPromptSysadmin = f"{variable.usuarioSys}@{variable.hostname}# "
    while msgPromptSysadmin not in buff:
        resp = chan.recv(9999)
        buff = f"{buff}{resp}"
        #print(resp.decode())

    # Ejecución de comando.
    print(f"\n---Ejecución de comando \"{cmd}\"")
    time.sleep(1)
    chan.send(cmd + '\n')

    #Esperar ejecución de comando
    buff = ''
    resp = ''
    while True:
         resp = chan.recv(9999)
         buff = f"{buff}{resp}"
         print(resp.decode())
        
         #Se requiere usuario de seguridad.
         msgUsuarioDeSeguridadNecesario = f"This command requires authorization by a user having a 'security' role."
         if msgUsuarioDeSeguridadNecesario in buff and "Username:" in buff:
            # Enviar usuario de seguridad.
            time.sleep(1)
            chan.send(variable.securityUserName + '\n')

            buff = ''
            resp = ''
            while True:
                resp = chan.recv(9999)
                buff = f"{buff}{resp}"
                print(resp.decode())
         
                msgUsuarioDeSeguridadPassword = f"Password:"
                if msgUsuarioDeSeguridadPassword in buff:
                    # Enviar password de seguridad.
                    time.sleep(1)
                    chan.send(variable.securityUserPassword + '\n')

                    buff = ''
                    resp = ''
                    while True:
                        resp = chan.recv(9999)
                        buff = f"{buff}{resp}"
                        print(resp.decode())
                
                        msgPassphraseForFile = f"Enter new passphrase for key export file:"
                        if msgPassphraseForFile in buff:
                            # Enviar passphareForFile.
                            time.sleep(1)
                            chan.send(variable.passphraseForFileEncription + '\n')

                            buff = ''
                            resp = ''
                            while True:
                                resp = chan.recv(9999)
                                buff = f"{buff}{resp}"
                                print(resp.decode())
                        
                                msgRepPassphraseForFile = f"Re-enter new passphrase for key export file"
                                if msgRepPassphraseForFile in buff:
                                    # Enviar passphareForFile.
                                    time.sleep(1)
                                    chan.send(variable.passphraseForFileEncription + '\n')

                                    buff = ''
                                    resp = ''
                                    while True:
                                        resp = chan.recv(9999)
                                        buff = f"{buff}{resp}"
                                        print(resp.decode())
                                                                                
                                        if msgPromptSysadmin in buff:
                                            # #Claves exportadas
                                            time.sleep(1)
                                            
                                            print(f"---Ejecución de comando \"{cmd}\": OK")

                                            cadena_texto = buff.replace("\\r\\n", "  ")
                                            subcadena_a_buscar = "encryption_keys"

                                            # Divide la cadena en palabras
                                            palabras = cadena_texto.split()
                                            # Extrae las palabras que contienen la subcadena
                                            palabras_con_subcadena = [palabra for palabra in palabras if subcadena_a_buscar in palabra]

                                            # Devolver el fichero de claves
                                            fichero_claves = palabras_con_subcadena[0]

                                            return(f"OK", fichero_claves)

def send_clave_ssh(clave_ssh, chan):
    #Esperar prompt
    buff = ''
    resp = ''
    msgPromptSysadmin = f"{variable.usuarioSys}@{variable.hostname}# "
    while msgPromptSysadmin not in buff:
        resp = chan.recv(9999)
        buff = f"{buff}{resp}"
        #print(resp.decode())

    # Ejecución de comando.
    time.sleep(1)
    cmd = f"adminaccess add ssh-keys user sysadmin" 
    print(f"\n---Ejecución de comando \"{cmd}\"")
    chan.send(cmd + '\n')

    #Esperar ejecución de comando
    buff = ''
    resp = ''
    while True:
         resp = chan.recv(9999)
         buff = f"{buff}{resp}"
         print(resp.decode())

         msgClaveSSH = f"Enter the key and then press Control-D, or press Control-C to cancel."
         if msgClaveSSH in buff:
            #Enviar la clave ssh
            ruta_archivo = f"{clave_ssh}"
            try:
                with open(ruta_archivo, "r") as archivo:
                    # Leer el contenido del archivo
                    contenido = archivo.read()
            except FileNotFoundError:
                print(f"Error: El archivo '{ruta_archivo}' no fue encontrado.")
                contenido = ""  # O cualquier valor que desees si no se encuentra el archivo

            # Enviar el contenido de la clave ssh.
            time.sleep(1)
            chan.send(contenido + '\n' + '\x04')

            buff = ''
            resp = ''
            while True:
                resp = chan.recv(9999)
                buff = f"{buff}{resp}"
                print(resp.decode())
         
                msgKeyAccepted = f"SSH Key accepted"
                if msgKeyAccepted in buff and msgPromptSysadmin in buff:
                    # Clave ssh agregada.
                    time.sleep(1)
                    print(f"---Ejecución de comando \"{cmd}\": OK")
                    return("OK")
import paramiko
import os
import time

import variable
import funciones

### CONECTAR AL DATA DOMAIN A CONFIGURAR como SYSADMIN
print("---Conectarse al DD como sysadmin.")
cliente = paramiko.SSHClient()
resultado = funciones.conectar_a_data_domain(variable.ipDD, variable.usuarioSys, variable.passwordSys, cliente)
print(f"---Conectarse al DD como sysadmin: {resultado}")
if resultado == "NOT OK":
    exit()
### FIN CONECTAR AL DATA DOMAIN A CONFIGURAR como SYSADMIN

#########  ENCRIPTACIÓN DE FILESYSTEM     #########
###Ver el estado previo de la configuración para encriptación
print("#####     Ver el estado inicial de la configuración para encriptación de filesystem.")

canal = cliente.invoke_shell()
cmd = f"filesys encryption show"
resultado = funciones.send_cmd_shell(cmd,canal)

canal = cliente.invoke_shell()
cmd = f"filesys encryption embedded-key-manager show"
resultado = funciones.send_cmd_shell(cmd,canal)

canal = cliente.invoke_shell()
cmd = f"filesys encryption keys show summary"
resultado = funciones.send_cmd_shell(cmd,canal)

canal = cliente.invoke_shell()
cmd = f"filesys encryption status"
resultado = funciones.send_cmd_shell(cmd,canal)
###Fin ver el estado previo de la configuración para encriptación

###Realizar la configuración para encriptación de filesystem.
print("#####     Iniciar la configuración para encriptación de filesystem.")

canal = cliente.invoke_shell()
cmd = f"filesys encryption enable"
resultado = funciones.send_cmd_shell(cmd,canal)

canal = cliente.invoke_shell()
cmd = f"filesys restart"
resultado = funciones.send_restart_filesystem(cmd,canal)

canal = cliente.invoke_shell()
cmd = f"filesys encryption embedded-key-manager keys create"
resultado = funciones.send_cmd_shell(cmd,canal)

canal = cliente.invoke_shell()
cmd = f"filesys encryption embedded-key-manager set key-rotation-policy none"
resultado = funciones.send_cmd_shell(cmd,canal)

canal = cliente.invoke_shell()
cmd = f"filesys encryption algorithm set aes_256_cbc"
resultado = funciones.send_cmd_shell(cmd,canal)

canal = cliente.invoke_shell()
cmd = f"filesys restart"
resultado = funciones.send_restart_filesystem(cmd,canal)

canal = cliente.invoke_shell()
cmd = f"filesys encryption apply-changes"
resultado = funciones.send_encryption_apply_changes(cmd,canal)

canal = cliente.invoke_shell()
cmd = f"filesys clean start"
resultado = funciones.send_cmd_shell(cmd,canal)

canal = cliente.invoke_shell()
cmd = f"filesys encryption keys export"
resultado, fichero_claves = funciones.send_encryption_keys_export(cmd,canal)

print(f"Se ha creado el fichero de claves: {fichero_claves}. Debe ser recuperado y guardado en lugar seguro.")

### RECUPERAR EL FICHERO DE CLAVES
### ENVIAR CLAVE SSH
canal = cliente.invoke_shell()
resultado = funciones.send_clave_ssh(variable.clave_ssh, canal)
### FIN ENVIAR CLAVE SSH

#########  RECUPERAR EL FICHERO DE CLAVES
cmd = f"scp {variable.usuarioSys}@{variable.ipDD}:{fichero_claves}  /home/alonsl/DPS-DD-config/template-python"
resultado = funciones.ejecutar_comando(cmd)
#########  FIN RECUPERAR EL FICHERO DE CLAVES

###Fin realizar la configuración para encriptación de filesystem.


###Ver el estado final de la configuración para encriptación
print("#####     Ver el estado final de la configuración para encriptación de filesystem.")

canal = cliente.invoke_shell()
cmd = f"filesys encryption show"
resultado = funciones.send_cmd_shell(cmd,canal)

canal = cliente.invoke_shell()
cmd = f"filesys encryption embedded-key-manager show"
resultado = funciones.send_cmd_shell(cmd,canal)

canal = cliente.invoke_shell()
cmd = f"filesys encryption keys show summary"
resultado = funciones.send_cmd_shell(cmd,canal)

canal = cliente.invoke_shell()
cmd = f"filesys encryption status"
resultado = funciones.send_cmd_shell(cmd,canal)
###Fin ver el estado final de la configuración para encriptación

#########  FIN ENCRIPTACIÓN DE FILESYSTEM     #####

cliente.close()


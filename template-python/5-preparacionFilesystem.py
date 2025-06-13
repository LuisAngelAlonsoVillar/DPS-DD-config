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

#########     CREACIÓN DE FILESYSTEM     #########
print("\n#####     Inicio preparación de filesystem.")

canal = cliente.invoke_shell()
print(f"\n---Crear y habilitar el filesystem")
resultado = funciones.crear_filesystem(canal)
print(f"\n---Crear y habilitar el filesystem: {resultado}")

print("\n#####     Fin preparación de filesystem.")
#########  FIN CREACIÓN DE FILESYSTEM     #########

#########  REVISION CIFS           #########
print("\n#####     Revisión CIFS.")
canal = cliente.invoke_shell()
cmd = f"cifs status"
resultado = funciones.send_cmd_shell(cmd,canal)

canal = cliente.invoke_shell()
cmd = f"cifs option show all"
resultado = funciones.send_cmd_shell(cmd,canal)

canal = cliente.invoke_shell()
cmd = f"cifs option set restrict-anonymous enabled"
resultado = funciones.send_cmd_shell(cmd,canal)

canal = cliente.invoke_shell()
cmd = f"cifs option show all"
resultado = funciones.send_cmd_shell(cmd,canal)

canal = cliente.invoke_shell()
cmd = f"cifs disable"
resultado = funciones.send_cmd_shell(cmd,canal)
print("\n#####     Fin revisión CIFS.")
#########  FIN REVISION CIFS       #########

#########  REVISION NFS            #########
print("\n#####     Inicio revisión NFS.")

canal = cliente.invoke_shell()
cmd = f"nfs status"
resultado = funciones.send_cmd_shell(cmd,canal)

canal = cliente.invoke_shell()
cmd = f"nfs option show all"
resultado = funciones.send_cmd_shell(cmd,canal)

print("\n#####     Fin revisión NFS.")
#########  FIN REVISION NFS        #########

#########  REVISION DDBOOST        #########
print("\n#####     Inicio revisión ddboost.")

canal = cliente.invoke_shell()
cmd = f"ddboost status"
resultado = funciones.send_cmd_shell(cmd,canal)

canal = cliente.invoke_shell()
cmd = f"ddboost enable"
resultado = funciones.send_cmd_shell(cmd,canal)

canal = cliente.invoke_shell()
cmd = f"ddboost file-replication option show"
resultado = funciones.send_cmd_shell(cmd,canal)

canal = cliente.invoke_shell()
cmd = f"ddboost option show"
resultado = funciones.send_cmd_shell(cmd,canal)


canal = cliente.invoke_shell()
cmd = f"ddboost option set global-authentication-mode none global-encryption-strength high"
resultado = funciones.send_cmd_shell(cmd,canal)

canal = cliente.invoke_shell()
cmd = f"ddboost option show"
resultado = funciones.send_cmd_shell(cmd,canal)

print("\n#####     Fin revisión ddboost.")
#########  FIN REVISION DDBOOST    #########


cliente.close()


import paramiko
import os
import time

import variable
import funciones
import scp

### CONECTAR AL DATA DOMAIN A CONFIGURAR como SYSADMIN
print("---Conectarse al DD como sysadmin.")
cliente = paramiko.SSHClient()
resultado = funciones.conectar_a_data_domain(variable.ipDD, variable.usuarioSys, variable.passwordSys, cliente)
print(f"---Conectarse al DD como sysadmin: {resultado}")
if resultado == "NOT OK":
    exit()
### FIN CONECTAR AL DATA DOMAIN A CONFIGURAR como SYSADMIN

### ENVIAR CLAVE SSH
canal = cliente.invoke_shell()
resultado = funciones.send_clave_ssh(variable.clave_ssh, canal)
### FIN ENVIAR CLAVE SSH

#########  FIN ENCRIPTACIÓN DE FILESYSTEM     #####
cmd = f""
def ejecutar_comando(cmd):
#########  FIN ENCRIPTACIÓN DE FILESYSTEM     #####





cliente.close()


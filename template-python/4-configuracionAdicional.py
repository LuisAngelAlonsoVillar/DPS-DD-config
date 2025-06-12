import paramiko
import os
import time

import variable
import funciones

### CONECTAR AL DATA DOMAIN A CONFIGURAR como SYSADMIN
print("---Conectarse al DD como sysadmin.")
cliente = paramiko.SSHClient()
resultado = funciones.conectar_a_data_domain(variable.ipDD, variable.usuarioSys, variable.passwordSys, cliente)
print(f"---{resultado}")
### FIN CONECTAR AL DATA DOMAIN A CONFIGURAR como SYSADMIN

#########     CONFIGURACION ADICIONAL          #########
print("\n#####     Inicio configuración adicional.")

print("\n#####     Creando usuarios adicionales.")
### CREAR USUARIO SYSADMIN ADICIONAL
print(f"\n---Crear usuario sysadmin adicional: {variable.admAdicionalName}")
canal = cliente.invoke_shell()
resultado = funciones.crear_admin_users(variable.admAdicionalName, variable.admAdicionalPassword, variable.admAdicionalUID, canal)
print(f"---{resultado}")
### FIN CREAR USUARIO SYSADMIN ADICIONAL
### CREAR USUARIO emc
print(f"\n---Crear usuario emc: {variable.emcUserName}")
canal = cliente.invoke_shell()
resultado = funciones.crear_admin_users(variable.emcUserName, variable.emcUserPassword, variable.emcUserUID, canal)
print(f"---{resultado}")
### FIN CREAR USUARIO emc

### CREAR USUARIO DE SEGURIDAD ADICIONAL
### CONECTAR AL DATA DOMAIN A CONFIGURAR como securityUser
print("---Conectarse al DD como securityUser.")
clienteSecurity = paramiko.SSHClient()
resultado = funciones.conectar_a_data_domain(variable.ipDD, variable.securityUserName, variable.securityUserPassword, clienteSecurity)
print(f"---{resultado}")

print(f"\n---Crear usuario de seguridad adicional: {variable.securityUserAdicionalName}")
canalSecurity = clienteSecurity.invoke_shell()
resultado = funciones.crear_security_users(variable.securityUserAdicionalName, variable.securityUserAdicionalPassword, variable.securityUserAdicionalUID, canalSecurity)
print(f"---{resultado}")
### FIN CREAR USUARIO DE SEGURIDAD ADICIONAL
print("\n#####     Fin de creación de usuarios adicionales.")

######### FIN CONFIGURACION ADICIONAL          #########

cliente.close()


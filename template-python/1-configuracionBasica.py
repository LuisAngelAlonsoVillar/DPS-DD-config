import paramiko
import os
import time
import datetime

import variable
import funciones

### CONECTAR AL DATA DOMAIN A CONFIGURAR como SYSADMIN
print("---Conectarse al DD como sysadmin.")
cliente = paramiko.SSHClient()
resultado = funciones.conectar_a_data_domain(variable.ipDD, variable.usuarioSys, variable.passwordSys, cliente)
print(f"---{resultado}")
### FIN CONECTAR AL DATA DOMAIN A CONFIGURAR como SYSADMIN

### Establecer el hostname
print("\n#####     Iniciar la configuración básica.")
print("#####     Establecer el hostname.")

canal = cliente.invoke_shell()
cmd = f"net set hostname {variable.hostname}"
print(f"\n---Ejecución de comando \"{cmd}\"")
resultado = funciones.send_cmd_shell(cmd,canal)
print(f"---Ejecución de comando \"{cmd}\": {resultado}")
### FIN Establecer el hostname

#########	CONFIGURACIÓN BÁSICA	#########
### CREAR EL USUARIO DE SEGURIDAD
print("#####     Crear el usuario de seguridad.")
canal = cliente.invoke_shell()
resultado = funciones.crear_security_user1(canal)
print(f"---{resultado}")
### FIN CREAR EL USUARIO DE SEGURIDAD

### CREAR LA PASSPHRASE
print("#####     Establecer la passphrase.")
canal = cliente.invoke_shell()
cmd = f"system passphrase set"
print(f"\n---Ejecución de comando \"{cmd}\"")
resultado = funciones.establecer_passphrase(cmd,canal)
print(f"---{resultado}")

print("#####     Establecer longitud mínima de passphrase.")
canal = cliente.invoke_shell()
cmd = f"system passphrase option set min-length {variable.passphraseMinLength}"
print(f"\n---Ejecución de comando \"{cmd}\"")
resultado = funciones.send_cmd_shell(cmd,canal)
print(f"---Ejecución de comando \"{cmd}\": {resultado}")


### FIN CREAR LA PASSPHRASE

### ESTABLECER SECURITY OFFICER
### CONECTAR AL DATA DOMAIN A CONFIGURAR como securityUser
print("#####     Establecer la oficina de seguridad.")
print("---Conectarse al DD como securityUser.")
clienteSecurity = paramiko.SSHClient()
resultado = funciones.conectar_a_data_domain(variable.ipDD, variable.securityUserName, variable.securityUserPassword, clienteSecurity)
print(f"---{resultado}")
### FIN CONECTAR AL DATA DOMAIN A CONFIGURAR como securityUser

canalSecurity = clienteSecurity.invoke_shell()
cmd = f"authorization policy set security-officer enabled"
print(f"\n---Ejecución de comando \"{cmd}\"")
resultado = funciones.habilitar_security_officer(cmd, canalSecurity)
print(f"---Ejecución de comando \"{cmd}\": {resultado}")

clienteSecurity.close()
### FIN ESTABLECER SECURITY OFFICER

### Establecer el domainname
print("#####     Establecer el domainname.")

canal = cliente.invoke_shell()
cmd = f"net set domainname {variable.domainname}"
print(f"\n---Ejecución de comando \"{cmd}\"")
resultado = funciones.send_cmd_shell(cmd,canal)
print(f"---Ejecución de comando \"{cmd}\": {resultado}")
### FIN Establecer el domainname

### Establecer el timezone
print("#####     Establecer el timezone.")

canal = cliente.invoke_shell()
cmd = f"config set timezone {variable.timezone}"
print(f"\n---Ejecución de comando \"{cmd}\"")
resultado = funciones.send_cmd_shell(cmd,canal)
print(f"---Ejecución de comando \"{cmd}\": {resultado}")
### FIN Establecer el timezone

### Establecer la hora
print("#####     Establecer la hora.")

canal = cliente.invoke_shell()
cmd = f"ntp disable"
print(f"\n---Ejecución de comando \"{cmd}\"")
resultado = funciones.send_cmd_shell(cmd,canal)
print(f"---Ejecución de comando \"{cmd}\": {resultado}")

hora_actual = datetime.datetime.now()
hora_formateada = hora_actual.strftime('%m%d%H%M')

canal = cliente.invoke_shell()
cmd = f"system set date {hora_formateada}"
print(f"\n---Ejecución de comando \"{cmd}\"")
resultado = funciones.establecer_hora(cmd,canal)
print(f"---Ejecución de comando \"{cmd}\": {resultado}")

canal = cliente.invoke_shell()
cmd = f"ntp enable"
print(f"\n---Ejecución de comando \"{cmd}\"")
resultado = funciones.send_cmd_shell(cmd,canal)
print(f"---Ejecución de comando \"{cmd}\": {resultado}")
### FIN Establecer la hora

### Establecer el timeserver
print("#####     Establecer el timeserver.")

canal = cliente.invoke_shell()
cmd = f"ntp reset timeservers"
print(f"\n---Ejecución de comando \"{cmd}\"")
resultado = funciones.send_cmd_shell(cmd,canal)
print(f"---Ejecución de comando \"{cmd}\": {resultado}")

canal = cliente.invoke_shell()
cmd = f"ntp add timeserver {variable.timeserver}"
print(f"\n---Ejecución de comando \"{cmd}\"")
resultado = funciones.send_cmd_shell(cmd,canal)
print(f"---Ejecución de comando \"{cmd}\": {resultado}")
### FIN Establecer el timeserver

### Establecer el location
print("#####     Establecer el location.")

canal = cliente.invoke_shell()
cmd = f"config set location \"{variable.location}\""
print(f"\n---Ejecución de comando \"{cmd}\"")
resultado = funciones.send_cmd_shell(cmd,canal)
print(f"---Ejecución de comando \"{cmd}\": {resultado}")
### FIN Establecer el location

### Establecer el dns
print("#####     Establecer el dns.")

canal = cliente.invoke_shell()
cmd = f"net set dns {variable.dns}"
print(f"\n---Ejecución de comando \"{cmd}\"")
resultado = funciones.send_cmd_shell(cmd,canal)
print(f"---Ejecución de comando \"{cmd}\": {resultado}")
### FIN Establecer el dns

### Establecer el mailserver
print("#####     Establecer el mailserver.")

canal = cliente.invoke_shell()
cmd = f"config set mailserver {variable.mailserver}"
print(f"\n---Ejecución de comando \"{cmd}\"")
resultado = funciones.send_cmd_shell(cmd,canal)
print(f"---Ejecución de comando \"{cmd}\": {resultado}")
### FIN Establecer el mailserver

### Establecer el adminEmail
print("#####     Establecer el adminEmail.")

canal = cliente.invoke_shell()
cmd = f"config set admin-email {variable.adminEmail}"
print(f"\n---Ejecución de comando \"{cmd}\"")
resultado = funciones.send_cmd_shell(cmd,canal)
print(f"---Ejecución de comando \"{cmd}\": {resultado}")
### FIN Establecer el adminEmail

### Establecer el alertSummary
print("#####     Establecer el alertSummary.")

canal = cliente.invoke_shell()
cmd = f"autosupport reset alert-summary"
print(f"\n---Ejecución de comando \"{cmd}\"")
resultado = funciones.send_cmd_shell(cmd,canal)
print(f"---Ejecución de comando \"{cmd}\": {resultado}")

canal = cliente.invoke_shell()
cmd = f"autosupport add alert-summary emails {variable.alertSummary}"
print(f"\n---Ejecución de comando \"{cmd}\"")
resultado = funciones.send_cmd_shell(cmd,canal)
print(f"---Ejecución de comando \"{cmd}\": {resultado}")
### FIN Establecer el alertSummary

### Establecer el asupDetailed
print("#####     Establecer el asupDetailed.")

canal = cliente.invoke_shell()
cmd = f"autosupport reset asup-detailed"
print(f"\n---Ejecución de comando \"{cmd}\"")
resultado = funciones.send_cmd_shell(cmd,canal)
print(f"---Ejecución de comando \"{cmd}\": {resultado}")

canal = cliente.invoke_shell()
cmd = f"autosupport add asup-detailed emails {variable.asupDetailed}"
print(f"\n---Ejecución de comando \"{cmd}\"")
resultado = funciones.send_cmd_shell(cmd,canal)
print(f"---Ejecución de comando \"{cmd}\": {resultado}")
### FIN Establecer el asupDetailed

#########	FIN CONFIGURACIÓN BÁSICA	#########

cliente.close()


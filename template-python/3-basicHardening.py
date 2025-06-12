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

#########     BASIC HARDENING          #########
print("\n#####     Inicio Basic Hardening.")

### Establecer Password aging
# Ver configuración actual
print("#####     Password aging. Ver configuración actual.")

canal = cliente.invoke_shell()
cmd = f"user password aging option show"
print(f"\n---Ejecución de comando \"{cmd}\"")
resultado = funciones.send_cmd_shell(cmd,canal)
print(f"---Ejecución de comando \"{cmd}\": {resultado}")
canal = cliente.invoke_shell()
cmd = f"user password aging show sysadmin"
print(f"\n---Ejecución de comando \"{cmd}\"")
resultado = funciones.send_cmd_shell(cmd,canal)
print(f"---Ejecución de comando \"{cmd}\": {resultado}")

# Establecer nuevos valores
print("#####     Password aging. Establecer nuevos valores.")

canal = cliente.invoke_shell()
cmd = f"user password aging option set min-days-between-change {variable.minDaysBetweenChange} max-days-between-change {variable.maxDaysBetweenChange} warn-days-before-expire  {variable.warnDaysBeforeExpire} disable-days-after-expire {variable.disableDaysAfterExpire}"
print(f"\n---Ejecución de comando \"{cmd}\"")
resultado = funciones.send_cmd_shell(cmd,canal)
print(f"---Ejecución de comando \"{cmd}\": {resultado}")
canal = cliente.invoke_shell()
cmd = f"user password aging set sysadmin max-days-between-change {variable.sysadminMaxDaysBetweenChange} warn-days-before-expire  {variable.sysadminUserWarnDaysBeforeExpire}"
print(f"\n---Ejecución de comando \"{cmd}\"")
resultado = funciones.send_cmd_shell(cmd,canal)
print(f"---Ejecución de comando \"{cmd}\": {resultado}")

# Ver configuración final
print("#####     Password aging. Ver configuración final.")

canal = cliente.invoke_shell()
cmd = f"user password aging option show"
print(f"\n---Ejecución de comando \"{cmd}\"")
resultado = funciones.send_cmd_shell(cmd,canal)
print(f"---Ejecución de comando \"{cmd}\": {resultado}")
canal = cliente.invoke_shell()
cmd = f"user password aging show sysadmin"
print(f"\n---Ejecución de comando \"{cmd}\"")
resultado = funciones.send_cmd_shell(cmd,canal)
print(f"---Ejecución de comando \"{cmd}\": {resultado}")
### FIN Establecer Password aging

### Establecer Password strength
# Ver configuración actual
print("#####     Password strength. Ver configuración final.")

canal = cliente.invoke_shell()
cmd = f"user password strength show"
print(f"\n---Ejecución de comando \"{cmd}\"")
resultado = funciones.send_cmd_shell(cmd,canal)
print(f"---Ejecución de comando \"{cmd}\": {resultado}")

# Establecer nuevos valores
print("#####     Password strength. Establecer nuevos valores.")

canal = cliente.invoke_shell()
cmd = f"user password strength set min-length {variable.minLength} min-one-lowercase {variable.minOneLowercase} min-one-uppercase {variable.minOneUppercase} min-one-digit {variable.minOneDigit} min-one-special {variable.minOneSpecial} max-three-repeat {variable.maxThreeRepeat} passwords-remembered {variable.passwordsRemembered} min-positions-changed {variable.minPositionsChanged} dictionary-match {variable.dictionaryMatch}"
print(f"\n---Ejecución de comando \"{cmd}\"")
resultado = funciones.send_cmd_shell(cmd,canal)
print(f"---Ejecución de comando \"{cmd}\": {resultado}")

# Ver configuración final
print("#####     Password strength. Ver configuración final.")

canal = cliente.invoke_shell()
cmd = f"user password strength show"
print(f"\n---Ejecución de comando \"{cmd}\"")
resultado = funciones.send_cmd_shell(cmd,canal)
print(f"---Ejecución de comando \"{cmd}\": {resultado}")
### FIN Establecer Password strength

### Establecer Password lock and hash
# Ver configuración actual
print("#####     Password lock. Ver configuración actual.")

canal = cliente.invoke_shell()
cmd = f"adminaccess option show"
print(f"\n---Ejecución de comando \"{cmd}\"")
resultado = funciones.send_cmd_shell(cmd,canal)
print(f"---Ejecución de comando \"{cmd}\": {resultado}")

# Establecer nuevos valores
print("#####     Password lock. Establecer nuevos valores.")

canal = cliente.invoke_shell()
cmd = f"adminaccess option set login-max-attempts {variable.loginMaxAttempts}"
print(f"\n---Ejecución de comando \"{cmd}\"")
resultado = funciones.send_cmd_shell(cmd,canal)
print(f"---Ejecución de comando \"{cmd}\": {resultado}")

canal = cliente.invoke_shell()
cmd = f"adminaccess option set login-unlock-timeout {variable.loginUnlockTimeout}"
print(f"\n---Ejecución de comando \"{cmd}\"")
resultado = funciones.send_cmd_shell(cmd,canal)
print(f"---Ejecución de comando \"{cmd}\": {resultado}")

canal = cliente.invoke_shell()
cmd = f"adminaccess option set password-hash {variable.passwordHashAlgorithm}"
print(f"\n---Ejecución de comando \"{cmd}\"")
resultado = funciones.send_cmd_shell(cmd,canal)
print(f"---Ejecución de comando \"{cmd}\": {resultado}")

# Ver configuración final
print("#####     Password lock. Ver configuración final.")

canal = cliente.invoke_shell()
cmd = f"adminaccess option show"
print(f"\n---Ejecución de comando \"{cmd}\"")
resultado = funciones.send_cmd_shell(cmd,canal)
print(f"---Ejecución de comando \"{cmd}\": {resultado}")
### FIN Establecer Password lock and hash

### Establecer Adminaccess protocols & timeout
# Ver configuración actual
print("#####     Adminaccess protocols & timeout. Ver configuración actual.")

canal = cliente.invoke_shell()
cmd = f"adminaccess show"
print(f"\n---Ejecución de comando \"{cmd}\"")
resultado = funciones.send_cmd_shell(cmd,canal)
print(f"---Ejecución de comando \"{cmd}\": {resultado}")

# Establecer nuevos valores
print("#####     Adminaccess protocols & timeout. Establecer nuevos valores.")

canal = cliente.invoke_shell()
cmd = f"adminaccess disable telnet"
print(f"\n---Ejecución de comando \"{cmd}\"")
resultado = funciones.send_cmd_shell(cmd,canal)
print(f"---Ejecución de comando \"{cmd}\": {resultado}")

canal = cliente.invoke_shell()
cmd = f"adminaccess disable ftp"
print(f"\n---Ejecución de comando \"{cmd}\"")
resultado = funciones.send_cmd_shell(cmd,canal)
print(f"---Ejecución de comando \"{cmd}\": {resultado}")

canal = cliente.invoke_shell()
cmd = f"adminaccess disable ftps"
print(f"\n---Ejecución de comando \"{cmd}\"")
resultado = funciones.send_cmd_shell(cmd,canal)
print(f"---Ejecución de comando \"{cmd}\": {resultado}")

canal = cliente.invoke_shell()
cmd = f"adminaccess disable http"
print(f"\n---Ejecución de comando \"{cmd}\"")
resultado = funciones.send_cmd_shell(cmd,canal)
print(f"---Ejecución de comando \"{cmd}\": {resultado}")

canal = cliente.invoke_shell()
cmd = f"adminaccess ssh option set session-timeout {variable.sshSessionTimeout}"
print(f"\n---Ejecución de comando \"{cmd}\"")
resultado = funciones.send_cmd_shell(cmd,canal)
print(f"---Ejecución de comando \"{cmd}\": {resultado}")

canal = cliente.invoke_shell()
cmd = f"adminaccess web option set session-timeout {variable.webSessionTimeout}"
print(f"\n---Ejecución de comando \"{cmd}\"")
resultado = funciones.send_cmd_shell(cmd,canal)
print(f"---Ejecución de comando \"{cmd}\": {resultado}")

# Ver configuración final
print("#####     Adminaccess protocols & timeout. Ver configuración final.")

canal = cliente.invoke_shell()
cmd = f"adminaccess show"
print(f"\n---Ejecución de comando \"{cmd}\"")
resultado = funciones.send_cmd_shell(cmd,canal)
print(f"---Ejecución de comando \"{cmd}\": {resultado}")
### FIN Establecer Adminaccess protocols & timeout

######### FIN BASIC HARDENING          #########

cliente.close()


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

#########     BASIC HARDENING          #########
print("\n#####     Inicio Basic Hardening.")

### Establecer Password aging
# Ver configuración actual
print("#####     Password aging. Ver configuración actual.")

canal = cliente.invoke_shell()
cmd = f"user password aging option show"
resultado = funciones.send_cmd_shell(cmd,canal)

canal = cliente.invoke_shell()
cmd = f"user password aging show sysadmin"
resultado = funciones.send_cmd_shell(cmd,canal)

# Establecer nuevos valores
print("#####     Password aging. Establecer nuevos valores.")

canal = cliente.invoke_shell()
cmd = f"user password aging option set min-days-between-change {variable.minDaysBetweenChange} max-days-between-change {variable.maxDaysBetweenChange} warn-days-before-expire  {variable.warnDaysBeforeExpire} disable-days-after-expire {variable.disableDaysAfterExpire}"
resultado = funciones.send_cmd_shell(cmd,canal)

canal = cliente.invoke_shell()
cmd = f"user password aging set sysadmin max-days-between-change {variable.sysadminMaxDaysBetweenChange} warn-days-before-expire  {variable.sysadminUserWarnDaysBeforeExpire}"
resultado = funciones.send_cmd_shell(cmd,canal)

# Ver configuración final
print("#####     Password aging. Ver configuración final.")

canal = cliente.invoke_shell()
cmd = f"user password aging option show"
resultado = funciones.send_cmd_shell(cmd,canal)

canal = cliente.invoke_shell()
cmd = f"user password aging show sysadmin"
resultado = funciones.send_cmd_shell(cmd,canal)
### FIN Establecer Password aging

### Establecer Password strength
# Ver configuración actual
print("#####     Password strength. Ver configuración final.")

canal = cliente.invoke_shell()
cmd = f"user password strength show"
resultado = funciones.send_cmd_shell(cmd,canal)

# Establecer nuevos valores
print("#####     Password strength. Establecer nuevos valores.")

canal = cliente.invoke_shell()
cmd = f"user password strength set min-length {variable.minLength} min-one-lowercase {variable.minOneLowercase} min-one-uppercase {variable.minOneUppercase} min-one-digit {variable.minOneDigit} min-one-special {variable.minOneSpecial} max-three-repeat {variable.maxThreeRepeat} passwords-remembered {variable.passwordsRemembered} min-positions-changed {variable.minPositionsChanged} dictionary-match {variable.dictionaryMatch}"
resultado = funciones.send_cmd_shell(cmd,canal)

# Ver configuración final
print("#####     Password strength. Ver configuración final.")

canal = cliente.invoke_shell()
cmd = f"user password strength show"
resultado = funciones.send_cmd_shell(cmd,canal)
### FIN Establecer Password strength

### Establecer Password lock and hash
# Ver configuración actual
print("#####     Password lock. Ver configuración actual.")

canal = cliente.invoke_shell()
cmd = f"adminaccess option show"
resultado = funciones.send_cmd_shell(cmd,canal)

# Establecer nuevos valores
print("#####     Password lock. Establecer nuevos valores.")

canal = cliente.invoke_shell()
cmd = f"adminaccess option set login-max-attempts {variable.loginMaxAttempts}"
resultado = funciones.send_cmd_shell(cmd,canal)

canal = cliente.invoke_shell()
cmd = f"adminaccess option set login-unlock-timeout {variable.loginUnlockTimeout}"
resultado = funciones.send_cmd_shell(cmd,canal)

canal = cliente.invoke_shell()
cmd = f"adminaccess option set password-hash {variable.passwordHashAlgorithm}"
resultado = funciones.send_cmd_shell(cmd,canal)

# Ver configuración final
print("#####     Password lock. Ver configuración final.")

canal = cliente.invoke_shell()
cmd = f"adminaccess option show"
resultado = funciones.send_cmd_shell(cmd,canal)
### FIN Establecer Password lock and hash

### Establecer Adminaccess protocols & timeout
# Ver configuración actual
print("#####     Adminaccess protocols & timeout. Ver configuración actual.")

canal = cliente.invoke_shell()
cmd = f"adminaccess show"
resultado = funciones.send_cmd_shell(cmd,canal)

# Establecer nuevos valores
print("#####     Adminaccess protocols & timeout. Establecer nuevos valores.")

canal = cliente.invoke_shell()
cmd = f"adminaccess disable telnet"
resultado = funciones.send_cmd_shell(cmd,canal)

canal = cliente.invoke_shell()
cmd = f"adminaccess disable ftp"
resultado = funciones.send_cmd_shell(cmd,canal)

canal = cliente.invoke_shell()
cmd = f"adminaccess disable ftps"
resultado = funciones.send_cmd_shell(cmd,canal)

canal = cliente.invoke_shell()
cmd = f"adminaccess disable http"
resultado = funciones.send_cmd_shell(cmd,canal)

canal = cliente.invoke_shell()
cmd = f"adminaccess ssh option set session-timeout {variable.sshSessionTimeout}"
resultado = funciones.send_cmd_shell(cmd,canal)

canal = cliente.invoke_shell()
cmd = f"adminaccess web option set session-timeout {variable.webSessionTimeout}"
resultado = funciones.send_cmd_shell(cmd,canal)

# Ver configuración final
print("#####     Adminaccess protocols & timeout. Ver configuración final.")

canal = cliente.invoke_shell()
cmd = f"adminaccess show"
resultado = funciones.send_cmd_shell(cmd,canal)
### FIN Establecer Adminaccess protocols & timeout

######### FIN BASIC HARDENING          #########

cliente.close()


import os

ipDD =          "192.168.227.130"
serialNumber =  "AUDVX8NBKMFEUP"
usuarioSys =       "sysadmin"
passwordSys =      "D3ll.3MC.1234567"

###CONFIGURACIÓN BÁSICA
hostname =          "cmdtc060"

#Adding security user
#Inicializado más abajo

#Set system passphrase
passphraseClave     =   "Dell.EMC.passphrase.1234567"
passphraseMinLength = "15"

domainname =        "luis.com"

timezone =          "Europe/Madrid"
timeserver =        "22.17.160.1"

location =          "Luis Angel CPD"
dns =               "22.0.0.2"
mailserver =        "23.1.36.173"
adminEmail =        "adminEmail@luis.com"
alertSummary =      "alertasSumary@luis.com"
asupDetailed =      "asupMail@luis.com"
###FIN CONFIGURACIÓN BÁSICA

###LICENCIAR EL DD
public_key = "/home/alonsl/.ssh/id_rsa.pub"
licenciaDD = f"{os.environ.get("PWD")}/licencia.lic"
###FIN LICENCIAR EL DD

### BASIC HARDENING
#Password aging
minDaysBetweenChange	= "1"
maxDaysBetweenChange	= "90"
warnDaysBeforeExpire	= "15"
disableDaysAfterExpire	= "never"
#Change sysadmin password aging
sysadminMaxDaysBetweenChange    = maxDaysBetweenChange
sysadminUserWarnDaysBeforeExpire    = warnDaysBeforeExpire
#Change securityUser password aging
securityUserMaxDaysBetweenChange    = maxDaysBetweenChange
securityUserWarnDaysBeforeExpire    = warnDaysBeforeExpire


#Password strength
minLength			= "15"
minOneLowercase	    = "enabled"
minOneUppercase	    = "enabled"
minOneDigit		    = "enabled"
minOneSpecial		= "enabled"
maxThreeRepeat		= "enabled"
passwordsRemembered	= "8"
minPositionsChanged	= "3"
dictionaryMatch	    = "enabled"

#Password
loginMaxAttempts	= "5"
loginUnlockTimeout	= "300"
passwordHashAlgorithm = "sha512"

#adminaccess protocols timeout
sshSessionTimeout	= "1800"
webSessionTimeout	= "1800"
### FIN BASIC HARDENING

### CONFIGURACION ADICIONAL

### Usuarios adicionales
#Adding security user1
securityUserName        = "securityuser"
securityUserPassword    = "D3ll.3MC.security.1234567"
securityUserUID         = "600"
#Adding another admin user"
admAdicionalName		=  "sysadmin2"
admAdicionalPassword	= "D3ll.3MC.sysadmin2.1234567"
admAdicionalUID			=  "601"
#Adding emc user
emcUserName		= "emcuser"
emcUserPassword	= "D3ll.3MC.emcuser.1234567"
emcUserUID 		= "602"
#Adding another sec user
securityUserAdicionalName		=  "securityuser2"
securityUserAdicionalPassword	=  "D3ll.3MC.securityuser2.1234567"
securityUserAdicionalUID		=  "603"
### FIN CONFIGURACION ADICIONAL

### PREPARACIÓN DE FILESYSTEM
#Opciones para lo siguiente:
#   enclosures <enclosure-list  #Por ejemplo: enclosures 2:1 2:2 3:1
#   disks <disk-list>           #Por ejemplo: disks 2.1 2.3 2.4 2.5 
#   <LUN-list>                  #Por ejemplo: "dev3,dev4,dev5 spindle-group 1"
#el comando será:   f"storage add tier active {tierActive}"
#el comando será:   f"storage add tier cache {tierCache}"
tierActive  = f"dev3 spindle-group 1"
tierCache   = f""
### FIN PREPARACIÓN DE FILESYSTEM

### ENCRIPTACIÓN DE FILESYSTEM
tierActive  = f"dev3 spindle-group 1"
tierCache   = f""
### FIN ENCRIPTACIÓN DE FILESYSTEM
passphraseForFileEncription     =   "Dell.EMC.passphrase.1234567"
clave_ssh = "/home/alonsl/.ssh/id_rsa.pub"
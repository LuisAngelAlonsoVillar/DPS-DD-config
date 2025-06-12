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

#########	LICENCIAR EL DD	#########
print("\n#####     Licenciamiento del Data Domain.")

canal = cliente.invoke_shell()
resultado = funciones.licenciar_Data_Domain(canal)
print(f"Resultado de licenciamiento del Data Domain \"{variable.hostname}\": {resultado}")
#########	LICENCIAR EL DD	#########

cliente.close()


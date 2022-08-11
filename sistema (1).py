import getpass
from json import loads

def cadastro():
  print("-="*20,"\n")

cadastro()
print(" ")
cadastro()

while True:
	print("(1) login\n(2) cadastro\n(3) desativar conta\n(4) consultar usuários\n(5) sair")
	r = int(input("R: "))
	
	if (r == 5):
		break

	if (r == 4):
		cadastros_leitura = []
		with open("licaocursOnline.txt") as f:
			cadastros_leitura = f.readlines()

		cadastros = []
		for cadastro in cadastros_leitura:
			cadastro = str(cadastro).replace("\'", "\"")
			cadastros.append(loads(cadastro))

		keys = []
		for cadastro in cadastros:
			keys.append(list(cadastro.keys())[0])
			
		print("\nusuários ativos: " + ", ".join(keys) + "\n")

	if (r == 3):
		while True:

			cadastros_leitura = []
			with open("licaocursOnline.txt") as f:
				cadastros_leitura = f.readlines()
			
			cadastros = []
			for cadastro in cadastros_leitura:
				cadastro = str(cadastro).replace("\'", "\"") 
				cadastros.append(loads(cadastro)) 
				
			entradalogin = str(input('\ninfome o login: '))
			
			for cadastro in cadastros:
				try:
					if cadastro[entradalogin]:
						cadastros.remove({entradalogin: cadastro[entradalogin]})

						with open("licaocursOnline.txt", "w") as f:
							for cadastro in cadastros:
								f.write(str(cadastro) + "\n")

						print("\nusuário desativado\n")
						
						break
				except:
					if cadastros.index(cadastro) == len(cadastros) - 1:
						print("\nusuário incorreto\n")
			
			break
			
	
	if (r == 2):
		login = str(input("\ncrie seu login: ")) 
		senha = getpass.getpass("defina uma senha de acesso: ")
		
		while True:
			
			senha2 = getpass.getpass("confime sua senha: ")
		
			if senha2 == senha:
				usuario = {login: senha}
		
				with open("licaocursOnline.txt", "a") as f:
					f.write(str(usuario) + "\n")
				
				print("\nCadastro realizado com sucesso.\n")
		
				break
				
			else:
				continue

	if (r == 1):
		while True:
			
			cadastros_leitura = []
			with open("licaocursOnline.txt") as f:
				cadastros_leitura = f.readlines()
			
			cadastros = []
			for cadastro in cadastros_leitura:
				cadastro = str(cadastro).replace("\'", "\"") 
				cadastros.append(loads(cadastro)) 

			entradalogin = str(input('\ninfome seu login: '))
			entradasenha = getpass.getpass('senha de acesso: ')

			for cadastro in cadastros:
				login = list(cadastro.keys())[0]
				
				try:
					senha = cadastro[entradalogin]
					
					if (entradalogin == login and entradasenha == senha):
						print('\nusuario {} logado'.format(login))

						break
				
					elif (entradasenha != senha):
						print('senha incorreta, tente novamente\n')
	
						break
						
				except:
					if (cadastros.index(cadastro) == len(cadastros) - 1):
						print('\nusuário inexistente\n')
					
			break

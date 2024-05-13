from os import system
from getpass import getpass
from time import sleep
from colorama import init, Fore
import stdiomask 

init(autoreset = True)

def exibir_menu():
  print(Fore.GREEN +'''
    Bem-vindo ao sistema de login
          
    navegue através do menu abaixo:
    [1] Cadastrar novo usuario
    [2] Efetuar login
    [3] sair 
          ''')

  opcao = int(input('Digite a opção que deseja:'))
  return (opcao)

def fazer_login():
  login = input (' Digite seu nome de usuario:')
  senha = stdiomask.getpass(prompt ='senha', mask='*')
  return(login,senha)
  

def cadastro():
  nome = input('Digite se nome completo:')
  user = input (' Digite seu nome de usuario:')
  senha = input(' Digite sua senha ')
  with open('usuarios.txt', 'a', encoding='utf-8', newline='') as arquivo:
        arquivo.write(f'{user} {senha}\n')

def sair():
  exibir_menu()

def buscar_usuario(login,senha):
   usuarios = []
   try:
      with open('usuarios.txt','r+', encoding='Utf-8',  newline='') as arquivo:
         for linha in arquivo:
            linha = linha.strip(",")
            usuarios.append(linha.split())

            for usuario in usuarios:

             nome = usuario[0]
             password = usuario[1]
            if login == nome and senha == password:
             return True
   except FileNotFoundError:
      return False
   
   



while True:
  system('cls')
  opcao = exibir_menu()

  if opcao == 1:
      login, senha = fazer_login()
      if login == senha:
          print(Fore.YELLOW+'sua senha deve ser diferente do login:')
          senha = getpass('senha: ')
      user = buscar_usuario(login,senha)

      if user:
         print(Fore.RED + 'usuario ja existe!')
         sleep(2)
      
      else:
         with open('usuarios.txt','+a', encoding='Utf-8', newline ='') as arquivo: 
            arquivo.write(f'{login} {senha} \n')
         print(Fore.CYAN + 'Cadastro aprovado!')
         
         exibir_menu()
      


  elif opcao == 2:
     login,senha = fazer_login()
     user = buscar_usuario(login,senha)
     if user == True:
        print(Fore.CYAN + 'login realizado com sucesso:')
        sleep(1)
        exit()
     else:
        system('cls')
        print(Fore.RED+ 'Voce deve ter digitado nome de usuario oua senha errado!')
        sleep(2)
  else:
     system('cls')
     print(Fore.LIGHTMAGENTA_EX+ ' GoodBay!')
     break
      













 





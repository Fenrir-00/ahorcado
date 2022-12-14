 #!/bin/env python3
import sys
from sys import *
import os as termux
from os import *
import time
import random
while True:
 try:
  from lolpython import lol_py
  break
 except ModuleNotFoundError:
  os.system("pip install lolpython")
class color:
    morado = '\033[95m'
    blanco = '\033[97m'
    cyan = '\033[96m'
    azul  = '\033[94m'
    verde = '\033[92m'
    amarillo = '\033[93m'
    rojo = '\033[91m'
    fin = '\033[0m'


AHORCADO = ["""
      +---+
      |   |
          |
          |
          |
          |
    =========""", """
      +---+
      |   |
      O   |
          |
          |
          |
    =========""", """
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========""", """
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========""", """
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========""", """
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========""", """
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    ========="""]
def ganar():
 banner()
 print("")
 print(f"{color.amarillo} ...............GANASTE ERES LIBRE..............")
 print(f"{color.verde}")
 print("      O   ")
 print("     /|\  ")
 print("     / \  ")
 time.sleep(1)
 termux.system("clear")
 banner()
 print("")
 print(f"{color.amarillo} ...............GANASTE ERES LIBRE..............")
 print(f"{color.verde}")
 print("          O   ")
 print("         /|\  ")
 print("         / \  ")
 time.sleep(1)
 termux.system("clear")
 banner()
 print("")
 print(f"{color.amarillo} ...............GANASTE ERES LIBRE..............")
 print(f"{color.verde}")
 print("              O   ")
 print("             /|\  ")
 print("             / \  ")
 time.sleep(1)
 termux.system("clear")
 banner()
 print("")
 print(f"{color.amarillo} ...............GANASTE ERES LIBRE..............")
 print(f"{color.verde}")
 print("                  O   ")
 print("                 /|\  ")
 print("                 / \  ")
 time.sleep(1)
 termux.system("clear")
 banner()
 print("")
 print(f"{color.amarillo} ...............GANASTE ERES LIBRE..............")
 print(f"{color.verde}")
 print("                      O   ")
 print("                     /|\  ")
 print("                     / \  ")
 time.sleep(1)
 termux.system("clear")
 banner()
 print("")
 print(f"{color.amarillo} ...............GANASTE ERES LIBRE..............")
 print(f"{color.verde}")
 print("                          O   ")
 print("                         /|\  ")
 print("                         / \  ")
 time.sleep(1)
 termux.system("clear")
 banner()
 print("")
 print(f"{color.amarillo} ...............GANASTE ERES LIBRE..............")
 print(f"{color.verde}")
 print("                              O   ")
 print("                             /|\  ")
 print("                             / \  ")
 time.sleep(1)
 termux.system("clear")
 banner()
 print("")
 print(f"{color.amarillo} ...............GANASTE ERES LIBRE..............")
 print(f"{color.verde}")
 print("                                  O   ")
 print("                                 /|\  ")
 print("                                 / \  ")
 time.sleep(1)
 termux.system("clear")
 banner()
 print("")
 print(f"{color.amarillo} ...............GANASTE ERES LIBRE..............")
 print(f"{color.verde}")
 print("                                      O   ")
 print("                                     /|\  ")
 print("                                     / \  ")
def banner():
 termux.system("clear")
 print(f"""{color.cyan}

███╗   ███╗██╗   ██╗███████╗██████╗ ███████╗████████╗██╗  ██╗
████╗ ████║██║   ██║██╔════╝██╔══██╗██╔════╝╚══██╔══╝╚██╗██╔╝
██╔████╔██║██║   ██║█████╗  ██████╔╝█████╗     ██║    ╚███╔╝
██║╚██╔╝██║██║   ██║██╔══╝  ██╔══██╗██╔══╝     ██║    ██╔██╗
██║ ╚═╝ ██║╚██████╔╝███████╗██║  ██║███████╗   ██║   ██╔╝╚██╗
╚═╝     ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝╚══════╝   ╚═╝   ╚═╝  ╚═╝{color.fin}""")
 texto ="""
 |=======================================================|
 | Script by              : #FENRIR-00                   |
 | Version                : Version  2.1                 |
 | Follow me on Github    : https://github.com/Fenrir-00 |
 | Contact me on Telegram : @Ritorito1990                |
 ========================================================= """
 lol_py(texto)

def baile():
 print(f"{color.rojo}")
 termux.system("clear")
 banner()
 print(f"{color.rojo}")
 print(AHORCADO[0])
 time.sleep(1)
 termux.system("clear")
 banner()
 print(f"{color.rojo}")
 print(AHORCADO[1])
 time.sleep(1)
 termux.system("clear")
 banner()
 print(f"{color.rojo}")
 print(AHORCADO[2])
 time.sleep(1)
 termux.system("clear")
 banner()
 print(f"{color.rojo}")
 print(AHORCADO[3])
 time.sleep(1)
 termux.system("clear")
 banner()
 print(f"{color.rojo}")
 print(AHORCADO[4])
 time.sleep(1)
 termux.system("clear")
 banner()
 print(f"{color.rojo}")
 print(AHORCADO[5])
 time.sleep(1)
 termux.system("clear")
 banner()
 print(f"{color.rojo}")
 print(AHORCADO[6])
 time.sleep(1)
 termux.system("clear")
 print(f"{color.fin}")
def ahorcado():
 palabras = ['remolque','subrayador','supermercado','murcielago','cafeteria','orangutan','biblioteca','macarrones','loteria','dientes','vacaciones','influencer','edredon','radiador','colores','primavera','parapentista','humo','medicina','espejo','mochila','hielo','microfono','pelota','muñeca','telefono','literatura','principios','elegancia','avion','hierro','automovil', 'periscopio','medallista','dinero','muerdago', 'alimentacion','leire','mayi','daniel','patxi','murcielago','pedrusco','tarjeta','estufa','televisor','zapatilla', 'chimenea','informatica','matematico','princesa','constitucion','constructora','edificacion','antilope','almohada','cerrajero','prismatico','alfarero']
 palabrasecreta = (random.choice(palabras))
 vidas=0
 ahor=0
 solucion=""
 letrasacertadas=""
 fallos=""
 while 7 > vidas:
  banner()
  print(f"{color.rojo}")
  print(AHORCADO[ahor])
  print(f"{color.fin}")
  print(f"{color.rojo}................PALABRAS FALLADAS: "+(fallos))
  print(f"{color.fin}")
  print(solucion)
  print("")
  var2=input(f"{color.cyan}introduce una letra>>>{color.fin}")
  if var2 in palabrasecreta:
   solucion=""
   letrasacertadas = letrasacertadas+ str(var2)
   for i  in palabrasecreta:
    if i in letrasacertadas:
     solucion = solucion+i
    else:
     solucion = solucion+(" _")
   if solucion == palabrasecreta:
    ganar()
    print(f"{color.cyan}....QUIERES JUGAR OTRA VEZ....")
    print("[1] Si")
    print("[2] NO")
    jugar=input(">>>>>>>")
    if jugar == "1":
     ahorcado()
    break
  else:  
   fallos = fallos+str(var2)
   vidas+=1
   ahor+=1
 if vidas == 7:
  print("perdiste")
  print(palabrasecreta)
baile()
banner()
ahorcado()


from ascii_magic import AsciiArt
import pywhatkit as kt
import pyfiglet

print("-------------------WELCOME TO ASCII ART--------------------")
print("Ascii text choose 1")
print("Ascii 3D art choose 2")
print("Ascii image choose 3")
option=int(input("Select Any one option "))
if option==1:
   T = input("Enter Text you want to convert to ASCII art : ")
   ASCII_art_1 = pyfiglet.figlet_format(T)
   print(ASCII_art_1)
elif option==2:
  U = input("Enter Text you want to convert to 3D ASCII art : ")
  ASCII_art_1 = pyfiglet.figlet_format(U,font='isometric1')
  print(ASCII_art_1)
else:
  my_art = AsciiArt.from_url('https://github.com/Iam-Sherlock/Python-in-a-nushell/assets/53529867/cece5244-7595-4972-8a84-ae16a16fa63b')
  my_art.to_terminal()
  
  

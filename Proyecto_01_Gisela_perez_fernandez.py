import os
import pygame
# Declaramos las variables
vidas =int(3)
planetas_explorados = int(0)
opcion = int(0)
controlador = bool(False)
gemas = bool(False)

# Variables de gemas
gema1 = False
gema2 = False
gema3 = False

# Variables de los nombres de los planetas
planeta1 = "Marte"
planeta2 = "Venus"
planeta3 = "Júpiter"

#Imagen Titulo
print('''

                                                                                                    
                                                                                                    
               ██     ██            █████            █████████ █        █   ████          ██        
              ████    ██      █   ██    █   ███     ████ ██    ██      ██  █████████     ████       
             ██ ███   ██     ██  ██         ███     ██   ██   ███     ███  ███    ███   ██ ███      
            ███  ██   ██     █   ██        ████     ██   ██   ██      ██   ███    ██   ██   ██      
            ██   ██   ██    ██  ██ █████   ██ ██    █    ██   ██      ██   ██  ██      ██   ██      
           ██  █████  ██   ██   ███        ██ ███   █   ██    ██     ███   ███        ██  ████      
         █████   ██    ██ ██    ██        ██   ██  ██   ██     ██   ███    ████     █████   ██      
          ██     ██    ████     █       █ ██    ██ █    ██     ███ █ ██    █  ███    ██     ██      
         ██      ██     ██      ████████  █      ███    ██      ███  ██   ██    ██████      ██      
         █       █                       ██                                        ██       █       
                                                                                                    
                                                                                                    
                                                                                                    
                                                                                                    
                                                                                                    
                                                                                                    
              ██████     ████ █████          ██          ████    ██     ███      ██                 
             ██       █████    ██ ███      ██████     ███   ██  ███    █████    ███                 
            ██       ██        ██   ███    ██ ███    ██     ██  ██    ███ ███   ███                 
           ███       ███       ██    ██   ██   ██   ██     ██   ██    ██   █    ██                  
           ██ █████   ███     ██     ██  ██    ██  ██      ██   ██   ██    ██   ██                  
           ██           ███   ██   ███  █████████  ██          ██   ████████   ██                   
           █             ███  █████    ████    ██  ██          ██  ███     █   ██                   
           █      ██     ██████         █      ██  ███       █ ██  ██      █   ██    █              
           ██████    ████     █        █       █    ████████   ██  █       █   █████                
                              █        █                          ██                                
                                                                                                    
                                                                                                    
                                                                                                    
                                                                                                    
                                                                                                    
                                                                                                    

''')
input()
os.system('cls')


# Mensaje informativo inicial

print('''  
        
 o            o
  \          /
   \        /
    :-'""'-:
 .-'  ____  `-.
( (  (_()_)  ) )
 `-.   ^^   .-'
    `._==_.'
     __)(___
      
      ''')

#historia


print("==============================================================================================")
print("Bienvenido capitán,Indicame su nombre,por favor: ")
nombre=input()
print(f"{nombre},eres el encargado de salvar tu planeta,")
print('''¿Comoo?,¿no te han informado del desastre que puede haber si no lo consigues?
Bueno,no me queda otra opción tendre que informarte.

Los humanos hace unos años descubrieron un sistema solar oculto lleno de maravillosos planetas.
      
A lo largo de los años fuisteis invadiendo nuestros planetas,robando nuestras apreciadas gemas 
y luego dejandolas tiradas en otros planetas distintos. 
      
Capitán si no quieres que ocurra una catastrofe, visita los otros 3 planetas y recolectalas. ''')
print("==============================================================================================")

input()
os.system('cls')

#explicación basica del juego

print('''====================================================
Cada gema está custodiada en un planeta diferente,
y para obtenerla,deberás resolver un desafío 
matemático planteado por los Guardianes de los
Planetas. 
Sin embargo, los Guardianes son estrictos: si 
fallas,te quitarán una vida y no obtendrás la gema.

Comienzas la misión con 3 vidas. Si pierdes todas,tu 
nave será destruida y el universo perderá su última
esperanza.
Pero si logras recolectar las 3 gemas, ¡tu misión 
será un éxito y habrás salvado a tu mundo!
¡Buena suerte!
==================================================''')
input()
os.system('cls')  # limpiar pantalla

# Imprimimos las estadísticas iniciales
## INSERTAR IMAGEN
print('''                                                                                                    
                                                                                                    
                                                                                                    
        ▓▓▓▒        ▓▓▓▓▓                  ▓▓▓░        ▓▓▓▓▒                 ▒▓▓▓        ▒▓▓▓▓      
     ▓▓▓▓▓▓▓▓▓▒   ▓▓▓▓▓▓▓▓▓             ▓▓▓▓▓▓▓▓▓   ▒▓▓▓▓▓▓▓▓▓             ▓▓▓▓▓▓▓▓▓   ▓▓▓▓▓▓▓▓▓▓   
    ▓▓▓▓▓▓▓▓▓▓▓▓ ▓▓▓▓▓▓▓▓▓▓▓           ▓▓▓▓▓▓▓▓▓▓▓▓ ▓▓▓▓▓▓▓▓▓▓▓          ▒▓▓▓▓▓▓▓▓▓▓▓ ▓▓▓▓▓▓▓▓▓▓▓▓  
    ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓         ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓          ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓  
    ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░          ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓          ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓  
     ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒           ░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓            ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓   
      ▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓               ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓               ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒    
        ░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒                  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                   ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓      
           ▓▓▓▓▓▓▓▓▓▓▓░                       ▓▓▓▓▓▓▓▓▓▓▓                       ▓▓▓▓▓▓▓▓▓▓▓▓        
              ▓▓▓▓▓▓                            ▒▓▓▓▓▓▓                            ▓▓▓▓▓▓▒          
                ▓▓                                 ▓▓                                ▓▓░            
                                                                                                    
                                                                                                    
                                                                                                    
                                                                                                    
                                                                                                     ''')

print("=======================")
print("Estadísticas iniciales:")
print("=======================")
print(f"Vidas: {vidas}")
print(f"Planetas explorados: {planetas_explorados}")
print("=======================")
input()
os.system('cls')

# Bucle principal del juego

while vidas > 0 and gemas == False:

    # Mostrar menú de selección de planeta
    ## INSERTAR IMAGEN
    print('''                                                                                                    
                                                                                                    
                                                                          ░░░░░░░                   
           ░░░▒▒▒▒▒▒▒░░                    ░░░▒░░▒░░░░                ░░░▒▒▒▒▒▒▓▓▓▒░░               
         ░▒▒▓▒▓▒▒▒▒▒▒▒▒▒░░              ░░▒▒▒▒▒▓▓▒▒░░▒▒░            ░░░░▒▒▒▓▓▓▓▓▓▓██▒░              
        ░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░            ░░▒▓▓▒▒▒▒▒░░░░░░░▒          ░░▒▒▒▒░▒▒▒▒▒▓▓▓███▓░             
       ░▓▓▓▒▓▓▓▓▒▒▒▒▒▒▒▒▒▓▒░          ░▒▒░░░░░░░▒▒▓▓▓▓▓▓▓▒         ░▒▒░░░▒▒▒▒▓▓▓▓▓▓▓██▒░            
      ░▒▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░        ░░▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▒▒▒░        ░▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓██▓░            
      ░▒▒▒▒▒▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒░░        ░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░        ░▒▓▓▒▒▒▒▒░░░▒▒▒▓███▒░            
       ░▒▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒░          ░▓▓▓▒▒▒▒▒▒▒▒░░░▒▒▒▒▒         ░▒▒▒▒░░░▒▒▒▒▒▓▓▓███░░            
       ░▒▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▓▒░░          ░░▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▒░         ░░░░▒▒▒▒▒▒▒▒▓▓▓██▓░░             
         ░▒▓▓▓▓▓▓▓▓▓▓▓▓▓▒░              ░▒▓▓▓▓▓▓▒▒▒▒▒▒▒░             ░░▒▒▓▓▓▓▓▓▓██▓▒░               
           ░░▒▒▒▓▓▓▒▒▒░░                  ░░░▒▒▒▒▒░░░░░                ░░░░▒▒▒▒▒░░░                 
              ░░░░░░░                                                                               
                                                                                                    
              MARTE                          VENUS                        JÚPITER                
                                                                                                    
                                                                                                    ''')
    
    print("==============================")
    print("\n¿A qué planeta quieres ir?")
    print("1. Planeta Marte")
    print("2. Planeta Venus")
    print("3. Planeta Júpiter")
    print("4. Salir del juego")
    print("==============================")
    
    # selección de planeta
    opcion = int(input("Por favor, selecciona una opción (1-4): "))
    os.system('cls')


    # opción seleccionada
    if opcion == 1:
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load("musica/aterrizaje.mp3")
        pygame.mixer.music.play(loops=0)
        if gema1 == False:
            print(f"¡Vamos a {planeta1}!")
            pregunta = "¿Cuánto es 3+5?"
            respuesta_correcta = 8
        else:
            controlador = True

    elif opcion == 2: 
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load("musica/aterrizaje.mp3")
        pygame.mixer.music.play(loops=0)
        if gema2 == False:
            print(f"¡Vamos a {planeta2}!")
            pregunta = "¿Cuánto es 7-4?"
            respuesta_correcta = 3
            
        else:
            controlador = True

    elif opcion == 3:
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load("musica/aterrizaje.mp3")
        pygame.mixer.music.play(loops=0)
        if gema3 == False:
            print(f"¡Vamos a {planeta3}!")
            pregunta = "¿Cuánto es 6*2?"
            respuesta_correcta = 12
            
        else:
            controlador=True

    elif opcion == 4:
        print("¡Hasta la próxima!")
        break

    else:
        print("Opción no válida o planeta ya visitado.")
        
    # Seleccionar planeta
    if 1 <= opcion <= 3:
        if controlador == False:
            print(f"Pregunta del NPC: {pregunta}")
            respuesta_introducida = int(input("Ingresa tu respuesta: "))

            if respuesta_introducida == respuesta_correcta:
                pygame.init()
                pygame.mixer.init()
                pygame.mixer.music.load("musica/ganargema.mp3")
                pygame.mixer.music.play(loops=0)
                print("¡Correcto! Has ganado una gema.")
                #insertar imagen 
                print('''                                                                                                    
                                                                                                    

                                                                                                    
                                                                                                    
                                          █████████████████                                         
                                         ████   ██ ░█    █ █                                        
                                        █   ████     ████   █                                       
                                       ░██▒████░█████▓███████▒                                      
                                         ░█   █▓      █   ██                                        
                                           ██  █░ ░  █  ██                                          
                                             █  █   █  █▒                                           
                                              ██░█ ████                                             
                                                █████                                               
                                                  █                                                 
                                                                                                    
                                                                                                    
                                                                                                    ''')
                
                if opcion == 1:
                    gema1 = True
                elif opcion == 2:
                    gema2 = True
                elif opcion == 3:
                    gema3 = True
                input()
                os.system('cls')
                
            else:
                pygame.init()
                pygame.mixer.init()
                pygame.mixer.music.load("musica/gameover.mp3")
                pygame.mixer.music.play(loops=0)
                print("Incorrecto. Has perdido una vida.")
                vidas -= 1
                ## INSERTAR IMAGEN
                print('''
                                                                                                    
                                                                                                     
                                                                                                    
                                   ░▓▓▓▓▓▓░      ░░░                                                
                                  ░▓█▓█▓█▓░   ░▓▓▓▓▓▓▓░                                             
                                  ▓▓▓▓▓█▓▓▓   ▒▓█▓█▓█▓▓░                                            
                                  ░▓█▓█▓▓█▓░  ░▓▓▓▓▓▓▓▓░                                            
                                   ░▓▓▓█▓▓▓▒ ░▓▓█▓█▓█▓░                                             
                                     ▓▓▓█▓▓ ░▓▓▓▓▓▓█▒                                               
                                       ▓▓▓▒░▓▓█▓█▓░                                                 
                                        ░▒▓▒▓▓▒░                                                    
                                                                                                         
                                                                                                    
                                                                                                      ''')
                
                input()
                os.system('cls')

            planetas_explorados += 1
        else:
            print("Planeta ya visitado")
            controlador = False

# Verificar si se han recolectado todas las gemas
    if gema1 == True and gema2 == True and gema3 == True:
        gemas = True  # Todas las gemas recolectadas

# Fin del juego
if vidas == False:
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load("musica/gameover.mp3")
    pygame.mixer.music.play(loops=0)
    #Insertar imagen 
    print('''                                                                                                    
                                                                                                    
                                                                                                    
                                                                                                    
  
                                                                                                    
                                                                                                    
             ░▓▓▓█▓▓▒     ░▒▒▒░         ▒▓▓▓█▓▓░     ░▒▒▒░         ▒▓█▓▓█▓░     ▒▒▒▒░               
            ░▓▓█▓▓█▓░    ▓▓█▓▓█▓▒      ▒▓▓█▓▓▓▓    ░▓▓▓▓▓▓▓░      ▓▓▓▓█▓▓▒    ▒▓▓▓▓█▓▓░             
            ▒▓▓▓█▓▓▓▓▒   ▓▓▓█▓▓▓█░     ▒█▓▓█▓█▓▓░  ░▓█▓█▓█▓▓░     █▓█▓▓█▓█▒   ▒█▓█▓▓█▓▓             
             ▓▓█▓█▓█▓░  ░▓▓▓▓█▓▓▓░     ░▓█▓▓▓▓█▓░  ▒▓▓▓▓▓▓▓▓░     ░█▓█▓▓▓▓▒  ░▒▓▓▓█▓▓█▒             
              ▓▓▓▓▓▓▓▓░ ▓▓█▓▓▓█▓░       ░▓▓█▓█▓▓▓ ░▓▓█▓█▓█▓░       ░▓▓█▓█▓▓▒ ░▓▓█▓▓█▓▓              
               ░▓█▓█▓░░▓▓▓▓█▓▓▒           ▒▓▓▓█▓ ▒▓█▓▓▓▓▓▒           ▒▓▓▓█░ ▒▓▓▓▓█▓▓░               
                 ░▓▓▓░▓▓█▓▓▒░               ▒▓▓▓░▓▓▓█▓▒░              ░▒▓▓░▒█▓█▓▓▒░                 
                   ░▒▓▓▓░░                    ░▓▒▓▒░                     ▒▓▓▓▒░                     
                                                                                                    
                                                                                                    
                                                                                                    
 
                                                                                                    
                                                                                                    
                                                                                                    ''')
    print("Te has quedado sin vidas, ¡Hasta la próxima!")
# Mostrar estadísticas finales

if gemas == True:
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load("musica/ganarjuego.mp3")
    pygame.mixer.music.play(loops=0)
    
    ## INSERTAR IMAGEN
    print('''                                                                                                    
                                                                                                    
                                                                                                 
                                                                                                    
                                                                                                    
                                                                                                    
                                                                                                    
             ████████████████            ▒████████████████            ▒████████████████             
            █▒█   ▒█  █    █ █          ██ █   ██  █    █ █          ████   ██  █    █ █            
          ██   █ █      █ █   █        ██  ░███     ░█▓█   █▓       ██  ██ █     ▒███   █           
          ██▒██▒███████▒████████       ██▓██████████▒████████       ██░█▓░█▒█████▒███████▒          
            █    █      █   ░█           █   ▒█      █   ██           █    █      █   ██            
             ██  ██    █▒  █              ██  ██    █  ▒█              ██  ██    █   █              
               ██ █▒  ▒█ ██                 ██ █   ██ ██                 █  █   ██ █                
                 █▒█  █ █                    ██ █  █░█                     ███  █▓█                 
                  ▒████                        █████                        ██▒██                   
                    █                            █▓                           █                     
                                                                                                    
                                                                                                    
                                                                                                    
                                                                                                    
                                                                                                    
                                                                                                    
                                                                                                    ''')
    
    print("¡Felicidades! Has recolectado las 3 gemas y ganado el juego.")
    
    
    #Mostrar estadísticas finales
    print("==============================================")
    print("Estadísticas finales:")
    print(f"Vidas restantes: {vidas}")
    print(f"Planetas explorados: {planetas_explorados}")
    print("==============================================")

    print("Has completado la misión,¡hasta la próxima!")
    print('''                   <>
        .-"""-.       ||::::::==========
       /= ___  \      ||::::::==========
      |- /~~~\  |     ||::::::==========
      |=( '.' ) |     ||================
      \__\_=_/__/     ||================
       {_______}      ||================
     /` *       `'--._||
    /= .     [] .     { >
   /  /|ooo     |`'--'|| 
  (   )\_______/      ||
   \``\/       \      ||
    `-| ==    \_|     ||
      /         |     ||
     |=   >\  __/     ||
     \   \ |- --|     ||
      \ __| \___/     ||
     _{__} _{__}     ||
     (    )(    )     ||
 ^^~  `"""  `"""  ~^^^~^^~~~^^^~^^^~^^^~^^~^''')
 
input()
os.system('cls')


Algoritmo Proyecto
    // Declaración de variables iniciales
    Definir vidas Como Entero;
    Definir planetas_explorados Como Entero;
    Definir opcion Como Entero;
	Definir controlador Como Entero;
	Definir gemas Como Entero;
	//Variables de gemas 
	Definir gema1 Como Entero;
	Definir gema2 Como Entero;
	Definir gema3 Como Entero;
    // Variables para los planetas
    Definir planeta1 Como Caracter;
    Definir planeta2 Como Caracter;
    Definir planeta3 Como Caracter;
    
    //  preguntas y respuestas
    Definir pregunta Como Caracter;
    Definir respuesta_correcta Como Entero;
    Definir respuesta_introducida Como Entero;
    
    // Inicialización de variables
    vidas <- 3; //vidas al empezar
    planetas_explorados <- 0; 
	gema1<-0;
	gema2<-0;
	gema3<-0;
	gemas<-0;
    controlador<-0;
    // Nombres de los planetas
    planeta1 <- "Marte";
    planeta2 <- "Venus";
    planeta3 <- "Júpiter";
    
    //  mensaje informativo inicial
    Escribir "=============================================="
    Escribir "         ¡Bienvenido al Juego Espacial!       "
    Escribir "=============================================="
    Escribir "Tu objetivo es explorar los 3 planetas, responder "
    Escribir "correctamente a las preguntas que te hagan los personajes,"
    Escribir "y recolectar las 3 gemas sin quedarte sin vidas."
    Escribir "Comienzas con 3 vidas y 0 gemas."
    Escribir "=============================================="
    
    // estadísticas iniciales
    Escribir "Estadísticas iniciales:"
    Escribir "Vidas: ", vidas
    Escribir "Planetas explorados: ", planetas_explorados
    Escribir "=============================================="
    
    // Bucle principal del juego
    Mientras vidas > 0 Y gemas=0 Hacer
		//insertar imagen 
        // Mostrar menú de selección de planeta
        Escribir "¿A qué planeta quieres ir?"
        Escribir "1. Planeta Marte"
        Escribir "2. Planeta Venus"
        Escribir "3. Planeta Júpiter"
        Escribir "4. Salir del juego"
	
	
        
        // Leer opción 
        Escribir "Por favor, selecciona una opción (1-4):"
        Leer opcion;
        
        // opción seleccionada
        Segun opcion Hacer
            Caso 1: //insertar imagen
				Si gema1=0 Entonces
					Escribir "Has seleccionado viajar a ", planeta1, "."
					pregunta <- "¿Cuánto es 3 + 5?"
					respuesta_correcta <- 8
					gema1<-1;
				SiNo
					
					controlador<-1;
				Fin Si
                
            Caso 2: //insertar imagen
				Si gema2=0 Entonces
					Escribir "Has seleccionado viajar a ", planeta2, "."
					pregunta <- "¿Cuánto es 7 - 4?"
					respuesta_correcta <- 3
					gema2<-1;
				SiNo
				
					controlador<-1;
				Fin Si
               
            Caso 3: //insertar imagen
				Si gema3=0 Entonces
					Escribir "Has seleccionado viajar a ", planeta3, "."
					pregunta <- "¿Cuánto es 6 x 2?"
					respuesta_correcta <- 12
					gema3<-1
				SiNo
					
					controlador<-1;
				Fin Si
                
            Caso 4: //insertar imagen
                Escribir "¡Hasta la próxima!"
			De Otro Modo:
				Escribir "Opción no válida. Inténtalo de nuevo."
			
		FinSegun

// Seleccionar planeta
Si opcion >= 1 Y opcion <= 3 Entonces
	Si controlador=0 Entonces
		Escribir "Pregunta del NPC: ", pregunta       //insertar imagen
		Escribir "Ingresa tu respuesta:"
		Leer respuesta_introducida;
		
		Si respuesta_introducida = respuesta_correcta Entonces
			Escribir "¡Correcto! Has ganado una gema."    //insertar imagen
			
		SiNo
			Escribir "Incorrecto. Has perdido una vida."  //insertar imagen
			vidas <- vidas - 1
		FinSi
		
		
		planetas_explorados <- planetas_explorados + 1
	SiNo
		Escribir "Planeta ya visitado"
		controlador<-0;
	Fin Si
	
FinSi

// fin del juego
Si vidas = 0 Entonces
	Escribir "Te has quedado sin vidas. ¡Fin del juego!" //insertar imagen
FinSi

Si gema1=1 Y gema2=1 Y gema3=1 Entonces
	gemas<-1
SiNo
	gemas<-0;
Fin Si

	FinMientras

// Fin,mostrar estadísticas finales
Escribir "=============================================="
Si gema1=1 Y gema2=1 Y gema3=1 Entonces
	Escribir "¡Felicidades! Has recolectado las 3 gemas y ganado el juego." //insertar imagen
SiNo
	Escribir "Te has quedado sin vidas. ¡Fin del juego!" //insertar imagen
FinSi
Escribir "Estadísticas finales:"
Escribir "Vidas restantes: ", vidas
Escribir "Planetas explorados: ", planetas_explorados
Escribir "=============================================="
    
FinAlgoritmo

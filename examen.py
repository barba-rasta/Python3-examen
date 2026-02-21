import re
import os
from datetime import datetime
from colorama import init, Fore, Back, Style

# Inicializar colorama (autoreset=True para que no se mantengan colores)
init(autoreset=True)

def limpiar_pantalla():
    """Limpia la pantalla según el sistema operativo"""
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_bienvenida():
    """Muestra el mensaje de bienvenida al inicio del programa"""
    limpiar_pantalla()
    print(f"{'='*60}")
    print(f"{'EXAMEN EN PYTHON 3':^60}")
    print(f"{'Creado por Jorge Barba':^60}")
    print(f"{'='*60}{Style.RESET_ALL}\n")
    
    input(f"{Fore.LIGHTBLACK_EX}Presiona Enter para comenzar...{Style.RESET_ALL}")

def mostrar_despedida():
    """Muestra el mensaje de despedida al final del programa"""
    print(f"\n{Style.BRIGHT}{Back.CYAN}{Fore.WHITE}{'='*60}")
    print(f"{Back.CYAN}{Fore.WHITE}{'EXAMEN EN PYTHON 3':^60}")
    print(f"{Back.CYAN}{Fore.WHITE}{'Creado por Jorge Barba':^60}")
    print(f"{Back.CYAN}{Fore.WHITE}{'='*60}{Style.RESET_ALL}\n")
    
    print(f"{Fore.CYAN}¡Gracias por utilizar este examen!{Style.RESET_ALL}")
    print(f"{Fore.LIGHTBLACK_EX}Presiona Enter para salir...{Style.RESET_ALL}")
    input()

def solicitar_datos_usuario():
    limpiar_pantalla()
    print(f"{Style.BRIGHT}{Back.BLUE}{Fore.WHITE}=== REGISTRO DE USUARIO ===\n\033[0m")
    
    nombre = input(f"{Fore.CYAN}Ingresa tu nombre completo: \033[0m").strip()
    while not nombre:
        print(f"\n{Fore.RED}El nombre no puede estar vacío. Intenta de nuevo.\n\033[0m")
        nombre = input(f"{Fore.CYAN}Ingresa tu nombre completo: \033[0m").strip()
    
    # Preguntar por el país en lugar del correo
    pais = input(f"{Fore.CYAN}¿De qué país eres?: \033[0m").strip()
    while not pais:
        print(f"\n{Fore.RED}El país no puede estar vacío. Intenta de nuevo.\n\033[0m")
        pais = input(f"{Fore.CYAN}¿De qué país eres?: \033[0m").strip()
    
    limpiar_pantalla()
    
    # Retornar nombre y país
    return nombre, pais


def crear_examen():
    """Define 35 preguntas, opciones y respuestas correctas del examen de Python 3"""
    examen = [
        {
            "pregunta": "1. ¿Qué tipo de lenguaje es Python?",
            "opciones": [
                "A) Lenguaje compilado",
                "B) Lenguaje interpretado",
                "C) Lenguaje ensamblador",
                "D) Lenguaje de bajo nivel"
            ],
            "respuesta_correcta": "B"
        },
        {
            "pregunta": "2. ¿Cómo se define una función en Python?",
            "opciones": [
                "A) func mi_funcion():",
                "B) define mi_funcion():",
                "C) def mi_funcion():",
                "D) function mi_funcion():"
            ],
            "respuesta_correcta": "C"
        },
        {
            "pregunta": "3. ¿Qué estructura de datos es mutable y ordenada?",
            "opciones": [
                "A) Tupla",
                "B) Cadena de texto",
                "C) Lista",
                "D) Conjunto"
            ],
            "respuesta_correcta": "C"
        },
        {
            "pregunta": "4. ¿Qué palabra clave se usa para iniciar un bloque de manejo de excepciones?",
            "opciones": [
                "A) try",
                "B) catch",
                "C) error",
                "D) except"
            ],
            "respuesta_correcta": "A"
        },
        {
            "pregunta": "5. ¿Cómo se importa el módulo 'math'?",
            "opciones": [
                "A) include math",
                "B) import math",
                "C) using math",
                "D) load math"
            ],
            "respuesta_correcta": "B"
        },
        {
            "pregunta": "6. ¿Qué salida produce print(2 ** 3)?",
            "opciones": [
                "A) 6",
                "B) 8",
                "C) 9",
                "D) Error"
            ],
            "respuesta_correcta": "B"
        },
        {
            "pregunta": "7. ¿Qué palabra clave define una clase en Python?",
            "opciones": [
                "A) class",
                "B) object",
                "C) struct",
                "D) type"
            ],
            "respuesta_correcta": "A"
        },
        {
            "pregunta": "8. ¿Qué estructura de datos es inmutable y ordenada?",
            "opciones": [
                "A) Lista",
                "B) Tupla",
                "C) Conjunto",
                "D) Diccionario"
            ],
            "respuesta_correcta": "B"
        },
        {
            "pregunta": "9. ¿Cómo se escribe un comentario de una sola línea?",
            "opciones": [
                "A) /* Comentario */",
                "B) // Comentario",
                "C) # Comentario",
                "D) -- Comentario"
            ],
            "respuesta_correcta": "C"
        },
        {
            "pregunta": "10. ¿Qué método se usa para agregar un elemento al final de una lista?",
            "opciones": [
                "A) add()",
                "B) append()",
                "C) insert()",
                "D) extend()"
            ],
            "respuesta_correcta": "B"
        },
        {
            "pregunta": "11. ¿Qué salida produce print(10 % 3)?",
            "opciones": [
                "A) 3",
                "B) 1",
                "C) 0",
                "D) 3.33"
            ],
            "respuesta_correcta": "B"
        },
        {
            "pregunta": "12. ¿Qué palabra clave se usa para heredar de una clase padre?",
            "opciones": [
                "A) inherit",
                "B) extends",
                "C) super",
                "D) Se especifica entre paréntesis en la definición de la clase"
            ],
            "respuesta_correcta": "D"
        },
        {
            "pregunta": "13. ¿Qué estructura de datos almacena pares clave-valor?",
            "opciones": [
                "A) Lista",
                "B) Tupla",
                "C) Diccionario",
                "D) Conjunto"
            ],
            "respuesta_correcta": "C"
        },
        {
            "pregunta": "14. ¿Cómo se abre un archivo para escribir, sobrescribiendo su contenido si existe?",
            "opciones": [
                "A) open('archivo.txt', 'r')",
                "B) open('archivo.txt', 'w')",
                "C) open('archivo.txt', 'a')",
                "D) open('archivo.txt', 'x')"
            ],
            "respuesta_correcta": "B"
        },
        {
            "pregunta": "15. ¿Qué función convierte un valor a entero?",
            "opciones": [
                "A) str()",
                "B) float()",
                "C) int()",
                "D) bool()"
            ],
            "respuesta_correcta": "C"
        },
        {
            "pregunta": "16. ¿Qué salida produce print(len('Hola Mundo'))?",
            "opciones": [
                "A) 9",
                "B) 10",
                "C) 11",
                "D) 8"
            ],
            "respuesta_correcta": "B"
        },
        {
            "pregunta": "17. ¿Qué palabra clave se usa para salir de un bucle?",
            "opciones": [
                "A) break",
                "B) continue",
                "C) exit",
                "D) stop"
            ],
            "respuesta_correcta": "A"
        },
        {
            "pregunta": "18. ¿Qué método se usa para eliminar un elemento de un conjunto?",
            "opciones": [
                "A) remove()",
                "B) pop()",
                "C) delete()",
                "D) clear()"
            ],
            "respuesta_correcta": "A"
        },
        {
            "pregunta": "19. ¿Qué módulo se usa para trabajar con fechas y horas?",
            "opciones": [
                "A) time",
                "B) datetime",
                "C) date",
                "D) clock"
            ],
            "respuesta_correcta": "B"
        },
        {
            "pregunta": "20. ¿Qué salida produce print(bool(0))?",
            "opciones": [
                "A) True",
                "B) False",
                "C) None",
                "D) Error"
            ],
            "respuesta_correcta": "B"
        },
        {
            "pregunta": "21. ¿Cómo se define una lista vacía?",
            "opciones": [
                "A) lista = {}",
                "B) lista = ()",
                "C) lista = []",
                "D) lista = set()"
            ],
            "respuesta_correcta": "C"
        },
        {
            "pregunta": "22. ¿Qué palabra clave se usa para repetir un bloque de código mientras se cumpla una condición?",
            "opciones": [
                "A) for",
                "B) while",
                "C) repeat",
                "D) loop"
            ],
            "respuesta_correcta": "B"
        },
        {
            "pregunta": "23. ¿Qué método se usa para convertir una cadena a minúsculas?",
            "opciones": [
                "A) lower()",
                "B) upper()",
                "C) capitalize()",
                "D) title()"
            ],
            "respuesta_correcta": "A"
        },
        {
            "pregunta": "24. ¿Qué es PIP en Python?",
            "opciones": [
                "A) Un entorno virtual",
                "B) El intérprete de Python",
                "C) El gestor de paquetes oficial",
                "D) Un editor de código"
            ],
            "respuesta_correcta": "C"
        },
        {
            "pregunta": "25. ¿Qué salida produce print('Python'[1])?",
            "opciones": [
                "A) P",
                "B) y",
                "C) t",
                "D) Error"
            ],
            "respuesta_correcta": "B"
        },
        {
            "pregunta": "26. ¿Qué palabra clave se usa para llamar al constructor de la clase padre?",
            "opciones": [
                "A) parent",
                "B) super()",
                "C) base",
                "D) father"
            ],
            "respuesta_correcta": "B"
        },
        {
            "pregunta": "27. ¿Cómo se abre un archivo para leer y escribir sin sobrescribir?",
            "opciones": [
                "A) open('archivo.txt', 'r+')",
                "B) open('archivo.txt', 'w+')",
                "C) open('archivo.txt', 'a+')",
                "D) open('archivo.txt', 'rx')"
            ],
            "respuesta_correcta": "A"
        },
        {
            "pregunta": "28. ¿Qué estructura de datos no permite elementos duplicados?",
            "opciones": [
                "A) Lista",
                "B) Tupla",
                "C) Conjunto",
                "D) Diccionario"
            ],
            "respuesta_correcta": "C"
        },
        {
            "pregunta": "29. ¿Qué función devuelve el valor máximo de una secuencia?",
            "opciones": [
                "A) max()",
                "B) maximum()",
                "C) top()",
                "D) peak()"
            ],
            "respuesta_correcta": "A"
        },
        {
            "pregunta": "30. ¿Qué salida produce print(round(3.1416, 2))?",
            "opciones": [
                "A) 3.14",
                "B) 3.15",
                "C) 3",
                "D) 3.1416"
            ],
            "respuesta_correcta": "A"
        },
        {
            "pregunta": "31. ¿Qué palabra clave se usa para saltar la iteración actual de un bucle?",
            "opciones": [
                "A) break",
                "B) continue",
                "C) skip",
                "D) pass"
            ],
            "respuesta_correcta": "B"
        },
        {
            "pregunta": "32. ¿Qué método se usa para unir elementos de una lista en una cadena?",
            "opciones": [
                "A) join()",
                "B) concat()",
                "C) merge()",
                "D) combine()"
            ],
            "respuesta_correcta": "A"
        },
        {
            "pregunta": "33. ¿Qué es un entorno virtual en Python?",
            "opciones": [
                "A) Un programa para ejecutar código",
                "B) Un espacio aislado para instalar paquetes",
                "C) Un tipo de dato",
                "D) Un módulo para virtualización"
            ],
            "respuesta_correcta": "B"
        },
        {
            "pregunta": "34. ¿Qué salida produce print('Hola' + ' ' + 'Mundo')?",
            "opciones": [
                "A) HolaMundo",
                "B) Hola Mundo",
                "C) Error",
                "D) Hola  Mundo"
            ],
            "respuesta_correcta": "B"
        },
        {
            "pregunta": "35. ¿Qué palabra clave se usa para definir una constante en Python?",
            "opciones": [
                "A) const",
                "B) final",
                "C) No existe una palabra clave específica",
                "D) static"
            ],
            "respuesta_correcta": "C"
        }
    ]
    return examen

def mostrar_contador(correctas, incorrectas, total):
    """Muestra el contador de respuestas correctas e incorrectas"""
    porcentaje = (correctas / total) * 100 if total > 0 else 0
    print(f"\n{Style.BRIGHT}{Back.BLACK}{Fore.WHITE} CONTADOR DE RESPUESTAS ")
    print(f"{Fore.GREEN}✓ Correctas: {correctas}  {Fore.RED}✗ Incorrectas: {incorrectas}")
    print(f"{Fore.CYAN}Progreso: {correctas + incorrectas}/{total}  ({porcentaje:.1f}% completado)")
    print(f"{Style.RESET_ALL}")

def obtener_calificacion(porcentaje):
    """Devuelve la calificación según el porcentaje obtenido"""
    if porcentaje >= 90:
        return "EXCELENTE (A)", Fore.GREEN
    elif porcentaje >= 80:
        return "MUY BIEN (B)", Fore.LIGHTGREEN_EX
    elif porcentaje >= 70:
        return "BIEN (C)", Fore.YELLOW
    elif porcentaje >= 60:
        return "SUFICIENTE (D)", Fore.LIGHTYELLOW_EX
    else:
        return "INSUFICIENTE (F)", Fore.RED

def realizar_examen(examen):
    """Muestra el examen, registra respuestas y muestra puntaje parcial"""
    limpiar_pantalla()
    print(f"{Style.BRIGHT}{Back.GREEN}{Fore.WHITE}=== EXAMEN COMPLETO DE PYTHON 3 (35 PREGUNTAS) ===\n\033[0m")
    
    respuestas_usuario = []
    correctas = 0
    incorrectas = 0
    total_preguntas = len(examen)

    for num, pregunta in enumerate(examen, 1):
        # Mostrar contador en la parte superior
        mostrar_contador(correctas, incorrectas, total_preguntas)
        
        print(f"{Style.BRIGHT}{Fore.MAGENTA}--- PREGUNTA {num}/{total_preguntas} ---\033[0m")
        print(f"{Fore.WHITE}{pregunta['pregunta']}\033[0m")
        for opcion in pregunta["opciones"]:
            print(f"   {Fore.YELLOW}{opcion}\033[0m")
        
        # Validación de respuesta - CORREGIDO PARA ACEPTAR MAYÚSCULAS Y MINÚSCULAS
        while True:
            respuesta = input(f"\n{Fore.CYAN}Tu respuesta (A/B/C/D): ").strip().upper()
            if respuesta in ["A", "B", "C", "D"]:  # ← AHORA COMPARA CON MAYÚSCULAS
                break
            print(f"\n{Fore.RED}Respuesta inválida. Elige A, B, C o D (mayúscula o minúscula).\n\033[0m")
        
        respuestas_usuario.append(respuesta)
        
        # Verificar respuesta y mostrar resultado inmediatamente
        if respuesta == pregunta["respuesta_correcta"]:
            correctas += 1
            print(f"\n{Fore.GREEN}{Style.BRIGHT}✓ ¡CORRECTO!\033[0m")
        else:
            incorrectas += 1
            print(f"\n{Fore.RED}{Style.BRIGHT}✗ INCORRECTO\033[0m")
        
        # Mostrar cuál era la respuesta correcta
        opcion_correcta_texto = ""
        for opcion in pregunta["opciones"]:
            if opcion.startswith(pregunta["respuesta_correcta"] + ")"):
                opcion_correcta_texto = opcion
                break
        
        print(f"{Fore.WHITE}La respuesta correcta era: {Fore.YELLOW}{pregunta['respuesta_correcta']}) {opcion_correcta_texto[3:].strip()}\033[0m")
        
        input(f"\n{Fore.LIGHTBLACK_EX}Presiona Enter para continuar...\033[0m")
        limpiar_pantalla()
    
    return correctas, incorrectas, total_preguntas, respuestas_usuario

def mostrar_resultados_finales(nombre, pais, correctas, incorrectas, total, respuestas_usuario, examen):
    """Muestra los resultados finales con calificación"""
    limpiar_pantalla()
    
    porcentaje = (correctas / total) * 100
    calificacion, color_calif = obtener_calificacion(porcentaje)
    
    print(f"{Style.BRIGHT}{Back.BLUE}{Fore.WHITE}=== RESULTADOS FINALES ===\n\033[0m")
    print(f"{Fore.CYAN}Nombre: {Fore.WHITE}{nombre}\033[0m")
    print(f"{Fore.CYAN}País:   {Fore.WHITE}{pais}\033[0m")  # Cambiado de Correo a País
    print(f"{Fore.CYAN}Fecha:  {Fore.WHITE}{datetime.now().strftime('%d/%m/%Y %H:%M')}\n\033[0m")
    
    print(f"{Style.BRIGHT}{Back.BLACK}{Fore.WHITE} ESTADÍSTICAS \033[0m")
    print(f"{Fore.GREEN}✓ Respuestas correctas: {correctas}\033[0m")
    print(f"{Fore.RED}✗ Respuestas incorrectas: {incorrectas}\033[0m")
    print(f"{Fore.WHITE}Total de preguntas: {total}\n")
    
    print(f"{Style.BRIGHT}{Back.BLACK}{Fore.WHITE} CALIFICACIÓN \033[0m")
    print(f"{Fore.WHITE}Porcentaje obtenido: {color_calif}{porcentaje:.2f}%\033[0m")
    print(f"{Fore.WHITE}Calificación: {color_calif}{calificacion}\n\033[0m")
    
    # Mostrar resumen de errores
    if incorrectas > 0:
        print(f"{Style.BRIGHT}{Fore.RED}=== PREGUNTAS INCORRECTAS ===\033[0m")
        for i, (respuesta, pregunta) in enumerate(zip(respuestas_usuario, examen)):
            if respuesta != pregunta["respuesta_correcta"]:
                print(f"\n{Fore.YELLOW}Pregunta {i+1}: {Fore.WHITE}{pregunta['pregunta']}")
                print(f"{Fore.RED}Tu respuesta: {respuesta}\033[0m")
                print(f"{Fore.GREEN}Correcta: {pregunta['respuesta_correcta']}\033[0m")
    
    # Guardar resultados en archivo
    guardar_resultados(nombre, pais, correctas, incorrectas, total, porcentaje, calificacion)
    
    print(f"\n{Fore.CYAN}{Style.BRIGHT}¡Examen completado! Los resultados se han guardado en 'resultados_examen.txt'\033[0m")

def guardar_resultados(nombre, pais, correctas, incorrectas, total, porcentaje, calificacion):
    """Guarda los resultados en un archivo de texto"""
    fecha = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
    with open('resultados_examen.txt', 'a', encoding='utf-8') as f:
        f.write(f"\n{'='*50}\n")
        f.write(f"FECHA: {fecha}\n")
        f.write(f"NOMBRE: {nombre}\n")
        f.write(f"PAÍS: {pais}\n")  # Cambiado de CORREO a PAÍS
        f.write(f"CORRECTAS: {correctas}/{total}\n")
        f.write(f"INCORRECTAS: {incorrectas}/{total}\n")
        f.write(f"PORCENTAJE: {porcentaje:.2f}%\n")
        f.write(f"CALIFICACIÓN: {calificacion}\n")
        f.write(f"{'='*50}\n")

def main():
    """Función principal que ejecuta el examen"""
    try:
        # Mostrar mensaje de bienvenida al inicio
        mostrar_bienvenida()
        
        # Solicitar datos del usuario
        nombre, pais = solicitar_datos_usuario()  # Cambiado de correo a pais
        
        # Crear y realizar el examen
        examen = crear_examen()
        correctas, incorrectas, total, respuestas_usuario = realizar_examen(examen)
        
        # Mostrar resultados finales
        mostrar_resultados_finales(nombre, pais, correctas, incorrectas, total, respuestas_usuario, examen)  # Cambiado correo por pais
        
        # Mostrar mensaje de despedida al final
        mostrar_despedida()
        
    except KeyboardInterrupt:
        print(f"\n\n{Fore.YELLOW}Examen interrumpido por el usuario.\033[0m")
    except Exception as e:
        print(f"\n{Fore.RED}Error inesperado: {e}\033[0m")

if __name__ == "__main__":
    main()

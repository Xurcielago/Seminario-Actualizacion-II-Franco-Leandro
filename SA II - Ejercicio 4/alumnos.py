alumnos = []

def calcular_promedio(materias):
    if not materias:
        return 0.0
    suma = sum(materia[1] for materia in materias)
    return suma / len(materias)

def buscar_alumno(nombre):
    for i in range(len(alumnos)):
        if alumnos[i][0].lower() == nombre.lower():
            return i
    return -1

def buscar_materia(indice_alumno, nombre_materia):
    materias = alumnos[indice_alumno][1]
    for i in range(len(materias)):
        if materias[i][0].lower() == nombre_materia.lower():
            return i
    return -1

def ver_alumnos(lista_alumnos=None):
    datos = lista_alumnos if lista_alumnos is not None else alumnos
    
    if not datos:
        print("\nNo hay alumnos registrados.")
        return

    print("\n--- LISTA DE ALUMNOS ---")
    for alumno in datos:
        nombre = alumno[0]
        materias = alumno[1]
        promedio = calcular_promedio(materias)
        
        print(f"\nAlumno: {nombre} | Promedio: {promedio:.2f}")
        for materia in materias:
            print(f"  - {materia[0]}: {materia[1]}")
    print("------------------------")

def agregar_modificar_nota(indice_alumno):
    nombre = alumnos[indice_alumno][0]
    materia_nombre = input(f"Ingrese el nombre de la materia para {nombre}: ").strip().capitalize()
    
    try:
        nota = float(input(f"Ingrese la nota para {materia_nombre}: "))
        if nota < 0 or nota > 10:
            print("La nota debe estar entre 0 y 10.")
            return
    except ValueError:
        print("Error: Debe ingresar un valor numérico.")
        return

    indice_materia = buscar_materia(indice_alumno, materia_nombre)
    
    if indice_materia != -1:
        alumnos[indice_alumno][1][indice_materia][1] = nota
        print(f"Nota de {materia_nombre} modificada con éxito para {nombre}.")
    else:
        alumnos[indice_alumno][1].append([materia_nombre, nota])
        print(f"Materia {materia_nombre} agregada con éxito a {nombre}.")

def agregar_alumno():
    nombre = input("\nIngrese el nombre del nuevo alumno: ").strip().capitalize()
    
    indice = buscar_alumno(nombre)
    if indice != -1:
        print(f"El alumno '{nombre}' ya está registrado.")
        opcion = input("¿Desea modificar o agregar una nota para este alumno? (s/n): ").strip().lower()
        if opcion == 's':
            agregar_modificar_nota(indice)
    else:
        alumnos.append([nombre, []])
        print(f"Alumno '{nombre}' agregado con éxito.")
        
        opcion = input("¿Desea cargarle una materia ahora? (s/n): ").strip().lower()
        if opcion == 's':
            agregar_modificar_nota(len(alumnos) - 1)

def solicitar_modificacion():
    nombre = input("\nIngrese el nombre del alumno al que desea agregar/modificar notas: ").strip().capitalize()
    indice = buscar_alumno(nombre)
    
    if indice == -1:
        print(f"El alumno '{nombre}' no existe en el sistema.")
    else:
        agregar_modificar_nota(indice)

def ordenar_y_mostrar_promedios():
    alumnos_ordenados = sorted(alumnos, key=lambda x: calcular_promedio(x[1]), reverse=True)
    ver_alumnos(alumnos_ordenados)

def mejor_promedio():
    if not alumnos:
        print("\nNo hay alumnos para evaluar.")
        return
        
    mejor_alumno = alumnos[0]
    max_promedio = calcular_promedio(mejor_alumno[1])
    
    for alumno in alumnos[1:]:
        promedio_actual = calcular_promedio(alumno[1])
        if promedio_actual > max_promedio:
            max_promedio = promedio_actual
            mejor_alumno = alumno
            
    print(f"\nEl alumno con mejor promedio es {mejor_alumno[0]} con una nota de {max_promedio:.2f}")

def mostrar_menu():
    while True:
        print("\n" + "="*30)
        print(" GESTOR DE CALIFICACIONES")
        print("="*30)
        print("1. Ver alumnos")
        print("2. Agregar alumno")
        print("3. Agregar o modificar notas")
        print("4. Ver alumno con mejor promedio (Bonus)")
        print("5. Ver alumnos ordenados por promedio (Bonus)")
        print("6. Salir")
        
        opcion = input("Seleccione una opción: ").strip()
        
        if opcion == '1':
            ver_alumnos()
        elif opcion == '2':
            agregar_alumno()
        elif opcion == '3':
            solicitar_modificacion()
        elif opcion == '4':
            mejor_promedio()
        elif opcion == '5':
            ordenar_y_mostrar_promedios()
        elif opcion == '6':
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    mostrar_menu() 

#Repasar if __name__ == "__main__":

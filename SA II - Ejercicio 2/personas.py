## ============================================================
##  Sistema de registro de personas
##  Ejecución: python personas.py
## ============================================================

def mostrar_tabla(lista, titulo):
    print(f"\n{'=' * 45}")
    print(f"  {titulo}")
    print(f"{'=' * 45}")
    print(f"  {'NOMBRE':<20} {'EDAD':>6} {'NOTA':>8}")
    print(f"  {'-' * 38}")
    for persona in lista:
        print(f"  {persona[0]:<20} {persona[1]:>6} {persona[2]:>8.2f}")
    print(f"{'=' * 45}")


def pedir_numero(mensaje, tipo):
    while True:
        try:
            valor = tipo(input(mensaje))
            if tipo == float and not (0 <= valor <= 10):
                print("⚠  La nota debe estar entre 0 y 10. Intentá de nuevo.")
                continue
            if tipo == int and valor <= 0:
                print("La edad debe ser un número positivo. Intentá de nuevo.")
                continue
            return valor
        except ValueError:
            esperado = "un número entero" if tipo == int else "un número decimal"
            print(f"Eso no es válido. Ingresá {esperado}.")


def main():
    personas = [] 

    print("\n" + "=" * 45)
    print("   SISTEMA DE REGISTRO DE PERSONAS")
    print("=" * 45)
    print("  Ingresá los datos de cada persona.")
    print("  Comandos disponibles en el campo NOMBRE:")
    print("    'finalizar'  -> cerrar sistema")
    print("    'listar'     -> ver lista")
    print("=" * 45)

    # ── Bucle principal ──
    while True:
        print(f"\n  [ Persona #{len(personas) + 1} ]")

        nombre = input("  Nombre      : ").strip()

        # Condición de salida
        if nombre.lower() in ("finalizar"):
            break

        # Comando listar
        if nombre.lower() == "listar":
            if not personas:
                print("Todavía no hay personas registradas.")
            else:
                mostrar_tabla(personas, f"LISTADO PARCIAL — {len(personas)} persona/s")
            continue

        if not nombre:
            print("El nombre no puede estar vacío.")
            continue

        edad = pedir_numero("  Edad        : ", int)
        nota = pedir_numero("  Nota (0-10) : ", float)

        personas.append([nombre, edad, nota])
        print(f"'{nombre}' registrado correctamente.")

    # ── Salida ──
    if not personas:
        print("\n  No se registró ninguna persona. Cerrando el sistema.")
        return

    mostrar_tabla(personas, "LISTADO EN ORDEN DE INGRESO")

    ordenada = sorted(personas, key=lambda p: p[2], reverse=True)
    mostrar_tabla(ordenada, "LISTADO ORDENADO POR NOTA (mayor a menor)")

    promedio = sum(p[2] for p in personas) / len(personas)
    print(f"\n  Promedio general de notas: {promedio:.2f}")
    print(f"  Total de personas registradas: {len(personas)}")
    print("\n  Sistema cerrado.")

main()
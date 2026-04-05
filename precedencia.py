def generar_gramatica(operadores):
    niveles = len(operadores)
    no_terminales = [f"E{i}" for i in range(niveles + 1)]

    print("\nGramática:")

    for i in range(niveles):
        op = operadores[i]
        print(f"{no_terminales[i]} -> {no_terminales[i]} {op} {no_terminales[i+1]} | {no_terminales[i+1]}")

    print(f"{no_terminales[-1]} -> num")

def ejemplos():
    print("\nEjemplos:")
    print("4 + 3 * 2  => 4 + (3 * 2)")
    print("a + b * c - d  => primero *, luego + y -")


def validar_operadores(operadores):
    validos = ['+', '-', '*', '/']

    if len(operadores) == 0:
        return False, "No se ingresaron operadores"

    for op in operadores:
        if op not in validos:
            return False, f"Operador inválido: '{op}'"

    # evitar duplicados seguidos
    for i in range(len(operadores) - 1):
        if operadores[i] == operadores[i+1]:
            return False, f"Operadores repetidos: '{operadores[i]}'"

    return True, ""

def procesar_linea(linea):
    operadores = linea.split()

    print("\n==============================")
    print("Operadores:", linea)

    valido, error = validar_operadores(operadores)
    if not valido:
        print("\n Error:", error)
        print("==============================")
        return

    generar_gramatica(operadores)
    ejemplos()

    print("==============================")

def main():
    try:
        while True:
            linea = input().strip()
            if linea:
                procesar_linea(linea)
    except EOFError:
        pass

if __name__ == "__main__":
    main()

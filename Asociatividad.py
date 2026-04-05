class Nodo:
    def __init__(self, valor, izq=None, der=None):
        self.valor = valor
        self.izq = izq
        self.der = der

def evaluar(nodo):
    if nodo.izq is None and nodo.der is None:
        return int(nodo.valor)
    
    if nodo.valor == '+':
        return evaluar(nodo.izq) + evaluar(nodo.der)
    elif nodo.valor == '-':
        return evaluar(nodo.izq) - evaluar(nodo.der)
    elif nodo.valor == '*':
        return evaluar(nodo.izq) * evaluar(nodo.der)
    elif nodo.valor == '/':
        return evaluar(nodo.izq) / evaluar(nodo.der)

def imprimir_arbol(nodo, nivel=0):
    if nodo is not None:
        imprimir_arbol(nodo.der, nivel + 1)
        print("   " * nivel + str(nodo.valor))
        imprimir_arbol(nodo.izq, nivel + 1)

def construir_izquierda(tokens):
    nodo = Nodo(tokens[0])
    i = 1
    while i < len(tokens):
        op = tokens[i]
        siguiente = Nodo(tokens[i+1])
        nodo = Nodo(op, nodo, siguiente)
        i += 2
    return nodo

def construir_derecha(tokens):
    nodo = Nodo(tokens[-1])
    i = len(tokens) - 2
    while i > 0:
        op = tokens[i]
        anterior = Nodo(tokens[i-1])
        nodo = Nodo(op, anterior, nodo)
        i -= 2
    return nodo

def validar_tokens(tokens):
    operadores = ['+', '-', '*', '/']

    if len(tokens) % 2 == 0:
        return False, "Estructura inválida (faltan operandos u operadores)"

    for i, t in enumerate(tokens):
        if i % 2 == 0:
            if not t.isdigit():
                return False, f"Se esperaba número en posición {i}, se encontró '{t}'"
        else:
            if t not in operadores:
                return False, f"Se esperaba operador en posición {i}, se encontró '{t}'"

    return True, ""

def procesar_linea(linea):
    tokens = linea.split()

    print("\n==============================")
    print("Expresión:", linea)

    valido, error = validar_tokens(tokens)
    if not valido:
        print("\n Error:", error)
        print("==============================")
        return

    try:
        print("\n--- Asociatividad Izquierda ---")
        izq = construir_izquierda(tokens)
        imprimir_arbol(izq)
        print("Resultado:", evaluar(izq))

        print("\n--- Asociatividad Derecha ---")
        der = construir_derecha(tokens)
        imprimir_arbol(der)
        print("Resultado:", evaluar(der))

    except Exception as e:
        print("\n Error durante evaluación:", e)

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

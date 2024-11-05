class ExpressionEvaluator:
    def __init__(self):
        # Diccionario de operadores, donde cada operador tiene una tupla con su precedencia y su operación
        self.operators = {
            "+": (1, lambda x, y: x + y),
            "-": (1, lambda x, y: x - y),
            "*": (2, lambda x, y: x * y),
            "/": (2, lambda x, y: x // y)
        }

    def eval_prefix(self, tokens):
        # Evalúa una expresión en notación prefija usando una pila
        stack = []
        # Recorremos los tokens en orden inverso
        for token in reversed(tokens):
            if token.isdigit():
                # Si el token es un dígito, lo convertimos a entero y lo apilamos
                stack.append(int(token))
            else:
                # Si el token es un operador, desempilamos dos operandos y aplicamos el operador
                op1 = stack.pop()
                op2 = stack.pop()
                stack.append(self.operators[token][1](op1, op2))
        return stack[0]  # El resultado final queda en el tope de la pila

    def eval_postfix(self, tokens):
        # Evalúa una expresión en notación postfija usando una pila
        stack = []
        for token in tokens:
            if token.isdigit():
                # Si el token es un dígito, lo convertimos a entero y lo apilamos
                stack.append(int(token))
            else:
                # Si el token es un operador, desempilamos dos operandos y aplicamos el operador
                op2 = stack.pop()
                op1 = stack.pop()
                stack.append(self.operators[token][1](op1, op2))
        return stack[0]  # El resultado final queda en el tope de la pila

    def infix_from_prefix(self, tokens):
        # Convierte una expresión en notación prefija a infija
        stack = []
        for token in reversed(tokens):
            if token.isdigit():
                # Si el token es un dígito, lo apilamos directamente
                stack.append(token)
            else:
                # Si el token es un operador, desempilamos dos operandos y construimos la expresión
                op1 = stack.pop()
                op2 = stack.pop()
                # Verificamos si necesitamos paréntesis para mantener la precedencia correcta
                if self.needs_parentheses(token, op1):
                    op1 = f"({op1})"
                if self.needs_parentheses(token, op2):
                    op2 = f"({op2})"
                # Creamos la expresión en notación infija y la apilamos
                expression = f"{op1} {token} {op2}"
                stack.append(expression)
        return stack[0]  # La expresión infija completa queda en el tope de la pila

    def infix_from_postfix(self, tokens):
        # Convierte una expresión en notación postfija a infija
        stack = []
        for token in tokens:
            if token.isdigit():
                # Si el token es un dígito, lo apilamos directamente
                stack.append(token)
            else:
                # Si el token es un operador, desempilamos dos operandos y construimos la expresión
                op2 = stack.pop()
                op1 = stack.pop()
                # Verificamos si necesitamos paréntesis para mantener la precedencia correcta
                if self.needs_parentheses(token, op1):
                    op1 = f"({op1})"
                if self.needs_parentheses(token, op2):
                    op2 = f"({op2})"
                # Creamos la expresión en notación infija y la apilamos
                expression = f"{op1} {token} {op2}"
                stack.append(expression)
        return stack[0]  # La expresión infija completa queda en el tope de la pila

    def needs_parentheses(self, operator, operand):
        # Determina si es necesario usar paréntesis en base a la precedencia de operadores
        if operand.isdigit():
            # Si el operando es un número, no se requieren paréntesis
            return False
        # Obtenemos la precedencia del operador externo y la del operador en el operando
        outer_prec = self.operators[operator][0]
        inner_prec = self.operators[operand.split()[1]][0]
        # Agregamos paréntesis si la precedencia interna es menor o si es igual y el operador es de izquierda
        return inner_prec < outer_prec or (inner_prec == outer_prec and operator in "-/")

    def execute(self, action):
        # Procesa una acción dada por el usuario
        parts = action.split()
        command = parts[0]  # Comando de la acción (EVAL, MOSTRAR o SALIR)

        if command == "SALIR":
            # Si el comando es SALIR, se termina la ejecución
            return False

        order = parts[1]  # Indica el orden de la notación (PRE o POST)
        expr = parts[2:]  # Tokens de la expresión

        if command == "EVAL":
            # Evalúa la expresión en base al orden (PRE o POST)
            result = self.eval_prefix(expr) if order == "PRE" else self.eval_postfix(expr)
            print(result)
        elif command == "MOSTRAR":
            # Convierte la expresión en notación infija en base al orden (PRE o POST)
            result = self.infix_from_prefix(expr) if order == "PRE" else self.infix_from_postfix(expr)
            print(result)

        return True  # Continua ejecutando hasta que se indique SALIR


def main():
    # Función principal que ejecuta el evaluador en un bucle hasta que el usuario quiera salir
    evaluator = ExpressionEvaluator()
    while True:
        action = input("Ingrese una acción: ")
        if not evaluator.execute(action):
            break  # Salir del bucle si el usuario ingresó SALIR


if __name__ == "__main__":
    main()

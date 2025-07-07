def calculator():
    while True:
        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            operation = input("Digite a operação (+, -, *, /): ")

            if operation == "+":
                result = num1 + num2
            elif operation == "-":
                result = num1 - num2
            elif operation == "*":
                result = num1 * num2
            elif operation == "/":
                if num2 == 0:
                    print("Divisão por zero não é permitida.")
                result = num1 / num2
            else:
                raise ValueError("Operação inválida. Use +, -, * ou /.")

            print(f"O resultado de {num1} {operation} {num2} é: {result}")
            break

        except Exception as e:
            print(f"Erro inesperado: {e}. Tente novamente.")


if __name__ == "__main__":
    calculator()

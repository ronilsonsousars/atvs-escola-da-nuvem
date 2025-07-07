def process_number(user_input):
    try:
        number = int(user_input)
        if number % 2 == 0:
            print(f"{number} é par.")
            return True
        else:
            print(f"{number} é ímpar.")
            return False
    except ValueError:
        print("Erro: Por favor, insira um número inteiro válido.")
        return None


def main():
    count_even = 0
    count_odd = 0

    while True:
        user_input = input(
            "Digite um número inteiro (ou 'fim' para sair do programar): "
        ).lower()

        if user_input == "fim":
            print("Saindo do programa...")
            break

        result = process_number(user_input)
        if result is True:
            count_even += 1
        elif result is False:
            count_odd += 1

    print(f"Números pares: {count_even}, Números ímpares: {count_odd}")


if __name__ == "__main__":
    main()

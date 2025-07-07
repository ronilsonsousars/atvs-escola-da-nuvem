def is_strong_password(password):
    if len(password) < 8:
        return False
    if not any(char.isdigit() for char in password):
        return False
    return True


def main():
    while True:
        user_input = input("Digite uma senha (ou 'sair' para encerrar): ")

        if user_input.lower() == "sair":
            print("Saindo do programa...")
            break
        if is_strong_password(user_input):
            print("Senha forte!")
        else:
            print(
                "Senha fraca. A senha deve ter pelo menos 8 caracteres e conter pelo menos um número."
            )


if __name__ == "__main__":
    main()

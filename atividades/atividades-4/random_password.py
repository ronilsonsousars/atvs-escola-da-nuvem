import random
import string


DEFAULT_CHARACTERS = string.ascii_letters + string.digits + "!@#$%&"


def random_password(size: int, characters: str = DEFAULT_CHARACTERS) -> str:
    """Gera uma senha aleatória com tamanho mínimo de 8 caracteres.
    Returns:
        int: O comprimento da senha validado.

    Raises:
        ValueError: Se a entrada não puder ser convertida para um número inteiro.
    """
    return "".join(random.choice(characters) for _ in range(size))


def validate_input() -> int:
    """Valida a entrada do usuário para o tamanho da senha."""
    while True:
        try:
            length = int(input("\nDigiteo tamnho da senha (mínimo 8): "))
            if length < 8:
                print("ERROR: O tamanho da senha deve ser maior ou igual a 8.")
                continue
            return length
        except ValueError:
            print("ERROR: Dado inserido inválido. Insira um número inteiro")


def main():
    try:
        password = random_password(validate_input())
        print(f"\nSua nova senha é: {password}")
    except ValueError as e:
        print(f"Error{e}")


if __name__ == "__main__":
    main()

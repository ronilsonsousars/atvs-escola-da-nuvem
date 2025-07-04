def palindrome(text):
    clean_text = "".join(char.lower() for char in text if char.isalnum())

    return clean_text == clean_text[::-1]


def check_palindrome(text):
    if palindrome(text):
        return f"O texto insiserido `{text}` é um exemplo de palindromo"
    else:
        return f"O texto insiserido `{text}` não é um exemplo de palindromo"


print(
    "Palíndromo é uma palavra ou frase que se lê igual de trás para frente. \nExemplos: radar, arara, rir\n"
)

phrase = input("Digite uma palavra ou frase: ")

result = check_palindrome(phrase)
print(result)

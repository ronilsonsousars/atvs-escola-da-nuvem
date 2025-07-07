def main():
    notes = []
    while True:
        user_input = input("Digite a nota do aluno (ou 'fim' para encerrar): ")

        if user_input.lower() == "fim":
            print("Saindo do programa...")
            break
        try:
            note = float(user_input)
            if 0 <= note <= 10:
                notes.append(note)
            else:
                print("Nota inválida. Digite uma nota de 0 a 10.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")

    if notes:
        average = sum(notes) / len(notes)
        print(f"A média da turma é: {average:.2f}")
    else:
        print("Nenhuma nota válida foi registrada.")


if __name__ == "__main__":
    main()

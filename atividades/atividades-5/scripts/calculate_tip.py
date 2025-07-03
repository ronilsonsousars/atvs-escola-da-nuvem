def calculate_tip():
    try:
        bill_amount = float(input("Informe o valor total da conta: R$ "))
        tip_percentage = float(input("Informe a porcentagem de gorjeta desejada (%): "))

        tip = (tip_percentage / 100) * bill_amount
        total_with_tip = bill_amount + tip

        print(f"\nGorjeta: R$ {tip:.2f}")
        print(f"Total a pagar com gorjeta: R$ {total_with_tip:.2f}")

    except ValueError:
        print("Por favor, insira valores numéricos válidos.")


calculate_tip()

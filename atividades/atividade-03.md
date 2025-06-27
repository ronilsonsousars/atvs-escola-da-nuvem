# Atividade Prática 03
Data: 27-06-2025 <br>

## 1- Classificador de Idade

```python
idade = int(input("Digite sua idade: "))

if idade < 0:
    print("Idade inválida.")
elif idade <= 12:
    print("Classificação: Criança")
elif idade <= 17:
    print("Classificação: Adolescente")
elif idade <= 59:
    print("Classificação: Adulto")
else:
    print("Classificação: Idoso")
```

## 2- Calculadora de IMC

```python
peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))

imc = peso / (altura ** 2)
print(f"Seu IMC é: {imc:.2f}")

if imc < 18.5:
    classificacao = "Abaixo do peso"
elif imc < 25:
    classificacao = "Peso normal"
elif imc < 30:
    classificacao = "Sobrepeso"
else:
    classificacao = "Obeso"

print(f"Classificação: {classificacao}")
```

## 3- Conversor de Temperatura
Crie um programa que converta temperaturas entre Celsius, Fahrenheit e Kelvin.
O usuário deve informar a temperatura, a unidade de origem e a unidade para qual deseja converter.

```python
# Tela de exibição
print("=" * 40)
print("CONVERSOR DE TEMPERATURA")
print("=" * 40)
print(f"""Unidades disponíveis:
- C: Celsius
- F: Fahrenheit
- K: Kelvin""")
print("-" * 40)

temperatura = float(input("\nDigite a temperatura a ser convertida: "))
print("\nEscolha a unidade de ORIGEM:")
unidade_origem = input("-> Digite C, F ou K: ").strip().upper()

print("\nEscolha a unidade de DESTINO:")
unidade_destino = input("-> Digite C, F ou K: ").strip().upper()

if unidade_origem == "C":
    if unidade_destino == "F":
        temperatura_convertida = (temperatura * 9/5) + 32
        print(f"\n{temperatura}°C é igual a {temperatura_convertida:.2f}°F")
    elif unidade_destino == "K":
        temperatura_convertida = temperatura + 273.15
        print(f"\n{temperatura}°C é igual a {temperatura_convertida:.2f}K")
    else:
        print("Unidade de destino inválida.")

elif unidade_origem == "F":
    if unidade_destino == "C":
        temperatura_convertida = (temperatura - 32) * 5/9
        print(f"\n{temperatura}°F é igual a {temperatura_convertida:.2f}°C")
    elif unidade_destino == "K":
        temperatura_convertida = (temperatura - 32) * 5/9 + 273.15
        print(f"\n{temperatura}°F é igual a {temperatura_convertida:.2f}K")
    else:
        print("Unidade de destino inválida.")

elif unidade_origem == "K":
    if unidade_destino == "C":
        temperatura_convertida = temperatura - 273.15
        print(f"\n{temperatura}K é igual a {temperatura_convertida:.2f}°C")
    elif unidade_destino == "F":
        temperatura_convertida = (temperatura - 273.15) * 9/5 + 32
        print(f"\n{temperatura}K é igual a {temperatura_convertida:.2f}°F")
    else:
        print("Unidade de destino inválida.")

else:
    print("Unidade de origem inválida.")
```

## 4- Verificador de Ano Bissexto

```python
ano = int(input("Digite um ano: "))

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f"{ano} é um ano bissexto.")
else:
    print(f"{ano} não é um ano bissexto.")
```


# Atividade Prática 02
Data: 26-06-2025 <br>

## 1- Conversor de Moeda

```python
valor_reais = 100.00
taxa_dolar = 5.20
taxa_euro = 6.15

valor_dolares = valor_reais / taxa_dolar
valor_euros = valor_reais / taxa_euro

print(f"Valor em Reais: R$ {valor_reais:.2f}")
print(f"Valor em Dólares: $ {valor_dolares:.2f}")
print(f"Valor em Euros: € {valor_euros:.2f}")
```

## 2- Calculadora de Desconto

```python
nome_produto = "Camiseta"
preco_original = 50.00
porcentagem_desconto = 20

desconto = (porcentagem_desconto / 100) * preco_original
preco_final = preco_original - desconto

print(f"Produto: {nome_produto}")
print(f"Preço Original: R$ {preco_original:.2f}")
print(f"Desconto: R$ {desconto:.2f} ({porcentagem_desconto}%)")
print(f"Preço Final: R$ {preco_final:.2f}")

```

## 3- Calculadora de Média Escolar

```python
nota1 = 7.5
nota2 = 8.0
nota3 = 6.5

media = (nota1 + nota2 + nota3) / 3

print(f"Nota 1: {nota1:.2f}")
print(f"Nota 2: {nota2:.2f}")
print(f"Nota 3: {nota3:.2f}")
print(f"Média: {media:.2f}")
```


## 4- Calculadora de Consumo de Combustível

```python
distancia_percorrida = 300  # em km
combustivel_gasto = 25  # em litros

consumo_medio = distancia_percorrida / combustivel_gasto

print(f"Distância Percorrida: {distancia_percorrida} km")
print(f"Combustível Gasto: {combustivel_gasto} litros")
print(f"Consumo Médio: {consumo_medio:.2f} km/l")
```

# Atividade Prática 07
Data: 10-07-2025 <br>

Lendo e escrevendo arquivos externos com Python.

## 1. Escrevendo um arquivo CSV

O script `escrever_csv.py` demonstra como escrever dados em um arquivo CSV.

```python
import csv

# Dados a serem escritos no arquivo CSV
dados = [
    ['Nome', 'Idade', 'Cidade'],
    ['Alice', 20, 'São Paulo'],
    ['Beatriz', 24, 'Rio de Janeiro'],
    ['Caio', 28, 'Belo Horizonte']
]

# Nome do arquivo CSV
arquivo_csv = 'dados.csv'

# Escrevendo os dados no arquivo CSV
with open(arquivo_csv, mode='w', newline='') as arquivo:
    escrever = csv.writer(arquivo)
    escrever.writerows(dados)

print(f"Arquivo '{arquivo_csv}' escrito com sucesso.")
```
## 2. Lendo um arquivo CSV

O script `ler_csv.py` demonstra como ler dados de um arquivo CSV.

```python
import csv

# Nome do arquivo CSV
arquivo_csv = 'dados.csv'

# Lendo os dados do arquivo CSV
with open(arquivo_csv, mode='r') as arquivo:
    leitor = csv.reader(arquivo)
    for linha in leitor:
        print(linha)
print(f"Arquivo '{arquivo_csv}' lido com sucesso.")
```

## 3. Escrevendo um arquivo JSON

O script `escrever_json.py` demonstra como escrever dados em um arquivo JSON.

```python
import json

# Dados a serem escritos no arquivo JSON
dados = [
    {'Nome': 'Alice', 'Idade': 20, 'Cidade': 'São Paulo'},
    {'Nome': 'Beatriz', 'Idade': 24, 'Cidade': 'Rio de Janeiro'},
    {'Nome': 'Caio', 'Idade': 28, 'Cidade': 'Belo Horizonte'}
]

# Nome do arquivo JSON
arquivo_json = 'dados.json'

# Escrevendo os dados no arquivo JSON
with open(arquivo_json, mode='w') as arquivo:
    json.dump(dados, arquivo)

print(f"Arquivo '{arquivo_json}' escrito com sucesso.")
```

## 4. Lendo um arquivo JSON

O script `ler_json.py` demonstra como ler dados de um arquivo JSON.

```python
import json

# Nome do arquivo JSON
arquivo_json = 'dados.json'

# Lendo os dados do arquivo JSON
with open(arquivo_json, mode='r') as arquivo:
    dados = json.load(arquivo)
    for item in dados:
        print(item)

print(f"Arquivo '{arquivo_json}' lido com sucesso.")
```

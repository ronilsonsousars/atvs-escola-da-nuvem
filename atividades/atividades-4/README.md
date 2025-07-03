# # Atividade Prática 04
Data: 03-07-2025 <br>

Uma coleção de scripts Python práticos e divertidos para diversas finalidades, desde a geração de senhas seguras até a consulta de informações em APIs públicas.

## 🔑 Gerador de Senhas Aleatórias

Este script gera senhas aleatórias e seguras com um comprimento definido pelo usuário.


**Como usar:**

1.  Execute o script em seu terminal:
    ```bash
    python random_password.py
    ```
2.  Quando solicitado, digite o comprimento desejado para a senha (o mínimo é 8 caracteres).
3.  A nova senha será exibida no terminal.

**[🕵️‍♂️ visualizar o código](scripts/random_password.py)**

## 📮 Consulta de CEP

Este programa consulta informações de endereço a partir de um CEP brasileiro, utilizando a API gratuita [ViaCEP](https://viacep.com.br/).

**Recursos:**

  * Exibe o logradouro, bairro, cidade e estado correspondentes ao CEP informado.
  * Valida a entrada para garantir que o CEP tenha 8 dígitos numéricos.

**Como usar:**

1.  Execute o script:
    ```bash
    python check-zip-code.py
    ```
2.  Digite um CEP válido (apenas números) quando solicitado.
3.  As informações do endereço serão exibidas.

**[📍 visualizar o código](scripts/check-zip_code.py)**

## 💹 Cotação de Moedas

Consulte a cotação de uma moeda estrangeira em relação ao Real Brasileiro (BRL) em tempo real. Este script utiliza a [AwesomeAPI](https://docs.awesomeapi.com.br/api-de-moedas) para obter os dados mais recentes.

**Recursos:**

  * Mostra o valor de compra atual (`bid`).
  * Informa o valor máximo (`high`) e mínimo (`low`) do dia.
  * Exibe a data e a hora da última atualização.

**Como usar:**

1.  Execute o script no terminal:
    ```bash
    python check_exchange_rate.py
    ```
2.  Insira o código da moeda que deseja consultar (por exemplo, `USD`, `EUR`, `ARS`).
3.  A cotação atual será exibida.

**[💱 visualizar o código](scripts/check_exchange_rate.py)**

## 🥸 Gerador de Perfis

Este script divertido gera um perfil de usuário completamente aleatório, ideal para preenchimento de dados de teste. A API [Random User Generator](https://randomuser.me/) é utilizada para buscar os dados.

**Recursos:**

  * Gera um nome completo.
  * Fornece um endereço de e-mail fictício.
  * Mostra o país de origem do usuário.

**Como usar:**

1.  Simplesmente execute o script:
    ```bash
    python generate_profile.py
    ```
2.  Um novo perfil de usuário aleatório será gerado e exibido a cada execução.

**[🧑‍💼 visualizar o código](scripts/generate_profile.py)**

-----

### **Dependências**

Para os scripts que fazem consultas a APIs (`check-zip-code.py`, `check_exchange_rate.py`, `generate_profile.py`), é necessário ter a biblioteca `requests` instalada.

Você pode instalá-la usando o pip:

```bash
pip install requests
```

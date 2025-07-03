import requests
from typing import Dict, Any


def fetch_exchange_data(currency_code: str) -> Dict[str, Any]:
    """
    Consulta a API AwesomeAPI para obter cotação de uma moeda em relação ao BRL.
    """
    url = f"https://economia.awesomeapi.com.br/json/last/{currency_code}-BRL"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()

        key = f"{currency_code}BRL"
        if key not in data:
            raise ValueError("Moeda não encontrada ou código invalido.")

        return data[key]

    except KeyError as e:
        raise KeyError("Erro na requisição - {e}") from e


def parse_exchange_data(data: Dict[str, Any]) -> Dict[str, str]:
    """
    Extrai dados relevantes da cotação.
    """
    try:
        return {
            "valor_atual": data["bid"],
            "valor_maximo": data["high"],
            "valor_minimo": data["low"],
            "data_hora": data["create_date"],
            "moeda": data["code"],
        }
    except KeyError as e:
        raise KeyError("Erro ao extrair dados da cotação: chave ausente - {e}") from e


def format_exchange_info(info: Dict[str, str]) -> str:
    """
    Formata os dados da cotação para exibição.
    """
    return (
        f"\nCotação atual de {info['moeda']} em relação ao BRL:\n"
        f"Valor atual: R$ {info['valor_atual']}\n"
        f"Valor máximo: R$ {info['valor_maximo']}\n"
        f"Valor mínimo: R$ {info['valor_minimo']}\n"
        f"Data e hora da última atualização: {info['data_hora']}\n"
    )


def validate_input() -> str:
    """Valida a entrada do usuário informando a cotação correta."""
    while True:
        try:
            validate_exchange = (
                input("Digite o código da moeda (ex: USD, EUR, GBP): ").strip().upper()
            )

            if not validate_exchange.isalpha() or len(validate_exchange) != 3:
                print("Código da moeda inválido. Use 3 letras, como 'USD' ou 'EUR'.")
                continue
            return validate_exchange

        except ValueError:
            print("ERROR: Valor inserido inválido.")


def main() -> None:
    """
    Exibi as informações de endereço.
    """
    currency = validate_input()

    try:
        raw_data = fetch_exchange_data(currency)
        exchange_info = parse_exchange_data(raw_data)
        formatedd = format_exchange_info(exchange_info)

        print(formatedd)

    except (requests.RequestException, ValueError, KeyError) as e:
        print(f"Erro ao consultar a cotação: {e}")


if __name__ == "__main__":
    main()

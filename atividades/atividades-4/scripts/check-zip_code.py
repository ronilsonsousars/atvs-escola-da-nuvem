import requests
from typing import Dict, Any


def fetch_address_data(cep: str) -> Dict[str, Any]:
    """
    Consulta a API ViaCEP com o CEP fornecido.
    """
    url = f"https://viacep.com.br/ws/{cep}/json/"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()

        if "erro" in data:
            raise ValueError("CEP não encontrado.")

        return data

    except requests.RequestException as e:
        raise requests.RequestException(f"Erro na requisição HTTP: {e}") from e


def parse_address_data(data: Dict[str, Any]) -> Dict[str, str]:
    """
    Extrai logradouro, bairro, cidade e estado dos dados do CEP.
    """
    try:
        return {
            "logradouro": data["logradouro"],
            "bairro": data["bairro"],
            "cidade": data["localidade"],
            "estado": data["uf"],
        }

    except KeyError as e:
        raise KeyError("Erro ao extrair dados do endereço: chave ausente - {e}") from e


def format_address(address: Dict[str, str]) -> str:
    """
    Formata os dados do endereço para exibição.
    """
    return (
        f"\nLogradouro: {address['logradouro']}\n"
        f"\nBairro: {address['bairro']}\n"
        f"\nCidade: {address['cidade']}\n"
        f"\nEstado: {address['estado']}\n"
    )


def validate_input() -> str:
    """Valida a entrada do usuário informando o CEP correto."""
    while True:
        try:
            validate_zip_code = input(
                "Digite o CEP da cidade que deseja buscar informações (somente números): "
            ).strip()

            if not validate_zip_code.isdigit() or len(validate_zip_code) != 8:
                print("CEP digitado inválido. Deve conter 8 números")
                continue
            return validate_zip_code

        except ValueError:
            print(
                "ERROR: CEP inserido inválido. Insira somente números inteiro e o CEP deve conter 8 números"
            )


def main() -> None:
    """
    Exibi as informações de endereço.
    """
    cep = validate_input()

    try:
        raw_data = fetch_address_data(cep)
        address = parse_address_data(raw_data)
        formatted = format_address(address)
        print(formatted)

    except (requests.RequestException, ValueError, KeyError) as e:
        print(f"Erro ao consultar o CEP: {e}")


if __name__ == "__main__":
    main()

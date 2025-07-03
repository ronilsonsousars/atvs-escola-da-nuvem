import requests
from typing import Dict, Any


def fetch_user_data() -> Dict[str, Any]:
    """
    Busca dados de um usuário aleatório da API Random User Generator.
    """
    url = "https://randomuser.me/api/"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()

        if "results" not in data or not data["results"]:
            raise ValueError("Resposta da API não contém dados do usuário.")

        return data

    except requests.RequestException as e:
        raise requests.RequestException(f"Erro ao acessar a API: {e}") from e


def parse_user_profile(data: Dict[str, Any]) -> Dict[str, str]:
    """
    Extrai informações relevantes do perfil do usuário.
    """
    try:
        user = data["results"][0]
        name = f"{user['name']['first']} {user['name']['last']}"
        email = user["email"]
        country = user["location"]["country"]

        return {"name": name, "email": email, "country": country}

    except KeyError as e:
        raise KeyError("Erro ao extrair dados do usuário: chave ausente - {e}") from e


def format_profile(profile: Dict[str, str]) -> str:
    """
    Formata os dados do endereço para exibição.
    """
    return (
        f"\nNome: {profile['name']}\n"
        f"\nEmail: {profile['email']}\n"
        f"\nPaís: {profile['country']}\n"
    )


def main() -> None:
    """
    Exibi as informações de perfil.
    """
    print("Gerando o perfil do usuário aleatório...")
    try:
        raw_data = fetch_user_data()
        profile = parse_user_profile(raw_data)
        formatedd = format_profile(profile)

        print(formatedd)

    except (requests.RequestException, ValueError, KeyError) as e:
        print(f"Erro ao gerar  o perfil: {e}")


if __name__ == "__main__":
    main()

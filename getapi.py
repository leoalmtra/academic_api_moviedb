import requests

API_KEY = "API_KEY"
BASE_URL = "https://api.themoviedb.org/3/search/movie"

def consultar_filme(titulo):
    params = {
        "api_key": API_KEY,
        "query": titulo,
        "language": "pt-BR"
    }

    response = requests.get(BASE_URL, params=params)

    if response.status_code != 200:
        return {"erro": "Falha ao acessar a API"}

    dados = response.json()

    # Verifica se encontrou algum filme
    if not dados["results"]:
        return {"erro": "Filme não encontrado"}

    filme = dados["results"][0]  # pega o primeiro resultado

    titulo_filme = filme.get("title", "Não informado")
    ano = filme.get("release_date", "Não informado")[:4]
    sinopse = filme.get("overview", "Sinopse não disponível")

    return {
        "titulo": titulo_filme,
        "ano": ano,
        "sinopse": sinopse
    }
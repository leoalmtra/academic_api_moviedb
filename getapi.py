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

    titulo_filme = filme.get("title") or "Não informado"
    release_date = filme.get("release_date")
    if release_date:
        ano = release_date[:4]
    else:
        ano = "S/D"
    sinopse = filme.get("overview") or "Não há sinopse disponível"

    return {
        "titulo": titulo_filme,
        "ano": ano,
        "sinopse": sinopse

    }

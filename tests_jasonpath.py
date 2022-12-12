import requests
import jsonpath


# GET Avaliações
avaliacoes = requests.get('http://localhost:8000/api/v2/avaliacoes/')

resultados = jsonpath.jsonpath(avaliacoes.json(), 'results')
print(resultados)

primeira = jsonpath.jsonpath(avaliacoes.json(), 'results[0]')
print(primeira)

nome = jsonpath.jsonpath(avaliacoes.json(), 'results[0].nome')
print(nome)

avaliacoes = jsonpath.jsonpath(avaliacoes.json(), 'results[*].avaliacao')
print(avaliacoes)

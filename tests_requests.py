import requests


# GET Avaliações
avaliacoes = requests.get('http://localhost:8000/api/v2/avaliacoes/')

# Acessando o código de Status HTTP
#print(avaliacoes.status_code)

# Acessando os dados de resposta
#print(avaliacoes.json())

# Acessando os registros
#print(avaliacoes.json()['results'][0]['nome'])


# GET Cursos

headers = {'Authorization': 'Token aaa481823a32895b3b81eea307c249a891264ed7'}
cursos = requests.get(url='http://localhost:8000/api/v2/cursos/', headers=headers)

print(cursos.json())
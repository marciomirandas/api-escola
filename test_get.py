import requests


url_cursos = 'http://localhost:8000/api/v2/cursos/'
headers = {'Authorization': 'Token aaa481823a32895b3b81eea307c249a891264ed7'}

resultado = requests.get(url=url_cursos, headers=headers)

# Testando se o endpoint está correto
assert resultado.status_code == 200

# Testando a quantidade de registro
assert resultado.json()['count'] == 3

# Testando o título do primeiro curso está correto
assert resultado.json()['results'][0]['titulo'] == 'API Rest'

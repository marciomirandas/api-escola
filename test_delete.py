import requests


url_cursos = 'http://localhost:8000/api/v2/cursos/'
headers = {'Authorization': 'Token 50a4c79424b8cea6a4215cf394e19dac4b76e3f0'}
id = '3'

resultado = requests.delete(url=f'{url_cursos}{id}', headers=headers)

# Testando o código de status HTTP
assert resultado.status_code == 204


# Testando se o tamanho do conteúdo retornado é 0
assert len(resultado.text) == 0
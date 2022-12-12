import requests


url_cursos = 'http://localhost:8000/api/v2/cursos/'
headers = {'Authorization': 'Token 50a4c79424b8cea6a4215cf394e19dac4b76e3f0'}
id = '1'
curso_atualizado = {
    "titulo": "API Rest V2",
    "url": "http://www.apirest.com.br",
    "ativo": "True"
}

resultado = requests.put(url=f'{url_cursos}{id}', headers=headers, data=curso_atualizado)

# Testando o código de status HTTP
assert resultado.status_code == 200


# Testando se o nome do curso é o mesmo do informado
assert resultado.json()['titulo'] == curso_atualizado['titulo']

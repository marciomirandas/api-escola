import requests


url_cursos = 'http://localhost:8000/api/v2/cursos/'
headers = {'Authorization': 'Token 50a4c79424b8cea6a4215cf394e19dac4b76e3f0'}
novo_curso = {
    "titulo": "PHP3",
    "url": "http://www.php.com.br/3"
}

resultado = requests.post(url=url_cursos, headers=headers, data=novo_curso)

# Testando o código de status HTTP
assert resultado.status_code == 201


# Testando se o nome do curso é o mesmo do informado
assert resultado.json()['titulo'] == novo_curso['titulo']

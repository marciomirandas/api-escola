import requests


class TestCursos:
    url_cursos = 'http://localhost:8000/api/v2/cursos/'
    headers = {'Authorization': 'Token 50a4c79424b8cea6a4215cf394e19dac4b76e3f0'}


    def test_get_cursos(self):
        resposta = requests.get(url=self.url_cursos, headers=self.headers)

        assert resposta.status_code == 200


    def test_get_curso(self):
        resposta = requests.get(url=f'{self.url_cursos}1/', headers=self.headers)

        assert resposta.status_code == 200


    def test_post_curso(self):
        novo_curso = {
            "titulo": "PHP4",
            "url": "http://www.php4.com.br/4"
        }

        resposta = requests.post(url=self.url_cursos, headers=self.headers, data=novo_curso)

        assert resposta.status_code == 201
        assert resposta.json()['titulo'] == novo_curso['titulo']


    def test_put_curso(self):
        atualizado = {
            "titulo": "PHP3",
            "url": "http://www.php2dsfd.com.br/12"
        }

        resposta = requests.put(url=f'{self.url_cursos}1/', headers=self.headers, data=atualizado)

        assert resposta.status_code == 200



    def test_put_titulo_curso(self):
        atualizado = {
            "titulo": "PHP3.2",
            "url": "http://www.phpdsfdsj.com.br/98"
        }

        resposta = requests.put(url=f'{self.url_cursos}1/', headers=self.headers, data=atualizado)

        assert resposta.json()['titulo'] == atualizado['titulo']


    def test_delete_curso(self):
        
        resposta = requests.delete(url=f'{self.url_cursos}1/', headers=self.headers)

        assert resposta.status_code == 204 and len(resposta.text) == 0
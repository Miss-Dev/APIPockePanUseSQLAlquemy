from flask import Flask, request
from flask_restful import Api, Resource
from models import Usuarios, Pontos, Pontuacao, Charadas
from flask_httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()
app = Flask(__name__)
api = Api(app)


@auth.verify_password
def verificacao(login, senha):
    if not (login, senha):
        return False
    return Usuarios.query.filter_by(login=login, senha=senha).first()


class Ponto(Resource):
    @auth.verify_password()
    def post(self):
        try:
            dados = request.json
            ponto = Pontos(latitude=dados['latitude'], longitude=dados['longitude'])
            ponto.save()
            response = {
                'message': 'Ponto cadastrado no mapa',
                'codigo_ponto': ponto.codigo_ponto,
                'latitude': ponto.latitude,
                'longitude': ponto.longitude
            }
        except:
            response = {
                           "message": "Erro ao cadastrar ponto"
                       }, 500
        return response

    @auth.verify_password()
    def get(self):
        pontos = Pontos.query.all()
        return {
            'pontos_cadastrados': pontos
        }


class Charada(Resource):
    @auth.verify_password()
    def post(self):
        try:
            dados = request.json
            charada = Charadas(descricao=dados['descricao'], id_ponto=dados['id_ponto'])
            charada.save()
            response = {
                'message': 'Charada cadastrada com sucesso!',
                'id_charada': charada.id_charada,
                'descricao': charada.descricao
            }
        except:
            response = {
                           'message': 'Erro ao cadastrar charada'
                       }, 500
        return response

    @auth.verify_password()
    def get(self):
        charada = Charadas.query.all()
        return {
            'charadas_cadastradas': charada
        }


class PontuaJogadores(Resource):

    def post(self):
        try:
            dados = request.json
            pontuacao = Pontuacao(primeiro_vencedor=dados['primeiro'], segundo_vencedor=dados['segundo'],
                                  terceiro_vencedor=dados['terceiro'], id_charada=dados['id_charada'])
            pontuacao.save()
            response = {
                'message': 'Pontuacao cadastrada com sucesso!',
                'charada_relacionada': pontuacao.id_charada
            }
        except:
            response = {
                           'message': 'Erro ao cadastrar charada'
                       }, 500
        return response


api.add_resource(Ponto, '/pontos/')
api.add_resource(Charada, '/charadas/')

if __name__ == '__main__':
    app.run(debug=True)

from flask import Blueprint, jsonify, request
from . import db
from .models import Movie
#from .busca import pesquisar_registro
from .teste import pesquisar

main = Blueprint('main', __name__)

@main.route('/add_movie', methods=['POST'])
def add_movie():
    movie_data = request.get_json()

    new_movie = Movie(title=movie_data['title'], rating=movie_data['rating'])

    db.session.add(new_movie)
    db.session.commit()

    return 'Pronto', 201

@main.route('/movies', methods=['GET'])
def movies():

    movie_list = Movie.query.all()
    movies = []

    for movie in movie_list:
        movies.append({'title' : movie.title, 'rating' : movie.rating})

    return jsonify({'movies': movies})

@main.route('/search', methods=['GET'])
def search():
    return pesquisar('fisicos.txt', 'Einstein'), 200
    #f = open("fisicos.txt", "r")
    #texto = pesquisar('fisicos.txt', 'Einstein')
    #Lembrar de fechar o arquivo caso seja muito grande
    #Por causa da performance

#@main.route('/mostrar', methods=['GET', 'POST'])
#def busca():
    #pesquisa = pesquisar_registro('fel')
    #pesquisa = 'fel'
    #busca_data= request.get_json()
#    return pesquisar_registro('kel'), 200

@main.route('/pesquisar', methods=['POST'])
def pesquisar():
    data = request.json #usar data na função e retornar a busca em json
    return jsonify(data), 200 #trocar request.json apra request.form caso não dê certo. tem também o request.data

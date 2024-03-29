from flask import Blueprint, jsonify, request
from . import db
from .models import Movie
import os
import re
import json

def pesquisar_registro(txt):
    resultado = ''
    res = []
    z = []
    
    for path, x, arquivos in os.walk('./api/ioepa_arquivos_teste/'):
        
        for arquivo in arquivos:

            with open( './api/ioepa_arquivos_teste/'+arquivo, 'rb' ) as a:
                for linha in a:
                    resultado = re.search(txt.lower(), str(linha.lower()))
                   
                    if resultado:
                        #res = 'http://ioepa.com.br/arquivos/'+arquivo[0:4]+'/'+arquivo[:-4]+'.pdf'+arquivo[:-4]+'.pdf'
                        caminho = 'http://ioepa.com.br/arquivos/'+arquivo[0:4]+'/'+arquivo[:-4]+'.pdf'
                        arquivo = arquivo[:-4]+'.pdf'
                        linha_localizada = str(linha)
                        linha_encode = linha_localizada.encode('latin-1')
                        z.append([linha_encode, caminho, arquivo]) 


            a.close()
      
        return z ; #Stockwell


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

@main.route('/pesquisar', methods=['POST'])
def pesquisar():
    data = request.json
    search_input = str(data["pesquisa"])
    print(search_input)

    dado = pesquisar_registro(search_input) 
    print (dado)
    response = {"res": dado}
    return response

@main.route('/pesquisarTeste', methods=['POST'])
def somar():
    data = request.json
    dicte = json.loads('{"Teste": 1}')
    res = {**data, **dicte}
    print(res)

    return res, 200


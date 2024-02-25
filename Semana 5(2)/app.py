#1- importar o flask para a sua página
from flask import Flask, render_template 

import urllib.request, json

#2- criar uma variável com a classe Flask(__name__). Essa variável vai trazer o flask para o seu código 
#esse app é uma instância
app = Flask(__name__)

#3- criar rota: @app.route("/")
# Esse decorator informa ao flask qual URL vai ser acionada. When a user navigates to the root URL (/), Flask will execute the function immediately below the decorator and return the result to the user's browser.
#@: This symbol indicates that app.route() is a decorator, which is a special kind of function that modifies the behavior of another function without changing its source code.
#para criar um servidor local 

@app.route("/") #simbolo de página inicial  # Estamos criando o caminho da URL!!!!!!!!
def get_list_characters_page():
    url = 'https://rickandmortyapi.com/api/character/'
    # abrir a reponse
    response = urllib.request.urlopen(url)
    #variavel para ler os resultados
    data = response.read()
    #variavel que formata para json
    dict = json.loads(data)

    return render_template("characters.html", characters=dict['results'] ) #retorna um HTML. 2º parâmetro pode ter variáveis


@app.route('/locations')
def get_locations():
    url = 'https://rickandmortyapi.com/api/location'
    response = urllib.request.urlopen(url)
    data = response.read()
    location_data = json.loads(data)

    locations = []
    for item in location_data['results']:
        locations.append({
            'name': item['name'],
            'type': item['type'],
            'dimension': item['dimension']
            })

    return {'dicionario' : locations}


@app.route('/locations/<id>')
def locations(id):
    url = f'https://rickandmortyapi.com/api/location/{id}'
    response = urllib.request.urlopen(url)
    data = response.read()
    location_data = json.loads(data)

    location = {
        'name': location_data['name'],
        'type': location_data['type'],
        'dimension': location_data['dimension']
    }

    return render_template("dimension.html", dicionario = location)


@app.route("/lista") 
def get_list_characters():

    # criar variavel para receber o link da API (endpoint):
    url = 'https://rickandmortyapi.com/api/character/'
    response = urllib.request.urlopen(url)
    characters = response.read()
    dict = json.loads(characters)

    characters = []

    # modo mais fácil
    for item in dict['results']:
        characters.append({
            'name': item['name'], 
            'status': item['status'],
            'species': item['species'],
            'gender': item['gender'], 
            'origin': item['origin'],
            'location': item['location']
            })
    return {'personagens': characters}

    # for character in dict['results']:
    #     character =  {
    #     'name': character['name'],
    #     'status': character['status']
    #     }  

    #     characters.append(character)
    # return {'characters': characters}



@app.route("/profile/<id>")  #<> é o simbolo do flask para uma variável. Eu vou passar o valor de id 
def get_profile(id):
    url = 'https://rickandmortyapi.com/api/character/' + id
    response = urllib.request.urlopen(url)
    data = response.read()
    character_data = json.loads(data) #atributo da variável

    character_profile = {
        'name': character_data['name'],
        'status': character_data['status'],
        'species': character_data['species'],
        'gender': character_data['gender'],
        'origin': character_data['origin']['name'],
        'location': character_data['location']['name'], 
        'image': character_data['image']
    }


    return render_template("profile.html", profile= character_profile ) #retorna um HTML. 2º parâmetro pode ter variáveis




# dados = {'chave': 'valor'}

# @app.route('/oi')
# def hello_world2():
#     return {
#         'endpoint': dados
#     }

# @app.route('/luan')
# def hello_world3():
#     return '<a href="/oi">Clique aqui!</a>'

#1- importar o flask para a sua página
from flask import Flask, render_template 

import urllib.request, json

#2- criar uma variável com a classe Flask(__name__). Essa variável vai trazer o flask para o seu código 
#esse app é uma instância
app = Flask(__name__)



# ======================================== PERSONAGENS ========================================

# all characters  ------------------------------------------------

#3- criar rota: @app.route("/")
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


# characters especifico ------------------------------------------------

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


# JSON characters ------------------------------------------------
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


# ======================================== LOCALIZAÇÕES ========================================

@app.route("/all_dimensions") #simbolo de página inicial  # Estamos criando o caminho da URL!!!!!!!!
def get_dimensions():
    url = 'https://rickandmortyapi.com/api/location/'
    # abrir a reponse
    response = urllib.request.urlopen(url)
    #variavel para ler os resultados
    data = response.read()
    #variavel que formata para json
    dict = json.loads(data)

    return render_template("all_dimensions.html", dimensions=dict['results'] ) #retorna um HTML. 2º parâmetro pode ter variáveis



# locations especifico ------------------------------------------------
@app.route('/dimension/<id>')
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


# locations JSON ------------------------------------------------
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



# ======================================== EPISÓDIOS ========================================

# all episodes  ------------------------------------------------
@app.route("/all_episodes") #simbolo de página inicial  # Estamos criando o caminho da URL!!!!!!!!
def get_episodes():
    url = 'https://rickandmortyapi.com/api/episode/'
    # abrir a reponse
    response = urllib.request.urlopen(url)
    #variavel para ler os resultados
    data = response.read()
    #variavel que formata para json
    dict = json.loads(data)

    return render_template("all_episodes.html", episodes=dict['results'] ) #retorna um HTML. 2º parâmetro pode ter variáveis


# episode especifico ------------------------------------------------

@app.route("/episode/<id>")  #<> é o simbolo do flask para uma variável. Eu vou passar o valor de id 
def get_episode(id):
    url = 'https://rickandmortyapi.com/api/episode/' + id
    response = urllib.request.urlopen(url)
    data = response.read()
    episode_data = json.loads(data) #atributo da variável
    data = episode_data.get("characters", {})
    print(data)
    episode_profile = {
        'id': episode_data['id'],
        'name': episode_data['name'],
        'air_data': episode_data['air_date'],
        'personagens': data
    }
    return render_template("episode.html", episode = episode_profile ) #retorna um HTML. 2º parâmetro pode ter variáveis


# JSON episodes ------------------------------------------------
@app.route("/lista_ep") 
def get_list_episodes():

    # criar variavel para receber o link da API (endpoint):
    url = 'https://rickandmortyapi.com/api/episode/'
    response = urllib.request.urlopen(url)
    episodes = response.read()
    dict = json.loads(episodes)

    episodes = []

    # modo mais fácil
    for item in dict['results']:
        episodes.append({
            'id': item['id'],
            'name': item['name'], 
            })
    return {'personagens': episodes}

    # for character in dict['results']:
    #     character =  {
    #     'name': character['name'],
    #     'status': character['status']
    #     }  

    #     characters.append(character)
    # return {'characters': characters}


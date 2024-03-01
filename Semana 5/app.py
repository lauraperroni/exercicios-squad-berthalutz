from flask import Flask, render_template 
import urllib.request, json
app = Flask(__name__)



# ======================================== PERSONAGENS ========================================

# all characters  ------------------------------------------------

#3- criar rota: @app.route("/")
@app.route("/") 
def get_list_characters_page():
    url = 'https://rickandmortyapi.com/api/character/'
    # abrir a reponse
    response = urllib.request.urlopen(url)
    #variavel para ler os resultados
    data = response.read()
    #variavel que formata para json
    dict = json.loads(data)

    return render_template("characters.html", characters=dict['results'] )


# characters especifico ------------------------------------------------

@app.route("/profile/<id>")  
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
    return render_template("profile.html", profile= character_profile ) 


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



# ======================================== LOCALIZAÇÕES ========================================

@app.route("/all_dimensions") 
def get_dimensions():
    url = 'https://rickandmortyapi.com/api/location/'
    # abrir a reponse
    response = urllib.request.urlopen(url)
    #variavel para ler os resultados
    data = response.read()
    #variavel que formata para json
    dict = json.loads(data)

    return render_template("all_dimensions.html", dimensions=dict['results'] ) 


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
@app.route("/all_episodes") 
def get_episodes():
    url = 'https://rickandmortyapi.com/api/episode/'
    # abrir a reponse
    response = urllib.request.urlopen(url)
    #variavel para ler os resultados
    data = response.read()
    #variavel que formata para json
    dict = json.loads(data)

    return render_template("all_episodes.html", episodes=dict['results'] ) 


# episode especifico ------------------------------------------------

@app.route("/episode/<id>")  
def get_episode(id):
    url = 'https://rickandmortyapi.com/api/episode/' + id
    response = urllib.request.urlopen(url)
    data = response.read()
    episode_data = json.loads(data)

    # Fazendo o get de cada personagem
    data = episode_data["characters"]
    complete_data = []
    for item in data: 
        # Em cada volta --> O item vai ser o valor DO LINK (URL) de um personagem

        url_personagem = item 
        response_personagem = urllib.request.urlopen(url_personagem)
        data_personagem = response_personagem.read()
        personagem = json.loads(data_personagem) 
        complete_data.append([personagem['name'], personagem['image']])

    #Pegando os atributos do episódio 
    episode_profile = {
        'id': episode_data['id'],
        'name': episode_data['name'],
        'air_data': episode_data['air_date'],
        'personagens': complete_data
    }
    return render_template("episode.html", episode = episode_profile )


# JSON episodes ------------------------------------------------
@app.route("/lista_ep") 
def get_list_episodes():

    url = 'https://rickandmortyapi.com/api/episode/'
    response = urllib.request.urlopen(url)
    episodes = response.read()
    dict = json.loads(episodes)

    episodes = []

    for item in dict['results']:
        episodes.append({
            'id': item['id'],
            'name': item['name'], 
            })
    return {'personagens': episodes}



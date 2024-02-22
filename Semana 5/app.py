from flask import Flask, render_template
import urllib.request
import json

app = Flask(__name__)

@app.route('/')
def get_list_elements_page():
    url = "https://rickandmortyapi.com/api/character/"
    context = ssl._create_unverified_context()
    response = urllib.request.urlopen(url, context=context)
    data = response.read()
    dict = json.loads(data)
    
    return render_template("characters.html", characters=dict['results'])

@app.route('/profile/<id>')
def get_profile(id):
    url = "https://rickandmortyapi.com/api/character/"+id #+id
    context = ssl._create_unverified_context()
    response = urllib.request.urlopen(url, context=context)
    data = response.read()
    dict = json.loads(data)
    
    return render_template("profile.html", profile=dict)

@app.route('/lista')
def get_list_elements():
    url = "https://rickandmortyapi.com/api/character/"
    context = ssl._create_unverified_context()

    try:
        response = urllib.request.urlopen(url, context=context)
        characters = response.read()
        dict = json.loads(characters)

        characters_list = []

        for character in dict['results']:
            character_data = {
                "name": character['name'],
                "status": character['status'],
                "species": character['species'],
            }
            characters_list.append(character_data)
        
        return {"characters": characters_list}
    except Exception as e:
        return {"error": str(e)}

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


if __name__ == '__main__':
    app.run(debug=True)

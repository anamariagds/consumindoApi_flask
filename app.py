from flask import Flask, render_template, request
import urllib.request, json

app = Flask(__name__) #__name__ diz ao python para reconhecer o nome do seu arquivo

@app.route("/")
def get_list_characters_page():
    url = "https://rickandmortyapi.com/api/character/"
    response = urllib.request.urlopen(url)
    data = response.read()
    characters_list = json.loads(data) #um dicionario de dados

    return render_template("characters.html", characters=characters_list["results"])

@app.route("/personagem/<id>")
def get_profile(id):
    url = "https://rickandmortyapi.com/api/character/" + id
    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)

    return render_template("profile.html", profile=dict)

@app.route("/episodios")
def get_episodes_list():
    url = "https://rickandmortyapi.com/api/episode"
    response = urllib.request.urlopen(url)
    data = response.read()
    dict_episodes = json.loads(data)

    return render_template("episodes.html", episodes=dict_episodes['results'])
    

@app.route("/lista")
def get_list_characters():
    url = "https://rickandmortyapi.com/api/character/"
    response = urllib.request.urlopen(url) #Abrindo a url passada na variavel url
    characters = response.read()
    dict = json.loads(characters) #as informações da lista json são convertidas em um dicionário python

    characters = []

    for character in dict["results"]:
        character = {
            "name" : character["name"],
            "status": character["status"]
        }
        characters.append(character)

    return {"characters": characters}


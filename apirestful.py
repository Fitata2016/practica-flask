from flask import Flask, request
from flask_api import status
import requests
import platform
import psutil

app = Flask(__name__)
# API RAM Y OS
ram = psutil.virtual_memory().percent
os = platform.platform()

@app.route("/apiram")
def status():
    return {"Status":"Running, 200","Sistema Operativo":f"{os}","Uso de RAM":f"{ram}"},200

# API POKEMON
ENDPOINT_POKEAPI = "https://pokeapi.co/api/v2/pokemon/100" #cambia el numero final del enpoint entre 1-1000
response = requests.get(ENDPOINT_POKEAPI) 
response = response.json()
ability_name= response["abilities"][0]["ability"]["name"]

@app.route("/apipoke")
def ability():
       
    return f"La habilidad de tu pokemon es: {ability_name}"
print(ability())

if __name__=="__main__":
    app.run(host="127.0.0.2", port=10000, debug=True)

#ENPOINT: 127.0.0.2:10000 + "enpoint"
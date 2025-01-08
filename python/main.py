import requests

URL = 'https://api.pokemonbattle.ru/v2'
Token = '9e9c36b215ffa9c6dc7f828f5c3b43e1'
Header = {'content-type' : 'application/json', 'trainer_token': Token }


body_create = {
    "name": "pikachu",
    "photo_id": 1
}

body_new_name = {
    "pokemon_id": "184329",
    "name": "govyadina",
    "photo_id": 2
}

body_in_pokeball = {
    "pokemon_id": "184329"
}

body_knockout = {
    "pokemon_id": "95428"
}

response_create = requests.post(url = f'{URL}/pokemons', headers=Header, json=body_create)
print (response_create.text)

response_new_name = requests.put(url = f'{URL}/pokemons', headers=Header, json=body_new_name)
print (response_new_name.text)

response_in_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers=Header, json=body_in_pokeball)
print (response_in_pokeball.text)

'''response_knockout = requests.post(url = f'{URL}/pokemons/knockout', headers=Header, json=body_knockout)
print (response_knockout.text)'''
import requests
import pytest



URL = 'https://api.pokemonbattle.ru/v2'
Token = '9e9c36b215ffa9c6dc7f828f5c3b43e1'
Header = {'content-type' : 'application/json', 'trainer_token': Token }
trainer_id= '12760'

def test_status_code():
    response = requests.get(url= f'{URL}/trainers', params= {'trainer_id': trainer_id})
    assert response.status_code == 200


def test_trainer_id():
    response_trainer = requests.get(url= f'{URL}/trainers', params= {'trainer_id': trainer_id})
    assert response_trainer.json()["data"][0]["id"] == '12760'
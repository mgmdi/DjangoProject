import requests
from django.conf import settings

def get_user(user_id):
    response = requests.get('http://5e84eab9a8fdea00164ace7f.mockapi.io/customer')
    if(response.status_code == '200'):
        return response.json()
    else:
        return None


def update_user(user_data):
    print('update user')


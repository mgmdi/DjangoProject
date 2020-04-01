import requests
from django.conf import settings

def get_user(user_id):
    response = requests.get(settings.API_URL + user_id)
    return response.json()


def update_user(user_data):
    print('update user')


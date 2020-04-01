import requests
from django.conf import settings

def get_user(user_id):
    response = requests.get(settings.API_URL + user_id)
    if(response):
        return response.json()
    else:
        return None


def update_user(user_data, user_id):
    response = requests.post(settings.API_URL + user_id)
    if(response):
        return True
    else:
        return False



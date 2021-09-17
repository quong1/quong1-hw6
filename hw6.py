import requests
import os
from dotenv import find_dotenv, load_dotenv
import base64

load_dotenv(find_dotenv())
CLIENT_ID=os.getenv('CLIENT_ID')
CLIENT_SECRET=os.getenv('CLIENT_SECRET')

AUTH_URL = 'https://accounts.spotify.com/api/token'
ENDPOINTS_URL = 'https://api.spotify.com/v1/browse/new-releases'

join = f"{CLIENT_ID}:{CLIENT_SECRET}"
joinbytes = join.encode('ascii')
join64 = base64.b64encode(joinbytes)
join64_id=join64.decode('ascii')

def getToken():
    # POST
    auth_response = requests.post(AUTH_URL, 
        headers={
            'Authorization' : f'Basic {join64_id}'
            },
        data={
            'grant_type':'client_credentials'
            }
    )

    return auth_response.json()['access_token']


def getRelease(token):
    # GET
    response = requests.get(ENDPOINTS_URL, 
        headers={"Authorization": f"Bearer {token}"})
    reponse_data = response.json()
    try:
        for i in range(11):
            print(reponse_data['albums']['items'][i]['name'])
    except KeyError:
        print("Couldn't fetch new realeases!")


getRelease(getToken())
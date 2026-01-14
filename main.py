#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import requests
import twilio
API_KEY='FyG4Srx47QoH3KTmCqhEb7GkMpM1FKMd'
API_SECRET='dT10vDhU4EKqvyzC'
# password='5k*vbnmF72C?Bn8'
# email='dilyana.m.bodurova@gmail.com'

def take_token():
    # currently doesn't work
    auth_url='https://test.api.amadeus.com/v1/security/oauth2/token'
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    body={f'grant_type=client_credentials&client_id={API_KEY}&client_secret={API_SECRET}'}
    response = requests.post(url=auth_url,headers=headers, data=body)
    print(response.json())


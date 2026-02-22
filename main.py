#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve
# the program requirements.
import requests
import twilio
API_KEY='FyG4Srx47QoH3KTmCqhEb7GkMpM1FKMd'
API_SECRET='dT10vDhU4EKqvyzC'
SHEETY_ENDPOINT = 'https://docs.google.com/spreadsheets/d/10__l6VOu4YQLdRjI6q31kMzbkw6LNQC4bbktnul6dHU/edit?gid=0#gid=0'
amadeus_password='5k*vbnmF72C?Bn8'
email='dilyana.m.bodurova@gmail.com'



# 4. Pass the data back to the main.py file, so that you can print the data from main.py
from data_manager import DataManager
data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
# print(sheet_data)

#  5. In main.py check if sheet_data contains any values for the "iataCode" key.
#  If not, then the IATA Codes column is empty in the Google Sheet.
#  In this case, pass each city name in sheet_data one-by-one
#  to the FlightSearch class to get the corresponding IATA code
#  for that city using the Flight Search API.
#  You should use the code you get back to update the sheet_data dictionary.
if sheet_data[0]["iataCode"] == "":
    from flight_search import FlightSearch
    flight_search = FlightSearch()
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
    print(f"sheet_data:\n {sheet_data}")

    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()
#---------my code ---------------
# def take_token():
#     # currently doesn't work
#     auth_url='https://test.api.amadeus.com/v1/security/oauth2/token'
#     headers = {'Content-Type': 'application/x-www-form-urlencoded'}
#     body = {'grant_type': 'client_credentials', 'client_id': API_KEY, 'client_secret': API_SECRET}
#     response = requests.post(url=auth_url,headers=headers, data=body)
#     print(response.json())
#
# take_token()
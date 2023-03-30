import requests
from twilio.rest import Client

# some instances for weather data
api_key = "***" # your api key
weather_endpoint = "https://api.openweathermap.org/data/2.5/forecast"
weather_params = {
    "lat": 0, # your lat
    "lon": 0, # your lon
    "appid": api_key,
}

# importing weather data
weather_data_response = requests.get(weather_endpoint, weather_params)
weather_data_response.raise_for_status()

# twilio part
account_sid = '***' # your sid
auth_token = '***' # your token


def is_rainy():
    """
    check whether day is rainy
    :return: if day is rainy or snowy, it True
    """
    weather_of_12hour = weather_data_response.json()['list'][:4]
    for day in weather_of_12hour:
        if day['weather'][0]['id'] < 700:
            return True


if is_rainy():
    client = Client(account_sid, auth_token)
    try:
        message = client.messages \
            .create(
            body="It is a rainy day. Don't forget your umbrella",
            from_='***', # your twilio number
            to='***', # the number that you want to send message
        )
        print(message.status)
    except Exception as e:
        print(f"Error: {e}")
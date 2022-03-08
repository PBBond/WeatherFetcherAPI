import  requests

API_KEY = 'f43f69b3cc7aa14d8e3176e968867af3'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

city = input("Enter a city name: ")
request_url = f'{BASE_URL}?appid={API_KEY}&q={city}'
response = requests.get(request_url)

def kelvin_to_f(temp):
    result = (((temp - 273.15) * 9) / 5) + 32
    return round(result, 2)

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    temperature = data['main']['temp']

    print(f'Weather description: {weather}')
    print(f'Temperature: {kelvin_to_f(temperature)} degrees Fahrenheit')
else:
    print("Error")

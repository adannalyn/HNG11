from flask import Flask, request, jsonify
import requests

app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello():
    visitor_name = request.args.get('visitor_name', 'Visitor')

    client_ip = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)

    location_url = f'http://ip-api.com/json/{client_ip}'
    location_response = requests.get(location_url).json()
    city = location_response.get('city', 'Unknown')

    api_key = '5e3096a01a2e3f37899007dfa3ee3fca'
    weather_url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
    weather_response = requests.get(weather_url).json()
    temperature = weather_response['main']['temp']

    greeting = f'Hello, {visitor_name}! the temperature is {temperature} + degrees celsius in {city}'

    response_data = {
        'client_ip': client_ip,
        'location': city,
        'greeting': greeting
    }

    return jsonify(response_data)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)

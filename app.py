from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/api/hello', methods=['GET'])
def hello():
    visitor_name = request.args.get('visitor_name', 'Guest')

    # Get the client's IP address
    client_ip = request.headers.get('X-Forwarded-For', request.remote_addr)

    # Get the location based on IP address
    ipify_response = requests.get(f'https://geo.ipify.org/api/v2/country,city?apiKey=at_Y5YuOTDmVVYuxZHdaOZEgZeDmcUlC&ipAddress={client_ip}')
    ipify_data = ipify_response.json()
    city = ipify_data.get('location', {}).get('city', 'Unknown')

    # Get the weather data for the city
    openweather_response = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid5e3096a01a2e3f37899007dfa3ee3fca&units=metric')
    weather_data = openweather_response.json()
    temperature = weather_data.get('main', {}).get('temp', 'Unknown')

    # Create the greeting message
    greeting = f"Hello, {visitor_name}!, the temperature is {temperature} degrees Celcius in {city}"

    return jsonify({
        "client_ip": client_ip,
        "location": city,
        "greeting": greeting
    })

if __name__ == '__main__':
    app.run(debug=True)

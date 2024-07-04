from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/api/hello', methods=['GET'])
def hello():
    visitor_name = request.args.get("visitor_name", "Guest")

    # Get the client's IP address
    client_ip = request.headers.get('X-Forwarded-For', request.remote_addr)

    # Get the location based on IP address
    ipify_response = requests.get(f'https://geo.ipify.org/api/v2/country,city?apiKey=at_Y5YuOTDmVVYuxZHdaOZEgZeDmcUlC&ipAddress={client_ip}')
    ipify_data = ipify_response.json()
    city = ipify_data.get('location', {}).get('city', 'Unknown')
    latitude = ipify_data.get('location', {}).get('lat', 0)
    longitude = ipify_data.get('location', {}).get('lng', 0)

    # Get the weather data for the location
    open_meteo_response = requests.get(f'https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true')
    weather_data = open_meteo_response.json()
    temperature = weather_data.get('current_weather', {}).get('temperature', 'Unknown')

    # Create the greeting message
    greeting = f'Hello, {}!, the temperature is {temperature} degrees Celsius in {city}'.format(visitor_name.strip('"'))

    return jsonify({
        "client_ip": client_ip,
        "location": city,
        "greeting": greeting
    })

if __name__ == '__main__':
    app.run(debug=True)

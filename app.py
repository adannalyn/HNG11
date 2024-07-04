from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/api/hello')
def hello():
    visitor_name = request.args.get('visitor_name')
    client_ip = request.remote_addr

    # Get location and temperature using an API
    # Here we use ip-api.com, but you can explore other options 
    response = requests.get(f'http://ip-api.com/json/{client_ip}')
    if response.status_code == 200:
        data = response.json()
        location = data.get('city', 'Unknown')
        temperature = data.get('temp', 'Unknown')
        greeting = f"Hello, {visitor_name}!, the temperature is {temperature} degrees Celcius in {location}"
    else:
        location = "Unknown"
        temperature = "Unknown"
        greeting = f"Hello, {visitor_name}! I can't get the weather information right now."

    return jsonify({
        "client_ip": client_ip,
        "location": location,
        "greeting": greeting
    })

if __name__ == "__main__":
    app.run(debug=True)

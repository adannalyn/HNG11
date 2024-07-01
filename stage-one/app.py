from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/hello', methods=['GET'])
def hello():
    visitor_name = request.args.get('visitor_name', 'Guest')
    client_ip = request.remote_addr
    location = "New Yok"
    temperature = 11
    greeting = f"Hello, {visitor_name}! The temperature is {temperature} degrees celsius in {location}"
    
    return jsonify({
        "client_ip": client_ip,
        "location": location,
        "greeting": greeting
    })
    
if __name__ = '__main__':
    app.run(debug=True)

from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)


API_KEY = '1a4f34b7732c8636bfdc8597252a539c'

@app.route('/')
def home():
    return render_template('index.html')  # Ensure you have an index.html in the 'templates' folder

@app.route('/get_weather', methods=['GET'])
def get_weather():
    city = request.args.get('city')
    if not city:
        return jsonify({"error": "City is required"}), 400

    # URL for the OpenWeather API
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
    
    # Send a GET request to fetch weather data
    response = requests.get(url)
    data = response.json()

    # Check for valid response
    if data.get('cod') != 200:
        return jsonify({"error": "City not found"}), 404
    
    # Return weather data as JSON response
    weather_info = {
        "city": data['name'],
        "temperature": data['main']['temp'],
        "humidity": data['main']['humidity'],
        "weather": data['weather'][0]['description']
    }
    
    return jsonify(weather_info)

if __name__ == "__main__":
    app.run(debug=True)

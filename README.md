Weather App
A simple weather application built with Flask (Python) and OpenWeather API. This app allows users to get the current weather information for any city. It displays temperature, humidity, and weather description, and it's designed to be simple, user-friendly, and responsive.

Features
Get weather information for any city.
Displays current temperature, humidity, and weather description.
User-friendly UI built with HTML and styled using CSS.
Built using Flask and OpenWeather API.
Requirements
To run the app, you’ll need the following installed:

Python 3.x
Flask
Requests library
You can install the required dependencies using pip:

Copy
Edit
pip install -r requirements.txt
Setup Instructions
1. Clone the repository
First, clone this repository to your local machine.

bash
Copy
Edit
git clone <repository_url>
cd weather_app
2. Install dependencies
Create a virtual environment (optional but recommended):

bash
Copy
Edit
python -m venv venv
Activate the virtual environment:

Windows:
bash
Copy
Edit
venv\Scripts\activate
macOS/Linux:
bash
Copy
Edit
source venv/bin/activate
Install the required dependencies:

bash
Copy
Edit
pip install -r requirements.txt
3. Set up OpenWeather API Key
Make sure you have an API key from OpenWeather. You can get it by signing up at OpenWeather.

Once you have the API key, replace the API_KEY value in app.py with your own key:

python
Copy
Edit
API_KEY = 'your_api_key_here'
4. Run the Flask App
To start the Flask application, run:

bash
Copy
Edit
python app.py
The app will run on http://127.0.0.1:5000. Open this URL in your web browser.

Usage
Open the app in your browser: http://127.0.0.1:5000.
Enter a city name in the input field and click Get Weather.
The app will show the current weather information for the entered city:
Temperature (in °C)
Humidity (in %)
Weather description (e.g., sunny, cloudy)


from flask import Flask, jsonify
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import os
from selenium.webdriver.chrome.service import Service
from threading import Thread
import time

app = Flask(__name__)

url = 'https://double.turbogames.io/'

# Configure Chrome options
chrome_options = Options()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--remote-debugging-port=9222")

# Initialize the WebDriver
driver = webdriver.Chrome(service=Service(executable_path=os.environ.get("CHROMEDRIVER_PATH")), options=chrome_options)
driver.get(url)

# Initialize global variable
numeric_value = "Not updated yet"

def update_numeric_value():
    global numeric_value
    while True:
        try:
            # Get the complete page content
            page_source = driver.page_source

            # Create a BeautifulSoup object to parse the page content
            soup = BeautifulSoup(page_source, 'html.parser')

            # Extract specific content using BeautifulSoup methods
            divcontent = soup.find('div', class_='active').get_text(strip=True)

            # Convert content to a number and check if it's in the desired range
            value = int(divcontent)
            if 0 <= value <= 14:
                numeric_value = value
        except Exception as e:
            numeric_value = f"An error occurred: {str(e)}"
            time.sleep(5)  # Pause for 5 seconds before next scrape

@app.route('/get_numeric_value', methods=['GET'])
def capture_and_transcribe():
    return jsonify({'numeric_value': numeric_value})

if __name__=='__main__':
    # Start the background task
    t = Thread(target=update_numeric_value)
    t.start()

    # Start the Flask app
    app.run(port=5000, debug=True)

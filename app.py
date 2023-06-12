from flask import Flask, jsonify
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import os
import logging
from selenium.webdriver.chrome.service import Service
from threading import Thread
import time

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

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
numeric_value = ""

def update_numeric_value():
    global numeric_value
    while True:
            # Obter o conteúdo completo da página
            page_source = driver.page_source

            # Criar um objeto BeautifulSoup para analisar o conteúdo da página
            soup = BeautifulSoup(page_source, 'html.parser')

            # Extrair o conteúdo específico usando métodos do BeautifulSoup
            # Por exemplo, suponha que você queira extrair o conteúdo de uma div com a classe "my-div-class"
            div_content = soup.find('div', class_='active').text
            numeric_value = div_content

@app.route('/get_numeric_value', methods=['GET'])
def capture_and_transcribe():
    return jsonify({'numeric_value': numeric_value})

if __name__=='__main__':

    app.run(port=5000, debug=True)

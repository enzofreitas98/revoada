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
numeric_value = None

@app.route('/get_numeric_value', methods=['GET'])
def capture_and_transcribe():
    global numeric_value

    while True:
            # Obter o conteúdo completo da página
        page_source = driver.page_source

            # Criar um objeto BeautifulSoup para analisar o conteúdo da página
        soup = BeautifulSoup(page_source, 'html.parser')

            # Extrair o conteúdo específico usando métodos do BeautifulSoup
            # Por exemplo, suponha que você queira extrair o conteúdo de uma div com a classe "my-div-class"
        div_content = soup.find('div', class_='active').text

            # Converter o conteúdo para um número e verificar se está no intervalo desejado
        numeric_value = int(div_content)  # supondo que div_content seja uma string numérica
        if 0 <= numeric_value <= 14:
            break

    return jsonify({'numeric_value': numeric_value})


if __name__=='__main__':
    # Start the background task
    t = Thread(target=update_numeric_value)
    t.start()

    # Start the Flask app
    app.run(port=5000, debug=True)

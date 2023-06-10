from flask import Flask, jsonify
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import os

app = Flask(__name__)

url = 'https://double.turbogames.io/'

# Configurar opções do Chrome
chrome_options = Options()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_SHIM")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")  # Adicionei essa linha
chrome_options.add_argument("--remote-debugging-port=9222")

# Iniciar o WebDriver
driver = webdriver.Chrome(options=chrome_options)
driver.get(url)

is_triggered = False

@app.route('/get_numeric_value', methods=['GET'])
def capture_and_transcribe():
    global is_triggered

    if not is_triggered:
        is_triggered = True
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
    app.run(port=5000, debug=True)

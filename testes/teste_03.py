# Instalar o Selenium e outras dependências
!pip install selenium

# Instalar o Chrome e o ChromeDriver
!apt-get update
!apt-get install -y wget unzip
!wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
!dpkg -i google-chrome-stable_current_amd64.deb
!apt --fix-broken install -y
!wget https://chromedriver.storage.googleapis.com/114.0.5735.90/chromedriver_linux64.zip
!unzip chromedriver_linux64.zip

# Configurar o ChromeDriver
import os
os.environ['WEBDRIVER_PATH'] = '/content/chromedriver'
os.environ['PATH'] += ':/content/chromedriver'

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Configurar as opções do Chrome
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')  # Executar em modo headless
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

# Inicializar o navegador
driver = webdriver.Chrome('chromedriver', options=chrome_options)

# Abrir a página de login
driver.get("https://www.example.com/login")  # Substitua pela URL real da página de login

# Esperar alguns segundos para a página carregar
time.sleep(2)

# Encontrar os campos de usuário e senha e inserir as credenciais
username = driver.find_element(By.ID, "username")  # Substitua "username" pelo ID real do campo de usuário
password = driver.find_element(By.ID, "password")  # Substitua "password" pelo ID real do campo de senha

username.send_keys("seu_usuario")  # Substitua "seu_usuario" pelo nome de usuário real
password.send_keys("sua_senha")    # Substitua "sua_senha" pela senha real

# Enviar o formulário
password.send_keys(Keys.RETURN)

# Esperar alguns segundos para ver o resultado
time.sleep(2)

# Verificar se o login foi bem-sucedido (exemplo: verificar se um elemento específico está presente na página após o login)
try:
    welcome_message = driver.find_element(By.ID, "welcome-message")  # Substitua "welcome-message" pelo ID real do elemento
    print("Login bem-sucedido!")
except:
    print("Falha no login.")

# Fechar o navegador
driver.quit()


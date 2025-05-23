from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configurar o WebDriver
driver = webdriver.Chrome(executable_path='/content/chromedriver')

# Navegar até a página do formulário
driver.get('https://exemplo.com/formulario')

try:
    # Esperar até que o campo de nome esteja presente
    nome = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'nome'))
    )

    # Preencher o campo de nome
    nome.send_keys('João Silva')

    # Preencher o campo de e-mail
    email = driver.find_element(By.ID, 'email')
    email.send_keys('joao.silva@example.com')

    # Preencher o campo de senha
    senha = driver.find_element(By.ID, 'senha')
    senha.send_keys('senha123')

    # Clicar no botão de submit
    submit = driver.find_element(By.ID, 'submit')
    submit.click()

    # Esperar até que a mensagem de confirmação esteja presente
    confirmacao = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'confirmacao'))
    )

    # Verificar se a mensagem de confirmação está correta
    assert 'Formulário enviado com sucesso' in confirmacao.text

finally:
    # Fechar o navegador
    driver.quit()


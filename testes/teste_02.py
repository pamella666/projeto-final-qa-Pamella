from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Iniciar o WebDriver (ajuste o caminho se necessário)
driver = webdriver.Chrome(executable_path='/caminho/para/seu/chromedriver')

# Acessar a página de teste
driver.get('https://www.selenium.dev/selenium/web/web-form.html')

try:
    # Esperar até que o campo de texto esteja presente
    text_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, 'my-text'))
    )

    # Preencher os campos
    text_box.send_keys('João Silva')

    # Clicar no botão "Submit"
    submit_button = driver.find_element(By.TAG_NAME, 'button')
    submit_button.click()

    # Esperar a resposta da submissão
    message = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, 'h1'))
    )

    # Verificar a mensagem de sucesso
    assert 'Form submitted' in message.text
    print('✅ Formulário enviado com sucesso!')

finally:
    driver.quit()


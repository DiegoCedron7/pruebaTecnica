import sys
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Constantes
PATH_SERVICE = "C:\\Users\\Diewi\\Downloads\\chromedriver_win32.zip\\chromedriver.exe"
PATH_CSV = "C:\\Users\\Diewi\\Desktop\\lista_de_perfiles.csv"
PATH_LOGIN = "https://www.linkedin.com/login"
USER = "lewopo6411@meidecn.com"
PASSWORD = "teo123123"
MESSAGE = "Hola soy Diego y esta es mi prueba tecnica! :) "
CONNECT = "Conectar"

# Configuración del navegador
service = Service(executable_path=PATH_SERVICE)
driver = webdriver.Chrome(service=service)
driver.get(PATH_LOGIN)

# Cargar el csv para usarlo en 'Mandar mensaje'
with open(PATH_CSV, "r") as f:
    profiles = f.readlines()

# Login
try:
    driver.find_element(By.ID, "username").send_keys(USER)
    driver.find_element(By.ID, "password").send_keys(PASSWORD)
    driver.find_element(By.CSS_SELECTOR, "form.login__form button[type='submit']").click()
except:
    print("No se pudo conectar con la cuenta.")
    driver.quit()
    sys.exit()

# Logica para abrir los perfiles
for profile in profiles:
    driver.get(profile)
    time.sleep(2)

    # Lógica para mandar mensaje.
    connect_button_text = driver.find_element(By.CSS_SELECTOR,
                                              ".pvs-profile-actions button.artdeco-button--primary span") \
        .get_attribute('innerHTML').strip()

    # Selección del camino que se debería seguir.
    if connect_button_text == CONNECT:
        # Boton Conectar PRINCIPAL
        driver.find_element(By.CSS_SELECTOR, ".pvs-profile-actions button.artdeco-button--primary").click()
        time.sleep(3)
    else:
        # Botón MÁS
        driver.find_element(By.CSS_SELECTOR, ".pvs-profile-actions button.artdeco-button--muted").click()
        time.sleep(3)
        # Botón Conectar MODAL-- MÁS
        driver.execute_script("document.querySelector('.pvs-overflow-actions-dropdown__content ul li:nth-child(3) > "
                              "div').click()")
    # Botón Añadir nota
    driver.find_element(By.CSS_SELECTOR, ".artdeco-modal__actionbar button.artdeco-button--muted").click()
    time.sleep(1)

    # Escribir la nota
    driver.find_element(By.CSS_SELECTOR, ".artdeco-modal__content div textarea").send_keys(MESSAGE)
    time.sleep(4)

    # Botón enviar
    driver.find_element(By.CSS_SELECTOR, ".artdeco-modal__actionbar button.artdeco-button--primary").click()
    time.sleep(4)

driver.quit()

from selenium import webdriver
import time
import csv
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


browser = webdriver.Chrome()

browser.get("https://www.facebook.com/login")

usuario = browser.find_element_by_xpath("//*[@id='email']")

usuario.send_keys('guillermoguzman.2016@gmail.com')

contraseña = browser.find_element_by_xpath("//*[@id='pass']")


contraseña.send_keys('Guillermo16')

time.sleep(5)

browser.find_element_by_xpath("//*[@id='loginbutton']").click()

time.sleep(7)



with open('groups-04-Oct-2019.csv') as File:
    reader = csv.reader(File)
    for row in reader:
        try:
            browser.get("https://www.facebook.com/groups/"+row[0])
            time.sleep(7)
            browser.find_element_by_xpath("//*[@id='facebook']/body").click()
            time.sleep(5)
            WebDriverWait(browser, 40).until(EC.elementToBeClickable((By.XPATH, "//input[@placeholder='¿Qué vendes?']")))
            time.sleep(3)
            ventas = browser.find_element_by_xpath("//input[@placeholder='¿Qué vendes?']")
            ventas.click()
            time.sleep(5)
            ventas = browser.find_element_by_xpath("//input[@placeholder='¿Qué vendes?']")
            ventas.send_keys("vendo terreno en colonia caroya")
            time.sleep(7)
            precio = browser.find_element_by_xpath("//input[@placeholder='Precio']")
            precio.send_keys('250000')
            time.sleep(5)
            browser.find_element_by_xpath("//input[@placeholder='Agrega la ubicación (opcional)']").send_keys(Keys.TAB + 'Vendo lote con escritura con todos los servicios.whatsapp:3513289703')
            time.sleep(5)
            foto = browser.find_element_by_xpath("//input[@data-testid='add-more-photos']")
            foto.send_keys('C://Users/guille16/PycharmProjects/conecion de base de datos/WhatsApp Image 2019-10-01 at 16.45.15.jpeg')
            time.sleep(15)
            foto = browser.find_element_by_xpath("//input[@data-testid='add-more-photos']")
            foto.send_keys('C://Users/guille16/PycharmProjects/conecion de base de datos/WhatsApp Image 2019-10-01 at 16.45.16.jpeg')
            time.sleep(15)
            foto = browser.find_element_by_xpath("//input[@data-testid='add-more-photos']")
            foto.send_keys('C://Users/guille16/PycharmProjects/conecion de base de datos/WhatsApp Image 2019-10-01 at 16.45.17.jpeg')
            time.sleep(15)
            siguiente = browser.find_element(By.XPATH, '//span[text()="Siguiente"]').click()
            time.sleep(15)
            publicar = browser.find_element(By.XPATH, '//span[text()="Publicar"]').click()

            time.sleep(8)

        except NoSuchElementException:
            print("grupo no encontrado")

        except ElementNotInteractableException:
            print("elemento no iterable")

        except TimeoutException:
            print("tiempo de espera termino")




























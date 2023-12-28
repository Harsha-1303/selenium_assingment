from selenium import webdriver
from pyshadow.main import Shadow
import time

driver = webdriver.Chrome()
driver.implicitly_wait(10)
shadow = Shadow(driver)
driver.maximize_window()

driver.get("https://devomni.annalect.com/")
username=shadow.find_element('input#username')
username.send_keys("adminqa.test@annalect.com")

driver.execute_script("document.querySelector('#portal-login > portal-login').shadowRoot.querySelector('#eid-login-btn').click()")

time.sleep(5)
password=shadow.find_element('input#password')
password.send_keys("4`>7s`^w2XeE}|")

driver.execute_script("document.querySelector('#portal-login > portal-login').shadowRoot.querySelector('#eid-login-btn').click()")
time.sleep(10)

logo=driver.execute_script("return document.querySelector('#outlet > portal-app-container').shadowRoot.querySelector('#logo')")

color = logo.value_of_css_property("color")
print(color)

font = logo.value_of_css_property('font-size')
print(font)

fontfamily = logo.value_of_css_property('font-family')
print(fontfamily)

width=logo.value_of_css_property('width')
print(width)

time.sleep(10)






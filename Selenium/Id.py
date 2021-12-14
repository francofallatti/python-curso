from selenium import webdriver
import time

controller = webdriver.Chrome(executable_path="Drivers/chromedriver.exe")
controller.get("https://www.udemy.com/join/login-popup/?locale=es_ES&response_type=html&next=https%3A%2F%2Fwww.udemy.com%2F")
time.sleep(2)

email_selector = controller.find_element_by_id("email--1")
password_selector = controller.find_element_by_id("id_password")

email_selector.send_keys("")
time.sleep(5)
password_selector.send_keys("")
time.sleep(5)

login = controller.find_element_by_id("submit-id-submit")
login.click()
time.sleep(5)

# controller.quit()
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

try:
    driver.get("https://example.com")

    print(f"Título: {driver.title}")
    print(f"URL: {driver.current_url}")

    enlaces = driver.find_elements(By.TAG_NAME, "a")
    print(f"Número de enlaces: {len(enlaces)}")

finally:
    driver.quit()
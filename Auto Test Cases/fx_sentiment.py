from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time
import os

service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

url = 'http://13.232.58.176:8002/'

text_to_enter1 = "2017/04/01"
text_to_enter2 = "2024/07/01"
screenshot_path = os.path.join(os.path.expanduser("~"), "Downloads", "screenshot.png")

try:
    print("Opening the web application...")
    driver.get(url)

    print("Waiting for the first input element...")
    file_input1 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div[1]/div[1]/div/div/div/section/div[1]/div/div/div/div[3]/div[1]/div/div/div/div/div/div/div/div/input'))
    )
    print("First input element located.")

    print("Waiting for the second input element...")
    file_input2 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div[1]/div[1]/div/div/div/section/div[1]/div/div/div/div[3]/div[2]/div/div/div/div/div/div/div/div/input'))
    )
    print("Second input element located.")

    # Enter the text in the input fields
    print(f"Entering text: {text_to_enter1}")
    file_input1.send_keys(text_to_enter1)
    time.sleep(2)

    print(f"Entering text: {text_to_enter2}")
    file_input2.send_keys(text_to_enter2)
    time.sleep(2)

    # Simulate pressing the Enter key on the second input field
    print("Simulating Enter key press on the second input field")
    file_input2.send_keys(Keys.ENTER)
    time.sleep(10)

    # Ensure the dropdown button is interactable and click it using JavaScript
    print("Waiting for the dropdown button...")
    dropdown_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div[1]/div[1]/div/div/div/section/div[1]/div/div/div/div[5]/details/summary'))
    )
    print("Clicking the dropdown button using JavaScript...")
    driver.execute_script("arguments[0].click();", dropdown_button)
    time.sleep(2)

    # Fetch the result element
    print("Fetching the result element...")
    result_element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div[1]/div[1]/div/div/div/section/div[1]/div/div/div/div[5]/details/div'))
    )

    print("Result captured successfully")
    result_text = result_element.text.strip()
    print("Output of the application after entering the text:")
    print(result_text)

    # Click the dropdown button
    print("Clicking the dropdown button...")
    dropdown_button.click()
    time.sleep(2)

    # Find all clickable links in the result element
    links = WebDriverWait(driver, 20).until(
        EC.visibility_of_all_elements_located((By.XPATH, '//*[@id="root"]/div[1]/div[1]/div/div/div/section/div[1]/div/div/div/div[5]/details/div//a'))
    )

    # Click the first 10 clickable links and copy the URLs
    print("Clicking the first 10 clickable links in the result section:")
    for i, link in enumerate(links[:10]):
        link_text = link.text.strip()
        link_url = link.get_attribute("href")
        print(f"\n{i+1}. {link_text}")
        print(f"URL: {link_url}")
        result_element.send_keys(f"\n\n{i+1}. {link_text}\nURL: {link_url}\n\n")
        link.click()
        time.sleep(5)  # Increase the wait time to ensure the page loads
        driver.back()
        time.sleep(2)

except Exception as e:
    print(f"An error occurred: {str(e)}")

finally:
    # Close the browser
    print("Closing the browser...")
    driver.quit()
    print("Browser closed.")

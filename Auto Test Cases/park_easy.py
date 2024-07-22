from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
import os
import requests

def park_easy(file_park_easy):

    service = ChromeService(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    url = 'http://52.66.10.81:8001/'
    
   


    try:
        print("Opening the web application...")
        driver.get(url)

        print("Waiting for the file upload button element...")
        upload_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div[1]/div[1]/div/div/div/section/div[1]/div/div/div/div[2]/div/section/button'))
        )
        print("File upload button located.")
        upload_button.click()
        time.sleep(2)

        print("Waiting for the actual file input element...")
        file_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//input[@type="file"]'))
        )
        print("File input element located.")

        # Make sure the file input element is visible and interactable
        driver.execute_script("arguments[0].style.display = 'block'; arguments[0].style.visibility = 'visible';", file_input)

        # Upload first file
        print(f"Sending the first file path to the input element: {file_park_easy}")
        file_input.send_keys(file_park_easy)
        time.sleep(2)

        print("Files uploaded successfully")

        time.sleep(20)

        print("Fetching the result element...")
        result_element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div[1]/div[1]/div/div/div/section/div[1]/div/div/div/div[4]/div/div'))
        )
        result_text = result_element.text
        print("Result captured successfully")

        print("Output of the application after uploading the files:")
        print(result_text)
        return "Working"

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return "An error occurred"

    finally:
        # Close the browser
        print("Closing the browser...")
        driver.quit()
        print("Browser closed.")

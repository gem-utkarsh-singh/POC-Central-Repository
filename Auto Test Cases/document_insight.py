from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time
import os
 
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()


url = 'http://13.232.58.176:8001/'

file_path1 = r'C:\Users\Utkarsh.Singh\Gemini Projects\POC-Central-Repository\DOCS\POCs Sample documents\earnings call report docs\META-Q1-2023-Earnings-Call-Transcript.pdf'
screenshot_path = os.path.join(os.path.expanduser("~"), "Downloads", "screenshot.png")

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
    print(f"Sending the first file path to the input element: {file_path1}")
    file_input.send_keys(file_path1)
    time.sleep(10)

    print("Files uploaded successfully")

    print("Waiting for the submit button...")
    submit_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div[1]/div[1]/div/div/div/section/div[1]/div/div/div/div[3]/div/button'))
    )
    submit_button.click()
    driver.execute_script("arguments[0].style.display = 'block'; arguments[0].style.visibility = 'visible';", file_input)

    print("Submitted")
    print("Files uploaded successfully")

    input_xpath = '//*[@id="root"]/div[1]/div[1]/div/div/div/section/div[1]/div/div/div/div[5]/div/div/div/div[1]/div[1]/input'

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, input_xpath)))

    # Find the input field using XPath
    input_field = driver.find_element(By.XPATH, input_xpath)

    # Clear any existing text in the input field
    input_field.clear()

    # Enter a value into the input field
    input_field.send_keys('Hiring')
    input_field.send_keys(Keys.RETURN)

    driver.execute_script("arguments[0].style.display = 'block'; arguments[0].style.visibility = 'visible';", input_field)
    time.sleep(5)
    print(f"Saving screenshot to: {screenshot_path}")
    driver.save_screenshot(screenshot_path)
    print("Screenshot saved successfully")
    time.sleep(5)
    b_tag = driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div[1]/div/div/div/section/div[1]/div/div/div/div[39]/div/div/p/font/b')
    b_text = b_tag.text
    print(f"Aggrigate Possitive Score = {b_text}")
    time.sleep(20)
    print("Result captured successfully")

    print("Output of the application after uploading the files:")
    # print(result_text)

except Exception as e:
    print(f"An error occurred: {str(e)}")

finally:
    # Close the browser
    print("Closing the browser...")
    driver.quit()
    print("Browser closed.")

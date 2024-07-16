from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time
import os

driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
driver.maximize_window()
url = 'http://52.66.10.81:8502/'

file_path1 = r'C:\Users\Utkarsh.Singh\Gemini Projects\POC-Central-Repository\DOCS\Document Intelligence Bot.pptx'
screenshot_path = os.path.join(os.path.expanduser("~"), "Downloads", "document_inteligence_screenshot.png")

try:
    print("Opening the web application...")
    driver.get(url)
    wait = WebDriverWait(driver, 20)
    print("Waiting for the file upload button element...")
    upload_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div[1]/div[1]/div/div/div/section[1]/div[1]/div[2]/div/div/div/div/div[2]/div/section/button'))
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
    time.sleep(5)

    print("Files uploaded successfully")

    print("Waiting for the submit button...")
    submit_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div[1]/div[1]/div/div/div/section[1]/div[1]/div[2]/div/div/div/div/div[3]/div/button'))
    )
    submit_button.click()
    driver.execute_script("arguments[0].style.display = 'block'; arguments[0].style.visibility = 'visible';", file_input)

    print("Submitted")
    print("Files uploaded successfully")

    print("Waiting for the submit button...")
    xpath_of_text_area = '//*[@id="text_input_1"]'  # Replace with your XPath

    # Find the text area using XPath
    text_area = driver.find_element(By.XPATH, xpath_of_text_area)

    # Write text into the text area and hit Enter
    text_area.send_keys('Give the summary of the file' + Keys.RETURN)
    time.sleep(10)
    div_element = driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div[1]/div/div/div/section[2]/div[1]/div/div/div/div[4]/div/div')

    # Find all <p> tags within the div
    p_elements = div_element.find_elements(By.TAG_NAME, 'p')

    # Print the text content of each <p> tag
    print(f"\n\n Extracted File Summary Text:\n\n")
    for p in p_elements:
        print(p.text)
    print('\n\n\n')
except Exception as e:
    time.sleep(100)
    print(f"An error occurred: {str(e)}")

finally:
    # Close the browser
    print("Closing the browser...")
    driver.quit()
    print("Browser closed.")

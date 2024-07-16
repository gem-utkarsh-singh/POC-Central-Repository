
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

 
url = 'http://13.232.253.41:8001/'
 
file_path1 = r'C:\Users\Utkarsh.Singh\Gemini Projects\POC-Central-Repository\DOCS\POCs Sample documents\organization structure docs\ex_3_document_1.pdf'
file_path2 = r'C:\Users\Utkarsh.Singh\Gemini Projects\POC-Central-Repository\DOCS\POCs Sample documents\organization structure docs\ex_3_document_2.pdf'
 
try:
    print("Opening the web application...")
    driver.get(url)
 
    print("Waiting for the file input element...")
    upload_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div[1]/div[1]/div/div/div/section/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/section/button'))
    )
    print("File upload button located.")
    upload_button.click()
    time.sleep(2)
 
    print("Waiting for the actual file input element...")
    file_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//input[@type="file"]'))
    )
    print("File input element located.")
 
    driver.execute_script("arguments[0].style.display = 'block'; arguments[0].style.visibility = 'visible';", file_input)
 
    # Upload first file
    print(f"Sending the first file path to the input element: {file_path1}")
    file_input.send_keys(file_path1)
    time.sleep(2)
 
    # Upload second file
    print(f"Sending the second file path to the input element: {file_path2}")
    file_input.send_keys(file_path2)
    print("File paths sent to the input element.")
 
    time.sleep(5)
 
    print("Files uploaded successfully")
 
    print("Waiting for the submit button...")
    submit_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div[1]/div[1]/div/div/div/section/div[1]/div/div/div/div[3]/div/button/div/p'))
    )
    submit_button.click()
    driver.execute_script("arguments[0].style.display = 'block'; arguments[0].style.visibility = 'visible';", file_input)
 
    print("Submitted")
 
    time.sleep(20)
 
    print("Fetching the result element...")
   
    # result_element = WebDriverWait(driver, 20).until(
    #     EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div[1]/div[1]/div/div/div/section/div[1]/div/div/div/div[14]/div/div/button'))
    # )
    result_element = driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div[1]/div/div/div/section/div[1]/div/div/div/div[14]/div/div/button')
    # print(result_element)
 
    clipboard_text = result_element.get_attribute("data-clipboard-text")
 
    print("Clipboard text:", clipboard_text)
 
    print("Output of the application after uploading the files:")
 
except Exception as e:
    try:
        span_element = driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div[1]/div/div/div/section/div[1]/div/div/div/div[7]/div/div/div/div/div[1]/span')
 
        # Extract and print the text
        span_text = span_element.text
        print(f"\n\n\n{span_text}\n\n\nAn error occurred: {str(e)}")
    except:
        print(f"An error occurred: {str(e)}")
 
finally:
    # Close the browser
    print("Closing the browser...")
    driver.quit()
    print("Browser closed.")
 
 
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

url = 'http://13.232.58.176:5005/'

file_path1 = r'C:\Users\Hemant.Surariya\PycharmProjects\Tester Bot Script\SAMPLE DOCUMENTS\Document Information Retrieval Bot\Sample Documents\30092022_commercial-invoice.pdf'
screenshot_path = os.path.join(os.path.expanduser("~"), "Downloads", "screenshot.png")

try:
    print("Opening the web application...")
    driver.get(url)

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
    time.sleep(10)
    xpath_of_text_area = '//*[@id="root"]/div[1]/div[1]/div/div/div/section[2]/div[3]/div/div/div/div/div/div/div/div/div[1]/div/textarea'  # Replace with your XPath

    # Find the text area using XPath
    text_area = driver.find_element(By.XPATH, xpath_of_text_area)

    # Write text into the text area and hit Enter
    text_area.send_keys('Give the summary of the file' + Keys.RETURN)
    time.sleep(10)
    p_tag = driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div[1]/div/div/div/section[2]/div[1]/div/div/div/div[4]/div[2]/div/div/div/div/div/div/p')
    p_text = p_tag.text

    print(f"\n\n\nExtracted File Summary Text: {p_text}\n\n")





except Exception as e:
    print(f"An error occurred: {str(e)}")
    try: 
        span_element = driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div[1]/div/div/div/section[2]/div[1]/div/div/div/div[2]/div/div/div/div/div[1]/span')

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

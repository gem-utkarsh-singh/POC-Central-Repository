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

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

url = 'http://localhost:8501/'

try:
    print("Opening the web application...")
    driver.get(url)
    print("url opened")
    time.sleep(10)
    model = ["llama3-8b-8192", "mixtral-8x7b-32768", "llama3-70b-8192", "gemma-7b-it"]
    input_xpath = '//*[@id="root"]/div[1]/div[1]/div/div/div/section/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[2]/input'
    question = ["what is profit of amazon", "what is profit of netflix", "what is profit of meta", "what is profit of spotify"]
    t = 0
    for i in model: 

    
    # Find the input field using XPath
        input_field = driver.find_element(By.XPATH, input_xpath)

        # Clear any existing text in the input field
        input_field.clear()

        # Enter a value into the input field
        input_field.send_keys(i)
        input_field.send_keys(Keys.RETURN)
        driver.execute_script("arguments[0].style.display = 'block'; arguments[0].style.visibility = 'visible';", input_field)
        time.sleep(3)

        xpath_of_text_area = '//*[@id="root"]/div[1]/div[1]/div/div/div/section/div[3]/div/div/div/div/div/div/div/div/div[1]/div/textarea'  # Replace with your XPath

        # Find the text area using XPath
        text_area = driver.find_element(By.XPATH, xpath_of_text_area)

        # Write text into the text area and hit Enter
        text_area.send_keys(question[t] + Keys.RETURN)
        t+=1
        time.sleep(4)
    
    WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'bot-message')))

# Find all div elements with the class bot-message
    bot_messages = driver.find_elements(By.CLASS_NAME, 'bot-message')

    # Extract and print the text from each bot_message div
    for message in bot_messages:
        inner_div = message.find_element(By.XPATH, './div')  # Locate the inner div
        print(inner_div.get_attribute('innerHTML'))
    print("\n\n\nAll four model checked and all are in working condition\n\n\n")






except Exception as e:
    time.sleep(100)
    print(f"An error occurred: {str(e)}")
    try: 
        span_element = driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div[1]/div/div/div/section[2]/div[1]/div/div/div/div[2]/div/div/div/div/div[1]/span')

        # Extract and print the text
        span_text = span_element.text
        print(f"\n\n\n{span_text}\n\n\nAn error occurred: {str(e)}")
    except:
        print(f"An error occurred: {str(e)}")

finally:
    time.sleep
    # Close the browser
    print("Closing the browser...")
    driver.quit()
    print("Browser closed.")

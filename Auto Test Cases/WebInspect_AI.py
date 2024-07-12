
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time
import os
 
def main():
   driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

 
 
   url = 'http://13.232.58.176:8004/'
   text_to_enter = "https://www.saucedemo.com/"
 
   try:
        print("Opening the web application...")
        driver.get(url)
 
        print("Waiting for the actual file input element...")
        file_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div[1]/div[1]/div/div/div/section/div[1]/div/div/div/div[2]/div[2]/div/div/div/div/div/div[1]/div/input'))
        )
        print("File input element located.")
 
        # Make sure the file input element is visible and interactable
        make_element_visible(driver, file_input)
 
        # Enter the text in the input field
        print(f"Entering text: {text_to_enter}")
        file_input.send_keys(text_to_enter)
        time.sleep(2)
 
        # Simulate pressing the Enter key
        print("Simulating Enter key press")
        file_input.send_keys(Keys.RETURN)
        time.sleep(10)
        wait = WebDriverWait(driver, 10)
        hover_over_div = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="bui9__anchor"]')))
 
        # Perform hover action
        actions = ActionChains(driver)
        actions.move_to_element(hover_over_div).perform()
 
        # Wait until the download button is visible and clickable
        download_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="bui8__anchor"]/button')))
 
        # Click the download button
        download_button.click()
 
        time.sleep(5)
 
       
 
        # Wait for the feature dropdown to be clickable
        print("Waiting for the feature dropdown to be clickable...")
        dropdown = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div[1]/div[1]/div/div/div/section/div[1]/div/div/div/div[6]/div/div/div/div[1]'))
        )
        print("Dropdown located.")
 
        # Click the dropdown to show the options
        dropdown.click()
        time.sleep(2)
 
        # Fetch all options within the dropdown
        print("Fetching all options within the dropdown...")
        options = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, '//*[@id="root"]/div[2]/div/div/div/div/div/div/ul/div/div'))
        )
        print(f"Number of options found: {len(options)}")
 
        for index, option in enumerate(options):
            print(f"Selecting option {index + 1}...")
            dropdown.click()
            time.sleep(1)
 
            option.click()
            time.sleep(2)
 
            click_generate_button(driver)
 
       
 
        # Click the code generation dropdown
        click_code_generation_dropdown(driver)
       
 
        button = driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div[1]/div/div/div/section/div[1]/div/div/div/div[13]/div/div/button')
 
        # Extract the data-clipboard-text attribute
        clipboard_text = button.get_attribute('data-clipboard-text')
        print("Feature_file_text :", clipboard_text, "\n\n")
 
        time.sleep(3)
        button = driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div[1]/div/div/div/section/div[1]/div/div/div/div[18]/div/div/button')
 
        # Extract the data-clipboard-text attribute
        clipboard_text = button.get_attribute('data-clipboard-text')
        print("Code_genration_text :", clipboard_text, "\n\n")
 
 
   except Exception as e:
        # time.sleep(10000)
        print(f"An error occurred: {str(e)}")
 
   finally:
        # Close the browser
        print("Closing the browser...")
        driver.quit()
        print("Browser closed.")
 
def make_element_visible(driver, element):
    driver.execute_script("arguments[0].style.display = 'block'; arguments[0].style.visibility = 'visible';", element)
 
 
def click_generate_button(driver):
    print("Waiting for the 'Generate Test Case' button to be clickable...")
    generate_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div[1]/div[1]/div/div/div/section/div[1]/div/div/div/div[12]/div[1]/div/div/div/div/div/button'))
    )
    print("Generate Test Case button located.")
 
    print("Clicking the 'Generate Test Case' button...")
    generate_button.click()
    time.sleep(5)
 
def click_code_generation_dropdown(driver):
    print("Waiting for the code generation dropdown to be clickable...")
    dropdown = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div[1]/div[1]/div/div/div/section/div[1]/div/div/div/div[16]/div/div/div/div[1]'))
    )
    print("Dropdown located.")
 
    # Click the dropdown to show the options
    dropdown.click()
    time.sleep(2)
 
    print("Fetching all options within the code generation dropdown...")
    code_options = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, '//*[@id="root"]/div[2]/div/div/div/div/div/div/ul/div/div'))
    )
    print(f"Number of code generation options found: {len(code_options)}")
 
    for index, option in enumerate(code_options):
        print(f"Selecting code generation option {index + 1}...")
        dropdown.click()
        time.sleep(1)
 
        option.click()
        time.sleep(5)
 
if __name__ == "__main__":
    main()
 
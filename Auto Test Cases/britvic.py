from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
import time

# Initialize the Chrome driver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()

url = 'http://52.66.10.81:8501/'

try:
    print("Opening the web application...")
    driver.get(url)
    
    # Define the wait variable
    wait = WebDriverWait(driver, 10)
    
    print("Waiting for the element to be present and hover over it...")
    hover_over_div = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div[1]/div[1]/div/div/div/section/div[1]/div/div/div/div[2]/div[1]/div/div/div/div[4]/div/div/div[2]/div[1]/div/div/div[2]')))
    
    print("Performing hover action...")
    actions = ActionChains(driver)
    actions.move_to_element(hover_over_div).perform()
    
    print("Waiting until the download button is visible and clickable...")
    download_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="bui5__anchor"]/button')))
    
    print("Clicking the download button...")
    download_button.click()
    
    print("Pausing to allow for any processing or downloads to complete...")
    time.sleep(5)
    
except Exception as inner_e:
    print(f"An additional error occurred while handling the initial error: {str(inner_e)}")

finally:
    # Close the browser
    print("Closing the browser...")
    driver.quit()
    print("Browser closed.")

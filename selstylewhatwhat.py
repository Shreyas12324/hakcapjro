from selenium.common.exceptions import TimeoutException
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import csv
import random


csv_file_path = 'contacts_messages.csv'


message_to_send = 'Hello'  


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


link = 'https://web.whatsapp.com'
driver.get(link)

input("Press Enter after scanning QR code and loading WhatsApp Web...")


with open(csv_file_path, 'r', newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        num = row[1] 
        link = f'https://web.whatsapp.com/send/?phone={num}'
        driver.get(link)

        try:
            input_box = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//div[@contenteditable='true'][@data-tab='1']"))
            )
            input_box.send_keys(message_to_send + Keys.ENTER)

           
            time.sleep(random.uniform(5, 10))  
        except TimeoutException as e:
            print(f"Timeout error: {str(e)}")
            
        except Exception as e:
            print(f"An error occurred: {str(e)}")
           

# Quit the driver
driver.quit()

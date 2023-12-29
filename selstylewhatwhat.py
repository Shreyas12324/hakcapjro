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

# Update the path to your CSV file containing numbers and messages
csv_file_path = 'contacts_messages.csv'

# Set your message
message_to_send = 'Hello'  # Replace 'Hello' with your desired message

# Create driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open browser with default link
link = 'https://web.whatsapp.com'
driver.get(link)

# Allow time for manual login and scanning QR code
input("Press Enter after scanning QR code and loading WhatsApp Web...")

# Read data from the modified CSV file
with open(csv_file_path, 'r', newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        num = row[1]  # Extracting the phone number from the CSV file
        link = f'https://web.whatsapp.com/send/?phone={num}'
        driver.get(link)

        try:
            input_box = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//div[@contenteditable='true'][@data-tab='1']"))
            )
            input_box.send_keys(message_to_send + Keys.ENTER)

            # Wait for the message to be sent (adjust this wait time accordingly)
            time.sleep(random.uniform(5, 10))  # Random sleep between 5 to 10 seconds
        except TimeoutException as e:
            print(f"Timeout error: {str(e)}")
            # Handle the timeout exception
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            # Handle the error or wait for the page to stabilize before proceeding

# Quit the driver
driver.quit()

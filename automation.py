from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
import time
import random
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException

options = Options()
options.add_argument("executable_path=C:/Users/Soumick/Desktop/cv/Selenium/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(options=options)
driver.get('http://159.89.38.11/')


# Step 1: Input email
email_input = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//input[@id='email-1']")))
email_input.clear()
email_input.send_keys("test@orangetoolz.com")

# Step 2: Input password
password_input = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//input[@id='password-1']")))
password_input.clear()
password_input.send_keys("8Kh8nTe*^jdk")

# Step 3: Login
login = driver.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[4]/button[1]")
login.click()

# Wait for the site to finish loading
wait = WebDriverWait(driver, 10)
wait.until(EC.title_contains("Dashboard"))  # Replace with the expected title or any other suitable condition


# Step 4: Click on 'Contact Manage'
contact_manage_link = driver.find_element(By.XPATH, "//i[@class='fas fa-id-card fa-lg']")
contact_manage_link.click()

# Wait for the 'Contact Manage' text to be visible
contact_manage_text = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Contact Manage']")))

# Click on the 'Contact Manage' 
contact_manage_text.click()


add_contact = WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.XPATH, "//a[normalize-space()='Add Contact']")))
add_contact.click()

add_grp = WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Add New Group']")))
add_grp.click()

number_input = WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.XPATH, "//input[@name='name']")))
number_input.clear()
number_input.send_keys("automation962023")

number_input = WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.XPATH, "//textarea[@placeholder='Write your group description here...']")))
number_input.clear()
number_input.send_keys("This is automation 962023")

close_tag = WebDriverWait(driver,15).until(EC.visibility_of_element_located((By.XPATH, "//button[normalize-space()='Close']")))
print('close_tag', close_tag)
close_tag.click()

checkboxes = WebDriverWait(driver,15).until(EC.presence_of_all_elements_located((By.XPATH, "//label[@for='checkbox-4-03' or @for='checkbox-4-0269' or @for='checkbox-4-0270']")))
for checkbox in checkboxes:
    checkbox.click()


#number_input = WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Enter Number']")))
#number_input.clear()
#number_input.send_keys("99")



number_input = WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Enter Number']")))
number_input.clear()

while True:
    number = random.randint(1, 100)  # Generate a random number between 1 and 100
    
    number_input.send_keys(str(number))  # Convert the number to a string and send it to the input field
    
    # Wait for the error message to  timeout
    try:
        error_message = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//span[contains(text(),'The number has already been taken.')]")))
        number_input.clear()
        continue
    except TimeoutException:
        break


number_input_email = WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Enter Email address']")))
number_input_email.clear()
number_input_email.send_keys("automation96@gmail.com")


number_input_first_name = WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Enter First name']")))
number_input_first_name.clear()
number_input_first_name.send_keys("automation96")

number_input_last_name = WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Enter Last name']")))
number_input_last_name.clear()
number_input_last_name.send_keys("test")

birthday_input = WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Enter your birthday']")))
birthday_input.clear()
birthday_input.send_keys("1990-01-01")

number_input_city = WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Enter your city']")))
number_input_city.clear()
number_input_city.send_keys("mohammadpur")

number_input_state = WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Enter your state']")))
number_input_state.clear()
number_input_state.send_keys("adabor")

number_input_country = WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Enter your country']")))
number_input_country.clear()
number_input_country.send_keys("Bangladesh")

number_input_zip = WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Enter your Zip']")))
number_input_zip.clear()
number_input_zip.send_keys("adabor")


number_address = WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.XPATH, "//textarea[@placeholder='Enter your address']")))
number_address.clear()
number_address.send_keys("Dhaka,Mohammadpur,Adabor,1207")

add_data = WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.XPATH, "//button[normalize-space()='Add Contact']")))
add_data.click()


# Pause
time.sleep(5) 

# Close the browser
driver.quit()

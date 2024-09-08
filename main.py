from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementClickInterceptedException
from sms import telegram_sms # for balck phone
from mms import telegram_mms # for balck phone sending screenshot
from all_phones import phone_alert  # for balck phone & samsung phone
from datetime import datetime
import time
import os

# -----------------------------------------------------
#----------------------- HYDERABAD --------------------
# -----------------------------------------------------
# Function to perform the operations on the webpage
def slot_hyd(driver):
    try:
        # Solve captcha (assuming the captcha solving process is handled outside)
        h_start= "--------Checking for HYDERABD--------"
        print(h_start)
        telegram_sms(h_start)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        h_time_a = datetime.now().strftime("%H:%M:%S")
        h_msg_a = f"Captcha solving started at  {h_time_a}"
        print(h_msg_a)
        telegram_sms(h_msg_a)

        time.sleep(75)
        
        try:
            h_tick_element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#anchor-state > div.check > img')))
            h_msg_cap = "Captcha Solved Successfully"
            print ("h_msg_cap")
            telegram_sms(h_msg_cap)
        except Exception as e:
            h_e_error = f"CAPTCHA ISSUE : {e}"
            h_e_issue = "Captcha might be successfull : not sure"
            print(h_e_issue)
            telegram_sms(h_e_issue)

        button_next = (By.CSS_SELECTOR, 'button.mat-primary') 
        button_element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(button_next))
        
        h_msg_b="Proceeding to second page"
        print(h_msg_b)
        telegram_sms(h_msg_b)
        button_element.click()

        # Navigate to page 2 and perform actions
        time.sleep(4) # wait for page to load

        
        # Click on the first option - java intervention needed
        element1 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mat-select-value-1"]')))
        driver.execute_script("arguments[0].scrollIntoView(true);", element1)
        time.sleep(1)
        try:
            element1.click()
            print("student type selected - Xpath method")
        except ElementClickInterceptedException:
            # Handle interception by scrolling more or using JavaScript click
            driver.execute_script("arguments[0].click();", element1)
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, '#mat-option-9 > .mat-option-text').click()
        print("student type selected - CSS method")


        # Click on the second option
        element2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mat-select-value-3"]')))
        driver.execute_script("arguments[0].scrollIntoView(true);", element2)
        time.sleep(1)
        try:
            element2.click()
            print("city selected - Xpath method")
        except ElementClickInterceptedException:
            # Handle interception by scrolling more or using JavaScript click
            driver.execute_script("arguments[0].click();", element2)
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, '#mat-option-15 > .mat-option-text').click()
        print("city selected - CSS method")

        # Click on the third option
        element3 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mat-select-value-5"]')))
        driver.execute_script("arguments[0].scrollIntoView(true);", element3)
        time.sleep(1)
        try:
            element3.click()
            print("No. of Persons selected- Xpath method")
        except ElementClickInterceptedException:
            # Handle interception by scrolling more or using JavaScript click
            driver.execute_script("arguments[0].click();", element3)
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, '#mat-option-0 > .mat-option-text').click()
        print("No. of Persons selected- CSS method")

        time.sleep(2)

        # Take Sceenshot
        h_time_ss= datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        h_file_path = f'C:/visa/hyd-{h_time_ss}.png'
        os.makedirs(os.path.dirname(h_file_path), exist_ok=True)
        driver.save_screenshot(h_file_path)

        #Send Screenshot
        telegram_mms(h_file_path)


        # Check if the element indicating no available slots is present
        WebDriverWait(driver, 6).until(EC.presence_of_element_located((By.XPATH, '//*[@id="main-content"]/app-dashboard/app-institutions/app-institutions/app-national-visa/div/app-national-visa-reservation-appointment/app-national-visa-reservation-appointment-page/div/div/app-national-visa-reservation-appointment-data/app-visa-reservation-appointment-form/form/div/div/div')))
        
        try:
            # Check if the element is present on the page
            driver.find_element(By.XPATH, '//*[@id="main-content"]/app-dashboard/app-institutions/app-institutions/app-national-visa/div/app-national-visa-reservation-appointment/app-national-visa-reservation-appointment-page/div/div/app-national-visa-reservation-appointment-data/app-visa-reservation-appointment-form/form/div/div/div')

            # If element is found, print a success message
            h_time_c = datetime.now().strftime("%H:%M:%S")
            h_msg_c = f"Slot status as on  {h_time_c}: NO SLOTS available in HYDERABD : or error check screenshot"
            telegram_sms(h_msg_c)
            print(h_msg_c)

        except NoSuchElementException:
            # If element is not found, then the slots are available
            h_msg_x = "SLOTS AVAILABLE in HYDERABAD !! "
            for _ in range(10):
                telegram_sms(h_msg_x)
                phone_alert(h_msg_x)
                time.sleep(1)
            time.sleep(600)

            return "YESS"  # Return "YESS" status if slots are available
             
    except TimeoutException:
        # Handle timeout exceptions for any WebDriverWait statements
        h_time_ea = datetime.now().strftime("%H:%M:%S")
        h_ea = f"Operation timed out at {h_time_ea}"
        print(h_ea)
        telegram_sms(h_ea)

    except NoSuchElementException as e:
        # Handle specific element not found exceptions
        h_eb =f"Element not found: {e}"
        print(h_eb)
        telegram_sms(h_eb)


    except ElementClickInterceptedException as e:
        # Handle element click intercepted exceptions
        h_ec=f"Element click intercepted: {e}"
        print(h_ec)
        telegram_sms(h_ec)

    return "NO LUCK"  # Return "NO LUCK" status by default

# -----------------------------------------------------
#----------------------- CHENNAI ----------------------
# -----------------------------------------------------

def slot_chn(driver):
    try:
        # Solve captcha (assuming the captcha solving process is handled outside)
        c_welcome= "--------Checking for CHENNAI--------"
        print(c_welcome)
        telegram_sms(c_welcome)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        c_time_a = datetime.now().strftime("%H:%M:%S")
        c_msg_a = f"Captcha solving started at  {c_time_a}"
        print(c_msg_a)
        telegram_sms(c_msg_a)

        time.sleep(75)

        try:
            c_check_div = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//div[@class='check']")))
            c_msg_cap = "Captcha Solved Successfully"
            print (c_msg_cap)
            telegram_sms(c_msg_cap)
        except Exception as e:
            c_e_error = f"CAPTCHA ISSUE : {e}"
            c_e_issue = "Captcha might be solved - not sure"
            print(c_e_issue)
            telegram_sms(c_e_issue)


        button_next = (By.CSS_SELECTOR, 'button.mat-primary') 
        button_element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(button_next))
        
        c_msg_b="Proceeding to second page"
        print(c_msg_b)
        telegram_sms(c_msg_b)
        button_element.click()

        # Navigate to page 2 and perform actions
        time.sleep(3) # wait for page to load

        
        # Click on the first option - java intervention needed
        element1 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mat-select-value-1"]')))
        driver.execute_script("arguments[0].scrollIntoView(true);", element1)
        time.sleep(1)
        try:
            element1.click()
            print("student type selected - Xpath method")
        except ElementClickInterceptedException:
            # Handle interception by scrolling more or using JavaScript click
            driver.execute_script("arguments[0].click();", element1)
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, '#mat-option-9 > .mat-option-text').click()
        print("student type selected - CSS method")


        # Click on the second option
        element2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mat-select-value-3"]')))
        driver.execute_script("arguments[0].scrollIntoView(true);", element2)
        time.sleep(1)
        try:
            element2.click()
            print("city selected - Xpath method")
        except ElementClickInterceptedException:
            # Handle interception by scrolling more or using JavaScript click
            driver.execute_script("arguments[0].click();", element2)
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, '#mat-option-14 > .mat-option-text').click()
        print("city selected - CSS method")

        # Click on the third option
        element3 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mat-select-value-5"]')))
        driver.execute_script("arguments[0].scrollIntoView(true);", element3)
        time.sleep(1)
        try:
            element3.click()
            print("No. of Persons selected- Xpath method")
        except ElementClickInterceptedException:
            # Handle interception by scrolling more or using JavaScript click
            driver.execute_script("arguments[0].click();", element3)
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, '#mat-option-0 > .mat-option-text').click()
        print("No. of Persons selected- CSS method")

        time.sleep(2)
        # Take Sceenshot
        c_time_ss= datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        c_file_path = f'C:/visa/hyd-{c_time_ss}.png'
        os.makedirs(os.path.dirname(c_file_path), exist_ok=True)
        driver.save_screenshot(c_file_path)

        #Send Screenshot
        telegram_mms(c_file_path)


        # Check if the element indicating no available slots is present
        WebDriverWait(driver, 6).until(EC.presence_of_element_located((By.XPATH, '//*[@id="main-content"]/app-dashboard/app-institutions/app-institutions/app-national-visa/div/app-national-visa-reservation-appointment/app-national-visa-reservation-appointment-page/div/div/app-national-visa-reservation-appointment-data/app-visa-reservation-appointment-form/form/div/div/div')))
        
        try:
            # Check if the element is present on the page
            driver.find_element(By.XPATH, '//*[@id="main-content"]/app-dashboard/app-institutions/app-institutions/app-national-visa/div/app-national-visa-reservation-appointment/app-national-visa-reservation-appointment-page/div/div/app-national-visa-reservation-appointment-data/app-visa-reservation-appointment-form/form/div/div/div')

            # If element is found, print a success message
            c_time_c = datetime.now().strftime("%H:%M:%S")
            c_msg_c = f"Slot status as on  {c_time_c}: NO SLOTS available in Chennai or error Check screenshot"
            telegram_sms(c_msg_c)
            print(c_msg_c)

        except NoSuchElementException:
            # If element is not found, then the slots are available
            c_msg_x = "SLOTS AVAILABLE in CHENNAI !! "
            for _ in range(10):
                telegram_sms(c_msg_x)
                phone_alert(c_msg_x)
            time.sleep(600)


            return "YESS"  # Return "YESS" status if slots are available
             


    except TimeoutException:
        # Handle timeout exceptions for any WebDriverWait statements
        c_time_ea = datetime.now().strftime("%H:%M:%S")
        c_ea = f"Operation timed out at {c_time_ea}"
        print(c_ea)
        telegram_sms(c_ea)

    except NoSuchElementException as e:
        # Handle specific element not found exceptions
        c_eb =f"Element not found: {e}"
        print(c_eb)
        telegram_sms(c_eb)


    except ElementClickInterceptedException as e:
        # Handle element click intercepted exceptions
        c_ec=f"Element click intercepted: {e}"
        print(c_ec)
        telegram_sms(c_ec)

    return "NO LUCK"  # Return "NO LUCK" status by default

# -----------------------------------------------------
#----------------------- BANGLORE ---------------------
# -----------------------------------------------------

def slot_bln(driver):
    try:
        # Solve captcha (assuming the captcha solving process is handled outside)
        b_welcome= "--------Checking for BANGALORE--------"
        print(b_welcome)
        telegram_sms(b_welcome)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        b_time_a = datetime.now().strftime("%H:%M:%S")
        b_msg_a = f"Captcha solving started at  {b_time_a}"
        print(b_msg_a)
        telegram_sms(b_msg_a)
        time.sleep(75)


        try:
            b_check_div = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//div[@class='check']")))
            b_msg_cap = "Captcha Solved Successfully"
            print (b_msg_cap)
            telegram_sms(b_msg_cap)
        except Exception as e:
            b_e_error = f"CAPTCHA ISSUE : {e}"
            b_e_issue = "Captcha might be solved - not sure"
            print(b_e_issue)
            telegram_sms(b_e_issue)

        button_next = (By.CSS_SELECTOR, 'button.mat-primary') 
        button_element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(button_next))
        
        msg_b="Proceeding to second page"
        print(msg_b)
        telegram_sms(msg_b)
        button_element.click()

        # Navigate to page 2 and perform actions
        time.sleep(4) # wait for page to load

        
        # Click on the first option - java intervention needed
        element1 = WebDriverWait(driver, 6).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mat-select-value-1"]')))
        driver.execute_script("arguments[0].scrollIntoView(true);", element1)
        time.sleep(1)
        try:
            element1.click()
            print("student type selected - Xpath method")
        except ElementClickInterceptedException:
            # Handle interception by scrolling more or using JavaScript click
            driver.execute_script("arguments[0].click();", element1)
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, '#mat-option-9 > .mat-option-text').click()
        print("student type selected - CSS method")


        # Click on the second option
        element2 = WebDriverWait(driver, 6).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mat-select-value-3"]')))
        driver.execute_script("arguments[0].scrollIntoView(true);", element2)
        time.sleep(1)
        try:
            element2.click()
            print("city selected - Xpath method")
        except ElementClickInterceptedException:
            # Handle interception by scrolling more or using JavaScript click
            driver.execute_script("arguments[0].click();", element2)
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, '#mat-option-13 > .mat-option-text').click()
        print("city selected - CSS method")

        # Click on the third option
        element3 = WebDriverWait(driver, 6).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mat-select-value-5"]')))
        driver.execute_script("arguments[0].scrollIntoView(true);", element3)
        time.sleep(1)
        try:
            element3.click()
            print("No. of Persons selected- Xpath method")
        except ElementClickInterceptedException:
            # Handle interception by scrolling more or using JavaScript click
            driver.execute_script("arguments[0].click();", element3)
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, '#mat-option-0 > .mat-option-text').click()
        print("No. of Persons selected- CSS method")

        time.sleep(2)
        # Take Sceenshot
        b_time_ss= datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        b_file_path = f'C:/visa/hyd-{b_time_ss}.png'
        os.makedirs(os.path.dirname(b_file_path), exist_ok=True)
        driver.save_screenshot(b_file_path)

        #Send Screenshot
        telegram_mms(b_file_path)


        # Check if the element indicating no available slots is present
        WebDriverWait(driver, 6).until(EC.presence_of_element_located((By.XPATH, '//*[@id="main-content"]/app-dashboard/app-institutions/app-institutions/app-national-visa/div/app-national-visa-reservation-appointment/app-national-visa-reservation-appointment-page/div/div/app-national-visa-reservation-appointment-data/app-visa-reservation-appointment-form/form/div/div/div')))
        
        try:
            # Check if the element is present on the page
            driver.find_element(By.XPATH, '//*[@id="main-content"]/app-dashboard/app-institutions/app-institutions/app-national-visa/div/app-national-visa-reservation-appointment/app-national-visa-reservation-appointment-page/div/div/app-national-visa-reservation-appointment-data/app-visa-reservation-appointment-form/form/div/div/div')

            # If element is found, print a success message
            b_time_c = datetime.now().strftime("%H:%M:%S")
            b_msg_c = f"Slot status as on  {b_time_c}: NO SLOTS available in BANGALORE or error. Check sreenshot"
            telegram_sms(b_msg_c)
            print(b_msg_c)

        except NoSuchElementException:
            # If element is not found, then the slots are available
            b_msg_x = "SLOTS AVAILABLE in BANGALORE !! "
            for _ in range(10):
                telegram_sms(b_msg_x)
                phone_alert(b_msg_x)
            
            time.sleep(600)

            return "YESS"  # Return "YESS" status if slots are available
             

    except TimeoutException:
        # Handle timeout exceptions for any WebDriverWait statements
        b_time_ea = datetime.now().strftime("%H:%M:%S")
        b_ea = f"Operation timed out at {b_time_ea}"
        print(b_ea)
        telegram_sms(b_ea)

    except NoSuchElementException as e:
        # Handle specific element not found exceptions
        b_eb =f"Element not found: {e}"
        print(b_eb)
        telegram_sms(b_eb)


    except ElementClickInterceptedException as e:
        # Handle element click intercepted exceptions
        b_ec=f"Element click intercepted: {e}"
        print(b_ec)
        telegram_sms(b_ec)

    return "NO LUCK"  # Return "NO LUCK" status by default

# -----------------------------------------------------
#----------------------- MAIN SCRIPT ------------------
# -----------------------------------------------------
# Main script to repeat operation every 10 minutes until status is "YESS"
if __name__ == "__main__":
    options = Options()
    options.add_argument(r"--user-data-dir=C:\\Users\\Kalyan\\AppData\\Local\\Google\\Chrome\\User Data")
    options.add_argument(r'--profile-directory=Profile 1')
    service = Service(r'C:\\driver\\chromedriver.exe')

    try:
        while True:
            main_time_k = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            msg_m_k = f"{'- ' * 30}\n Slot Check Session Starts : {main_time_k} \n{'- ' * 30}"
            print(msg_m_k)
            telegram_sms(msg_m_k)

            options = Options()
            options.add_argument(r"--user-data-dir=C:\\Users\\Kalyan\\AppData\\Local\\Google\\Chrome\\User Data")
            options.add_argument(r'--profile-directory=Profile 1')
            service = Service(r'C:\\driver\\chromedriver.exe')

            driver = webdriver.Chrome(service=service, options=options)
            driver.get("https://secure2.e-konsulat.gov.pl/placowki/211/wiza-krajowa/wizyty/weryfikacja-obrazkowa")
            driver.maximize_window()

            # For HYDERABAD 
            h_status = slot_hyd(driver)
            time.sleep(2)
            driver.quit()
            print("hyderabad session closed")
            
            time.sleep(900) # wait till next city 



            options = Options()
            options.add_argument(r"--user-data-dir=C:\\Users\\Kalyan\\AppData\\Local\\Google\\Chrome\\User Data")
            options.add_argument(r'--profile-directory=Profile 1')
            service = Service(r'C:\\driver\\chromedriver.exe')
            driver = webdriver.Chrome(service=service, options=options)
            driver.get("https://secure2.e-konsulat.gov.pl/placowki/211/wiza-krajowa/wizyty/weryfikacja-obrazkowa")
            driver.maximize_window()
            # For CHENNAI
            c_status = slot_chn(driver)
            time.sleep(2)
            driver.quit()
            print("Chennai session closed")

            time.sleep(900) # wait till next city 


            options = Options()
            options.add_argument(r"--user-data-dir=C:\\Users\\Kalyan\\AppData\\Local\\Google\\Chrome\\User Data")
            options.add_argument(r'--profile-directory=Profile 1')
            service = Service(r'C:\\driver\\chromedriver.exe')
            driver = webdriver.Chrome(service=service, options=options)
            driver.get("https://secure2.e-konsulat.gov.pl/placowki/211/wiza-krajowa/wizyty/weryfikacja-obrazkowa")
            driver.maximize_window()
            
            # For BANGALORE
            b_status = slot_bln(driver)
            time.sleep(2)
            driver.quit()
            print("Banglore session closed")


            print("session closes")

            m_session_msg = f"{'-' * 10} CHECKING ENDED {main_time_k} {'-' * 10}"
            print(m_session_msg)
            

            if h_status == "YESS" or c_status == "YESS" or b_status == "YESS": 
                m_msgg = "Slots Available"
                for _ in range(10):
                    telegram_sms(m_msgg)
                    phone_alert(m_msgg)
                    time.sleep(1)
                time.sleep(900)

                break  # Exit loop if status is "YESS" # remove this if you htink code has issues


            # Wait for 10 minutes before repeating
            time.sleep(600)  # 600 seconds = 10 minutes

    except Exception as e:
        msg_err= f"An error occurred: {str(e)}"
        print(msg_err)
        telegram_sms(msg_err)

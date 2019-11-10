from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep


emailId=input('Enter EmailID: ')
password=input('Enter Password: ')
searchWord=input('Enter the Subject of the Mail: ')


emailID_xpath="//*[@id='identifierId']"
password_xpath="//*[@id='password']/div[1]/div/div[1]/input"
search_xpath="//*[@id='gs_lc50']/input[1]"
attachment_email_xpath="//*[@id=':m8']"
search_btn_xpath="//*[@id='aso_search_form_anchor']/button[4]"
attachment_xpath="//*[@id=':oh']"
download_btn_xpath="//*[@id=':or']/div"

driver = webdriver.Chrome('chromedriver')
driver.maximize_window()
driver.get("https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
wait = WebDriverWait(driver, 1000)

input_email = wait.until(EC.visibility_of_element_located((By.XPATH, emailID_xpath)))
input_email.send_keys(emailId + Keys.ENTER)



input_password = wait.until(EC.visibility_of_element_located((By.XPATH, password_xpath)))
input_password.send_keys(password + Keys.ENTER)

input_search=wait.until(EC.presence_of_element_located((By.XPATH,search_xpath)))
input_search.send_keys(searchWord+Keys.ENTER)


input_click_mail=wait.until(EC.visibility_of_element_located((By.XPATH,attachment_email_xpath)))
input_click_mail.click()

attachment=wait.until(EC.visibility_of_element_located((By.XPATH,attachment_xpath)))
hover = ActionChains(driver).move_to_element(attachment)
hover.perform()


download_btn=wait.until(EC.visibility_of_element_located((By.XPATH,download_btn_xpath)))
download_btn.click()


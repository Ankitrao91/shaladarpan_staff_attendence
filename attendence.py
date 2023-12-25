


from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)





driver.get("https://rajshaladarpan.nic.in/SD3/Home/Public2/OfficeLoginNew.aspx")


driver.find_element(By.XPATH, '/html/body/form/div[4]/div[5]/div/div[2]/div[1]/input').send_keys("224671")
driver.find_element(By.XPATH, '/html/body/form/div[4]/div[5]/div/div[2]/div[2]/input[1]').send_keys("Raaz@0786")

time.sleep(15)
driver.find_element(By.XPATH, '/html/body/form/div[4]/div[5]/div/div[2]/div[5]/input[2]').click()




time.sleep(3)

driver.find_element(By.XPATH, '/html/body/div/form/div[5]/div/div/div/div[2]/div/div/ul/li[5]/a/span').click() 
# karmik
time.sleep(3)





driver.find_element(By.XPATH, '/html/body/div/form/div[5]/div/div/div/div[2]/div/div/ul/li[5]/ul/li[22]/a').click()
#karmik upastithi




time.sleep(3)
driver.find_element(By.XPATH, '/html/body/div[1]/form/div[6]/div/div/div/div[2]/div[2]/div[2]/div[2]/div/div/div[3]/button').click()
#alert box



time.sleep(3)
driver.find_element(By.XPATH, '/html/body/div/form/div[6]/div/div/div/div[2]/div[2]/div[1]/div[3]/div/div/div/table/tbody/tr[3]/td[2]/a').click()
#govt sr.sec.school 224671

time.sleep(3)





for i in range(2,25):
    sel = Select(driver.find_element(By.XPATH, f'/html/body/div/form/div[6]/div/div/div/div[2]/div[2]/div[1]/div[3]/div/div[1]/div/table/tbody/tr[{i}]/td[6]/select'))
    sel.select_by_index(1)

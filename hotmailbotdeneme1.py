from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import random
furkand = random.randint(1, 99999)
furkandsifre = "furkandmaster778"
driver_path = "C:\\Users\\PC\\Downloads\\chromedriver.exe"

browser = webdriver.Chrome(executable_path=driver_path)

browser.get("https://signup.live.com/signup")
time.sleep(3)
browser.find_element_by_xpath('//*[@id="liveSwitch"]').click()
time.sleep(2)
mail = browser.find_element_by_xpath('//*[@id="MemberName"]')
time.sleep(1)
mail.send_keys("furkandbot"+str(furkand)) #mail adı
time.sleep(2)
browser.find_element_by_xpath('//*[@id="iSignupAction"]').click() #giriş yap tusu
time.sleep(3)
sifre = browser.find_element_by_xpath('//*[@id="PasswordInput"]') #şifregiriş yeri
time.sleep(1)
sifre.send_keys(furkandsifre) #mail adı
time.sleep(2)
browser.find_element_by_xpath('//*[@id="iSignupAction"]').click() #giriş yap tusu
time.sleep(2)
ad = browser.find_element_by_xpath('//*[@id="FirstName"]') 
time.sleep(1)
ad.send_keys("furkan") # ad
time.sleep(2)
soyad = browser.find_element_by_xpath('//*[@id="LastName"]') 
time.sleep(1)
soyad.send_keys("masta") # ad
time.sleep(2)
browser.find_element_by_xpath('//*[@id="iSignupAction"]').click() #giriş yap tusu
time.sleep(2)
dgun = browser.find_element_by_xpath('//*[@id="BirthDay"]') 
time.sleep(1)
dgun.send_keys("1")
time.sleep(1)
dgun = browser.find_element_by_xpath('//*[@id="BirthYear"]') 
time.sleep(1)
select = Select(browser.find_element_by_xpath('//*[@id="BirthMonth"]'))
select.select_by_value('2')
dgun.send_keys("2000")
time.sleep(2)
browser.find_element_by_xpath('//*[@id="iSignupAction"]').click() 
time.sleep(2)
browser.find_element_by_xpath('/div[5]/span/a[2]/span').click() 
from selenium.webdriver.common.keys import Keys
browser.send_keys(Keys.RETURN)








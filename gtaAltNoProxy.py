import string

from selenium import webdriver
import time
import random
from selenium.common.exceptions import ElementNotInteractableException, NoSuchElementException, \
    ElementClickInterceptedException
from selenium.webdriver.common.by import By


def buyGTA():
    driver.get('https://www.epicgames.com/fn/7600-4776-6319')
    time.sleep(2)
    driver.get("https://www.epicgames.com/account/password?from=launcherPDP&lang=en_US#2fa-signup")
    time.sleep(3)
    driver.find_element_by_xpath(
        '//*[@id="passwordView"]/div[2]/div/div/div[2]/div/div/div[3]/div/div/div/div[7]/button').click()
    time.sleep(4)
    input("Paste code and click enter.")
    time.sleep(1)
    driver.get('https://www.epicgames.com/store/en-US/product/grand-theft-auto-v/home')
    time.sleep(2)
    # mature = driver.find_elements_by_xpath('//*[@id="dieselReactWrapper"]/div/div[4]/main/div[2]/div/div[1]/p')
    # if not mature:
    #     print("Good!")
    # else:
    #     driver.find_element_by_xpath(
    #         '//*[@id="dieselReactWrapper"]/div/div[4]/main/div[2]/div/div[2]/div/button').click()
    #     time.sleep(2)
    #     print("Clicking continue.")
    # # error catch
    # time.sleep(2)
    # driver.find_element_by_xpath('/html/body/div/div/div[4]/main/div/div/div[2]/div/div[2]/div[2]/div/div/div[3]/div/div/div/div[3]/div/button').click()
    # time.sleep(4)
    # driver.find_element_by_xpath('//*[@id="purchase-app"]/div/div[4]/div[1]/div[2]/div[5]/div/div/button').click()
    input("Enter")
    print("Game has been purchased")
    time.sleep(7)
    file1.write("\n"+username + password)

def createAccount():
    driver.get("https://www.epicgames.com/fn/7600-4776-6319")
    time.sleep(1)
    while True:
        try:
            driver.find_element_by_xpath('/html/body/div/div/header/nav/div/div[2]/div/div[3]/ul/li/a/span').click()
            break
        except ElementNotInteractableException:
            driver.get('https://www.epicgames.com/fortnite/logout');
            time.sleep(4)
            driver.get("https://www.epicgames.com/fn/7600-4776-6319")
    driver.find_element_by_xpath('//*[@id="FnMobile-overlaySignUp"]').click()
    time.sleep(2) #IF USA IP THEN UNCOMMENT THIS. NETHERLANDS VPN DOESNT NEED IT
    # driver.find_element_by_xpath('//*[@id="month"]').click()  # month
    # driver.find_element_by_xpath('/html/body/div[3]/div[3]/ul/li[4]').click()
    # time.sleep(1)
    # driver.find_element_by_xpath('//*[@id="day"]').click()
    # driver.find_element_by_xpath('/html/body/div[3]/div[3]/ul/li[4]').click()
    # time.sleep(1)
    # driver.find_element_by_xpath('//*[@id="year"]').send_keys("1990")
    # driver.find_element_by_xpath('//*[@id="continue"]').click()
    time.sleep(3)  # new acc
    driver.find_element_by_xpath('//*[@id="name"]').send_keys("Matthew")
    driver.find_element_by_xpath('//*[@id="lastName"]').send_keys("Marcilio")
    driver.find_element_by_xpath('//*[@id="displayName"]').send_keys(username)
    driver.find_element_by_xpath('//*[@id="email"]').send_keys(mail)
    driver.find_element_by_xpath('//*[@id="password"]').send_keys(password)
    driver.find_element_by_xpath('//*[@id="termsOfService"]').click()
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="btn-submit"]').click()
    time.sleep(3)
    while True:
        try:
            emailTaken = driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div/div[2]/div/form/h6[2]')
            print("email bad!")
            nextEmail()
            driver.find_element_by_xpath('//*[@id="email"]').clear()
            driver.find_element_by_xpath('//*[@id="email"]').send_keys(mail)
            time.sleep(1)
            print("Clicking")
            driver.find_element_by_xpath('//*[@id="btn-submit"]').click()
        except:
            verify = driver.find_elements_by_xpath('//*[@id="code"]')
            if not verify:
                print("captcha")
                time.sleep(5)
            else:
                input("Click enter once verification entered")
                break
def nextEmail():
    global mail
    position = mail.find('.')
    mail = mail[:position] +mail[position+1] +'.'+mail[position+2:]
    print(mail)
    return mail
def random_string(string_length=13):
    # Generate a random string of letters and digits
    letters_digits = string.ascii_letters + string.digits
    return ''.join(random.choice(letters_digits) for i in range(string_length))
mail = ""      #enter you your email here with a period after first letter
password = "" #password here
username = random_string()
pos = 1
driver = webdriver.Firefox()
file1 = open("MyFile.txt","a")
i=mail.find('.')
def createAndBuy():
    while i < len(mail) - 10:
        username = random_string()
        print(mail)
        createAccount()
        print("Account Created")
        buyGTA()
        print("GTA Purchased")
        nextEmail()
def createAllAccs():
    while i < len(mail) - 10:
        global username
        username = random_string()
        print(mail)
        createAccount()
        nextEmail()
def loginAlreadyMade():
    driver.get("https://www.epicgames.com/fn/7600-4776-6319")
    time.sleep(1)
    while True:
        try:
            driver.find_element_by_xpath('/html/body/div/div/header/nav/div/div[2]/div/div[3]/ul/li/a/span').click()
            break
        except ElementNotInteractableException:
            driver.get('https://www.epicgames.com/fortnite/logout');
            time.sleep(4)
            driver.get("https://www.epicgames.com/fn/7600-4776-6319")
    driver.find_element_by_xpath('//*[@id="FnMobile-overlaySignUp"]').click()
    time.sleep(4)
    driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div/div[2]/div/div[3]/a/p').click()
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="usernameOrEmail"]').send_keys(nextEmail())
    driver.find_element_by_xpath('//*[@id="password"]').send_keys(password)
    time.sleep(3)
    driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div/div[2]/div/form/div[4]/button/span').click()
    input("enter after login successful")
    driver.get('https://launcher-website-prod07.ol.epicgames.com/purchase?showNavigation=true&namespace=0584d2013f0149a791e7b9bad0eec102&offers=954871df36d3456ca1face43aa5c2e62#/purchase/verify?_k=tvego8')
    input("enter after purchase")
def buyAllAccs():
    while i < len(mail) - 10:
        loginAlreadyMade()
#createAllAccs() #only creates accounts for email
#buyAllAccs()  #only purchases game for accounts already made
createAndBuy()  #creates accounts and buys it
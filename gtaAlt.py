# import string
# import zipfile
#
# from selenium import webdriver
# import time
# import random
# from selenium.webdriver import Chrome
# from selenium.common.exceptions import ElementNotInteractableException, TimeoutException, NoSuchElementException
# from selenium.webdriver import ActionChains
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.wait import WebDriverWait
# ip = ' 71.83.189.175'
# port = 8080
#
# def get_chromedriver(use_proxy=False, user_agent=None):
#     username = 'foo'
#     password = 'bar'
#
#     manifest_json = """
#     {
#         "version": "1.0.0",
#         "manifest_version": 2,
#         "name": "Chrome Proxy",
#         "permissions": [
#             "proxy",
#             "tabs",
#             "unlimitedStorage",
#             "storage",
#             "<all_urls>",
#             "webRequest",
#             "webRequestBlocking"
#         ],
#         "background": {
#             "scripts": ["background.js"]
#         }
#     }
#     """
#
#     background_js = """
#     var config = {
#             mode: "fixed_servers",
#             rules: {
#             singleProxy: {
#                 scheme: "http",
#                 host: "%(ip)s",
#                 port: %(port)s
#             }
#             }
#         }
#     chrome.proxy.settings.set({value: config, scope: "regular"}, function() {});
#     function callbackFn(details) {
#         return {
#             authCredentials: {
#                 username: "%(username)s",
#                 password: "%(password)s"
#             }
#         }
#     }
#     chrome.webRequest.onAuthRequired.addListener(
#                 callbackFn,
#                 {urls: ["<all_urls>"]},
#                 ['blocking']
#     )
#     """ % {'ip': ip, 'port': port, 'username': username, 'password': password}
#
#     plugin_file = 'proxy_auth_plugin.zip'
#     with zipfile.ZipFile(plugin_file, 'w') as zp:
#         zp.writestr("manifest.json", manifest_json)
#         zp.writestr("background.js", background_js)
#     chrome_options = Options()
#     chrome_options.add_extension(plugin_file)
#     chrome_options.add_argument("user-data-dir=C:\\Users\\cbass\\AppData\\Local\\Google\\Chrome\\User Data")
#     #chrome_options.add_argument("--window-size=500,500")
#     driver = Chrome(options=chrome_options)
#     return driver
# # def wait_for_element(driver, xpath):
# #     try:
# #         WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, xpath)))
# #         return True
# #     except TimeoutException:
# #         print("Loading took too much time!")
# #         return False
# def random_string(string_length=13):
#     # Generate a random string of letters and digits
#     letters_digits = string.ascii_letters + string.digits
#     return ''.join(random.choice(letters_digits) for i in range(string_length))
# # def read_proxys():
# #     lines = []
# #     with open("proxies.txt", "r") as file:
# #         for line in file:
# #             lines.append(line)
# #
# #     with open("proxies.txt", "r+") as file:
# #         for line in file:
# #             beegining_of_proxy = line[line.find("]") + 1:-2]
# #             global ip, port
# #             ip = beegining_of_proxy[0:beegining_of_proxy.find(":")]
# #             port = beegining_of_proxy[beegining_of_proxy.find(":") + 1:]
# #             lines.remove(line)
# #             break
# #         file.seek(0)
# #         file.truncate()
# #         for line in lines:
# #             file.write(line)
# #
# class Website:
#     def __init__(self, first, last, email):
#         self.first = first
#         self.last = last
#         self.email = email
#         self.url = "https://www.epicgames.com/fn/7600-4776-6319"
#         self.is_good_proxy = False
#
#         while not self.is_good_proxy:
#             self.driver = get_chromedriver(True)
#             #self.driver.minimize_window()
#             try:
#                 self.driver.set_page_load_timeout(80)
#                 self.driver.get(self.url)
#                 print(ip)
#                 # check for internet
#                 try:
#                     error = self.driver.find_element_by_class_name("error-code")
#                     if error.text == "ERR_PROXY_CONNECTION_FAILED" or error.text == "DNS_PROBE_FINISHED_NO_INTERNET" or error.text == "ERR_NAME_NOT_RESOLVED" or error.text == "ERR_TUNNEL_CONNECTION_FAILED" or error.text == "ERR_EMPTY_RESPONSE" or error.text == "ERR_TOO_MANY_RETRIES":
#                         print("No internet connection... retrying...")
#                         self.driver.quit()
#                         #read_proxys()
#                 except NoSuchElementException:
#                     print("Success, proxy is valid!")
#                     self.is_good_proxy = True
#             except TimeoutException as ex:
#                 print('Proxy took to long... retrying...')
#                 self.driver.quit()
#                 #read_proxys()
#
#     def log_account(self):
#         # with open('generated.txt', 'a') as file:
#         #     file.write(web.email + ":" + "ThxNMan4!" + "\n")
#         print("")
#
#     def create_account(self):
#         while True:
#             try:
#                 self.driver.find_element_by_xpath('/html/body/div/div/header/nav/div/div[2]/div/div[3]/ul/li/a/span').click()
#                 break
#             except ElementNotInteractableException:
#                 self.driver.get('https://www.epicgames.com/fortnite/logout');
#                 time.sleep(3)
#                 self.driver.get("https://www.epicgames.com/fn/7600-4776-6319")
#         self.driver.find_element_by_xpath('//*[@id="FnMobile-overlaySignUp"]').click()
#         time.sleep(7)
#         while True:
#             try:
#                 self.driver.find_element_by_xpath('//*[@id="month"]').click()
#                 self.driver.find_element_by_xpath('/html/body/div[3]/div[3]/ul/li[4]').click()
#                 time.sleep(1)
#                 self.driver.find_element_by_xpath('//*[@id="day"]').click()
#                 self.driver.find_element_by_xpath('/html/body/div[3]/div[3]/ul/li[4]').click()
#                 time.sleep(1)
#                 self.driver.find_element_by_xpath('//*[@id="year"]').send_keys("1990")
#                 self.driver.find_element_by_xpath('//*[@id="continue"]').click()
#                 time.sleep(1)
#                 break
#             except NoSuchElementException:
#                 if input("1 if not")==1:
#                     break
#                 else:
#                     return
#             except self.driver.find_element_by_xpath('//*[@id="name"]').click():
#                 break
#         #self.driver.find_element_by_xpath('//*[@id="month"]').click()
#
#         time.sleep(1)  # new acc
#         self.driver.find_element_by_xpath('//*[@id="name"]').send_keys(self.first)
#         self.driver.find_element_by_xpath('//*[@id="lastName"]').send_keys(self.last)
#         self.driver.find_element_by_xpath('//*[@id="displayName"]').send_keys("sdsd")
#         self.driver.find_element_by_xpath('//*[@id="email"]').send_keys(self.email)
#         self.driver.find_element_by_xpath('//*[@id="password"]').send_keys("") #pass
#         self.driver.find_element_by_xpath('//*[@id="termsOfService"]').click()
#         usernameTaken = self.driver.find_elements_by_xpath('//*[@id="root"]/div/div/div/div/div[2]/div/form/div[3]/div/div/text()')
#         if not usernameTaken:
#             print("Username Good.")
#         else:
#             print("Username bad")
#             self.driver.find_element_by_xpath('//*[@id="displayName"]').send_keys(random_string(13))
#         self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div/div[2]/div/form/div[8]/button/span').click()
#         time.sleep(3)
#         emailTaken = self.driver.find_elements_by_xpath('//*[@id="root"]/div/div/div/div/div[2]/div/form/h6[2]')
#         if not emailTaken:
#             print("email good!")
#         else:
#             print("email bad!")
#             #nextEmail()
#             return
#         # account done
#         if input("If it is a captcha and then you get an error type 1 and click enter, if everything is good then paste code in site and click enter, then hit enter in python IDE.") == "1":
#             #nextEmail()
#             return
#         else:
#             print("Authenticating 2FA")
#         time.sleep(1)
#     def buyGame(self):
#         self.driver.get('https://www.epicgames.com/fn/7600-4776-6319')
#         time.sleep(2)
#         self.driver.get("https://www.epicgames.com/account/password?from=launcherPDP&lang=en_US#2fa-signup")
#         time.sleep(3)
#         self.driver.find_element_by_xpath('//*[@id="passwordView"]/div[2]/div/div/div[2]/div/div/div[3]/div/div/div/div[7]/button').click()
#         time.sleep(4)
#         input("Paste code and click enter.")
#         time.sleep(1)
#         self.driver.get('https://www.epicgames.com/store/en-US/product/grand-theft-auto-v/home')
#         time.sleep(2)
#         mature = self.driver.find_elements_by_xpath('//*[@id="dieselReactWrapper"]/div/div[4]/main/div[2]/div/div[1]/p')
#         if not mature:
#             print("Good!")
#         else:
#             self.driver.find_element_by_xpath('//*[@id="dieselReactWrapper"]/div/div[4]/main/div[2]/div/div[2]/div/button').click()
#             time.sleep(2)
#             print("Clicking continue.")
#         # error catch
#         self.driver.find_element_by_xpath('/html/body/div/div/div[4]/main/div/div/div[2]/div/div[2]/div[2]/div/div/div[3]/div/div/div/div[3]/div/button').click()
#         time.sleep(4)
#         self.driver.find_element_by_xpath('//*[@id="purchase-app"]/div/div[4]/div[1]/div[2]/div[5]/div/div/button').click()
#         print("Game has been purchased")
#         time.sleep(7)
#         #nextEmail()
# #
# #
# # read_proxys()
# #
# #      #enter you your email here
# email = "" #email
# first = random_string(13)
# last = random_string(8)
# web = Website(first, last, email)
# #
# # def nextEmail():
# #     global email
# #     position = email.find('.')
# #     email = email[:position] +email[position+1] +'.'+email[position+2:]
# #     print(email)
# #     return email
# #
# # i = 0
# # while i < 4:
# #     web.create_account()
# #     if input("Enter 1 if wanna buy else anything")=="1":
# #         web.buyGame()
# #     web.driver.get(web.url)
# #     email = nextEmail()
# #     first = random_string(13)
# #     last = random_string(8)
# #     web.first = first
# #     web.last = last
# #     web.email = email
# #     i += 1

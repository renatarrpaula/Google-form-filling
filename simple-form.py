from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
#from webdriver_manager.chrome import ChromeDriverManager

option = webdriver.ChromeOptions()
# incognito option prevents the browser from storing any history, cookies, etc...
option.add_argument("-incognito")
#option.add_argument("--headless")
#option.add_argument("disable-gpu")

ser = Service(r"./chromedriver.exe")
browser = webdriver.Chrome(service=ser, options=option)
#browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

#open the form
browser.get("https://forms.gle/FoAoauz53Xy7A4n68")

# Use the following snippets to get elements by their xpaths
textbox_short = browser.find_element(By.XPATH, """//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input""")
textbox_long = browser.find_elements(By.XPATH,"""//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div[2]/textarea""")
radiobuttons_NO = browser.find_element(By.XPATH, """//*[@id="i16"]""")
checkbox_YES = browser.find_element(By.XPATH, """//*[@id="i30"]""")

# Actions
time.sleep(5) # wait 5 seconds for page to load
textbox_short.send_keys("Answer One")
time.sleep(4)
textbox_long[0].send_keys("Answer Two")
time.sleep(3)
radiobuttons_NO.click()
time.sleep(2)
checkbox_YES.click()
time.sleep(2)

# Send answers
enviar = browser.find_element(By.XPATH, """//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span""")
enviar.click()

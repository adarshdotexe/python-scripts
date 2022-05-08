"""
Make sure to run the following commands first using command prompt:
pip install selenium
pip install chromedriver_py
pip install schedule

Also change Your Email And Pass Down Below

To exit from terminal when program is running press Ctrl+C
"""

# Assign email id and password
mail_address = 'RollNumber@student.nitandhra.ac.in'
password = ''

# import required modules
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from chromedriver_py import binary_path
import schedule

def Glogin(mail_address, password):
    # Login Page
    driver.get(
        'https://accounts.google.com/ServiceLogin?hl=en&passive=true&continue=https://www.google.com/&ec=GAZAAQ')
  
    # Input Gmail ID
    driver.find_element_by_id("identifierId").send_keys(mail_address)
    driver.find_element_by_id("identifierNext").click()
    driver.implicitly_wait(10)
  
    # Input Password
    driver.find_element_by_xpath(
        '//*[@id="password"]/div[1]/div/div[1]/input').send_keys(password)
    driver.implicitly_wait(10)
    driver.find_element_by_id("passwordNext").click()
    driver.implicitly_wait(10)

    # Go to Google Home Page
    driver.get('https://google.com/')
    driver.implicitly_wait(100)
  
  
def turnOffMicCam():
    # Turn off Microphone
    driver.find_element_by_xpath(
        '/html/body/div[1]/c-wiz/div/div/div[9]/div[3]/div/div/div[4]/div/div/div[1]/div[1]/div/div[4]/div[1]/div/div/div').click()
    driver.implicitly_wait(3000)
  
    # Turn off Camera
    time.sleep(1)
    driver.find_element_by_xpath(
        '/html/body/div[1]/c-wiz/div/div/div[9]/div[3]/div/div/div[4]/div/div/div[1]/div[1]/div/div[4]/div[2]/div/div').click()
    driver.implicitly_wait(3000)
  
  
def joinNow():
    # Join Meet
    driver.implicitly_wait(2000)
    driver.find_element_by_xpath(
        '/html/body/div[1]/c-wiz/div/div/div[9]/div[3]/div/div/div[4]/div/div/div[2]/div/div[2]/div/div[1]/div[1]').click()
    print("You have successfully joined the meet!")
  
  
# Create Chrome Instamce
opt = Options()
opt.add_argument('--disable-blink-features=AutomationControlled')
opt.add_argument('--disable-infobars')
opt.add_argument('--start-maximized')
opt.add_experimental_option("prefs", {
    "profile.default_content_setting_values.media_stream_mic": 1,
    "profile.default_content_setting_values.media_stream_camera": 1,
    "profile.default_content_setting_values.geolocation": 1,
    "profile.default_content_setting_values.notifications": 1
})

driver = webdriver.Chrome(executable_path=binary_path, options=opt)

def main(code,duration=60):

    if password == '':
        print("Please enter your email id and password in the code at line 9 for the program to work")
        driver.quit()
        exit()

    # Login to Google Account
    Glogin(mail_address, password)
    time.sleep(5)
    # Go to Google Meet
    driver.get('https://meet.google.com/lookup/' + code)
    time.sleep(5)

    # Turn off Camera and Mic
    # turnOffMicCam()
    # time.sleep(5)

    # Join the Class
    joinNow()

    # Wait for Class to End
    time.sleep(duration*59)

    # Quit
    driver.quit()


##########
# Monday #
##########
# CS203 60 Mins
schedule.every().monday.at("09:00").do(main, code = 'CS203')
# MA239 60 Mins
schedule.every().monday.at("10:00").do(main, code = 'MA239')
# EC237 120 Mins
schedule.every().monday.at("13:00").do(main, code = 'EC237', duration = 120)


###########
# Tuesday #
###########
# EC237 60 Mins
schedule.every().tuesday.at("09:00").do(main, code = 'EC237')
# CS204 60 Mins
schedule.every().tuesday.at("10:00").do(main, code = 'CS204')
# CS203 60 Mins
schedule.every().tuesday.at("11:00").do(main, code = 'CS203')
# CS206 180 Mins
schedule.every().tuesday.at("11:00").do(main, code = 'CS206', duration = 180)


#############
# Wednesday #
#############
# MA239 60 Mins
schedule.every().wednesday.at("09:00").do(main, code = 'MA239')
# EC237 60 Mins
schedule.every().wednesday.at("10:00").do(main, code = 'EC237')
# CS204 60 Mins
schedule.every().wednesday.at("11:00").do(main, code = 'CS204')
# CS202 60 Mins
schedule.every().wednesday.at("13:00").do(main, code = 'CS202')

############
# Thursday #
############
# MA239 60 Mins
schedule.every().thursday.at("09:00").do(main, code = 'MA239')
# CS202 60 Mins
schedule.every().thursday.at("10:00").do(main, code = 'CS202')
# EC237 60 Mins
schedule.every().thursday.at("11:00").do(main, code = 'EC237')
# CS205 180 Mins
schedule.every().thursday.at("13:00").do(main, code = 'CS205', duration = 180)

############
# Friday #
############
# CS204 60 Mins
schedule.every().friday.at("09:00").do(main, code = 'CS204')
# CS203 60 Mins
schedule.every().friday.at("10:00").do(main, code = 'CS203')
# CS202 60 Mins
schedule.every().friday.at("11:00").do(main, code = 'CS202')

while True:
    schedule.run_pending()
    time.sleep(120)
    print("No tasks pending")

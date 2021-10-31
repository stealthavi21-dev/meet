
from selenium import  webdriver
from datetime import datetime,date
from selenium.webdriver.common.alert import Alert
import pause
import time
import keyring
import getpass
from timings import Times
datetime.today().strftime('%A')
from selenium.webdriver.support.expected_conditions import alert_is_present
from selenium.webdriver.support.wait import WebDriverWait
from cryptography.fernet import Fernet
key = b'pRmgMa8T0INjEAfksaq2aafzoZXEuwKI7wDe4c1F8AY='
cipher_suite = Fernet(key)
with open('C:\sz\mssqltip_bytes.bin', 'rb') as file_object:
    for line in file_object:
        encryptedpwd = line
uncipher_text = (cipher_suite.decrypt(encryptedpwd))
plain_text_encryptedpassword = bytes(uncipher_text).decode("utf-8") #convert to string
def launch(link,pwd,term):
    # options = Options()
    # options.set_preference("media.navigator.permission.disabled", True)

    option = webdriver.FirefoxOptions()
    option.add_argument("--disable-infobars")
    option.add_argument("start-maximized")#start at top
    option.add_argument("--disable-extensions")
    option.set_preference("permissions.default.microphone", 1)
    option.set_preference("permissions.default.camera", 1)
    b = webdriver.Firefox(options=option)
    b.get("https://accounts.google.com/signin/v2/identifier?service=classroom&passive=1209600&continue=https%3A%2F%2Fclassroom.google.com%2Fu%2F0%2Fh&followup=https%3A%2F%2Fclassroom.google.com%2Fu%2F0%2Fh&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
    c1 = b.find_element_by_id("identifierId")
    c1.click()
    e1 = c1.send_keys("as2377@srmist.edu.in")
    b1 = b.find_element_by_xpath("//button[@class='VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ VfPpkd-LgbsSe-OWXEXe-dgl2Hf nCP5yc AjY5Oe DuMIQc qIypjc TrZEUc lw1w4b']")
    b1.click()
    time.sleep(3)
    c2 = b.find_element_by_xpath("//div[@class='Xb9hP']/input[@class='whsOnd zHQkBf']")
    p1 = c2.send_keys(pwd)
    b2 = b.find_element_by_xpath("//button[@class='VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ VfPpkd-LgbsSe-OWXEXe-dgl2Hf nCP5yc AjY5Oe DuMIQc qIypjc TrZEUc lw1w4b']")
    b2.click()
    print(link)
    b.get(link)
    time.sleep(1)
    # Turning off video
    b.find_element_by_xpath(
        "//div[@aria-label='Turn off microphone (ctrl + d)']").click()
    time.sleep(1)
    # turning off audio
    b.find_element_by_xpath(
        "//div[@aria-label='Turn off camera (ctrl + e)']").click()
    time.sleep(1)
    # Join class
    b.find_element_by_xpath(
        "//span[@class='l4V7wb Fxmcue']").click()
    # end=b.find_element_by_xpath("//button[@class='VfPpkd-Bz112c-LgbsSe yHy1rc eT1oJ tWDL4c jh0Tpd Gt6sbf QQrMi ftJPW']")
    # end.click()
    pause.until(datetime(year=datetime.now().year, month=datetime.now().month,
                         day=datetime.now().day, hour=int(term[0]), minute=int(term[1]), microsecond=0))
    b.close()



pswd=plain_text_encryptedpassword
while (True):
    cur = datetime.now()

    try:
        if(cur.hour==9 and cur.minute>=1):
            launch(Times(day=cur.weekday(),index=0).clastime(),pswd,[10,0])
            pause.until(datetime(year=datetime.now().year,month=datetime.now().month,
                                 day=datetime.now().day,hour=10,minute=5,microsecond=0))
        elif(cur.hour==10 and cur.minute>6):
            launch(Times(day=cur.weekday(),index=1).clastime(),pswd,[11,0])
            pause.until(datetime(year=datetime.now().year, month=datetime.now().month,
                                 day=datetime.now().day, hour=11, minute=7, microsecond=0))
        elif(cur.hour==12 and cur.minute>0):
            launch(Times(day=cur.weekday(),index=2).clastime(),pswd,[12,0])
            pause.until(datetime(year=datetime.now().year, month=datetime.now().month,
                                 day=datetime.now().day, hour=13, minute=45, microsecond=0))
        elif (cur.hour>=13 and cur.minute>=00):
            launch(Times(day=cur.weekday(),index=3).clastime(),pswd,[15,30])
            pause.until(datetime(year=datetime.now().year, month=datetime.now().month,
                                 day=datetime.now().day, hour=15, minute=30, microsecond=0))
    except Exception as e:
        print(e)
        print("Browser Terminated")


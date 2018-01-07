from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time,sys,requests

res = requests.get("http://textuploader.com/dce2k/raw")
url = res.text

chrome_options = Options()  
chrome_options.binary_location = r"/app/.apt/usr/bin/google-chrome"
errors = 0
while True:
    try:
        print("-----SURPRISE---DIGGER--------By-UDIT-CHOUHAN")
        
        driver = webdriver.Chrome(chrome_options=chrome_options)
        #driver = webdriver.Chrome(executable_path="chromedriver.exe", chrome_options=chrome_options)
        
        driver.get(url)
        while True:
            driver.switch_to_frame(driver.find_element_by_xpath('/html/body/center/form/div/iframe'))
            captcha = driver.find_element_by_class_name('verify-me-progress')
            captcha.click()
            tt=0
            while True:
                bar = driver.find_element_by_xpath('//*[@id="verify-me-progress"]')
                style = bar.get_attribute("style")
                style = style.replace("width: ","")[:3]
                style = style.replace(";","")
                if "100" in style:
                    print(">> Captcha Verified in " + str(tt) + " seconds. Claiming...")
                    driver.switch_to_default_content()
                    break
                time.sleep(1)
                tt+=1
                if tt >= 500:
                    print(">> Taking tooo much time! Retrying...")
                    crash_program

            submit = driver.find_element_by_xpath("/html/body/center/form/a/input")
            submit.click()
    except:
        errors += 1
        if errors == 5:
            driver.quit()
            crash_program
        driver.quit()
        continue

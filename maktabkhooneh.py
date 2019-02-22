from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
import os

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

# links.append(str(browser.find_element_by_css_selector(".hq-video-dl").get_attribute("href")))
# browser.find_element_by_css_selector(".next.undecored_link").click()


def linkReader() :
    links = []
    f = open("links.txt",'r')
    m = f.readlines()
    f.close()
    i = 0
    while i < len(m) :
        if len(m[i]) < 5 :
            pass
        else :
            links.append(m[i].strip())
        i += 1
    return links

def logging_in(browser) :
    browser.find_element_by_css_selector("#show_login").click()
    time.sleep(1)
    browser.find_element_by_css_selector("#login-email").send_keys("tsp5majidi@gmail.com")
    browser.find_element_by_css_selector("#login-pass").send_keys("majidi6444")
    browser.find_element_by_css_selector("#signin-submit").click()
    time.sleep(1)

def goingToClass(browser) :
    browser.find_element_by_css_selector('.lesson-links').click()

def linkGetter(browser) :
    return browser.find_element_by_css_selector(".hq-video-dl").get_attribute("href")

def next(browser) :
    link = browser.find_element_by_css_selector(".next.undecored_link").get_attribute("href")
    if len(str(link)) > 4 :
        try :
            browser.find_element_by_css_selector(".next.undecored_link").click()
        except Exception as e:
            if "is not clickable at point" in str(e) :
                return False
        return True
    else :
        return False

def linkWriter(link) :
    f = open("hrefs.txt","a")
    f.write(link+"\n")
    f.close()

def lineWriter() :
    f = open("hrefs.txt","a")
    f.write("------------------------------------------------\n")
    f.close()

def action(browser) :
    logging_in(browser)
    goingToClass(browser)
    linkGetter(browser)

def main() :
    option = webdriver.ChromeOptions()
    browser = webdriver.Chrome(chrome_options=option)
    main_urls = linkReader()
    if len(main_urls) > 0:
        browser.get(main_urls[0])
        logging_in(browser)
        time.sleep(2)
        for link in main_urls :
            browser.get(link)
            lineWriter()
            hrefs = []
            goingToClass(browser)
            while True :
                item = linkGetter(browser)
                linkWriter(item)
                if not(next(browser)) :
                    break

main()

# find_elements_by_css_selector
# get_attribute

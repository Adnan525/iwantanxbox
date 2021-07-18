import time
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime, timedelta
import smtplib

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH = "C:\Program Files (x86)\chromedriver.exe"
lastSentRetailer = "";

target = "https://www.xbox.com/en-AU/consoles/xbox-series-x#purchase"
counter = 0



def alertStock(retailer, linkURL):
    print(f"================>XBOX may be available now, check retailer's website, retailer : {retailer}")

    # if lastSentRetailer != retailer:
    #
    #     main.lastSentRetailer = retailer
    with smtplib.SMTP("smtp.gmail.com", 587) as smtpmanager:
        smtpmanager.ehlo()
        # encrypt
        smtpmanager.starttls()
        smtpmanager.ehlo()

        email = "emailAddress"
        password = "password"

        now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        subject = "XBOX available now"
        body = f"Please check the following retailer's webiste-\nRetailer: {retailer}\nTime checked: {now}\nURL:{linkURL}"
        msg = f'From: Selenium Automation - XBOX - Adnaan\nSubject: {subject}\n\n{body}'

        smtpmanager.login(email, password)
        smtpmanager.sendmail(email, "adnaan525@gmail.com", msg)
        print("================Email notification sent================")
        smtpmanager.quit()


# def getRetailer(i):
#     if i == 0:
#         return "Amazon"
#     elif i == 1:
#         return "EB Games"
#     elif i == 2:
#         return "Big W"
#     elif i == 3:
#         return "Harvey Norman"
#     else:
#         return "JB Hi-Fi"



def findXBOX():
    driver = webdriver.Chrome(PATH)
    driver.get(target)

    topContentBlockList_3 = driver.find_element_by_id("TopContentBlockList_3")
    cTAdiv = topContentBlockList_3.find_element_by_class_name("CTAdiv")
    availButton = cTAdiv.find_element_by_class_name("c-call-to-action")
    availButton.click()

    buyBoxPurchases = driver.find_element_by_class_name("buyBoxPurchases")
    purchBoxes = buyBoxPurchases.find_element_by_class_name("purchBoxes")
    standalonePurch = purchBoxes.find_element_by_id("standalonePurch")
    buyGroup = standalonePurch.find_element_by_class_name("buy-group")
    selectRetButton = buyGroup.find_element_by_class_name("c-call-to-action")
    selectRetButton.click()

    time.sleep(3)
    # can jump straight to this instead of running the previous code blocks
    print(f"================> Checked on : {datetime.now().strftime('%H:%M:%S')}")
    cDialog = driver.find_element_by_class_name("c-dialog")
    dialogbox = cDialog.find_element_by_class_name("dialogbox")
    doc = dialogbox.find_element_by_xpath("//div[@role = 'document']")
    lbbody = doc.find_element_by_class_name("lbbody")
    prod1 = lbbody.find_element_by_class_name("prod1")

    hatchretailers = prod1.find_elements_by_class_name("hatchretailer")

    for retailer in hatchretailers:
        # global counter
        # retailerHardTyped = getRetailer(counter)
        # if counter == 4:
        #     counter = 0
        # altTag = retailer.find_element_by_xpath("//span[@class='retlogo']//img").get_attribute("alt")
        # print(retailer.find_element_by_class_name("retlogo").find_element_by_xpath("//img").get_attribute('alt'))
        logos = retailer.find_element_by_css_selector("span.retlogo img")
        retailerName = str(logos.get_attribute("alt")).split(" ")[0];
        price = retailer.find_element_by_class_name("retprice")
        stock = retailer.find_element_by_class_name("retstockbuy")

        #check stock to get the link
        if "OUT OF STOCK" != stock.text:
            link = stock.find_element_by_css_selector("a.c-call-to-action.f-lightweight").get_attribute("href")
            alertStock(retailerName, link)
        # counter += 1
        print("Retalier : {shop}, current price : {priceStr}, stock status : {status}"
              .format(shop=retailerName, priceStr=price.text, status=stock.text))

    time.sleep(3)
    print(f"================> Scheduled check on : {datetime.now()+ timedelta(hours=1)}\n")
    driver.quit()



# def textStyling(str):
#     print("==========>{str}".format(str = str))

# if __name__ == '__main__':
#
#     conStatus = requests.get(target)
#     if conStatus.ok:
#         textStyling("Connection Established")
#         source = conStatus.text
#         soupInstance = BeautifulSoup(source, "lxml")
#         #retailers = soupInstance.find("h1", class_ ="c-heading-1a x-hidden-focus")
#         # retailerName = retailers.find("span", class_ = "retline retlogo")
#
#         print(soupInstance.find("div", class_= "option text-uppercase"))
#
#
#     else:
#         textStyling(f"Connection to URl: {target} could not be established, found status {conStatus.status_code}")
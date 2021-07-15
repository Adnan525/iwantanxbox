from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

target = "https://www.xbox.com/en-AU/consoles/xbox-series-x#purchase"

def alertStock(str):
    if "OUT OF STOCK" != str:
        print("================XBOX may be available now, check retailer's website================")

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


#can jump straight to this instead of running the previous code blocks
cDialog = driver.find_element_by_class_name("c-dialog")
dialogbox = cDialog.find_element_by_class_name("dialogbox")
doc = dialogbox.find_element_by_xpath("//div[@role = 'document']")
lbbody = doc.find_element_by_class_name("lbbody")
prod1 = lbbody.find_element_by_class_name("prod1")

hatchretailers = prod1.find_elements_by_class_name("hatchretailer")
for retailer in hatchretailers:
    #altTag = retailer.find_element_by_xpath("//span[@class='retlogo']//img").get_attribute("alt")
    print(retailer.find_element_by_class_name("retlogo"))
    price = retailer.find_element_by_class_name("retprice")
    stock = retailer.find_element_by_class_name("retstockbuy")
    alertStock(stock.text)
    print("Retalier : retailer, current price : {priceStr}, stock status : {status}".format(priceStr = price.text, status = stock.text))



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
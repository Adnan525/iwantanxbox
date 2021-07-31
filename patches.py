from selenium import webdriver
import time
import logging

PATH = "C:\Program Files (x86)\chromedriver.exe"
logging.basicConfig(level=logging.INFO, filename="xboxStock.log")

#patches will return availability

def amazonPatch(link: str):
    logging.info("================>Checking AMAZON patch")
    driverAmazonPatch = webdriver.Chrome(PATH)
    driverAmazonPatch.get(link)
    time.sleep(10)
    availabilityAmazon = driverAmazonPatch.find_element_by_id("availability_feature_div")
    # subAvail = availabilityAmazon.find_element_by_id("availability")
    temp = availabilityAmazon.find_element_by_css_selector(".a-size-medium")
    logging.info(f"================>Amazon availability on amazonPatch: {temp.text}")
    time.sleep(3)
    return False if temp.text == "Currently unavailable." else True
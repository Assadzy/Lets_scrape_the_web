from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import csv
from time import sleep
from selenium.webdriver.chrome.options import Options

driver = webdriver.Chrome()
driver.get()

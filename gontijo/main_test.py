from xpaths import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import os
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome(executable_path='./gontijo/chromedriver/chromedriver')

url = 'https://www.gontijo.com.br/'
driver.get(url)
time.sleep(1)

saindo_de = "governador valadares-mg"
indo_para = "belo horizonte-mg"

data_partida = "10/10/2020"
data_volta = "30/10/2020"

driver.find_element_by_xpath(saindo_de_xpath).send_keys(saindo_de)
time.sleep(0.5)
driver.find_element_by_xpath(saindo_de_xpath).send_keys(Keys.DOWN)
time.sleep(0.5)
driver.find_element_by_xpath(saindo_de_xpath).send_keys(Keys.TAB)
time.sleep(0.5)

driver.find_element_by_xpath(indo_para_xpath).send_keys(indo_para)
time.sleep(0.5)
driver.find_element_by_xpath(indo_para_xpath).send_keys(Keys.DOWN)
time.sleep(0.5)
driver.find_element_by_xpath(indo_para_xpath).send_keys(Keys.TAB)
time.sleep(1)

driver.find_element_by_xpath(data_de_partida_xpath).send_keys(data_partida)
time.sleep(0.5)
driver.find_element_by_xpath(data_de_volta_xpath).send_keys(data_volta)
time.sleep(0.5)
driver.find_element_by_xpath(pesquisar_passagens_btn_xpath).click()
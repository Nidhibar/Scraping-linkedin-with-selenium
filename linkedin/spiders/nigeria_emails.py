from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
import parameters
from parsel import Selector

driver=webdriver.Chrome()
driver.maximize_window()
sleep(0.5)
driver.get('https://www.linkedin.com/')
sleep(6)
driver.find_element_by_xpath('//a[text()="Sign in"]').click()
sleep(3)

username=driver.find_element_by_name('session_key')
username.send_keys('nidhibar24@gmail.com')
sleep(0.5)

password=driver.find_element_by_name('session_password')
password.send_keys('ihdiN@42') #instead type parameters.password for referencing from that file
sleep(0.5)
#click on signin button
driver.find_element_by_xpath('//button[text()="Sign in"]').click()
sleep(7)
driver.get('https://www.google.com/')
sleep(4)
search_input=driver.find_element_by_name("q")
 search_input.send_keys('Aerix Global Solutions (Nigeria) Limited - Aerix official website')
sleep(1)
search_input.send_keys(Keys.RETURN)
sleep(3)

profiles=driver.find_elements_by_xpath('//*[@class="r"]/a[1]')
driver.get(profile)
sleep(3)
# sel=Selector(text=driver.page_source)
# name=sel.xpath('//title/text()').extract_first().split(' | ')
# jobtitle=sel.xpath('//h2/text()')[2].extract().strip()
# schools=sel.xpath('//*[contains(@class,"pv-entity__school-name")]/text()').extract()

driver.quit()
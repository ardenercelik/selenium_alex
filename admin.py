import os
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

def frame_switch(css_selector):
  driver.switch_to.frame(driver.find_element_by_xpath(css_selector))
#sifre id ekle

epostaUrl = '//*[@id="txtUyeGirisEmail"]'
passwordUrl = '//*[@id="txtUyeGirisPassword"]'
girisyapUrl = '//*[@id="mainHolder_Panel1"]/div/div/div/div[6]/button'

stokKodu = '//*[@id="cphPageContent_txtbxStokKodu"]'
urunAdi = '//*[@id="txtbxUrunAdi"]'
adresOlustur = '//*[@id="tabs1"]/div/div/div[6]/div/a'
marka = '//*[@id="btnFiltreMarkaSecim"]'
markaSec = '//*[@id="form1"]/div[7]/table/tbody/tr[1]/td[5]/button'
markaEkle = '//*[@id="form1"]/div[6]/table/tbody/tr[2]/td/button'


driver = webdriver.Chrome('./chromedriver.exe')
mouse = webdriver.ActionChains(driver)
driver.get('https://www.alturkuaz.com/Admin/UrunIslemleri.aspx')

UserElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(epostaUrl))
UserElement.send_keys(USER)
UserElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(passwordUrl))
UserElement.send_keys(PASS)
WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(girisyapUrl)).click()

#select dogal taslar
select = WebDriverWait(driver, 10).until(lambda driver: Select(driver.find_element_by_xpath('//*[@id="divKategoriler"]/select')))
select.select_by_value('17')

element = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath('//*[@id="tabs1"]/div/div/div[1]/div[2]/a[1]'))
mouse.move_to_element(element).click().perform()

select = WebDriverWait(driver, 10).until(lambda driver: Select(driver.find_element_by_xpath('//*[@id="divBreadcrumb"]/select')))
select.select_by_value('17')

driver.find_element_by_xpath(stokKodu).send_keys('666')
driver.find_element_by_xpath(urunAdi).send_keys('arden-deneme')

element = driver.find_element_by_xpath(adresOlustur)
mouse.move_to_element(element).click().perform()
driver.find_element_by_xpath(marka).click()

#frame degistir 
frame_switch('/html/body/div[3]/div/div/div[1]/div/iframe')


WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(markaSec)).click()
print(driver.window_handles)
WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(markaEkle)).click()
driver.find_element_by_xpath('//*[@id="txt_Marka_Ara"]').send_keys('sdf')
print(driver.window_handles)
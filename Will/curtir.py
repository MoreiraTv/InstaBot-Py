from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from random import randint

def curtir_fotos_com_a_hastag(self, hashtag):
    driver = self.driver
    driver.get("https://www.instagram.com/explore/tags/" + hashtag + "/")
    sleep(5)
    for i in range(
        1, 3
    ):  # Altere o segundo valor aqui para que ele desça a quantidade de páginas que você quiser: quer que ele desça 5 páginas então você deve alterar de range(1,3) para range(1,5)
        driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")
        sleep(3)
    hrefs = driver.find_elements_by_tag_name("a")
    pic_hrefs = [elem.get_attribute("href") for elem in hrefs]
    print(hashtag + " fotos: " + str(len(pic_hrefs)))
    testes = [
        href
        for href in pic_hrefs
        if hashtag in href and href.index("https://www.instagram.com/p") != -1
    ]

    for pic_href in pic_hrefs:
        try:
            pic_href.index("https://www.instagram.com/p")
        except ValueError as err:
            print("pulando link inválido")
            continue
        driver.get(pic_href)
        driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")
        try:
            if driver.find_element_by_xpath('//section/span/button[@type="button"]/div[2]/span/svg[@aria-label="Curtir"]'): 
                driver.find_element_by_xpath(
                    '//section/span/button[@type="button"]').click()
                sleep(randint(19, 23))
        except Exception as e:
            print(e)
            sleep(5)
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
            section = driver.find_element_by_css_selector("section.ltpMr.Slqrh")
            buttonLike = section.find_element_by_css_selector("button.wpO6b")
            if(buttonLike):
                test = buttonLike
                buttonLike.click()
                print(test)
            # if(buttonCurtir):
            #     driver.find_element_by_xpath("//*[@aria-label='Curtir']").click()
            #driver.find_element_by_xpath("//*[@aria-label='Like']")
            #driver.find_element_by_xpath("//*[@aria-label='Curtir']")

            sleep(randint(19, 23))
        except Exception as e:
            print(e)
            sleep(5)
# def curtir_fotos_com_a_hastag(self, hashtag):
#     driver = self.driver
#     driver.get("https://www.instagram.com/explore/tags/" + hashtag + "/")
#     sleep(2)

#     # gathering photos
#     pic_hrefs = []
#     for i in range(1, 7):
#         try:
#             driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#             sleep(2)
#             # get tags
#             hrefs_in_view = driver.find_elements_by_tag_name('a')
#             # finding relevant hrefs
#             hrefs_in_view = [elem.get_attribute('href') for elem in hrefs_in_view
#                                 if '.com/p/' in elem.get_attribute('href')]
#             # building list of unique photos
#             [pic_hrefs.append(href) for href in hrefs_in_view if href not in pic_hrefs]
#             # print("Check: pic href length " + str(len(pic_hrefs)))
#         except Exception:
#             continue

#     # Liking photos
#     unique_photos = len(pic_hrefs)
#     for pic_href in pic_hrefs:
#         driver.get(pic_href)
#         sleep(2)
#         driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#         try:
#             sleep(random.randint(2, 4))
#             # like_button = lambda: driver.find_element_by_xpath('//span[@aria-label="Curtir"]').click()
#             like_button = lambda:driver.find_element_by_xpath('//span[@aria-label="Curtir"]').click()
#             like_button().click()
#             for second in reversed(range(0, random.randint(18, 28))):
#                 print_same_line("#" + hashtag + ': unique photos left: ' + str(unique_photos)
#                                 + " | Sleeping " + str(second))
#                 sleep(1)
#         except Exception as e:
#             sleep(2)
#         unique_photos -= 1
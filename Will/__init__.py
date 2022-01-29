from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
import math
from seguir import seguirFollowPerfil
from curtir import curtir_fotos_com_a_hastag
from commentPost import InstagramBotComment

class InstagramBot:
    def __init__(self, cookies):
        self.cookies = cookies
        # ChromeProfile = webdriver.ChromeProfile()
        # ChromeProfile.set_preference("intl.accept_languages", "pt,pt-BR")
        # ChromeProfile.set_preference("dom.webnotifications.enabled", False)
        self.driver = webdriver.Chrome(
            executable_path=r"./chromedriver.exe"
        )  # Coloque o caminho para o seu geckodriver aqui
        # executable_path=r"./geckodriver.exe"

    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com")
        time.sleep(random.randint(2, 5))
        try:
            login_button = driver.find_element_by_xpath(
                "//a[@href='/accounts/login/?source=auth_switcher']"
            )
            login_button.click()
        except:
            print('já estamos na página de login')
            pass
        
        time.sleep(random.randint(2, 5))
        #entrando na conta de usario pela sesion Id token sem precisar da senha do usuario
        driver.add_cookie(self.cookies)

        print("entrando na conta de usario pela sesion Id token sem precisar da senha do usuario")
        driver.refresh()

        time.sleep(3)

        sizeElement = len(driver.find_elements_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]'))
        isPresent = sizeElement > 0
        
        if isPresent:
            time.sleep(random.randint(2, 5))
            driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]').click()
        
        #/html/body/div[5]/div/div/div/div[3]/button[2]
        time.sleep(random.randint(2, 3))
        self.capturaFollowCount()
        

    
    def capturaFollowCount(self):
        driver = self.driver
        driver.find_element_by_xpath('//section/nav/div[2]/div/div/div[3]/div/div[6]/span').click()
        time.sleep(random.randint(2, 5))
        driver.find_element_by_xpath('//section/nav/div[2]/div/div/div[3]/div/div[6]/div[2]/div[2]/div[2]/a[1]').click()
        time.sleep(random.randint(2, 5))
        follows = driver.find_element_by_xpath('//header/section/ul/li[2]/a/span').text
        
        print("Começando o codigo com ",follows,"seguidores")
        #//header/section/ul/li[1]/a/span

        curtir_fotos_com_a_hastag(self, 
            "programacao"
        )  # Altere aqui para a hashtag que você deseja usar.
        seguirFollowPerfil("filipedeschamps", 50)

    @staticmethod
    def type_like_a_person(sentence, single_input_field):
        """ Este código irá basicamente permitir que você simule a digitação como uma pessoa """
        print("going to start typing message into message share text area")
        for letter in sentence:
            single_input_field.send_keys(letter)
            time.sleep(random.randint(1, 5) / 30)


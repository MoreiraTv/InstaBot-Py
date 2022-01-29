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
    
    # def seguirFollowPerfil(self, perfil, countFollow):
    #     driver = self.driver

    #     driver.get("https://www.instagram.com/" + perfil)
    #     time.sleep(3)
    #     hrefPerfil = '/'+ perfil + '/followers/'
    #     elems = driver.find_element_by_css_selector("#react-root > section > main > div > header > section [href]").click()
        
    #     time.sleep(random.randint(2, 4))
    #     driver.find_element_by_css_selector('body > div.RnEpo.Yx5HN > div > div > div.isgrP > ul > div')
    #     time.sleep(random.randint(2, 4))
    #     rounds = math.ceil((countFollow / 12))
    #     print(rounds)
    #     for i in range(
    #         1, rounds
    #     ):  # Altere o segundo valor aqui para que ele desça a quantidade de páginas que você quiser: quer que ele desça 5 páginas então você deve alterar de range(1,3) para range(1,5)
    #         driver.execute_script(
    #             "let divElem = document.querySelector('body > div.RnEpo.Yx5HN > div > div > div.isgrP');document.querySelector('body > div.RnEpo.Yx5HN > div > div > div.isgrP').scrollTop +=357;"
    #         )
    #         time.sleep(random.randint(1, 5))



# jhonatanBot = InstagramBot(
#     #está com 170 follows
#     # {'domain': '.instagram.com', 'expiry': 1674084111, 'httpOnly': True, 'name': 'sessionid', 'path': '/', 'secure': True, 'value': '51284129573%3AVzR0jTdM6aRo94%3A0'}
#     # {'domain': '.instagram.com', 'expiry': 1674219274, 'httpOnly': True, 'name': 'sessionid', 'path': '/', 'secure': True, 'value': '51284129573%3Ag1z6etzQzy2Spv%3A2'}
#     { "domain": ".instagram.com", "expirationDate": cookie_expiration, "httpOnly": True, "name": "sessionid", "path": "/", "secure": True, "session": False, "value": cookie_value},
# )  # Entre com o usuário e senha aqui
# jhonatanBot.login()

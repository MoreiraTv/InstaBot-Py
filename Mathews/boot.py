from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
import math


class InstagramBot:
    def __init__(self, cookies):
        self.cookies = cookies
        self.driver = webdriver.Chrome(
            executable_path=r"./chromedriver.exe"
        )  # Coloque o caminho para o seu geckodriver aqui
        # executable_path=r"./geckodriver.exe"

    def progress_bar(self, done):
        print("\rProgress: [{0:50s}] {1:.1f}%".format('#' * int(done * 50), done * 100),end='')


    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com")
        time.sleep(3)
        try:
            login_button = driver.find_element_by_xpath(
                "//a[@href='/accounts/login/?source=auth_switcher']"
            )
            login_button.click()
        except:
            print('já estamos na página de login')
            pass
        
        time.sleep(3)
        #entrando na conta de usario pela sesion Id token sem precisar da senha do usuario
        driver.add_cookie(self.cookies)

        print("entrando na conta de usario pela sesion Id token sem precisar da senha do usuario")
        driver.refresh()

        time.sleep(3)

        sizeElement = len(driver.find_elements_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]'))
        isPresent = sizeElement > 0
        
        if isPresent:
            driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]').click()
        
        #/html/body/div[5]/div/div/div/div[3]/button[2]
        
        self.capturaFollowCount()
        
    
    def capturaFollowCount(self):
        driver = self.driver
        driver.find_element_by_xpath('//section/nav/div[2]/div/div/div[3]/div/div[6]/span').click()
        time.sleep(3)
        driver.find_element_by_xpath('//section/nav/div[2]/div/div/div[3]/div/div[6]/div[2]/div[2]/div[2]/a[1]').click()
        time.sleep(2)
        follows = driver.find_element_by_xpath('//header/section/ul/li[2]/a/span').text
        
        print("Você tem: ",follows,"seguidores!")
        #//header/section/ul/li[1]/a/span

        self.curtir_fotos_com_a_hastag(
            "memesbr"
        )  # Altere aqui para a hashtag que você deseja usar.

    @staticmethod
    def type_like_a_person(sentence, single_input_field):
        """ Este código irá basicamente permitir que você simule a digitação como uma pessoa """
        print("going to start typing message into message share text area")
        for letter in sentence:
            single_input_field.send_keys(letter)
            time.sleep(random.randint(1, 5) / 30)

    def curtir_fotos_com_a_hastag(self, hashtag):
        # driver = self.driver
        # driver.get("https://www.instagram.com/explore/tags/" + hashtag + "/")
        # time.sleep(5)
        # for i in range(
        #     1, 3
        # ):  # Altere o segundo valor aqui para que ele desça a quantidade de páginas que você quiser: quer que ele desça 5 páginas então você deve alterar de range(1,3) para range(1,5)
        #     driver.execute_script(
        #         "window.scrollTo(0, document.body.scrollHeight);")
        #     time.sleep(3)
        # hrefs = driver.find_elements_by_tag_name("a")
        # pic_hrefs = [elem.get_attribute("href") for elem in hrefs]
        # print(hashtag + " fotos: " + str(len(pic_hrefs)))
        # testes = [
        #     href
        #     for href in pic_hrefs
        #     if hashtag in href and href.index("https://www.instagram.com/p") != -1
        # ]

        # for pic_href in pic_hrefs:
        #     time.sleep(2)
        #     try:
        #         pic_href.index("https://www.instagram.com/p")
        #     except ValueError as err:
        #         print("pulando link inválido")
        #         continue
        #     driver.get(pic_href)
        #     driver.execute_script(
        #         "window.scrollTo(0, document.body.scrollHeight);")
        #     try:
        #         driver.find_element_by_xpath(
        #             '//section/span/button[@type="button"]').click()
        #         time.sleep(random.randint(19, 23))
        #     except Exception as e:
        #         print(e)
        #         time.sleep(5)
        
        self.seguirFollowPerfil("guigrillo13", 25)
    
    def seguirFollowPerfil(self, perfil, countFollow):
        driver = self.driver

        driver.get("https://www.instagram.com/" + perfil)
        time.sleep(3)
        hrefPerfil = '/'+ perfil + '/followers/'
        elems = driver.find_element_by_css_selector("#react-root > section > main > div > header > section [href]").click()
        
        time.sleep(2)
        element = driver.find_element_by_css_selector('body > div.RnEpo.Yx5HN > div > div > div.isgrP')
        time.sleep(2)
        rounds = countFollow
        # rounds = math.ceil((countFollow / 12))
        print("rounds: ",rounds)
        pagedrop = math.ceil((rounds / 2))
        print("carregando lista de pessoas para seguir!")
        buttons = driver.find_elements_by_css_selector('button.sqdOP.L3NKy.y3zKF')
        for z in range(1, pagedrop):
            self.progress_bar(z/pagedrop)
            time.sleep(1)
            driver.execute_script(#/html/body
                "let divElem = document.querySelector('body > div.RnEpo.Yx5HN > div > div > div.isgrP');document.querySelector('body > div.RnEpo.Yx5HN > div > div > div.isgrP').scrollTop +=365;"
            )
            time.sleep(3)
            buttons = driver.find_elements_by_css_selector('button.sqdOP.L3NKy.y3zKF')
        #f31726da9d07ae > button
        #sqdOP  L3NKy   y3zKF     seguir
        #sqdOP  L3NKy   y3zKF  seguir
        #sqdOP  L3NKy    _8A5w5     seguindo
        #  .button.sqdOP.L3NKy.y3zKF 
        # driver.execute_script(#/html/body
        #     "let divElem = document.querySelector('body > div.RnEpo.Yx5HN > div > div > div.isgrP');document.querySelector('body > div.RnEpo.Yx5HN > div > div > div.isgrP').scrollTop +=357;"
        # )
        time.sleep(3)
        # pic_buttons = [for elem in buttons]
        x = 1
        for pic_button in buttons:
            time.sleep(2)
            # driver.get(pic_button)
            print("já seguimos: ", x)
            if(x == rounds): break
        
            try:
                if(pic_button.text == "Seguindo"):
                    continue
                if(pic_button.text == "Solicitado"):
                    continue
                else:
                    pic_button.click()
                    x = x + 1
                time.sleep(random.randint(2, 6))
                    
            except Exception as e:
                print("error: ",e)
                time.sleep(5)

        
            #element.scrollTo(0, 100)
            #scrollPosition = 357
        print("acamos de seguir")
                

with open("../token_value", "r", encoding="utf-8") as tf:
    cookie_value = tf.read()

with open("../token_expiration", "r", encoding="utf-8") as tf:
    cookie_expiration = tf.read()

jhonatanBot = InstagramBot(
    { "domain": ".instagram.com", "expirationDate": cookie_expiration, "httpOnly": True, "name": "sessionid", "path": "/", "secure": True, "session": False, "value": cookie_value},
)
jhonatanBot.login()

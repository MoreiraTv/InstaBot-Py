import time
import random
import math
def progress_bar(done):
    print("\rProgress: [{0:50s}] {1:.1f}%".format('#' * int(done * 50), done * 100),end='')

def seguirFollowPerfil(self, perfil, countFollow):
    driver = self.driver
    driver.get("https://www.instagram.com/" + perfil)
    time.sleep(random.randint(2, 5))
    hrefPerfil = '/'+ perfil + '/followers/'
    elems = driver.find_element_by_css_selector("#react-root > section > main > div > header > section [href]").click()
    
    time.sleep(random.randint(2, 5))
    element = driver.find_element_by_css_selector('body > div.RnEpo.Yx5HN > div > div > div.isgrP')
    time.sleep(random.randint(2, 3))
    rounds = countFollow
    # rounds = math.ceil((countFollow / 12))
    print("rounds: ",rounds)
    pagedrop = math.ceil((rounds / 2))
    print("carregando lista de pessoas para seguir!")
    buttons = driver.find_elements_by_css_selector('button.sqdOP.L3NKy.y3zKF')
    for z in range(1, pagedrop):
        progress_bar(z/pagedrop)
        time.sleep(1)
        driver.execute_script(#/html/body
            "let divElem = document.querySelector('body > div.RnEpo.Yx5HN > div > div > div.isgrP');document.querySelector('body > div.RnEpo.Yx5HN > div > div > div.isgrP').scrollTop +=365;"
        )
        time.sleep(random.randint(2, 5))
        buttons = driver.find_elements_by_css_selector('button.sqdOP.L3NKy.y3zKF')
    lastButton = buttons.pop()
    if(lastButton.text == "Seguindo"):
        for z in range(1, pagedrop):
            progress_bar(z/pagedrop)
            time.sleep(1)
            driver.execute_script(#/html/body
                "let divElem = document.querySelector('body > div.RnEpo.Yx5HN > div > div > div.isgrP');document.querySelector('body > div.RnEpo.Yx5HN > div > div > div.isgrP').scrollTop +=365;"
            )
            time.sleep(random.randint(2, 5))
            buttons = driver.find_elements_by_css_selector('button.sqdOP.L3NKy.y3zKF')
    if(lastButton.text == "Solicitado"):
        for z in range(1, pagedrop):
            progress_bar(z/pagedrop)
            time.sleep(1)
            driver.execute_script(#/html/body
                "let divElem = document.querySelector('body > div.RnEpo.Yx5HN > div > div > div.isgrP');document.querySelector('body > div.RnEpo.Yx5HN > div > div > div.isgrP').scrollTop +=365;"
            )
            time.sleep(random.randint(2, 5))
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
        time.sleep(random.randint(3, 5))
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
            time.sleep(random.randint(4, 8))
                
        except Exception as e:
            print("error: ",e)
            time.sleep(5)
    
        #element.scrollTo(0, 100)
        #scrollPosition = 357
    print("acabamos de seguir")
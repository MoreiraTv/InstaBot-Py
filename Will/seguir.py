import math
def seguirFollowPerfil(self, perfil, countFollow):
    driver = self.driver

    driver.get("https://www.instagram.com/" + perfil)
    time.sleep(3)
    hrefPerfil = '/'+ perfil + '/followers/'
    elems = driver.find_element_by_css_selector("#react-root > section > main > div > header > section [href]").click()
    
    time.sleep(2)
    driver.find_element_by_css_selector('body > div.RnEpo.Yx5HN > div > div > div.isgrP > ul > div')
    time.sleep(2)
    rounds = math.ceil((countFollow / 12))
    print(rounds)
    for i in range(
        1, rounds
    ):  # Altere o segundo valor aqui para que ele desça a quantidade de páginas que você quiser: quer que ele desça 5 páginas então você deve alterar de range(1,3) para range(1,5)
        driver.execute_script(
            "let divElem = document.querySelector('body > div.RnEpo.Yx5HN > div > div > div.isgrP');document.querySelector('body > div.RnEpo.Yx5HN > div > div > div.isgrP').scrollTop +=357;"
            )
        time.sleep(3)
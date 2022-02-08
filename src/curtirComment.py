from selenium.webdriver.common.keys import Keys
import time
import random

  # def type_like_a_person(sentence, single_input_field):
  #     """ Este código irá basicamente permitir que você simule a digitação como uma pessoa """
  #   print("going to start typing message into message share text area")
  #   for letter in sentence:
  #       single_input_field.send_keys(letter)
  #       time.sleep(random.randint(1, 5) / 30)
def comente_e_curti_nas_fotos_com_a_hashtag(self, hashtag):
    links_de_posts = []
    driver = self.driver
    driver.get("https://www.instagram.com/explore/tags/" + hashtag + "/")
    time.sleep(5)
    for i in range(
        1, 10
    ):  # Altere o segundo valor aqui para que ele desça a quantidade de páginas que você quiser
        driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)
    hrefs = driver.find_elements_by_tag_name("a")
    pic_hrefs = [elem.get_attribute("href") for elem in hrefs]
    print(hashtag + " fotos: " + str(len(pic_hrefs)))
    nCurtidas = 0
    nComments = 0
    for link in pic_hrefs:
        try:
            if link.index("/p/") != -1:
                links_de_posts.append(link)
        except:
            pass
    for pic_href in links_de_posts:
        driver.get(pic_href)
        # driver.execute_script(
        #     "window.scrollTo(0, document.body.scrollHeight);")
        #Curtindo post
        try:
          section = driver.find_element_by_xpath("//*/section/main/div/div[1]/article/div/div[2]/div/div[2]/section[1]")
          buttonLike = section.find_element_by_css_selector("button.wpO6b")
          if buttonLike:
              isLiked = buttonLike.find_element_by_tag_name("svg").get_attribute("aria-label")
              if isLiked == "Curtir":
                  buttonLike.click()
                  nCurtidas= nCurtidas + 1
                  print("Já curtimos: ",nCurtidas," publicações")
                  time.sleep(random.randint(19, 23))
              else:
                  print("Publicação já estava curtida")
                  time.sleep(random.randint(3, 6))
        except Exception as e:
            print(e)
            time.sleep(5)
        
        #comentando Post
        try:
          # "Uau, vou aprender isso!",
          #     "Booom dms, preciso!",
          #     "incrivel!",
          #     "😊😮",
          comments = [
              "Morri kkkkkkk",
              "A não kkkkk",
              "Eu não aguento :V",
              "rsrsrs",
          ]  # Remova esses comentários e insira os seus comentários aqui(refente ao tipo de conteudo que irá comentar)
          driver.find_element_by_class_name("Ypffh").click()
          comment_input_box = driver.find_element_by_class_name("Ypffh")
          time.sleep(random.randint(10, 15))
          self.type_like_a_person(
              random.choice(comments), comment_input_box)
          time.sleep(random.randint(3, 10))
          #@type='submit', 
          driver.find_element_by_xpath(
              "//button[text() = 'Publicar']"
          ).click()
          nComments = nComments + 1
          print("comentarios",nComments)
          time.sleep(random.randint(16, 20))
        except Exception as e:
            print(e)
            time.sleep(5)
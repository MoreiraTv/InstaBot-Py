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
    
    time.sleep(3)
    if isPresent:
        driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]').click()
    
    #/html/body/div[5]/div/div/div/div[3]/button[2]
    
    self.capturaFollowCount()
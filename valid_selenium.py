from selenium import webdriver
from selenium.webdriver.common.by import By


def validalas():
    # Hozz létre egy Firefox driver példányt!
    driver = webdriver.Chrome()

    # Töltse be az oldaladat
    driver.get("https://dvmaja.github.io/Urlap_Validalas/")  # ide a github pages link kell

    # A nevek alapján kerestessük meg az űrlap elemeit!
    k_nev = driver.find_element(By.NAME, "kNev")
    v_nev = driver.find_element(By.NAME, "vNev")
    jelszo1 = driver.find_element(By.NAME, "jelszo1")
    jelszo2 = driver.find_element(By.NAME, "jelszo2")

    # ... 
    # A következő elemet nem kell átírnod:
    submit_gomb = driver.find_element(By.XPATH, "//input[@type='submit']")

    # Add meg a működő - majd később a nem működő - teszt adatokat!
    k_nev.send_keys("John")
    v_nev.send_keys("Smith")
    jelszo1.send_keys("12345")
    jelszo2.send_keys("12345")
    #k_nev.send_keys("valami")
    #v_nev.send_keys("23Béla")

    # ...

    # Kattints a submit gombra!
    submit_gomb.click()

    # Várunk egy keveset, hogy lássunk is valamit...
    driver.implicitly_wait(10)

    # Megnézzük, megjelent-e a div elemünk
    success_message = driver.find_element(By.XPATH, "//div[@class='success-message']")
    if success_message.is_displayed():
        print("Sikerült az űrlap küldése!")
    else:
        print("Nem sikerült az űrlap küldése!")

    # Csukjuk be a böngésző ablakot!
    driver.quit()

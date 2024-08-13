from time import sleep
from selenium import webdriver
from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as condicao_esperada

def iniciar_driver():
    chrome_options = Options()

    arguments = ['--lang=pt-BR', '--window-size=800, 600', '--incognito']
    # '--headless' = Roda em segundo plano sem abrir a janela

    for argument in arguments:
        chrome_options.add_argument(argument)

    caminho_padrao_para_download = 'E:\\Storage\\Desktop'

    chrome_options.add_experimental_option("prefs", {
        'download.default_directory': caminho_padrao_para_download,
        'download.directory_upgrade': True,
        'download.prompt_for_download': False,
        "profile.default_content_setting_values.notifications": 2,
        "profile.default_content_setting_values.automatic_downloads": 1,
    })
    driver = webdriver.Chrome(options=chrome_options)

    
    wait = WebDriverWait(
        driver,
        10,
        poll_frequency=1,
        ignored_exceptions=[
            NoSuchElementException,
            ElementNotVisibleException,
            ElementNotSelectableException
        ]
    )

    return driver, wait

driver, wait = iniciar_driver()
driver.get('https://instagram.com/')

campo_usuario = wait.until(condicao_esperada.element_to_be_clickable((By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')))
campo_usuario.send_keys(usuario)
sleep(3)

campo_senha = wait.until(condicao_esperada.element_to_be_clickable((By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')))
campo_senha.send_keys(senha)
sleep(3)

botao_login = wait.until(condicao_esperada.element_to_be_clickable((By.XPATH, '//*[@id="loginForm"]/div/div[3]/button')))
sleep(3)
botao_login.click()
sleep(20)

driver.get('https://www.instagram.com/{pagina}/')
sleep(3)
driver.execute_script('window.scrollTo(0, 500);')
sleep(3)

postagens = wait.until(condicao_esperada.visibility_of_any_elements_located((By.XPATH, '//div[@class="_aagu"]')))
sleep(3)
postagens[0].click()
sleep(5)

try:
    descurtido_button = driver.find_element(By.XPATH, '//section//*[@aria-label="Curtir"]')
    sleep(2)
    descurtido_button.click()
    print('Postagem foi curtida!')
    sleep(86400)
except:
    curtido_button = driver.find_element(By.XPATH, '//section//*[@aria-label="Descurtir"]')
    print('Postagem já está curtida!')
    sleep(86400)

input('')
driver.close()
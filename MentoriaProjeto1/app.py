# Tecnologias
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui as pg
import logging as lg
import schedule
from time import sleep	
import os 

# Firefox -> geckodriver

lg.basicConfig(level=lg.INFO, filename='app.log', format='%(asctime)s %(levelname)s %(message)s')


def iniciar_driver(site_url, detach=False, headless=False):
    lg.getLogger(__name__)
    try:
        chorme_options = Options()
        # Standard configuration for chrome
        '''
        --start-maximized # Inicia maximizado
        --lang=pt-BR # Define o idioma de inicialização, # en-US , pt-BR
        --incognito # Usar o modo anônimo
        --no-default-browser-check', # Desabilita a busca pelo browser default
        --window-position=0,0', # Define o posicionamento da janela
        --window-size=800,800 # Define a resolução da janela em largura e altura
        --headless # Roda em segundo plano(com a janela fechada)
        --disable-notifications # Desabilita notificações
        --disable-gpu # Desabilita renderização com GPU
        --block-new-web-contents', # Bloqueia pop-ups
        # para rodar na aws ec2:
        # '--disable-gpu', '--no-sandbox', '--headless', '--disable-dev-sh
        '''

        arguments = [
            '--lang=pt-BR', 
            '--window-size=1300,1000', 
            '--disable-notifications',
            '--incognito'
            ]
        for argument in arguments:
            chorme_options.add_argument(argument)

        # configuracoes adicionais do options:

        # rodar em segundo plano
        if headless:
            chorme_options.add_argument('--headless')

        # manter janela aberta
        if detach:
            chorme_options.add_experimental_option('detach', True)

        # desabilitar pop-up de navegador controlado por automacao
        chorme_options.add_experimental_option(
            'excludeSwitches', ['enable-automation'])

        # Using experimental settings
        chorme_options.add_experimental_option('prefs', {
            # Alterar o local padrão de ‘download’ de arquivos
            'download.default_directory': 'C:\\Users\gabri\\PycharmProjects\\Mentorias\\MentoriaProjeto1',
            # notificar o Google chrome sobre essa alteração
            'download.directory_upgrade': True,
            # Desabilitar a confirmação de ‘download’
            'download.prompt_for_download': False,
            # Desabilitar notificações
            'profile.default_content_setting_values.notifications': 2,
            # Permitir multiplos downloads
            'profile.default_content_setting_values.automatic_downloads': 1,

        })

        # Initializing webdriver

        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chorme_options)
        driver.get(site_url)

        wait = WebDriverWait(
            driver,
            10,
            poll_frequency=1,
            ignored_exceptions=[
                    NoSuchElementException,
                    ElementNotVisibleException,
                    ElementNotSelectableException,
                    TimeoutException
            ]
        )

        return driver, wait
    except Exception as e:
        lg.error(f'Error occurred while initializng driver: {type(e).__name__} - {e}')
        return None

# 1 - Preciso de uma automação para fazer a cotação em 2 sites na internet
# - kabum
# - Pichau
# "memória ram 8gb"

# 2 - Depois disso jogar numa planilha de Excel e calcular a margem(lucro)

# 3 - enviar em um grupo do whatsapp

# 4 - todos os dias as 06:00 da manhã
import os
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class WhatsWeb:
    # https://hub.asimov.academy/curso/navegando-na-internet-automaticamente-com-selenium
    def __init__(self):
        self.dir_path = os.getcwd()
        self.downloads = os.path.join(self.dir_path, "_downloads_whats")
        self.last_src = ''

        self.options = webdriver.ChromeOptions()
        profile = os.path.join(self.dir_path, "profile", "wpp")
        self.options.add_argument(r"user-data-dir={}".format(profile))
        # self.options.add_argument("--headless=new") # faz com que o chrome abra sem interface
        self.webdriver = webdriver.Chrome(options=self.options)
        self.webdriver.get("https://web.whatsapp.com")

        sleep(45) 
        # Esse sleep serve para termos tempo de ler o QRcode na primeira vez quer rodar o codigo,
        # nas proximas vezes que rodar esta linha poder ser excluida/comentada

    def buscar_conversa(self):
        try:
            print("Buscando conversa...")
            WebDriverWait(self.webdriver, timeout=10)\
                .until(EC.presence_of_element_located((By.XPATH, '//button[@aria-label="Pesquisar ou começar uma nova conversa"]')))
            print('achou conversa')
            caixa_de_pesquisa = self.webdriver.find_element(By.XPATH, (
                '//button[@aria-label="Pesquisar ou começar uma nova conversa"]'
            ))
            caixa_de_pesquisa.click()
            caixa_de_pesquisa.send_keys('I.S.A.A.C.')
            sleep(2)
            contato = self.webdriver.find_element(By.XPATH, '//*[@title="I.S.A.A.C."]')
            contato.click()
            print("Conversa encontrada e aberta!")
        except Exception as e:
            print(f"Erro ao buscar conversa: {e}")
            raise e

    def buscar_texto(self, post):
        try:
            texto = post[-1].find_element(By.CLASS_NAME, 'selectable-text').text
        except:
            texto = None
        return texto
    
    def baixa_arquivo(self, webdriver, post):
        # Não esqueça de ajustar no Chrome do Selenium a pasta padrão de download.
        midia = post[-1].find_element(By.XPATH, (
            '//*[@data-icon="down-context"]'
        ))
        midia.click()
        baixar = webdriver.find_element(By.XPATH, (
            '//*[@aria-label="Baixar"]'
        ))
        print('CLICK')
        baixar.click()

        arquivos = [
            os.path.join(self.downloads, f) 
            for f in os.listdir(self.downloads) 
            if os.path.isfile(os.path.join(self.downloads, f))
        ]

        arquivo_mais_novo = max(arquivos, key=os.path.getmtime)
        return arquivo_mais_novo

    def buscar_arquivo(self, webdriver, post):
        try:
            actions = ActionChains(webdriver)
            actions.move_to_element(post[-1]).perform()
            src = post[-1].find_element(By.TAG_NAME, 'img').get_attribute('src')
            return src

        except Exception as e:
            print(f"Erro ao ler mensagem: {e}")
            return None

    def ultima_msg(self):
        """ Captura a ultima mensagem da conversa """
        post = self.webdriver.find_elements(By.CLASS_NAME, 'message-out')
        msg = self.buscar_texto(post)
        if msg:
            return msg
        else:
            src = self.buscar_arquivo(self.webdriver, post)
            if self.last_src != src:
                self.last_src = src
                msg = self.baixa_arquivo(self.webdriver, post)
                return msg
            else:
                return None

if __name__ == '__main__':
    whats = WhatsWeb()
    whats.buscar_conversa()
    msg = ''
    last_msg = '/quit'
    while msg != '/quit':
        sleep(1)
        msg = whats.ultima_msg()
        if msg != last_msg and msg:
            print(f"Mensagem recebida: {msg}")
            last_msg = msg
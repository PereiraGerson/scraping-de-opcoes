from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time

# Diretório de download personalizado
diretorio_de_download = r'C:\Users\Consultorio\Documents\cotacao-opcao\cotacao'

# Configuração das opções do Chrome
options = webdriver.ChromeOptions()
prefs = {
    "download.default_directory": diretorio_de_download,
    "download.prompt_for_download": False,
    "download.directory_upgrade": True
}
options.add_experimental_option("prefs", prefs)

# Inicializa o navegador com as opções personalizadas
driver = webdriver.Chrome(options=options)

def baixar_arquivos(urls, espera_maxima=10):
    # Inicializa o navegador
    for url in urls:
        try:
            # Abre a página com o botão de download
            driver.get(url)
            
            # Espera até que o botão de download esteja disponível para ser clicado
            botao = WebDriverWait(driver, espera_maxima).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.dt-button.buttons-excel.buttons-html5')))
            botao.click()
            
            # Espera um tempo para garantir que o download seja concluído
            time.sleep(5)
            
            print(f'Download do arquivo de {url} concluído com sucesso.')
        except Exception as e:
            print(f'Erro ao baixar o arquivo de {url}: {e}')

# Lista de URLs para download
urls = [
    'https://opcoes.net.br/opcoes/bovespa/BOVA11',
    'https://opcoes.net.br/opcoes/bovespa/ABEV3',
    'https://opcoes.net.br/opcoes/bovespa/PETR4',
    'https://opcoes.net.br/opcoes/bovespa/VALE3',
    'https://opcoes.net.br/opcoes/bovespa/ITUB4',
    'https://opcoes.net.br/opcoes/bovespa/BBDC4',
    'https://opcoes.net.br/opcoes/bovespa/MGLU3'
]

try:
    baixar_arquivos(urls)
except Exception as e:
    print(f'Erro ao baixar os arquivos: {e}')

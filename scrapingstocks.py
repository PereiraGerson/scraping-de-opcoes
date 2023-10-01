import pyautogui
import time
from datetime import date
data = date.today()
formato_data = data.strftime( '%d-%m-%Y' )

lista = ['PETR4', 'BOVA11', 'BBDC4', 'MGLU3', 'ABEV3']

pyautogui.PAUSE = 0.5

pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')
time.sleep(1)
pyautogui.click(x=504, y=455)
time.sleep(1)
pyautogui.click(x=399, y=91) #CLICA NO ATALHO DA BARRA DO NAVEGADOR
time.sleep(5) # ESPERA PARA CARREGAR A PAGINA

# FAZ UM LOOP COM TODAS A AÇOES DA LISTA
for options in lista:
    options_with_date = options +' '+ formato_data # SALVA O ARQUIVO COM A DATA DO DIA
    time.sleep(1)
    pyautogui.click(x=263, y=179) # CLICA NO MENU PARA SELECIONAR O ATIVO
    time.sleep(1)
    pyautogui.write(options) # DIGITA O NOME DO ATIVO
    time.sleep(0.5)
    pyautogui.press('enter')
    time.sleep(0.5)
    pyautogui.click(x=1333, y=291)
    time.sleep(1)
    pyautogui.click(x=1315, y=285) # CLICA EM BAIXAR PLANILHA EXCEL
    time.sleep(1)
    pyautogui.write(options_with_date)
    pyautogui.press('enter')
    time.sleep(1)
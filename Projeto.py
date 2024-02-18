#bibliotecas
import pyautogui as Py
import time as T
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
#meu projeto de enviar messagens automaticas
#1.qual contato e a messagem vamos criar
contato = Py.prompt(text='coloque o contato que queria conversar') 
mensagem = Py.prompt(text='mensagem agora:')
#2.abrir webdriver/whatssap
navegador = webdriver.Firefox()
navegador.get('https://web.whatsapp.com/')
Py.alert(text='reconheça o Qr code')
#3.clicar na barra de pesquisa
barra_Pesquisa = navegador.find_element(By.CSS_SELECTOR, '._2vDPL')
barra_Pesquisa.click()
Py.typewrite(contato)
#4.clicar no contato
Py.click(169,297,duration=1)
T.sleep(1)
#5.barra de conversa enviar messagem
Py.typewrite(mensagem)
Py.press('enter')
#6.sair do whatssap
T.sleep(1)
Py.click(374,113,duration=1)
T.sleep(1)
Py.click(144,365, duration=1)
T.sleep(1)
Py.click(628,461,duration=1)
#sair do navegador
T.sleep(2)
navegador.quit()

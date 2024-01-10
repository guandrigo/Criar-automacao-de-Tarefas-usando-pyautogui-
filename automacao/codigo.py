# Criar automacao de Tarefas usando "pyautogui"
# Feito por: Gustavo Andrigo Alves
# Data: 09/01/2024

# Passo a Passo:
# Passo 1 - Entrar no sistema da empresa;
# Passo 2 - Fazer login;
# Passo 3 - Importar a base de dados (produtos);
# Passo 4 - Cadastrar um produto;
# Passo 5 - Repetir ate acabar a base de dados;

# Link do Sistema da Empresa: https://dlp.hashtagtreinamentos.com/python/intensivao/login

# pip install pyautogui

# clicar -> pyautogui.click
# escrever -> pyautogui.write
# apertar uma tecla -> pyautogui.press
# apertar duas ou mais teclas -> pyautogui.hotkey('tecla1', 'tecla2')
# usar scroll -> pyautogui.scroll(valor)

# para temporar um tempo especifico, usar: time.sleep(tempo)

#pip install pandas numpy openpyxl

# apertar a tecla windows
# digitar nome do programa
# apertar enter
# digitar link
# apertar enter

import pyautogui
import time
import pandas

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
tabela = pandas.read_csv('produtos.csv')


pyautogui.PAUSE = 1
pyautogui.press('win')
pyautogui.write('opera')
pyautogui.press('enter')
time.sleep(7)
pyautogui.write(link)
pyautogui.press('enter')
time.sleep(7)

pyautogui.click(x=522, y=287)
pyautogui.write('email')
pyautogui.press('tab')
pyautogui.write('senha')
pyautogui.press('tab')
pyautogui.press('enter')
time.sleep(2.5)


for linha in tabela.index: 
    pyautogui.click(x=503, y=202)
    #codigo
    codigo = tabela.loc[linha, 'codigo']
    pyautogui.write(codigo)
    pyautogui.press('tab')
    #marca
    pyautogui.write(tabela.loc[linha, 'marca'])
    pyautogui.press('tab')
    #tipo
    pyautogui.write(tabela.loc[linha, 'tipo'])
    pyautogui.press('tab')
    #categoria
    pyautogui.write(str(tabela.loc[linha, 'categoria']))
    pyautogui.press('tab')
    #preco_unitario
    pyautogui.write(str(tabela.loc[linha, 'preco_unitario']))
    pyautogui.press('tab')
    #custo
    pyautogui.write(str(tabela.loc[linha, 'custo']))
    pyautogui.press('tab')
    #obs
    obs = tabela.loc[linha, 'obs']
    if not pandas.isna(obs):
        pyautogui.write(obs)
    pyautogui.write('')
    pyautogui.press('tab')
    #enviar
    pyautogui.press('enter')
    pyautogui.scroll(5000)
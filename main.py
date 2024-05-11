
#passo 1: abrir site da instituição
#passo 2: fazer login
#passo 3: ir na aba do financeiro
#passo 4: copiar linha digitavel do boleto
#passo 5: fazer logout
#passo 6: abrir gmail
#passo 7: login no gmail
#passo 8: selecionar para quem deseja mandar o boleto
#passo 9: enviar email

#passo 1: abrir site da instituição
import pandas as pd
import pyautogui as pa
import time

pa.PAUSE = 0.5 # para os comandos nao se atropelarem

pa.press("win")
pa.write("edge")
pa.press("enter") # abrir navegador
time.sleep(3) # esperar o site carregar por 3 segundos para proximo comando
pa.write("<aqui fica o link de login do site>")
pa.press("enter")
time.sleep(5)

#passo 2:
pa.click(x=653, y=410) # coordenadas de click do mouse 
pa.write("<login>")
pa.press("tab")
pa.write("<senha>")
pa.press("enter")
time.sleep(10) # aguardar 10 segundos para o site institucional carregar

#passo 3: 
pa.click(x=30, y=190) # clicar na posicao onde fica a aba financeiro
time.sleep(1)
pa.scroll(-3000) # rolar a tela para baixo
pa.click(x=78, y=256) # clicar na posicao onde fica a aba financeiro
time.sleep(10)
pa.scroll(3000) # rolar a tela de volta para cima

#passo 4: copiar linha digitavel do boleto
pa.click(x=247, y=365) # selecionar tipo de boletos
time.sleep(1)
pa.click(x=283, y=459) # boletos em aberto
time.sleep(3)
pa.mouseDown(x=200, y=530) #pressionar o botão do mouse
time.sleep(1)
pa.moveTo(x=619, y=530) # para mover o mouse
pa.mouseUp() # para soltar o botão do mouse
pa.hotkey('ctrl', 'c') # para copiar linha digitavel

#passo 5: fazer logout
pa.click(x=1272, y=94) 
pa.click(x=1205, y=194) # clicar nos locais respectivos para login
time.sleep(1)

#passo 6: abrir gmail
pa.hotkey('ctrl', 't') # para abrir nova aba
pa.write("gmail.com")
pa.press("enter")
time.sleep(3)

#passo 7: login no gmail
pa.click(x=723, y=296) # local para clicar
pa.write("<seu email>")
pa.press("enter")
time.sleep(3)
pa.write("<senha>")
pa.press("enter")
time.sleep(5)

#passo 8: 
pa.click(x=84, y=158) # para começar um novo email
time.sleep(1)
pa.click(x=786, y=299) # para digitar destinatario
time.sleep(1)
pa.write("<email da pessoa escolhida>")
pa.press("tab") # confirmar 
pa.press("tab")
pa.write("Boleto")
pa.press("tab")
pa.write("<Oi, tudo bem?>")
pa.press("enter")
pa.write("<Segue linha digitavel do boleto: >")
pa.press("enter")
pa.press("enter")
pa.hotkey('ctrl', 'v') # colar linha digitavel
pa.press("enter")
time.sleep(3)
pa.press("tab") # selecionar botao para enviar
pa.press("enter") # enviar email

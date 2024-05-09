import pyautogui as pa
import pandas as pd
import time

pa.PAUSE = 0.5

#Go and log-in to the site

pa.press('win')
pa.write("chrome")
pa.press('enter')


time.sleep(0.5)
pa.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pa.press('enter')

time.sleep(2.25)
pa.press('tab')
pa.write("pythonimpressionador@gmail.com")

pa.press('tab')
pa.write("sua senha aqui")
pa.press('enter')

#Read the informations
table = pd.read_csv('Projetos\Projetinhos\Power_Up\pro.csv')

print(table)

for i in table.index:  
    codigo = table.loc[i, 'codigo']
    marca =  table.loc[i, 'marca']
    tipo = table.loc[i, 'tipo']
    categoria = str(table.loc[i, 'categoria'])
    preco_unitario = str(table.loc[i, 'preco_unitario'])
    custo = str(table.loc[i, 'custo'])
    obs = str(table.loc[i, 'obs'])
    
    pa.click(x=800, y=262)
    pa.write(codigo)

    pa.press('tab')
    pa.write(marca)

    pa.press('tab')
    pa.write(tipo)

    pa.press('tab')
    pa.write(categoria)

    pa.press('tab')
    pa.write(preco_unitario)

    pa.press('tab')
    pa.write(custo)

    pa.press('tab')
    if obs != "nan":
        pa.write(obs)
    
    pa.press('tab')
    pa.press('enter')
    pa.scroll(5000)
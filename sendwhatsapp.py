import pandas as pandas
import time
import urllib
import sys
import pyperclip


from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

contatos_df = pandas.read_excel("Enviar.xlsx")
#display(contatos_df)

navegador = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')
navegador.get("https://web.whatsapp.com/")

while len (navegador.find_elements_by_id('//*[@id="side"]')) < 1:
    time.sleep(1)

    for i, mensagem in enumerate (contatos_df['Mensagem']):
        pessoa = contatos_df.loc[i, "Pessoa"]
        numero = contatos_df.loc[i, "Numero"]
        texto =urllib.parse.quote(f" Oi {pessoa}! {mensagem}")
        link = f"https://web.whatsapp.com/send?phone={numero}&text={texto}"
        navegador.get(link)

while len(navegador.find_element_by_id('//*[@id="side"]')) <1:
    time.sleep(1)

navegador.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(Keys.ENTER)
time.sleep(10)        
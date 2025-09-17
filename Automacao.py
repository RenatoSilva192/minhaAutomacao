# Automação para o meu computador, inicialização diária, simplesmente enquanto pego um café.
# Passo 1: Entrar no Sistema da empresa: https://dlp.hashtagtreinamentos.com/python/intensivao/login
# Passo 2: Fazer login
# Passo 3: Importar a base de dados
# Passo 4: Cadastrar 1 produto
# Passo 5: Repetir para todos os produtos
# Biblioteca = pyautogui

import pyautogui
import pandas as pd

# Passo 1: Entrar no Sistema da empresa: https://dlp.hashtagtreinamentos.com/python/intensivao/login
# Abririndo o navegador chrome

pyautogui.PAUSE = 0.5 # Tempo de espera entre cada comando (Em todo o código) o pyautogui.sleep(2) é um tempo de espera específico

pyautogui.press("win") # Pressiona a tecla window
pyautogui.write("chrome") # Escreve chrome
pyautogui.press("enter") # Pressiona a tecla enter
pyautogui.sleep(2) # Espera 2 segundos o navegador abrir
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login") # Escreve o endereço do site
pyautogui.press("enter") # Pressiona a tecla enter

# Passo 2: Fazer login
pyautogui.sleep(2) # Espera 2 segundos o site carregar
pyautogui.click(x=3325, y=506) # Clica no campo de email
pyautogui.write("renato.silva.192@gmail.com") # Escreve o email
pyautogui.press("tab") # Pressiona a tecla tab para ir para o campo de senha
pyautogui.write("123456") # Escreve a senha
pyautogui.press("tab") # Pressiona a tecla tab para ir para o campo de senha
pyautogui.press("enter") # Pressiona a tecla enter para fazer login
pyautogui.sleep(3) # Espera 3 segundos o site carregar

# Passo 3: Importar a base de dados

tabela = pd.read_csv("Produtos.csv") # Lendo a base de dados com pandas e salvando na variável tabela
# print(tabela) # Mostrando a tabela no console

# Passo 4: Cadastrar 1 produto para entender o processo manual

# pyautogui.click(x=3300, y=373) # Clica no menu produtos

# codigo = "MOLO000251"
# pyautogui.write(codigo) # Escreve o código do produto
# pyautogui.press("tab") # Pressiona a tecla tab para ir para o campo

# marca = "Logitech"
# pyautogui.write(marca) # Escreve o código do produto
# pyautogui.press("tab") # Pressiona a tecla tab para ir para o campo

# tipo = "Mouse"
# pyautogui.write(tipo) # Escreve o código do produto
# pyautogui.press("tab") # Pressiona a tecla tab para ir para o campo

# categoria = "1"
# pyautogui.write(categoria) # Escreve o código do produto
# pyautogui.press("tab") # Pressiona a tecla tab para ir para o campo

# preco_unitario = "25.95"
# pyautogui.write(preco_unitario) # Escreve o código do produto
# pyautogui.press("tab") # Pressiona a tecla tab para ir para o campo

# custo = "6,50"
# pyautogui.write(custo) # Escreve o código do produto
# pyautogui.press("tab") # Pressiona a tecla tab para ir para o campo

# obs = ""
# pyautogui.write(obs) # Escreve o código do produto
# pyautogui.press("tab") # Pressiona a tecla tab para ir para o campo


# Passo 5: Repetir para todos os produtos da base de dados usando loop for

for linha in tabela.index: # Para cada linha na tabela faça o que está indentado abaixo

    pyautogui.click(x=3300, y=373) # Clica no menu produtos

    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(codigo) # Escreve o código do produto
    pyautogui.press("tab") # Pressiona a tecla tab para ir para o proximo campo

    marca = tabela.loc[linha, "marca"]
    pyautogui.write(marca) # Escreve o código do produto
    pyautogui.press("tab") # Pressiona a tecla tab para ir para o proximo campo

    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(tipo) # Escreve o código do produto
    pyautogui.press("tab") # Pressiona a tecla tab para ir para o proximo campo

    categoria = tabela.loc[linha, "categoria"]
    pyautogui.write(str(categoria)) # Escreve o código do produto
    pyautogui.press("tab") # Pressiona a tecla tab para ir para o proximo campo

    preco_unitario = tabela.loc[linha, "preco_unitario"]
    pyautogui.write(str(preco_unitario)) # Escreve o código do produto
    pyautogui.press("tab") # Pressiona a tecla tab para ir para o proximo campo

    custo = tabela.loc[linha, "custo"]
    pyautogui.write(str(custo)) # Escreve o código do produto
    pyautogui.press("tab") # Pressiona a tecla tab para ir para o proximo campo

    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs) # Escreve o código do produto
    
    pyautogui.press("tab") # Pressiona a tecla tab para ir para o proximo campo
    pyautogui.press("enter") # Pressiona a tecla enter para salvar o produto
    pyautogui.sleep(1) # Espera 1 segundo o site salvar o produto

pyautogui.scroll(4000) # Sobe a tela para o topo da página




# Automação para o meu computador, inicialização diária, simplesmente enquanto pego um café.
# Passo 1: Abrir o navegador e acessar a página do web.whatsapp.com
# Passo 2: Abrir uma nova aba no navegador e abrir o gmail
# Passo 3: Abrir uma nova aba no navegador, abrir o youtube.com e pesquisar por "Jornal Jovem Pan ao vivo"
# Passo 4: Abrir uma nova aba no navegador, abrir a "https://www.udemy.com/home/my-courses/learning/"
# Passo 5: Abrir o aplicativo "Steam" e ir para a biblioteca
# Passo 6: Abrir o aplicativo "Xbox" e ir para a biblioteca


import pyautogui

pyautogui.PAUSE = 1

# Passo 1: Abrir o navegador e acessar a página do web.whatsapp.com

pyautogui.press("Win")
pyautogui.write("Chrome")
pyautogui.press("enter")
pyautogui.write("web.whatsapp.com")
pyautogui.press("enter")
pyautogui.sleep(5)

# Passo 2: Abrir uma nova aba no navegador e abrir o gmail

pyautogui.hotkey('ctrl', 't')
pyautogui.write("http://gmail.com/")
pyautogui.press("enter")
pyautogui.sleep(3)

# Passo 3: Abrir uma nova aba no navegador, abrir o youtube.com e pesquisar por "Jornal Jovem Pan ao vivo"

pyautogui.hotkey('ctrl', 't')
pyautogui.write("youtube.com")
pyautogui.press("enter")
pyautogui.press('tab', presses=4)
pyautogui.write("Jornal Jovem Pan ao vivo")
pyautogui.press("enter")
pyautogui.sleep(3)
pyautogui.click(x=3258, y=430)

# Passo 4: Abrir uma nova aba no navegador, abrir a "https://www.udemy.com/home/my-courses/learning/"

pyautogui.hotkey('ctrl', 't')
pyautogui.write("https://www.udemy.com/home/my-courses/learning/")
pyautogui.press("enter")
pyautogui.sleep(4)


# Passo 5: Abrir o aplicativo "Steam" e ir para a biblioteca

pyautogui.press("Win")
pyautogui.write("Xbox")
pyautogui.press("enter")
pyautogui.sleep(4)

# Passo 6: Abrir o aplicativo "Xbox" e ir para a biblioteca

pyautogui.press("Win")
pyautogui.write("Steam")
pyautogui.press("enter")
pyautogui.sleep(7)
pyautogui.press("Esc")
pyautogui.click(x=240, y=64)
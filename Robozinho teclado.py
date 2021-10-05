# Para funcionar, deixe seu navegador na primeira opção dos seus programas.

import pyautogui

from time import sleep

def Firebase():

    # Segure o windows
    pyautogui.keyDown('win')

    # Pressione o botão 1
    pyautogui.press('1')

    # Solte o windows
    pyautogui.keyUp('win')

    # Segure o ctrl
    pyautogui.keyDown('ctrl')

    # Pressione o t
    pyautogui.press('t')

    # Solte o ctrl
    pyautogui.keyUp('ctrl')

    # Espere 2 segundos
    sleep(2)

    # Escreva Python
    pyautogui.write('Firebase')

    # Pressione enter
    pyautogui.press('enter')

Firebase()



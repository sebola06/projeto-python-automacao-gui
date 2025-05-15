import pyautogui as py
import time
import subprocess

# Espera 5 segundos para o usuário preparar a tela

time.sleep(5)
# Abre o Bloco de Notas

subprocess.Popen(['notepad.exe'])
time.sleep(2)  # Aguarda o aplicativo abrir

# Digitar texto

py.write('Automatizando o Bloco de Notas com PyAutoGUI!', interval=0.05)

# Salvar o arquivo

py.hotkey('ctrl', 's')
time.sleep(1)
py.write('automacao.txt')
py.press('enter')
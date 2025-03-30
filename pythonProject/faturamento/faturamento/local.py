import pyautogui
import time

# Aguarde 5 segundos para você posicionar o mouse
time.sleep(5)

# Obtenha as coordenadas atuais do mouse
x, y = pyautogui.position()

# Exiba as coordenadas
print(f"Coordenadas do mouse: X={x}, Y={y}")


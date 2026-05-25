import pyautogui
import time

pyautogui.hotkey("win")
pyautogui.write('paint')
pyautogui.press('enter')

time.sleep(1)
pyautogui.hotkey('alt', 'space')
time.sleep(1)
pyautogui.press('x')
time.sleep(1)

altura, largura = pyautogui.size()
a = altura / 2
l = largura / 2
pyautogui.moveTo(a,l)

pyautogui.dragRel(xOffset=0, yOffset=0, duration=0.4)
pyautogui.dragRel(xOffset=0, yOffset=100, duration=0.4)
pyautogui.dragRel(xOffset=300,yOffset=0, duration=0.4)
pyautogui.dragRel(xOffset=0,yOffset=-200, duration=0.4)
pyautogui.dragRel(xOffset=-250,yOffset=0, duration=0.4)
pyautogui.dragRel(xOffset=50,yOffset=100, duration=0.4)
pyautogui.dragRel(xOffset=0,yOffset=100, duration=0.4)

pyautogui.moveRel(-50, -200, duration=0.4)
pyautogui.dragRel(xOffset=-50,yOffset=100, duration=0.4)
pyautogui.dragRel(xOffset=100,yOffset=0, duration=0.4)
pyautogui.dragRel(xOffset=200,yOffset=0, duration=0.4)

tintaxy = pyautogui.locateCenterOnScreen('prova_samara\\tinta.png', confidence=0.95, grayscale=False ) #esqueci do grayscale
pyautogui.click(tintaxy, duration=1)
marromxy = pyautogui.locateCenterOnScreen('prova_samara\\marrom.png', confidence=0.98, grayscale=False )
amareloxy = pyautogui.locateCenterOnScreen('prova_samara\\amarelo.png', confidence=0.98, grayscale=False )
pyautogui.click(amareloxy, duration=1)

#pinta a casa (mão deu tempo de fazer)
pyautogui.moveTo(a,l)
pyautogui.moveRel(20,20)
pyautogui.click(clicks=2)
pyautogui.moveRel(100,0)
pyautogui.click(clicks=2)

pyautogui.click(marromxy)
pyautogui.moveTo(a,l)
pyautogui.moveRel(20,-20)
pyautogui.click(clicks=2)
pyautogui.moveRel(100,0)
pyautogui.click(clicks=2)

pyautogui.hotkey('ctrl', 's')
time.sleep(2)
pyautogui.write('C:\\Users\\14961454613\Desktop\\aulas_automacao_3infob\\correcao_prova\\desenhar2.py')
pyautogui.press('enter')

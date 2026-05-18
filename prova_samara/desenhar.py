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

xy8 = pyautogui.locateCenterOnScreen('prova_samara\\tinta.png', confidence=0.95 )
pyautogui.click(xy8, duration=1)
xy8 = pyautogui.locateCenterOnScreen('prova_samara\\marrom.png', confidence=0.95 )
pyautogui.click(xy8, duration=1)
xy8 = pyautogui.locateCenterOnScreen('prova_samara\\amarelo.png', confidence=0.95 )
pyautogui.click(xy8, duration=1)

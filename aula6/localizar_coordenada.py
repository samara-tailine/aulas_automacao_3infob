import pyautogui

#opção1:
#localiza uma imagem na tela e retorna uma caia, com coordenada x e y do ponto inicial da caixa left+top e altura e largura da caixa
box = pyautogui.locateOnScreen('aula6\\btn_8.png')
#com a caixa encontrada, a função center retorna a coordenada xy do centro da caixa "imagem"
centro_box = pyautogui.center(box)
print(centro_box)

#opção2

xy2 = pyautogui.locateCenterOnScreen('aula6\\btn_8.png', confidence=0.95)
print(xy2)

xy3 = pyautogui.locateCenterOnScreen('aula6\\btn_vermelho.png', confidence=0.5)
print(xy3)  
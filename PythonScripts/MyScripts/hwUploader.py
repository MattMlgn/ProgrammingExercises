import pyautogui as py
import time

print(py.position())


py.moveTo(902,802)
py.click(clicks=2, interval=1)
py.click(1335, 295)
py.typewrite("algorithm")
time.sleep(1)
py.click(904,401)
py.click(1383, 656)
py.click(849,861)
py.click(1380,295, clicks=2, interval=1)
py.typewrite("program01")
time.sleep(1)
py.click(909,559)
py.click(1383,656)
time.sleep(1)
py.scroll(-100)
py.moveTo(763,795)

#py.typewrite("https://q2a.di.uniroma1.it/homeworks/delivery?homework=2\n")

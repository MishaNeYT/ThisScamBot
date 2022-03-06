import pyautogui, time
time.sleep(5); f open("тут должен быть указан файл с готовыми сообщениями, например, aboba.txt (и в этой aboba.txt есть нужные сообщения для спама)", "r")
for line in f:
                  
    pyautogui.typewrite(line)
    pyautogui.press("enter")

import pyautogui, time
time.sleep(тут ты указываешь количество секунд, через которые начнётся спам (за это время нужно открыть соцсеть)); f open("тут должен быть указан файл с готовыми сообщениями, например, aboba.txt (и в этой aboba.txt есть нужные сообщения для спама)", "r")
for line in f:        
    pyautogui.typewrite(line)
    pyautogui.press("enter")

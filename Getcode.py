import pyautogui as py
import pyperclip
import time

def findandClick(png, delay, confidencevalue = 0.7):
    Po = py.locateOnScreen(png, confidence = confidencevalue)
    if(Po):
        py.click(Po)
        time.sleep(delay)

#마우스 움직여도 무시하고 동작
py.FAILSAFE = False

for i in range(3):
    findandClick(r"D:\Python\Tstory\Assets\Chrome.png", 3, 0.8)
    py.moveTo(920, 960)
    time.sleep(3)
    py.click()
    if py.locateOnScreen(r"D:\Python\Tstory\Assets\plus.png", confidence=0.9):
        break
pyperclip.copy("")

for i in range(3):
    py.moveTo(800, 70)
    time.sleep(1)
    py.click()
    time.sleep(1)
    py.press('backspace')
    time.sleep(1)
    #한글로 되어있으면 한글로 입력하니 영어로 설정 해둬야함.
    py.hotkey('ctrl', 'v')
    time.sleep(1)
    py.press('enter')
    time.sleep(5)
    findandClick(r"D:\Python\Tstory\Assets\Login.png", 3)
    findandClick(r"D:\Python\Tstory\Assets\Loginsave.png", 3)
    findandClick(r"D:\Python\Tstory\Assets\InputID.png", 3)
    py.write('')     
    findandClick(r"D:\Python\Tstory\Assets\InputPW.png", 3)
    py.write('')   
    time.sleep(1)
    py.press('enter')
    pyperclip.copy("")
    if py.locateOnScreen(r"D:\Python\Tstory\Assets\allowed.png", confidence=0.75):
        break

findandClick(r"D:\Python\Tstory\Assets\allowed.png", 5)
py.moveTo(800, 70)
time.sleep(1)
py.doubleClick()
time.sleep(1)
py.hotkey('ctrl', 'c')
time.sleep(1)
findandClick(r"D:\Python\Tstory\Assets\vscode.png", 5, 0.8)
py.moveTo(1376, 917)
time.sleep(3)
py.click()
findandClick(r"D:\Python\Tstory\Assets\Automation.png", 3)

if py.locateOnScreen(r"D:\Python\Tstory\Assets\code.png", confidence=0.9):
    Po = py.locateOnScreen(r"D:\Python\Tstory\Assets\code.png", confidence=0.9)
    if(Po):
        py.click(Po)
        time.sleep(1)
else:
    py.moveTo(872, 355)
    time.sleep(1)
    py.click()

    for i in range(8):
        py.scroll(500)

    time.sleep(1)
    Po = py.locateOnScreen(r"D:\Python\Tstory\Assets\code.png", confidence=0.9)
    if(Po):
        py.click(Po)
        time.sleep(1)

py.moveRel(150, 0)
time.sleep(1)
py.doubleClick()
time.sleep(1)
py.press('backspace')
time.sleep(1)
py.hotkey('ctrl', 'v')
time.sleep(1)
time.sleep(3)
py.hotkey('ctrl', 's')

# Po = py.locateOnScreen(r"D:\User Python\Code\Python\Tstory\Assets\code.png", confidence=0.9)
# if(Po):
#     py.click(Po)
#     time.sleep(1)

#현재 마우스 좌표 찾기
# while True:
#     print(py.position())
#     time.sleep(2)
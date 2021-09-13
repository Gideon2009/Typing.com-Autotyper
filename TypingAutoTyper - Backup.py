#import pyscreenshot as ImageGrab
from PIL import ImageGrab
import os
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
from pynput.keyboard import Key, Controller
import time
import pynput

import threading

badLetters = ['!', '@', '#', '$', '%', '^', '&', '*', '<', '>', '/', '\n']

def GetNextLine():
    im = ImageGrab.grab(bbox=(480, 700, 1400, 760))  # X1,Y1,X2,Y2
    im.save("TempImg.png")
    return pytesseract.image_to_string(Image.open('TempImg.png'))

def GetLoop():
    global i
    global ToType
    global screenshotInterval
    i = 0
    screenshotInterval = 7
    bruh = 0
    while True:
        if i > screenshotInterval:
            #time.sleep(0.5)
            temp = GetNextLine()
            
            if temp.replace('\n', '') in ToType or any(ele in temp for ele in badLetters):
                pass
            else:
                pix = ImageGrab.grab()
                pixColor = pix.getpixel((1400, 224))
                if pixColor == (214, 214, 214):
                    print(temp)
                    ToType += " " + temp
            i = 0
        time.sleep(0.025)

def typingLoop():
    global i
    global ToType
    global keyboard
    keyboard = Controller()  # Create the controller
    while True:
        try:
            keyboard.type(ToType[0])
            ToType = ToType[1 : : ]
        except:
            os.remove("TempImgFull.png")
            os.remove("TempImg.png")
            print("Files Removed!")
            break
        i += 1
        time.sleep(0.025)

if __name__=='__main__':
    
    print(5)
    time.sleep(1)
    print(4)
    time.sleep(1)
    print(3)
    time.sleep(1)
    print(2)
    time.sleep(1)
    print(1)
    time.sleep(1)

    temp = ' '

    getting = False

    try:
        pytesseract.pytesseract.tesseract_cmd = r'Tesseract\tesseract.exe'
        DirectoryTester = (pytesseract.image_to_string(Image.open('TempImgFull.png')))
        print('first')
    except:
        pytesseract.pytesseract.tesseract_cmd = r'Tesseract\Tesseract\tesseract.exe'
        print('second')

    im = ImageGrab.grab(bbox=(480, 150, 1400, 760))  # X1,Y1,X2,Y2

    im.save("TempImgFull.png")

    # Simple image to string
    ToType = (pytesseract.image_to_string(Image.open('TempImgFull.png')).replace('\n\n', ' ').replace('\n', ' ').replace('\r', '').replace('yy', ''))
    ToType = ToType[1 : : ]
    print(pytesseract.image_to_string(Image.open('TempImgFull.png')).replace('\n\n', ' ').replace('yy', ''))

    t1 = threading.Thread(target=GetLoop)
    t2 = threading.Thread(target=typingLoop)

    t1.start()
    t2.start()

    t2.join()
    input()

#game link : https://tbot.xyz/lumber/
import time
from pywinauto.keyboard import send_keys
from PIL import ImageGrab

time.sleep(4)
pause = 0.0175
sleep = 0.2

send_keys('{LEFT}', pause)
send_keys('{LEFT}', pause)

while True:
    time.sleep(sleep)
    colors = ImageGrab.grab((1380, 130, 1381, 630))

    branches = [
        colors.getpixel((0, 499)),
        colors.getpixel((0, 399)),
        colors.getpixel((0, 299)),
        colors.getpixel((0, 199)),
        colors.getpixel((0, 99)),
        colors.getpixel((0, 0))
    ]

    for c in branches:
        if c == (161, 116, 56):
            send_keys('{RIGHT}', pause)
            send_keys('{RIGHT}', pause)
        else:
            send_keys('{LEFT}', pause)
            send_keys('{LEFT}', pause)

import qrcode
import cv2
import time
import os
from matplotlib import pyplot as plt
import tkinter.filedialog

print("Make QRcode!\nver: 1.0.1\ninfo: https://twitter.com/Mc77xS\nYouTube: https://www.youtube.com/@tanahiro2010\nhomepage: https://tanahiro2010.zatunen.com")
print("注意!QRコードは (株)デンソーウェーブの登録商標です.")
time.sleep(2)
while True:
    index = input("Content( URL or Text or TEL or mailaddress ) >>")
    temp = qrcode.make(index)
    temp.save("temp\\temp.img")
    img = cv2.imread("temp\\temp.img")
    plt.imshow(img)
    plt.show()
    anser = input("Do you seve? y/n >>")
    if ( ( anser == "y" ) or ( anser == "yes" ) or ( anser == "Y" ) or ( anser == "YES" ) ):
        filename = input("File Name >>")
        target_dir = tkinter.filedialog.askdirectory()
        fdir = target_dir + "/" + filename + ".jpg"
        print(fdir)
        temp.save(fdir)
    os.remove('temp\\temp.img')
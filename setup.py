import urllib.request
import os
import time
print("Make QRcodeのセットアップを開始します\nStart setting up Make QRcode")
time.sleep(2)
print("必要なフォルダの作成中...\nCreating necessary folder...")
os.system("tree C:\\windows")
print("メインファイルをインストールします")
urllib.request.urlretrieve("https://botcreator.cloudfree.jp/app/MakeQRcode.exe", "MakeQRcode.exe")
print("ダウンロードが完了しました。")
input("何かキーを押して終了...")
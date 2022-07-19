# 美郷　雲海
# 今日の画像から、タイムラプスを作成する
# ファイル名は、YYYYmmDDHH.mp4
#
import os
import datetime
import cv2
from colorama import Fore
from colorama import Style
import glob

now = datetime.datetime.now()

# ビデオファイル名は、Today_YYYYmmDD.mp4
video_path = datetime.datetime.strftime(
    now, "/users/uchukamen/documents/unkai_misato/video/%Y%m%d_all.mp4")
# ビデオファイルが存在する場合は、削除する
if os.path.exists(video_path):
    os.remove(video_path)
    print("ビデオファイルを削除 :", video_path)

fourcc = cv2.VideoWriter_fourcc(* 'avc1')
fps = 10
out = cv2.VideoWriter(video_path, fourcc, fps, (854, 480))

file_path = datetime.datetime.strftime(
    now, "/users/uchukamen/documents/unkai_misato/images/%Y%m%d*.jpg")

files = glob.glob(file_path)
for file in files:
    if not os.path.exists(file):
        print("画像なし　スキップ: ", file)
        continue

    img = cv2.imread(file, cv2.IMREAD_COLOR)
    if img is None:
        print(Fore.RED, "🟥 imread error: ", file, Fore.RESET)
    else:
        print("out.write: ", file)
        out.write(img)

out.release()
print("終了")

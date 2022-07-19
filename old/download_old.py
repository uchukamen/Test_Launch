# 美郷 雲海の YouTube をダウンロードし、画像ファイルをセーブする
#
import subprocess
import os
import signal
import datetime
import time
import shutil

now = datetime.datetime.now()
print("⭐️ 処理開始", now)

# 画像ファイル
img = now.strftime("%Y%m%d%H%M.jpg")
img_path = "/users/uchukamen/documents/Unkai_Misato/images/" + img
img_path2 = "/users/uchukamen/documents/Unkai_Misato/images/misato.jpg"
# ビデオファイル
filename = now.strftime("tmp_%Y%m%d%H%M.mp4")
video_path = "/users/uchukamen/documents/Unkai_Misato/video/" + filename

# 実行前に、ゴミファイルがあれば削除
if os.path.exists(img_path):
    os.remove(img_path)
if os.path.exists(video_path):
    os.remove(video_path)

proc = subprocess.Popen(
    '/usr/local/bin/youtube-dl "https://www.youtube.com/watch?v=T_Qe2P2GvUs" --ffmpeg-location /usr/local/bin -f 94 -o ' + video_path, shell=True)
print("⭐️ youtube-dl を実行開始")
time.sleep(5)
proc.send_signal(signal.SIGINT)
print("⭐️ SIGINT を youtube-dl に送る")

print("⭐️ youtube-dl が終了するのを待つ")
proc.wait()
print("⭐️ youtube-dl が終了した", video_path)

ffmpeg_cmd = "/usr/local/bin/ffmpeg -ss 0 -vframes 1 " + \
    img_path + " -i " + video_path

print("⭐️ ffmpeg でビデオファイルから、画像を抽出する")
proc2 = subprocess.Popen(ffmpeg_cmd, shell=True)
print("⭐️ ffmpeg が終了するのを待つ")
proc2.wait()
print("⭐️ ffmpeg が終了した")

if os.path.exists(img_path):
    print("⭐️ 画像の取得に成功した", img_path)
    shutil.copy(img_path, img_path2)
else:
    print("🟥 画像の取得に失敗した")

# 一時ビデオファイルの削除
if os.path.exists(video_path):
    print("⭐️ 一時ビデオファイル削除: ", video_path)
    os.remove(video_path)
else:
    print("🟥 一時ビデオファイルが存在しない: ", video_path)

print("⭐️⭐️⭐️ 終了")

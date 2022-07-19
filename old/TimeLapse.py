import os
import time
import datetime
import urllib.error
import urllib.request
import cv2


def download_file(url, dst_path):
    try:
        with urllib.request.urlopen(url) as web_file:
            data = web_file.read()
            with open(dst_path, mode='wb') as local_file:
                local_file.write(data)
    except urllib.error.URLError as e:
        print(e)


fourcc = cv2.VideoWriter_fourcc(* 'x264')
fps = 10


startTime = datetime.datetime(2021, 10, 19, 5, 0, 0)
hours = 4


video_path = datetime.datetime.strftime(
    startTime, "/users/uchukamen/desktop/杖突峠_%Y%m%d%H%M%S.mp4")
# outfile = "/users/uchukamen/desktop/杖突峠.mp4"

out = cv2.VideoWriter(video_path, fourcc, fps, (1920, 1080))

for interval in range(0, hours * 60, 1):
    t = startTime + datetime.timedelta(minutes=interval)
    path = datetime.datetime.strftime(
        t, "/users/uchukamen/documents/杖突峠データ/%Y%m%d%H%M%S.jpg")

    if os.path.exists(path):
        print(path)
    else:
        print("not exist: " + path)
        continue

    img = cv2.imread(path, cv2.IMREAD_COLOR)
    if img is None:
        print("imread error")
        continue

    # 画像の大きさを取得
    # height, width, channels = img.shape[:3]
    # print("width: " + str(width))
    # print("height: " + str(height))

    out.write(img)

out.release()

# https://navi.city.chichibu.lg.jp/cloudview/pics/20200824/040059.jpg

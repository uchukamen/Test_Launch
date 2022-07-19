# 美郷　雲海
# 指定した日の、朝5時から、10時まで、画像をダウンロードし、タイムラプスを作成する
# ファイル名は、YYYYmmDDHH.mp4
# 夜5時から、朝9時まで、10分おきに実行開始するように plist を設定する
#
import os
import datetime
import cv2
from icecream import ic

def create_timelapse():
    # 今日
    dt = datetime.datetime.now()

    # 朝5時から
    startTime = datetime.datetime(
        dt.year, dt.month, dt.day, 5, 0, 0)
    endTime = datetime.datetime(
        dt.year, dt.month, dt.day, 10, 0, 0)

    # ビデオファイル名は、翌日のYYYYmmDD.mp4
    video_path = datetime.datetime.strftime(
        endTime, "/users/uchukamen/documents/unkai_misato/video/%Y%m%d.mp4")
    # ビデオファイルが存在する場合は、削除する
    if os.path.exists(video_path):
        os.remove(video_path)
        ic("ビデオファイルを削除 :", video_path)

    fourcc = cv2.VideoWriter_fourcc(* 'avc1')
    fps = 20
    out = cv2.VideoWriter(video_path, fourcc, fps, (854, 480))

    t = startTime

    while(t < endTime):
        # アップロードサイズが 10MB を超えると、アップロードエラー 400 となる
        # ビデオサイズを 10MB 以下に抑えるため、2分間隔にする
        t = t + datetime.timedelta(minutes=1)

        save_path = datetime.datetime.strftime(
            t, "/users/uchukamen/documents/unkai_misato/images/%Y%m%d%H%M.jpg")

        if not os.path.exists(save_path):
            ic("画像なし スキップ: ", save_path)
            continue

        ic("cv2.imread", save_path)
        img = cv2.imread(save_path, cv2.IMREAD_COLOR)
        if img is None:
            ic("imread error  スキップ: ", save_path)
            continue

        print("out.write: ", save_path)
        out.write(img)

    out.release()
    ic("🟢 終了")

def main():
    ic("🟩 tweet_timelapse main()")
    tweet_timelapse()

if __name__ == "__main__":
    main()
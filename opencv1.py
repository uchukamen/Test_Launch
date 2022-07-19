'''
YouTube から動画をキャプチャーして表示する
'''
import cv2
import apafy as pafy

ESC_KEY = 27

# ハワイ・マウナケアの星空ライブ
url = "https://www.youtube.com/watch?v=eH90mZnmgD4"

video = pafy.new(url)
best = video.getbest("mp4")
cap = cv2.VideoCapture(best.url)

while (True):
    ret, frame = cap.read()
    cv2.imshow('frame', frame)

    # 終了判定
    if cv2.waitKey(30) & 0xFF == ESC_KEY:
        break

cap.release()
cv2.destroyAllWindows()

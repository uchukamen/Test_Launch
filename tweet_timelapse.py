# mp4 を twitter にポストする
#
import os
import datetime
import cv2
import mylib
from icecream import ic


def create_timelapse() -> str:
    '''
    タイムラプスを作成し、
    ビデオファイルのパスを返す
    '''
    # 今日
    dt = datetime.datetime.now()

    # 朝5時から
    startTime = datetime.datetime(
        dt.year, dt.month, dt.day, 5, 0, 0)
    endTime = datetime.datetime(
        dt.year, dt.month, dt.day, 10, 0, 0)

    # ビデオファイル名は、翌日のYYYYmmDD.mp4
    video_out = datetime.datetime.strftime(
        endTime, "/users/uchukamen/documents/unkai_misato/video/%Y%m%d.mp4")
    # ビデオファイルが存在する場合は、削除する
    if os.path.exists(video_out):
        os.remove(video_out)
        ic("ビデオファイルを削除 :", video_out)

    fourcc = cv2.VideoWriter_fourcc(* 'avc1')
    fps = 20
    out = cv2.VideoWriter(video_out, fourcc, fps, (854, 480))

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

        ic("out.write: ", save_path)
        out.write(img)

    out.release()
    ic("🟢 create_timelapse 終了", video_out)
    return video_out


def create_message() -> str:
    t = datetime.datetime.now()

    # メッセージ
    message = "島根県美郷町 野間雲海ビュースポット ライブカメラ \n" \
        f'{t:%Y/%m/%d %H:%M}\n' \
        "https://www.youtube.com/watch?v=T_Qe2P2GvUs\n" \
        "より、今朝のタイムラプス自動生成テスト中\n" \
        "\n" \
        "説明: https://aiharasoft.com/wordpress/misato/\n" \
        "\n" \
        "美郷町雲海予報: 9月末より再開予定\n" \
        "https://gov.town.shimane-misato.lg.jp/unkai/\n" \
        "\n" \
        "#雲海 #美郷町 #美郷町雲海 #美郷町雲海検出"

    return message


def get_video_path() -> str:
    '''
    タイムラプスの動画のパスを返す
    '''
    dir = "/Users/uchukamen/Documents/Unkai_Misato/video/"
    t = datetime.datetime.now()
    filename = datetime.datetime.strftime(t, "%Y%m%d.mp4")
    video_path = dir + filename
    ic("get_video_path", video_path)
    return video_path


def tweet_timelapse():
    '''
    タイムラプスを作成して、ツイートする
    '''
    ic("🟩 tweet_timelapse tweet_timelapse()")
    video_in = create_timelapse()
    message = create_message()
    # video_in = get_video_path()
    mylib.tweet_video(message, video_in)


def main():
    ic("🟩 tweet_timelapse main()")
    tweet_timelapse()


if __name__ == "__main__":
    main()

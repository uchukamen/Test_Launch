# 美郷 雲海の YouTube をダウンロードし、画像ファイルをセーブする
#
import datetime
import mylib
import mylib_video
from icecream import ic
import shutil

def download():
    ic("🟩 download download")

    now = datetime.datetime.now()
    print("⭐️ 処理開始", now)

    # ビデオファイル
    filename = now.strftime("tmp_misato_%Y%m%d%H%M.mp4")
    video_out = "/users/uchukamen/documents/Unkai_Misato/video/" + filename

    ic("⭐️ ビデオをダウンロードする", video_out)
    url = "https://www.youtube.com/watch?v=T_Qe2P2GvUs"
    mylib_video.download(url, 10, video_out)

    # 画像ファイル
    img = now.strftime("%Y%m%d%H%M.jpg")
    img_path = "/users/uchukamen/documents/Unkai_Misato/images/" + img
    img_path2 = "/users/uchukamen/documents/Unkai_Misato/images/misato.jpg"
    ic("⭐️ ビデオから、画像を抽出する", video_out, img_path)
    mylib.check_file(video_out)
    mylib_video.get_frame(video_out, img_path)
    shutil.copy(img_path, img_path2)

    ic("⭐️ 一時ビデオファイル削除: ", video_out)
    mylib.delete_file(video_out)

def main():
    ic("🟩 download main()")
    download()


if __name__ == "__main__":
    main()

import vlc
import os
import usb_loop
import time
import usb_path


def main_video():
    Instance = vlc.Instance('--fullscreen')

    media_list = Instance.media_list_new()
    path = r"/media/korgoth/BIRD/"
    path = usb_path.get_path_usb()
    videos = os.listdir(path)

    for video in videos:
        media_list.add_media(Instance.media_new(os.path.join(path,video)))

    list_player = Instance.media_list_player_new()
    list_player.set_media_list(media_list)

    list_player.play()
    while True:
        time.sleep(2)
        if usb_loop.video_loop():
            list_player.stop()
            break

if __name__ == '__main__':
    main_video()

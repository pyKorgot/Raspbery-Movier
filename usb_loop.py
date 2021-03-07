import usb
import time
import videos_loop
import os
import threading


def run_udiskie():
    os.system('udiskie -a -n -t')


def video_loop(devices=7):
    usb_standart = sum(1 for i in (usb.core.find(find_all=True)))
    usb_len = (usb.core.find(find_all=True))
    usb_len = sum(1 for i in usb_len)
    if usb_len != devices:
        return True
    else: return False


def main_loop_usb():
    usb_standart = (usb.core.find(find_all=True))
    len_usb_standart = 6
    print(f'Standart List Usb: {len_usb_standart}')

    while True:
        usbs = usb.core.find(find_all=True)
        len_usb = sum(1 for i in usbs)

        if len_usb_standart < len_usb:
            len_usb_standart = len_usb
            print('Past usb')
            print(len_usb)
            time.sleep(5)
            videos_loop.main_video()
        
        elif len_usb_standart > len_usb:
            print('Extand usb')
            print(len_usb)
            len_usb_standart = len_usb

        time.sleep(3)

if __name__ == "__main__":
    th = threading.Thread(target=run_udiskie)
    th.start()
    main_loop_usb()

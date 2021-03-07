import subprocess


def get_path_usb():
    command = ['lsblk']
    p = subprocess.Popen(command, stdout=subprocess.PIPE)
    text = p.stdout.read()
    retcode = p.wait()

    text = text.decode('utf-8')
    text = text.split('\n')
    text = text[-2].split(' ')
    text = text[-1]

    return text

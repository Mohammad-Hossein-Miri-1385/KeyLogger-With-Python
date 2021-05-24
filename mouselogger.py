from pynput import mouse, keyboard
import os
import datetime


def mouse_log(x, y, button, pressed):
    CWD = os.getcwd()
    tt = datetime.datetime.today()
    MouseLogFile = open(str(CWD)+'\\mouse_log.txt', 'a')
    CurrentTime = '{}:{}:{}'.format(tt.hour, tt.minute, tt.second)
    if pressed == True:
        m = '{}\t:\t{} , {} , {}'.format(CurrentTime, x, y, button)
        MouseLogFile.write('{}\n'.format(m))

def mouse_start():
    with mouse.Listener( on_click= mouse_log) as lstn:
        lstn.join()


mouse_start()

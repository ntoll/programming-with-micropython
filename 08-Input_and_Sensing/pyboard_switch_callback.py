import pyb

sw = pyb.Switch()


def my_callback():
    pyb.LED(1).toggle()


sw.callback(my_callback)

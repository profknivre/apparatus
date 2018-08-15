__version__ = '0.0.2'

import lzma
import os
import signal


def xz_rotator(source, dest):
    """
    Move and xz rotator
    """
    f_in = open(source, 'rb')
    f_out = lzma.open(dest, 'wb')
    f_out.writelines(f_in)
    f_out.close()
    f_in.close()
    os.remove(source)


def xz_namer(default_name):
    return default_name+'.xz'


def get_slope(data):
    # y = a*x+b
    a, b = linreg(range(len(data)), data)
    return a


def linreg(x, y):
    """
    return a,b in solution to y = ax + b such that root mean square distance between trend line
    and original points is minimized

    found somewhere on the net
    """
    n = len(x)
    sx = sy = sxx = syy = sxy = 0.0
    for x_, y_ in zip(x, y):
        sx = sx + x_
        sy = sy + y_
        sxx = sxx + x_ * x_
        syy = syy + y_ * y_
        sxy = sxy + x_ * y_
    det = sxx * n - sx * sx
    try:
        return (sxy * n - sy * sx) / det, (sxx * sy - sx * sxy) / det
    except ZeroDivisionError:
        return 0, 0


class timeout:
    def __init__(self, seconds=1, error_message='Timeout'):
        self.seconds = seconds
        self.error_message = error_message

    def handle_timeout(self, signum, frame):
        raise TimeoutError(self.error_message)

    def __enter__(self):
        signal.signal(signal.SIGALRM, self.handle_timeout)
        signal.alarm(self.seconds)

    def __exit__(self, type_, value, traceback):
        signal.alarm(0)


class FileMutex:
    def __init__(self, fname='/tmp/smartie.mutex'):
        self.fname = fname
        self.f = None

    def __enter__(self):
        # if os.path.exists(self.fname):
        #     raise Exception('already running')
        self.f = open(self.fname, mode='x')
        self.f.write(str(os.getpid()))

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.f:
            self.f.close()
        if os.path.exists(self.fname):
            os.unlink(self.fname)


def get_my_ip(talking_to="8.8.8.8"):
    import socket
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect((talking_to, 80))
    ret = s.getsockname()[0]
    s.close()
    return ret


def valmap(value, istart, istop, ostart, ostop):
    """
    arduino like map function
    """
    return ostart + (ostop - ostart) * ((value - istart) / (istop - istart))
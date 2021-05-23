import sys
import os
import time
'''每10s自动备份铁人存档'''
while True:
    '''存档名'''
    filename = "turkey1 (3).hoi4"
    '''新名字时间名，例 2021-05-24-02_21_05.hoi4'''
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    if os.path.exists(filename):
        os.rename(filename, now + r".hoi4")

    time.sleep(10)


 

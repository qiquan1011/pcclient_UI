import psutil
import sys
import re


def processinfo(name):
    '''
    根据进程名称，获取进程ID
    :param name: 进程名称
    :return: 进程Id
    '''
    p=psutil.process_iter()
    for pid in p:
        if pid.name()==name:
            pid_id=pid.pid
            print(pid_id)
        return pid_id


if __name__=="__main__":
    processinfo("Galaxy.Gemini.Shell.exe")
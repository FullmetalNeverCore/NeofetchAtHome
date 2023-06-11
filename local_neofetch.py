import socket
import os
import platform
import subprocess
import psutil
import pyautogui
import cpuinfo
import datetime


class HardwareStat:

    def __init__(self) -> None:
        pass

    def local_ip(self):
        try:
            return socket.socket(socket.AF_INET,socket.SOCK_DGRAM).connect(("8.8.8.8",80)).getsockname()[0]
        except Exception:
            return None
    
    def host(self):
        try:
            return platform.node()
        except Exception:
            return None
    def get_uptime(self):
        try:
            try:
                return subprocess.check_output(["uptime -p"],shell=True,stdout=open(os.devnull, 'w'),stderr=subprocess.STDOUT).decode('utf-8')
            except Exception:
                return subprocess.check_output(["systeminfo | find 'System Boot Time'"],shell=True,stdout=open(os.devnull, 'w'),stderr=subprocess.STDOUT)
        except Exception:
            return "No uptime avab."
    def get_kernel(self):
        try:
            return platform.relese()
        except Exception:
            return None
        
    def screen_size(self):
        try:
            return subprocess.check_output(["xrandr | grep \'*\'"],shell=True,stdout=open(os.devnull, 'w'),stderr=subprocess.STDOUT).decode('utf-8')
        except Exception:
            return f'{pyautogui.size().width}x{pyautogui.size().height}'
        
    def os(self):
        try:
            return [f'{platform.system()}',f'{platform.release()}']
        except Exception:
            return None
    
    def cpu(self):
        try:
            return cpuinfo.get_cpu_info()['brand_raw']
        except:
            return None
    
    def ram(self):
        return f'{(str(psutil.virtual_memory().used / (1024 * 1024)))[0:5]}MiB / {(str(psutil.virtual_memory().total / (1024 * 1024)))[0:5]}MiB'
    
    def template(self):
        return f"""
                                ..,   {self.host()}
                    ....,,:;+ccllll   --------------------
      ...,,+:;  cllllllllllllllllll   OS: {self.os()[0]}
,cclllllllllll  lllllllllllllllllll   Kernel: {self.os()[1]}
llllllllllllll  lllllllllllllllllll   Uptime: {self.get_uptime()}
llllllllllllll  lllllllllllllllllll   
llllllllllllll  lllllllllllllllllll   Resolution: {self.screen_size()}
llllllllllllll  lllllllllllllllllll   CPU: {self.cpu()}
llllllllllllll  lllllllllllllllllll   Memory: {self.ram()}
                                      
llllllllllllll  lllllllllllllllllll   
llllllllllllll  lllllllllllllllllll  
llllllllllllll  lllllllllllllllllll   
llllllllllllll  lllllllllllllllllll   
llllllllllllll  lllllllllllllllllll   
`'ccllllllllll  lllllllllllllllllll
       `' \*::  :ccllllllllllllllll
                       ````''*::cll        
        
        
        """

if __name__ == "__main__":
    print(HardwareStat().template())

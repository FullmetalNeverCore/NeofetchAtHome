import socket
import os
import platform
import subprocess
import psutil
if platform.system() == 'Windows':
    import pyautogui


elif platform.system() == 'Linux':


    pass
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
                return subprocess.check_output(["uptime -p"],shell=True,stdout=open(os.devnull, 'w'),stderr=subprocess.STDOUT).decode('utf-8') if not platform.system() == "Linux" else subprocess.check_output(["uptime -p"],shell=True).decode('utf-8')
            except Exception:
                try:
                    getcuruptime = datetime.datetime.now() - datetime.datetime.strptime(str(subprocess.check_output('net statistics workstation | find "Statistics since"',shell=True)).split("b'Statistics since")[1].replace("PM\\r\\n","").replace("'","")[1:-1],"%m/%d/%Y %H:%M:%S")
                    return f'Weeks: {getcuruptime.days // 7} Days:{getcuruptime.days % 7} Hours: {getcuruptime.seconds //3600}'
                except Exception:
                    return "No uptime avab."
    def get_kernel(self):
        try:
            return platform.relese()
        except Exception:
            return None
        
    def screen_size(self):
            try:
                return subprocess.check_output(["hwinfo --monitor | grep 'Resolution:'"],shell=True,stdout=open(os.devnull, 'w'),stderr=subprocess.STDOUT).decode('utf-8').split('Resolution: ')[1] if not platform.system() == "Linux" else subprocess.check_output(["hwinfo --monitor | grep 'Resolution:'"],shell=True,stderr=subprocess.STDOUT).decode('utf-8').split('Resolution: ')[1] 
            except Exception as e:
                print(e)
                try:
                    print('here')
                    return f'{pyautogui.size().width}x{pyautogui.size().height}'
                except Exception:
                    print("No display was found")
        
    def os(self):
        try:
            if platform.system() == "Linux":
                return [f'{platform.system()}',f'{platform.release()}']
            else:
                return [platform.system(),str(subprocess.check_output('systeminfo | find "OS Name"',shell=True)).split(":")[1].replace("\\r\\n","").replace(" ","")]
        except Exception as e:
            print(e)
            if platform.system() == "Windows":
                return [f'{platform.system()}',f'None']
            return [None,None]
    
    def cpu(self):
        try:
            return cpuinfo.get_cpu_info()['brand_raw']
        except:
            return None
        
    def sys_man(self):
        try:
            if platform.system() == "Linux":
                try:
                    return subprocess.check_output('cat /sys/class/dmi/id/sys_vendor',shell=True).decode()
                except Exception as e:
                    return subprocess.check_output('cat /proc/cpuinfo | grep Model',shell=True).decode()
            else:
                return subprocess.check_output('wmic csproduct get vendor',shell=True).decode().strip().replace("Vendor","")[1]
        except Exception as e:
            print("ERR")
            print(e)
            return None 
    
    def ram(self):
        return f'{(str(psutil.virtual_memory().used / (1024 * 1024)))[0:5]}MiB / {(str(psutil.virtual_memory().total / (1024 * 1024)))[0:5]}MiB'
    
    def net(self):
        try:
            if not platform.system() == "Linux":
                return subprocess.check_output('ipconfig | findstr IPv4',shell=True).decode().strip()
            else:
                return subprocess.check_output('ip -4 addr show | grep inet',shell=True).decode().strip()
        except Exception:
            return None



    def template(self):
        return f"""
                                        {self.host()}
                                    --------------------
                                    OS: {self.os()[0]}
                                    Kernel: {self.os()[1]}
                                    Uptime: {self.get_uptime()}
                                    System Manufacturer: {self.sys_man()}
                                    Netowork Info: 
                                            {self.net()}
                                    Resolution: {self.screen_size()}
                                    CPU: {self.cpu()}
                                    Memory: {self.ram()}
                 
        """

if __name__ == "__main__":
    print(HardwareStat().template())
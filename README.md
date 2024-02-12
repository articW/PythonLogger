## A **simple yet complex** python keylogger for Windows 
>For educational purposes, built by [articW](https://github.com/articW) to [Pacific Security](https://site.pacificsec.com/en) bootcamp. Thx!

### Legal Disclaimer
The use of this keylogger project to attack targets without prior mutual consent is strictly prohibited and may be illegal. It is the sole responsibility of the end user to comply with all applicable local, state, and federal laws. The developers of this project hereby disclaim any liability and cannot be held responsible for any misuse or damage resulting from the use of this program. This project is intended for educational and research purposes only and should be used ethically and within the bounds of the law.

### Features
- Pure Python, no C modules to be compiled
- Global event hook on all keyboards, using cross-platform library [pynput](https://github.com/moses-palmer/pynput?tab=readme-ov-file)
- Modular construction, allowing systematically changes and upgrades
- No need to be executed in a Privileged context (AKA: no admin permissions required)
- Captures: 
    - Keyboard keys
    - Screenshot (multi-screen support), using [Pillow](https://github.com/python-pillow/Pillow)
    - Running processes
    - System Information (sysinfo)
- Human-readable logs:
    - Keys are aggregated to form words
    - Words are written to the file when the "Space bar" or "Enter key" is pressed
    - When "Backspace key" is pressed, it also deletes the character collected
    - Timestamp for each word
- Persistence:
    - Script added to Run key registry, executed automatically on every startup
    - Error handling to avoid crashes or windows/pop-ups
- Hidden attribute:
    - Script hides itself upon first execution
    - All resources created and used by the Script are also hidden (folders, screenshots, text files...)
- Multi-thread support:
    - Some functions are executed on exclusive threads, allowing independent loops
- Compression and removal: 
    - Files are compressed before being sent
    - When compressed, files are automatically removed from the source
- Hybrid Encryption (TLS Socket):
    - Files are sent to a server using a TLS Socket, encrypting all contents by default (ciphers autoamtically negoatiated between Client and Server). No encryption overhead
    - Session key (AES-256) encrypts data, while RSA 2048-bit used in handshake/key negotiation
- Telegram integration:
    - Notifications sent via Telegram Bot, to a channel or group (bot creation in [BotFather](https://telegram.me/BotFather) required)

### Getting started

#### System requirements
- MS Windows (tested on 11).
- [Python 3](https://www.python.org/downloads/) (tested on v. 3.12.1)
    - The `asyncio` module is required in the server-side Script, which was added to the Python Standard Library in Python 3.4. If your Python version is 3.3 or later (`python --version`), [asyncio](https://pypi.org/project/asyncio/) needs to be installed mannually. 

#### Usage

##### **Quick start**
1. `git clone https://github.com/articW/PythonLogger`
2. `cd PythonLogger`
3. `pip install -r requirements.txt`
4. Customize parameters in great-eye.py
##### **Generate a self-signed Server Key and Certificate**
1. `openssl req -new -newkey rsa:2048 -days 365 -nodes -x509 -keyout {keyfile} -out {certfile} -subj "/CN=localhost`
2. Add the key and certificate paths to the parameters in great-eye.py
##### **Start Server Script to receive the files**
1. `pip install python-telegram-bot`
2. `python barad-dur.py`
##### **Run as a Windowed Python script in Client**
1. `python great-eye.py`
##### **Run as a Windowless Python script in Client**
1. Change extension from `.py` to `.pyw`
2. `pythonw great-eye.pyw`
> Windows versions of python are installed with two executables, `python.exe` (Windowed) and `pythonw.exe` (Windoless). By default, both extensions are added to PATH variable. 

##### **How to stop the running script**
For testing purposes, the script is set to stop running when the "ESC" key is pressed on the client. This behavior is defined by the "on_release" function and controlled by "start_keyboard_listener".

To change this behavior, simply remove the `on_release=on_release` parameter from the "start_keyboard_listener" function. Then, to stop the running script, it will be necessary to kill the process manually.

#### Known limitations
- The network interface is based on Sockets. Therefore, a script can only receive one connection at a time. 
- The "SECRET" value is used solely to prevent bots and crawlers from easily communicating with the server-side Script. There is no need for encryption/hashing. 
- I'm not a professional software developer, so the code may not be perfect. I apologize for any shortcomings, but I've put a lot of effort into making it as effective as possible. I hope y'all find it useful.

### Video presentation
https://github.com/articW/PythonLogger/assets/56977852/5695bbff-2427-4d26-a6de-a612bec27273
- No manual interation was made in the video. There is some timing in my actions, but all was done by the script. You can try it yourself :)
- 00:02 - Script it's NOT hidden
- 00:10 - Script it's now hidden
- 00:13 - I've refreshed the Registry, that's why the "Windows Update" poped-up suddenly
- 00:18 - Dir "c:\temp\dados\" was created by the Script (00:00, there was no "temp" dir).
- 00:40 - As soon as I went back from the Browser, the "compress" function was executed, that's why everything vanished
- 01:00 - Again, as soon as I went to "Server" directory, the "data_transfer" function was executed. 

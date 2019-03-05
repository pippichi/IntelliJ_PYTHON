import os
import time

source = [r'D:\Python3.6\venv\qyf_message\send_message.py', r'D:\Python3.6\venv\qyf_message\send_message.py']
target_dir = r'C:\Users\HASEE\Desktop'
target = target_dir + time.strftime('%Y%m%d%H%M%S') + '.rar'
rar_command = "winrar '%s' %s" % (target, ''.join(source))
if os.system(rar_command) == 0:
    print('Successful backup to', target)
else:
    print('Backup Failed')
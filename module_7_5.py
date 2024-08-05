import os
import time

directory = r'C:\TempProject'
print(os.getcwd())

for root, dirs, files in os.walk(directory):
    for file in files:
        filepath = os.path.join(root, file)
        filesize = os.path.getsize(r'C:\TempProject\module_7_5.py')
        filetime = os.path.getmtime(r'C:\TempProject\module_7_5.py')
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        parent_dir = os.path.dirname(r'C:\TempProject\module_7_5.py')
        print(f'File found: {file}, Path: {filepath}, Size: {filesize} bytes, '
              f'Last edit time: {formatted_time}, Parent directory: {parent_dir}.')

@echo off && setlocal

pip install -r requirements.txt
pyinstaller Core\main.py --onedir -n yamlmake

pause
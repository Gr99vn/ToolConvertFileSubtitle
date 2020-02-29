import glob, os
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

def getFilePath():
    file_path = filedialog.askopenfilenames()
    return list(file_path)

def getFilePathByFolder():
    folderPath = filedialog.askdirectory()
    print('-->  Folder Path:', folderPath)
    os.chdir(folderPath)
    fileList = []
    for file in glob.glob("*.vtt"):
        fileList.append(file)
    return fileList
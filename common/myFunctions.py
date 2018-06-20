#encoding: utf-8
"""
@project = FtpTools
@file = functions
@function = 通用的函数
@author = Cindy
@create_time = 2018/6/15 14:23
@python_version = 3.x
"""

import os, configparser, zipfile, shutil
from pathlib import Path
import subprocess

#获取ftp上最新的zip文件
def get_new_file(ftp):
    allFile = []
    files = ftp.nlst()
    files.sort()
    for file in files:
        if file.endswith('zip'):
            allFile.append(file)
    return allFile[-1]


#读取配置文件
def get_config_value(group, name):
    config = configparser.ConfigParser()
    config.read('config.ini')
    value = config.get(group, name)
    return value


#创建下载目录
def make_download_dir(path):
    if os.path.exists(path) == False:
        os.mkdir(path)

# 获取文件名
def get_file_extension(fileName):
    return os.path.splitext(fileName)[1]


#解压zip文件
def unzip_file(fileName):
    zip_file = zipfile.ZipFile(fileName)
    newfile=''
    if os.path.isdir(fileName):
        pass
    else:
        newfile = fileName[0:fileName.find(get_file_extension(fileName))]
        if os.path.exists(newfile):
            print("{}文件夹已存在".format(newfile))
            return
        os.mkdir(newfile)
    for names in zip_file.namelist():
        path = Path(zip_file.extract(names, newfile))
        names = newfile + '\\' + names.encode('cp437').decode('gbk')
        path.rename(names)
    zip_file.close()


#启动软件 PDS产品名称统一写为PDS即可
def start_up(fileName, product='PDS'):
    filePath = fileName[0:fileName.find(get_file_extension(fileName))]
    if product == 'PDS':
        startPath = filePath + '\\' + r'shell\PDSShell.exe'
    else:
        startPath = filePath + '\\' + product + '.exe'
    print(startPath)
    if os.path.exists(startPath):
        subprocess.Popen(startPath)

#启动分支覆盖方式的软件
def start_up_copy(installpath, product):
    startPath = installpath + '\\' + product + '.exe'
    print(startPath)
    if os.path.exists(startPath):
        subprocess.Popen(startPath)



#复制分支包
def copy_release(source, target):
    try:
        for f in os.listdir(source):
            file_old = os.path.join(source, f)
            shutil.move(file_old, target)
            print(file_old)
    except Exception as e:
        print(e)




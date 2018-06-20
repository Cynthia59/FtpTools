#encoding: utf-8
"""
@project = FtpTools
@file = run
@function = 运行脚本
@author = Cindy
@create_time = 2018/6/15 13:26
@python_version = 3.x
"""
from common import myFTP, myFunctions as myFc

def RunFunc(productName):
    #读取配置文件
    product = myFc.get_config_value(productName, 'product')
    host = myFc.get_config_value(productName,'host')
    username = myFc.get_config_value(productName, 'username')
    password = myFc.get_config_value(productName, 'password')
    ftppath = myFc.get_config_value(productName, 'ftppath')
    localPath = myFc.get_config_value(productName, 'localPath')
    installPath = myFc.get_config_value(productName, 'installPath')
    # print(product, host, username, password, ftppath, localPath, installPath)
    # 下载zip文件
    f = myFTP.Ftp(host, username, password)
    ftp = f.connect()
    ftp.cwd(ftppath)
    newFile = myFc.get_new_file(ftp)
    # print(newFile)
    myFc.make_download_dir(localPath)
    r = f.download_file(ftp, newFile, localPath)
    # 解压文件
    if r:
        print("正在解压文件")
        newFile = localPath + '\\' + newFile
        myFc.unzip_file(newFile)
        #如果是分支包类型的，复制分支包
        if productName == 'AZ':
            print("正在复制分支包")
            file_dir = newFile.split('.')[0]+'\\release'
            print(file_dir, ' -> ',installPath)
            myFc.copy_release(file_dir, installPath)
            try:
                print("正在启动软件")
                myFc.start_up_copy(installPath, product)
            except Exception as e:
                print(e)
        #PDS软件及其它软件
        else:
            print("正在启动软件")
            myFc.start_up(newFile, product)
    ftp.quit()

# RunFunc("AZ")
# RunFunc("BE")
# RunFunc("Govern")
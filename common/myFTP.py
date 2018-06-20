#encoding: utf-8
"""
@project = FtpTools
@file = ftp
@function = ftp下载方法
@author = Cindy
@create_time = 2018/6/15 13:52
@python_version = 3.x
"""

import ftplib, socket, sys

class Ftp(object):
    def __init__(self, host, username, password, buffer_size=8192):
        self.host = host
        self.username = username
        self.password = password
        self.buffer_size = buffer_size

    def connect(self):
        try:
            ftp = ftplib.FTP(self.host)
            ftp.login(user=self.username, passwd=self.password)
            print('已连接到： "%s"' % self.host)
            return ftp
        except(socket.error, socket.gaierror):
            print('FTP登录失败，请检查FTP用户名、密码！')
            sys.exit(0)

    def download_file(self, ftp, fileName, localPath):
        localFileName = localPath +'\\'+fileName
        f = open(localFileName, 'wb').write
        try:
            print('正在下载文件： "%s"' % fileName)
            ftp.retrbinary("RETR%s" % fileName, f, self.buffer_size)
            print('成功下载文件： "%s"' % fileName)
        except ftplib.error_perm:
            return False
        return True

if __name__ == '__main__':
    f = Ftp('192.168.2.244','pds','pdsclient')
    ftp = f.connect()
    ftp.cwd('release/rar/exploreragency_vs2015_x64')
    # myFunctions.make_download_dir('E:/ftp')
    # f.download_file(ftp, myFunctions.get_new_file(ftp), 'E:/ftp')

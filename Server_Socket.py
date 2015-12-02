#!/usr/bin/python
# coding=UTF-8

import socket
import sys
import light

"""
Step1 建立Socket
Step2 Bind Socket
Step3 設定最大連線數
Step4 啟動Server(socket)
Step5 接收數據
Step6 傳送數據
Step7 關閉Socket
"""

D150 = light.LightControl(115200)

"""
Step1 建立Socket
"""
try:
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error, msg:
    print ('開啟socket失敗.訊息代碼：%d\n' % msg[0])
    sys.exit(1)
finally:
    print ('已開啟Socket.')
try:
    """
    Step2 Bind Socket
    """
    hostName = ''
    port = 8888

    """
    將Host Name轉為IP
    """
    try:
        serverIP = socket.gethostbyname(hostName)
        print('已綁定成功. IP : %s' % serverIP + '  of %s Host' % hostName)
    except socket.gaierror, msg:
        print ('無法取得%s的IP. 訊息代碼：%d' % (hostName, msg[0]))
        sys.exit(1)
    try:
        serverSocket.bind((serverIP, port))
    except socket.error, msg:
        print('綁定失敗.訊息代碼：%d' % msg[0])
        sys.exit(1)

    """
    Step3 設定最大連線數
    """
    serverSocket.listen(10)
    print ('最多連線數有10個.')

    """
    Step4 啟動Server(socket)
    """
    print ('已啟動Sever.')
    (cSock, addr) = serverSocket.accept()

    print('連進來的IP:%s @ %d'  %(str(addr[0]),addr[1]))

    """
    Step5 接收數據
    """
    try:
        if(D150.connect() == False):
            print('無法開啟 FTDI Devie')
        else:
            while True:
                data = cSock.recv(1024)
                print ('收到的數據 : %s' %(data))
                D150.forward(data)
                if (len(data)==1):
                    if ((data[0]=='q') or (data[0]=='Q')):
                        break;
                """
                else:
                    if(data == 'On'):
                        D150.power_on()
                    elif(data == 'Off'):
                        D150.power_off()
                """
    except socket.error , msg:
        print('接收數據失敗.訊息代碼：%d' % msg[0])
        sys.exit(1)

finally:
    """
    關閉Socket
    """
    print('準備關閉Socket')
    serverSocket.close()
    print('Socket已經關閉')
"""
try
    while True:
        str = input('Enter your input : ')
        print(str)

except KeyboardInterrupt:
    print '強迫中斷'
"""

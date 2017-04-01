#!/home/mihaly/hadoop/anaconda3/bin/python
from random import randint
import time
def client_thread(conn, ip, port, MAX_BUFFER_SIZE = 4096):
    res='{0:d}'.format(randint(1,1000))
    my_st = res+'\n'
    
    try:
        conn.send(my_st.encode("utf8"))
        
        return 0
    except:
        return -1

def start_server():

    import socket
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # this is for easy starting/killing the app
    soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    print('Socket created')
    soc.bind(("localhost", 9000))
    print('Socket bind complete')
    #Start listening on socket
    soc.listen(10)
    print('Socket now listening')
    while True:
        conn, addr = soc.accept()
        ip, port = str(addr[0]), str(addr[1])
        print('Accepting connection from ' + ip + ':' + port)
        time.sleep(1)
        while True: #conn.__getstate__:
            if client_thread(conn, ip, port) != 0:
                break
            time.sleep(1)
            print(".", end='')
    soc.close()

start_server()  

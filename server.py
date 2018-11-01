import socket
import argparse
import os
 
host = '172.16.126.25'
data_payload = 2048
backlog = 5
 
def echo_server(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_address = (host, port)
    print ("Starting up echo server on %s port %s" % server_address)
    sock.bind(server_address)
    sock.listen(backlog)
    while True:
        print ("Waiting to receive message from client")
        client, address = sock.accept()
        data = client.recv(data_payload)
        if data:
            # print ("Data: %s" %data)
            # dato = "nice too meet you"
            client.send(data)
            data = str(data.decode("utf-8"))
            if data == 'report-':
              print('Decode %s' % data)
              # command = '\"C:\\Program Files (x86)\\Irdeto Access\\PIsys\\Apps\\SecureClientReporter.exe 2 \\172.16.126.193/shared/'+data+'.txt 1 1 f l /q"'
              os.system("start c:/archivo.bat " + data)
        client.close()
 
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Socket Server Example')
    parser.add_argument('--port', action="store", dest="port",type=int, required=True)
    given_args = parser.parse_args()
    port = given_args.port

    echo_server(port)
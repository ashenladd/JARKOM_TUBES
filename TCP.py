### Mengimport yang dibutuhkan seperti threading dan socket
import threading # mengimport threading
import requestHandler # mengimport requestHandler
def threading_socket(connectionSocket):
    try: # menangkap error
        request = connectionSocket.recv(1024).decode() # menerima request dari client
        print(f'\nrequest: {request}')# print request
        header = request.split('\n') # memisahkan request berdasarkan \n
        print('header[1]:',header[1]) # print header[0]
        print('Header file name :',header[0].split()[1]) # print header[0].split()[1]
        response = requestHandler.requestHandler(filename=header[0].split()[1]) # memanggil fungsi requestHandler
        connectionSocket.send(response.encode()) # mengirim response ke client
        connectionSocket.send("\r\n".encode()) # mengirim response ke client
        connectionSocket.close() # menutup koneksi
    except IOError: # menangkap error
        connectionSocket.send("File Not Found".encode()) # mengirim response ke client
        connectionSocket.close() # menutup koneksi

from socket import * # mengimport socket
import sys # mengimport sys
serverSocket = socket(AF_INET, SOCK_STREAM) # membuat socket TCP
serverPort = 8080 # port server
serverSocket.bind(('', serverPort)) # binding socket
serverSocket.listen(1) # listen socket
#prepare server socket
while True: # looping forever
    print('Ready to serve ...') # print ready to serve
    print('Server is running on port', serverPort) # print server is running on port
    connectionSocket, addr = serverSocket.accept() # menerima koneksi dari client
    threading.Thread(target=threading_socket, args=(connectionSocket,)).start() # memulai thread
    

serverSocket.close()
sys.exit()
from socket import * # mengimport socket

def requestHandler(filename):
    print(filename) # print filename
    response_line = "HTTP/1.1 200 OK\r\n" # response line
    response_header = "Content-Type: text/html\r\n\r\n" # response header
    if filename == "/": # jika filename adalah /
        filename = "index.html" # filename adalah index.html
    try: # menangkap error
        fin = open("view/" + filename, "r") # membuka file
        message_body = fin.read() # membaca file
        fin.close() # menutup file
    except FileNotFoundError: # menangkap error
        fin = open("view/not_found.html", "r") # membuka file
        response_line = "HTTP/1.1 404 Not Found\r\n" # response line
        message_body = fin.read() # membaca file
        fin.close() # menutup file
    
    response = response_line + response_header + message_body # response
    return response # mengembalikan response
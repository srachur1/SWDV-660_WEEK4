import socket

MACHINE = '127.0.0.1'  
PORT = 9500

while True:
    
    userinput = input("Please enter an input or type quit to exit:")

    if userinput.lower() == "quit":
        break
        
    connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connection.connect((MACHINE, PORT))        
    connection.send(userinput.encode())
    response = connection.recv(1024).decode()
    print("Server's Response: " + response)




  
    
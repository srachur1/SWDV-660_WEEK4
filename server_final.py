import socket

MACHINE = '127.0.0.1' 
PORT = 9500      
     
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print ("Socket successfully created")
s.bind((MACHINE, PORT))    
s.listen(10)
print ("socket is listening")
    
while True:
      
    c, addr = s.accept()        
    inputdata = c.recv(1024).decode() 
    if inputdata.lower() == 'hello':
        response = "Hi"
        c.send(response.encode())
        
    else:
        response = "Goodbye"
        c.send(response.encode())
        
                                 
    c.close()




  
  

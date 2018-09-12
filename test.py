#second test 



import socket
 
class Netcat:

    """ Python 'netcat like' module """

    def __init__(self, ip, port):

        self.buff = ""
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((ip, port))

    def read(self, length = 4096):

        """ Read 1024 bytes off the socket """

        return self.socket.recv(length)
 
    def read_until(self, data):

        """ Read data into the buffer until we have data """

        while not data in self.buff:
            self.buff += self.socket.recv(1024)
 
        pos = self.buff.find(data)
        rval = self.buff[:pos + len(data)]
        self.buff = self.buff[pos + len(data):]
 
        return rval
 
    def write(self, data):

        self.socket.send(data)
    
    def close(self):

        self.socket.close()
# below is a extract from a sample exploit that
# interfaces with a tcp socket
#from netcat import Netcat

# start a new Netcat() instance
nc = Netcat('kids.spb.ctf.su', 23840)

# get to the prompt

for i in range(1,100):

    #byte_i=bytes('abc',encoding = 'utf-8')
    #print(byte_i)
    
    print (nc.read())
    print(bytes('123' ,encoding="utf-8"))
    nc.write(b'123')


#test commit





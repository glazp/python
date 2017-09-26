from socketserver import BaseRequestHandler, TCPServer
class EchoHandler(BaseRequestHandler):
    def handle(self):
        print('Zadanie polaczenia z', self.client_address)
        while True:
            msg = self.request.recv(8192)
            if not msg:
                break
            print (msg)
            self.request.send(msg)
if __name__ == '__main__':
   serv = TCPServer(('', 20000), EchoHandler)
   print ("Echo server started, port 20000")
   serv.serve_forever()

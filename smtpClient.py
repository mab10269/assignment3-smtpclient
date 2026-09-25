from socket import *

def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n My message"
    endmsg = "\r\n.\r\n"

    clientsocket = socket(af_inet, sock_stream)
    clientsocket.connect((mailserver, port))
    
    recv = clientSocket.recv(1024).decode()

    helloCommand = 'HELO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024).decode()

    mailfromcommand = "mail from: <alice@example.com>\r\n"
    clientsocket.send(mailfromcommand.encode())
    recv2 = clientsocket.recv(1024).decode()
    
    rctptocommand = "rcpt to: <bob@example.com>\r\n"
    clientsocket.send(rcpttocommand.encode())
    recv3 = clientsocket.recv(1024).decode()
    
    datacommand = "data\r\n"
    clientsocket.send(datacommand.encode())
    recv4 = clientsocket.recv(1024).decode()
    
    clientsocket.send(msg.encode())
    
    clientsocket.send(endmsg.())
    recv5 = clientsocket.recv(1024).decode()
    
    quitcommand = "quit\r\n"
    clientsocket.send(quitcommand.encode())
    recv6 = clientsocket.recv(1024).decode()

if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')

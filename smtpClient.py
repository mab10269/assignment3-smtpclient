from socket import *

def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n My message"
    endmsg = "\r\n.\r\n"

    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((mailserver, port))
    
    recv = clientSocket.recv(1024).decode()

    helloCommand = 'HELO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024).decode()

    mailfromcommand = "mail from: <alice@example.com>\r\n"
    clientSocket.send(mailfromcommand.encode())
    recv2 = clientSocket.recv(1024).decode()
    
    rctptocommand = "rcpt to: <bob@example.com>\r\n"
    clientSocket.send(rcpttocommand.encode())
    recv3 = clientSocket.recv(1024).decode()
    
    datacommand = "data\r\n"
    clientSocket.send(datacommand.encode())
    recv4 = clientSocket.recv(1024).decode()
    
    clientSocket.send(msg.encode())
    
    clientSocket.send(endmsg.encode())
    recv5 = clientSocket.recv(1024).decode()
    
    quitcommand = "quit\r\n"
    clientSocket.send(quitcommand.encode())
    recv6 = clientSocket.recv(1024).decode()

    clientSocket.close()

if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')

from socket import *
import base64
import ssl
import time

msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"

username = "testthismail2021@gmail.com"
password = "BlackPink21!"
mailTo = "thuyluu9595@gmail.com"

def main():

    # Choose a mail
    mailServer = "smtp.gmail.com"
    mailPort = 465

    context = ssl.create_default_context()

    with create_connection((mailServer,mailPort)) as sock:
        clientSocket = context.wrap_socket(sock, server_hostname=mailServer)

    # Create socket called clientSocket and establish a TCP connection with mailserver
    recv = clientSocket.recv(1024).decode()
    print(recv)
    if recv[:3] != '220':
        print('220 reply not received from server.')

    # Send HELO command and print server response.
    heloCommand = 'HELO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    print(recv1)
    if recv1[:3] != '250':
        print('250 reply not received from server.')

    #Infor for username and password
    base64_str = ("\x00" + username + "\x00" + password).encode()
    base64_str = base64.b64encode(base64_str)
    authMsg = "AUTH PLAIN ".encode() + base64_str + "\r\n".encode()
    clientSocket.send(authMsg)
    recv_auth = clientSocket.recv(1024)
    print(recv_auth.decode())

    # Send MAIL FROM command and print server response.
    # Fill in start
    mailFromCommand = "Mail FROM:<{}>\r\n".format(username)
    clientSocket.send(mailFromCommand.encode())
    recv2 = clientSocket.recv(1024).decode()
    print("After MAIL FROM command:" + recv2)
    # Fill in end

    # Send RCPT TO command and print server response.
    # Fill in start
    rcptToCommand = "RCPT TO:<{}>\r\n".format(mailTo)
    clientSocket.send(rcptToCommand.encode())
    recv3 = clientSocket.recv(1024).decode()
    print("After RCPT TO command: " + recv3)
    # Fill in end

    # Send DATA command and print server response.
    # Fill in start
    dataCommand = 'DATA\r\n'
    clientSocket.send(dataCommand.encode())
    recv4 = clientSocket.recv(1024).decode()
    print("After DATA command: " + recv4)
    # Fill in end

    # Send message data.
    # Fill in start
    subject = "Subject: Testing sending an email\r\n\r\n"
    clientSocket.send(subject.encode())

    date = time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.gmtime())
    date = date + "\r\n\r\n"
    clientSocket.send(date.encode())
    clientSocket.send(msg.encode())
    clientSocket.send(endmsg.encode())
    recv_msg = clientSocket.recv(1024)
    print("Response after sending message body:"+recv_msg.decode())
    # Fill in end

    # Message ends with a single period.
    # Fill in start
    clientSocket.send(endmsg.encode())
    recv5 = clientSocket.recv(1024).decode()
    print("After Message ends with a single period: " + recv5)
    # Fill in end

    # Send QUIT command and get server response.
    # Fill in start
    quitCommand = 'QUIT\r\n'
    clientSocket.send(quitCommand.encode())
    recv6 = clientSocket.recv(1024).decode()
    print(recv6)
    # Fill in end
    clientSocket.close()

if __name__ == '__main__':
    main()

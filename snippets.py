#to send
s.setblocking(True)
s.send('a')
s.setblocking(False)

#to receive
s.recv(64)  # 64 = buffer size

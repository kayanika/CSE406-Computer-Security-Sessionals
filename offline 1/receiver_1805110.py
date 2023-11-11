import socket
import socket
import Diffie_Hellman_1805110 as Diffie_Hellman 
import AES_1805110 as AES

# Create a TCP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 8000))
print("Connected to ALICE...")

# Receive p, g, and g^a (mod p) from ALICE
p = int(sock.recv(1024).decode())
print("p:",p)
g = int(sock.recv(1024).decode())
print("g:",g)
g_a = int(sock.recv(1024).decode())
print("g_a:",g_a)

# Generate Diffie-Hellman parameters


# Generate g^b (mod p) and send it to ALICE
g_b,b = Diffie_Hellman.Compute_g_b(g,p,130)
sock.sendall(str(g_b).encode())

# Compute the shared secret key
shared_key = Diffie_Hellman.computeSharedKey(g_a,b,p)

# Receive Ready Message
ready_msg = sock.recv(1024)
print(ready_msg.decode())

# Receive and decrypt the ciphertext 
ciphertext = sock.recv(1024)

plaintext = AES.decrypt(ciphertext.decode(), str(shared_key))

print("Decrypted message:", plaintext)

# Close the connection
sock.close()


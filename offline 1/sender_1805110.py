import socket
import Diffie_Hellman_1805110 as Diffie_Hellman
import AES_1805110 as AES

# Create a TCP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('localhost', 8000))
sock.listen(1)
print("ALICE is listening on port 8000...")

# Accept a connection 
conn, addr = sock.accept()
print("Connected to BOB:", addr)

# Send p, g, and g^a (mod p) to BOB
p =  Diffie_Hellman.generateSafePrime(130)
print(p,"is safe prime")
conn.sendall(str(p).encode())
g = Diffie_Hellman.generatePrimitiveRoot(p-10000,p-100,p)
print(g,"is primitive root")
conn.sendall(str(g).encode())
g_a,a = Diffie_Hellman.Compute_g_a(g,p,130)
print(g_a,"is g_a")
conn.sendall(str(g_a).encode())

# Receive B from BOB
g_b = int(conn.recv(1024).decode())

# Compute the shared secret key
shared_key = Diffie_Hellman.computeSharedKey(g_b,a,p)

# Inform that sender is ready for transmission
conn.sendall(b"ready for transmission")

# Encrypt and send the ciphertext to BOB
message = "In the year 1999, in the 10th month, from the sky will come the great King of Terror. He will bring back to life the great King of the Mongols. Before and after, Mars to reign by good fortune."


ciphertext = AES.encrypt( message,str(shared_key))
conn.sendall(ciphertext.encode())

# Close the connection
conn.close()
sock.close()

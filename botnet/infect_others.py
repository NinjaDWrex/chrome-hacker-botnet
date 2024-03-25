import socket
import nmap
#constants
NUM_OF_PORTS = 24000
#scan for other devices on the network
nm = nmap.PortScanner()
data = nm.scan(hosts="192.168.2.1/24", arguments="-sP")
print data['nmap']['scanstats']['uphosts']
#find the open ports of these devices
sock = socket.socket(socket.AF_INET, sock.SOCK_STREAM)
sock.settimeout(2)
for
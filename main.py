import socket

# Fixed IP address. The ideal way is to specify the IP address/URL when calling the function
hostname = socket.gethostname()
target = socket.gethostbyname(hostname)

# Initializing socket
sckt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Scan a single given port
def single_scan(port, target = target):
    try:
        sckt.connect((target, port))
        return True
    except:
        return False

# min and max represent the range of ports you want to scan
def multi_scan(min, max, target = target):
    available_ports = []
    for port in range(min, max):
        if single_scan(target, port):
            available_ports.append(port)
    
    return available_ports

# Test
print(single_scan(5000))
print(multi_scan(1, 5000))
from socket import *
import threading
import argparse

def tcp_scan(ip,port):
    print("Port Scan Initiated on: " + ip + "\n")
    sock = socket(AF_INET, SOCK_STREAM)
    sock.settimeout(0.5)
    try :
        sock.connect((ip,port))
        print("[+] TCP Port: " +str(port) + " Open")
    except:
        print("[+] TCP Port: " +str(port) + " CLOSED\n")



def udp_scan(ip, port):
    try:
        connect_sock = socket(AF_INET, SOCK_STREAM)
        connect_sock.connect(ip, port)
        print("[+] UDP Port: " + str(port) + " Open")
    except:
        print("[+] UDP port closed: " + str(port))


def check_req(ip, port, isUdp):
    for ports in port:
        if not (isUdp):
            potoc = threading.Thread(target=tcp_scan, args=(ip, int(ports)))
        else:
            potoc = threading.Thread(target=udp_scan, args=(ip, int(ports)))
        potoc.start()


def main():
    print("Welcome To TCP Port Scanner!\n")
    try:
        parser = argparse.ArgumentParser("TCP Scanner")
        parser.add_argument("-a", "--address", type=str, help="Enter the ip address to scan")
        parser.add_argument("-p", "--port", type=str, help="Enter The port to scan")
        parser.add_argument("-u", "--udp", action="store_true")
        args = parser.parse_args()
        ipaddress = args.address
        port = args.port.split(',')
        isUdp = args.udp
        check_req(ipaddress, port, isUdp)
    except:
        print("[+] No Arugments Supplied\n example: python ex3.py -a 192.168.43.224 -p 21,22,80")

if __name__ == "__main__":
    main()

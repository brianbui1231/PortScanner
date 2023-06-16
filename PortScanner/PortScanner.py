import socket as sck

def conScan(targetHost, targetPort):
   try:
        connectSocket = sck.socket(sck.AF_INET, sck.SOCK_STREAM)
        connectSocket.connect((targetHost, targetPort))
        print(f"[+] {targetPort}/tcp open")
   except:
        print(f"[-] {targetPort}/tcp closed")


def portScan(targetHost, targetPorts):
    try:
        targetIP = sck.gethostbyname(targetHost)
    except:
        print(f"[-] Cannot resolve {targetHost}: Unknown host")
        return
    try:
        targetName = sck.gethostbyaddr(targetIP)
        print(f"\n[+] Scan results for: {targetName[0]}")
    except:
        print(f"\n[+] Scan results for: {targetIP}")
    sck.setdefaulttimeout(1)
    for targetPort in targetPorts:
        print(f"Scanning port {targetPort}")
        conScan(targetHost, int(targetPort))

if __name__ == "__main__":
    option = input("Would you like to scan specific ports or all ports (0 - 1024)? (specific/all): ")
    if option == "specific":
        targetHost = input("Enter target host: ")
        targetIP = sck.gethostbyname(targetHost)
        targetPorts = input("Enter target ports separated by comma: ")
        if ',' in targetPorts:
            for targetPort in targetPorts.split(','):
                conScan(targetIP, int(targetPort))
        else:
            conScan(targetIP, int(targetPorts))

    elif option == "all":
        targetHost = input("Enter target host: ")
        targetPorts = range(0, 1024)
        portScan(targetHost, targetPorts)
        option2 = input("Would you like to scan more ports (1025 - 65536)? (y/n): ")
        if option2 == "y":
            targetPorts = range(1025, 65536)
            portScan(targetHost, targetPorts)
        else:
           exit()
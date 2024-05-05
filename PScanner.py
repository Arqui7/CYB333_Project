import socket

def PS(target_host, start_port, end_port):
   
    #Performs a port scan on the specified target host and port range.
    #target_host: The IP address or hostname of the target.
    #start_port: The starting port number for the scan.
    #end_port: The ending port number for the scan.
    
    print(f'Starting port scan on {target_host}...')
    
    try:
        # target host to IP address
        T_ip = socket.gethostbyname(target_host)
    except socket.gaierror:
        print("Hostname could not be found. Exiting...")
        return

    for port in range(start_port, end_port + 1):
        try:
            # Create a socket object
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # Set a timeout for the connection attempt (in seconds)
            s.settimeout(2)
            # Attempt to connect to the target host and port
            r = s.connect_ex((T_ip, port))
            # Check if the connection was successful
            if r == 0:
                print(f'Port {port} is open')
            else:
                print(f'Port {port} is closed')
            # Close the socket
            s.close()
        except KeyboardInterrupt:
            print("\nExiting...")
            return
        except socket.error:
            print("Couldn't connect to server. Exiting...")
            return

def main():
    target_host = input("Enter IP address or hostname: ")
    start_port = int(input("Enter the starting port number: "))
    end_port = int(input("Enter the ending port number: "))
    
    PS(target_host, start_port, end_port)

if __name__ == "__main__":
    main()

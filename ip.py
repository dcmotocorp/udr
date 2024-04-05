import socket

def get_ip_address():
    try:
        # Create a socket object
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # Connect to a remote host to determine the local IP address
        s.connect(("8.8.8.8", 80))
        # Get the IP address
        ip_address = s.getsockname()[0]
        # Close the socket
        s.close()
        return ip_address
    except socket.error as e:
        print("Error:", e)
        return None

# Get and print the IP address
ip_address = get_ip_address()
if ip_address:
    print("Your IP address is:", ip_address)
else:
    print("Failed to retrieve IP address.")

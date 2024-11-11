import socket

def dns_lookup():
    choice = input("Enter '1' for URL to IP lookup or '2' for IP to URL lookup: ")
    
    if choice == '1':
        url = input("Enter the URL: ")
        try:
            ip_address = socket.gethostbyname(url)
            print(f"The IP address for {url} is: {ip_address}")
        except socket.gaierror:
            print("Could not resolve the URL. Please check the URL and try again.")
    
    elif choice == '2':
        ip_address = input("Enter the IP address: ")
        try:
            host = socket.gethostbyaddr(ip_address)
            print(f"The URL for IP address {ip_address} is: {host[0]}")
        except socket.herror:
            print("Could not resolve the IP address. Please check the IP and try again.")
    
    else:
        print("Invalid choice. Please enter '1' or '2'.")

dns_lookup()

import socket

def ip_to_url(ip):
    url=socket.gethostbyaddr(ip)
    if url:
        print(f"domain name for ip is : {url[0]}")
    else:
        print("Invalid IP")

def url_to_ip(url):
    ip=socket.gethostbyname_ex(url)
    if ip:
        print(f"Ip address for url is : {ip[2][0]}")
    else:
        print("Invalid domain name")

input_type=int(input("INPUTS\n0. IP address\n1. URL\nWhat do you want to enter:"))

if input_type==0:
    ip=input("Enter the ip address:")
    ip_to_url(ip)
elif input_type==1:
    url=input("Enter the url:")
    url_to_ip(url)
else:
    print("Invalid Input")
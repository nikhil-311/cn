#subnetting.py
def determine_class_and_subnet(ip):
    first_octet = int(ip.split('.')[0])

    if 1 <= first_octet <= 126:
        ip_class = "A"
        subnet_mask = "255.0.0.0"
    elif 128 <= first_octet <= 191:
        ip_class = "B"
        subnet_mask = "255.255.0.0"
    elif 192 <= first_octet <= 223:
        ip_class = "C"
        subnet_mask = "255.255.255.0"
    elif 224 <= first_octet <= 239:
        ip_class = "D (Multicast)"
        subnet_mask = "Not applicable"
    elif 240 <= first_octet <= 255:
        ip_class = "E (Experimental)"
        subnet_mask = "Not applicable"
    else:
        ip_class = "Invalid IP Address"
        subnet_mask = "Not applicable"

    print(f"IP Class: {ip_class}")
    print(f"Default Subnet Mask: {subnet_mask}")

ip = input("Enter IP address (e.g., 192.168.1.1): ")
determine_class_and_subnet(ip)

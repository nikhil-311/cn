'''
subnet class:
class A: 000 to 127
class B: 128 to 191
class C: 192 to 223
class D: 224 to 239
class E: 239 to 255

Submask:
class A: 255.0.0.0
class B: 255.255.0.0
class C: 255.255.255.0
class D: 255.255.255.255
class E: 255.255.255.255
'''	

def ip_range(unit, class_name):
    print("Range:")
    unit[-1]='0'
    FROM=".".join(unit)
    print(f"From: {FROM}")

    unit[-1]='255'
    TO='.'.join(unit)
    print(f"To: {TO}")

def IP_class(address):
    unit=address.split(".")

    if int(unit[0])>=0 and int(unit[0])<=127:
        print(f"{address}\nClass A\nSubmask: 255.0.0.0")
        ip_range(unit,'A')

    elif int(unit[0])>=128 and int(unit[0])<=191:
        print(f"{address}\nClass B\nSubmask: 255.255.0.0")
        
        ip_range(unit,'B')
    elif int(unit[0])>=192 and int(unit[0])<=223:
        print(f"{address}\nClass C\nSubmask: 255.255.255.0")
        ip_range(unit,'C')
    elif int(unit[0])>=224 and int(unit[0])<=239:
        print(f"{address}\nClass D\nSubmask: 255.255.255.255")
        ip_range(unit,'D')
    elif int(unit[0])>=239 and int(unit[0])<=255:
        print(f"{address}\nClass E\nSubmask: 255.255.255.255")
        ip_range(unit,'E')
    else:
        print("ERROR IN IP ADDRESS")

IP=input("Enter the IP address:")
IP_class(IP)
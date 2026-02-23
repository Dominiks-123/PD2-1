nodes = [
    "Srv-Web-01;192.168.1.10;15;UP",
    "Srv-DB-01;192.168.1.20;450;UP",
    "Srv-Backup;10.0.0.5;0;DOWN",
    "Workstation-A;192.168.1.105;5;UP",
    "Srv-Proxy-01;172.16.0.1;10;up",
    "Srv-Mail;10.0.0.10;120;UP",
    "Router-Core;192.168.1.1;2;UP",
    "Srv-Dev-01;192.168.2.50;500;UP",
    "Printer-Main;192.168.1.200;0;down",
    "Srv-Log;10.0.0.15;105;UP"
]
x=input("ievadi ip adresi: ")
x=x.split(".")
y=0
n=0
while len(x)<4:
    x.append('0')
for row in nodes:
    ip=row.split(";")[1]
    ip=ip.split(".")
    name=row.split(';')[0]
    for now in range(4):
        if x[y]==ip[y] or x[y]=='0':
            n+=1
        if n==4:
            print(name)
        y+=1
    y=0
    n=0
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
n=0
k=0
for row in nodes:
    work=row.split(';')[3]
    name=row.split(';')[0]
    work=work.lower()
    if work=='up':
        n+=1
        print(f"{name} is up")
    k+=1
print(f"there is {n} out of {k} servers up")
from telnetlib import Telnet
cmd = input('Enter the Command :')
tn = Telnet('10.10.10.10')
tn.write(b'admin\n')
tn.write(b'admin\n')
tn.write(b'term length 0\n')
tn.write(cmd.encode('ascii') + b'\n')
tn.write(b'exit\n')
print(tn.read_all().decode('ascii'))
from scapy.all import *
import scapy.contrib.modbus as mb

packets = rdpcap("7.download_project.pcapng")

for packet in packets:
    if mb.ModbusPDUReservedFunctionCodeResponse in packet:
        data = packet.payload

data = str(data)
#print(data)
a, data = data.split("Z")
data = data[:-1]

print(data)

#data = data.replace("x", '')
#print(data)
#data = int(data, 16)
#print(data)
#data = bytes.fromhex(data)
#print(data)

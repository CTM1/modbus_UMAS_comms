from scapy.all import *
import scapy.contrib.modbus as mb

packets = rdpcap("7.download_project.pcapng")

responses = []

for packet in packets:
    if mb.ModbusPDUReservedFunctionCodeResponse in packet:
        data = packet.payload
        data = str(data)
        #print(data)
        _, data = data.split("Z", 1)
        responses.append(data)

#print(data)

for res in responses:
    print(res)



#data = data.replace("x", '')
#print(data)
#data = int(data, 16)
#print(data)
#data = bytes.fromhex(data)
#blalblaZdd

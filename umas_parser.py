from scapy.all import *
import scapy.contrib.modbus as mb

def parse_pcap(filepath: str):
    print("\n[*] Parsing pcap...")
    pcap = rdpcap(filepath)

    queries     = []
    responses   = []

    previous_request = ""

    for packet in pcap:
        if mb.ModbusPDUReservedFunctionCodeResponse in packet:
            umas_packet = bytes(packet.payload).split(b'Z')[1]
            if "Failed" in previous_request:
                print("[-] Failed to identify request")
                continue
            if 0xfe in umas_packet:
                print("[+] Response to request " + str(previous_request) + " OK")
            else:
                print("[-] Response to request " + str(previous_request) + " failed")

            responses.append(umas_packet)

        if mb.ModbusPDUReservedFunctionCodeRequest in packet:
            umas_packet = bytes(packet.payload).split(b'Z')[1]
            try:
                request = str(umas_packet[4])
            except:
                request = "Failed to identify request"
            previous_request = request

            queries.append(request)

    return queries, responses
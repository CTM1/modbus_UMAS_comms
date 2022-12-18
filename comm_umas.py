# Read PLC info, Monitor PLC, Check PLC, Keep Alive, Read Memory block, Stop PLC, Read Project Info
# Read ID, Read Card Info, Initialize Download, Download Block, End Strategy Download, Upload Block
import scapy
import optparse

# Here are some important variables concerning the UMAS ADU

FUNC_ID = 0x5a # UMAS protocol

unit_id = 0x00 # When not used, it's 0xff by default.
transaction_id = 0x00 # Give this (ID of the last request you sent + 1), if you don't know, leave as is.
# transaction_id = 0xDBF8

def cli():
    p = optparse.OptionParser(description='UMAS CLI',
                              prog='comm_umas', version='0.1', usage='usage: comm_umas.py <PLC_ip>:<port>')

def communicate():
    function_code = 0x5a


def connect_plc(dst_ip: str, port: str):
    print("[*] Setting up socket")
    plc_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    print("[*] Connecting to PLC at {}:{} ...", dst_ip, port)
    
    try: 
        s.connect(dst_ip, port)
        print("[+] Connected !")
    except Exception as e:
        print("[-] Connection failed: {}", e)

#                        Data MUST be a HEX string
def send_umas_packet(s: socket, data: str, request_type="default"):

    # A Modbus "frame" consists of an Application Data Unit (ADU), 
    # which encapsulates a Protocol Data Unit (PDU)
    # ADU = Address + PDU + Error check.
    # PDU = Function code + Data.

    print("[*] Sending {} request data ...", request_type)
    try: 
        data = bytes.fromhex(data)
        print("[+] Packet sent!")
    except Exception as e:
        print("[-] Invalid data string passed to send_umas_packet: {}", e)

    #                             Data len + function code
    adu = ModbusADURequest(len = len(data) + 1, unitId=unit_id)

    # Make TCP/IP packet
    packet = adu/data

    s.send(bytes(packet))

    print("[*] Receiving {} request response ...", request_type)

    try:
        response = s.recv(512)
        print("[+] Request response successfully received")
    except Exception as e:
        print("[-] Failed to receive request response properly: {}", e)

    return response

if __name___ = '__main__':
    main()
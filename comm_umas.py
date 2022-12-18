# Read PLC info, Monitor PLC, Check PLC, Keep Alive, Read Memory block, Stop PLC, Read Project Info
# Read ID, Read Card Info, Initialize Download, Download Block, End Strategy Download, Upload Block
import scapy
import argparse

def print_banner():
    END = '\001\033[0m\002'

    U = "╔╗ ╔╗╔═╗╔═╗╔═══╗╔═══╗    ╔═══╗╔╗   ╔══╗"
    M = "║║ ║║║║╚╝║║║╔═╗║║╔═╗║    ║╔═╗║║║   ╚╣╠╝"
    A = "║║ ║║║╔╗╔╗║║║ ║║║╚══╗    ║║ ╚╝║║    ║║ "
    S = "║║ ║║║║║║║║║╚═╝║╚══╗║    ║║ ╔╗║║ ╔╗ ║║ "
    C = "║╚═╝║║║║║║║║╔═╗║║╚═╝║    ║╚═╝║║╚═╝║╔╣╠╗"
    L = "╚═══╝╚╝╚╝╚╝╚╝ ╚╝╚═══╝    ╚═══╝╚═══╝╚══╝"

    banner = [U,M,A,S,C,L]
    init_color = 28
    txt_color = init_color
    cl = 0
    final = []

    for charset in range(0, 6):
        for pos in range(0, len(banner[charset])):
                clr = f'\033[38;5;{txt_color}m'
                char = f'{clr}{banner[charset][pos]}'
                final.append(char)
                cl += 1

        cl = 0
        txt_color = init_color
        init_color += 1

        final.append('\n   ')

    print(f"   {''.join(final)}")
    print(f'{END}2600 - krkn')

def cli():
    print_banner()                            
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
def send_umas_packet(sock, data: str, request_type="default"):

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

if __name__ == '__main__':
    print_banner()
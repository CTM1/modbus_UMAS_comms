# Read PLC info, Monitor PLC, Check PLC, Keep Alive, Read Memory block, Stop PLC, Read Project Info
# Read ID, Read Card Info, Initialize Download, Download Block, End Strategy Download, Upload Block
import scapy
import argparse
import messages
import sys

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

def connect_plc(dst_ip: str, port: str):
    print("[*] Setting up socket")
    plc_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    print("[*] Connecting to PLC at {}:{} ...", dst_ip, port)
    
    try: 
        s.connect(dst_ip, port)
        print("[+] Connected !")
    except Exception as e:
        print("[-] Connection failed: {}", e)
        return None
    
    return s

if __name__ == '__main__':
    data_fix = True
    print_banner()
    
    if len(sys.argv) < 2:
        print("Usage: comm_umas.py <PLC_ip>:<port>")
        exit(0)

    addr = sys.argv.split(':')
    plc_sock = connect_plc(addr[0], addr[1])
    messages.init_comms(plc_sock)
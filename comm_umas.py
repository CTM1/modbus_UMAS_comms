# Read PLC info, Monitor PLC, Check PLC, Keep Alive, Read Memory block, Stop PLC, Read Project Info
# Read ID, Read Card Info, Initialize Download, Download Block, End Strategy Download, Upload Block
import scapy
import socket
import argparse
import comm_messages
import parser_umas
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

    print("[*] Connecting to PLC at ", dst_ip, port)
    
    try: 
        plc_sock.connect((dst_ip, int(port)))
        print("[+] Connected !")
    except Exception as e:
        print("[-] Connection failed: ")
        print(e)
        exit(0)
        return None
    
    return plc_sock

if __name__ == '__main__':
    print_banner()
    print()

    print("comm_umas.py <PLC_ip>:<port> for network connection")
    print("comm_umas.py --pcap <filename> for parsing a .pcap for UMAS requests")

    if sys.argv[1] == '--pcap':
        queries, responses = parser_umas.parse_pcap(sys.argv[2])
        parser_umas.print_responses(responses)
    else:
        addr = sys.argv[1].split(':')
        plc_sock = connect_plc(addr[0], addr[1])
        print("Type 'help' for a list of requests")
        while True:
            print(">>> ", end='')
            cmd = input()
            if cmd == 'help':
                print(*comm_messages.protocol_list, sep='\n')
            else:
                try:
                    comm_messages.send_umas_packet(plc_sock, int(cmd))
                except Exception as e:
                    print("Invalid parameter: ")
                    print(e)
def parse_init_comm_res(packet):
    print("[*] INIT_COMMS response")
    
    if packet[1] == 0xfe:
        print("\t[+] OK - 0xfe")
        if (packet[2:4] != b''):
            print("\t[+] Frame Size: " + str(int.from_bytes(packet[2:4], 'little')))
            print("\t[+] Data: " + str(packet[4:]))
        else:
            print("\t[-] PLC Reserved")
        return

    if packet[1] == 0xfd:
        print("\t[-] KO - 0xfd")
    else:
        print("\t[?] Unknown Response")
    
    return

def parse_init_comm_req(packet):
    return

def parse_read_id_res(packet):
    return

def parse_read_id_req(packet):
    return

def parse_read_proj_info_res(packet):
    return

def parse_read_proj_info_req(packet):
    return

def parse_read_plc_info_res(packet):
    return

def parse_read_plc_info_req(packet):
    return

def parse_read_card_info_res(packet):
    return

def parse_read_card_info_req(packet):
    return

def parse_repeat_res(packet):
    return

def parse_repeat_req(packet):
    return

def parse_take_plc_res(packet):
    return

    
def parse_take_plc_req(packet):
    return

def parse_release_plc_res(packet):
    if packet[1] == 0xfe:
        print("\t[+] OK - 0xfe")
    elif packet[1] == 0xfd:
        print("\t[-] KO - 0xfd")
    else:
        print("\t[?] Unknown Response")
        return
    
def parse_release_plc_req(packet):
    return

def parse_keep_alive_res(packet):
    return

def parse_keep_alive_req(packet):
    return

def parse_init_comm_res(packet):
    print("[*] INIT_COMMS response")
    
    if packet[1] == 0xfe:
        print("\t[+] OK - 0xfe")
    elif packet[1] == 0xfd:
        print("\t[-] KO - 0xfd")
    else:
        print("\t[?] Unknown Response")
        pass


def parse_init_comm_req(packet):
    pass

def parse_read_id_res(packet):
    if packet[1] == 0xfe:
        print("\t[+] OK - 0xfe")
    elif packet[1] == 0xfd:
        print("\t[-] KO - 0xfd")
    else:
        print("\t[?] Unknown Response")
        pass


def parse_read_id_req(packet):
    pass

def parse_read_proj_info_res(packet):

    if packet[1] == 0xfe:
        print("\t[+] OK - 0xfe")
    elif packet[1] == 0xfd:
        print("\t[-] KO - 0xfd")
    else:
        print("\t[?] Unknown Response")
        pass


def parse_read_proj_info_req(packet):
    pass

def parse_read_plc_info_res(packet):

    if packet[1] == 0xfe:
        print("\t[+] OK - 0xfe")
    elif packet[1] == 0xfd:
        print("\t[-] KO - 0xfd")
    else:
        print("\t[?] Unknown Response")
        pass


def parse_read_plc_info_req(packet):
    pass

def parse_read_card_info_res(packet):
    if packet[1] == 0xfe:
        print("\t[+] OK - 0xfe")
    elif packet[1] == 0xfd:
        print("\t[-] KO - 0xfd")
    else:
        print("\t[?] Unknown Response")
        pass

def parse_read_card_info_req(packet):
    pass

def parse_repeat_res(packet):
    if packet[1] == 0xfe:
        print("\t[+] OK - 0xfe")
    elif packet[1] == 0xfd:
        print("\t[-] KO - 0xfd")
    else:
        print("\t[?] Unknown Response")
        pass

def parse_repeat_req(packet):
    pass

def parse_take_plc_res(packet):
    if packet[1] == 0xfe:
        print("\t[+] OK - 0xfe")
    elif packet[1] == 0xfd:
        print("\t[-] KO - 0xfd")
    else:
        print("\t[?] Unknown Response")
        pass
    
def parse_take_plc_req(packet):
    pass

def parse_release_plc_res(packet):
    if packet[1] == 0xfe:
        print("\t[+] OK - 0xfe")
    elif packet[1] == 0xfd:
        print("\t[-] KO - 0xfd")
    else:
        print("\t[?] Unknown Response")
        pass
    
def parse_release_plc_req(packet):
    pass

def parse_keep_alive_res(packet):
    if packet[1] == 0xfe:
        print("\t[+] OK - 0xfe")
    elif packet[1] == 0xfd:
        print("\t[-] KO - 0xfd")
    else:
        print("\t[?] Unknown Response - skipping")
        pass

def parse_keep_alive_req(packet):
    pass

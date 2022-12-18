# Set this to True in main() in case you'd like to pad the request with data
global data_fix
prefix = '525015'
suffix = ''

FUNC_ID = '5a' # UMAS protocol

# data MUST be a HEX string
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

def init_comms(sock):
    if data_fix:
        req_data = (FUNC_ID + prefix + '0001' + suffix)
    else:
        req_data = (FUNC_ID + '0001')

    res_data = send_umas_packet(sock, req_dat, "init_comms - 0x0001")

    print(res_data)

def read_plc_info(sock):
    response = {}
    if data_fix: 
        req_data = (FUNC_ID + prefix + '0004' + suffix) 
    else:
        req_data = (FUNC_ID + '0004')
    
    res_data = send_umas_packet(sock, req_data)

    print(res_data)

# Set this to True in main() in case you'd like to pad the request with a 
# session key or PLC ID
global data_fix
session_key = '525015'

FUNC_ID = '5a' # UMAS

protocol_list = [
    [0,  '0001', 'INIT_COMM'],
    [1,  '0002', 'READ_ID'],
    [2,  '0003', 'READ_PROJECT_INFO'],
    [3,  '0004', 'READ_PLC_INFO'],
    [4,  '0006', 'READ_CARD_INFO'],
    [5,  '000A', 'REPEAT'],
    [6,  '0010', 'TAKE_PLC_RESERVATION'],
    [7,  '0011', 'RELEASE_PLC_RESERVATION'],
    [8,  '0012', 'KEEP_ALIVE'],
    [9,  '0020', 'READ_MEMORY_BLOCK '],
    [10, '0022', 'READ_VARIABLES'],
    [11, '0023', 'WRITE_VARIABLES'],
    [12, '0024', 'READ_COILS_REGISTERS'],
    [13, '0025', 'WRITE_COILS_REGISTERS '],
    [14, '0030', 'INITIALIZE_UPLOAD'],
    [15, '0031', 'UPLOAD_BLOCK'],
    [16, '0032', 'END_STRATEGY_UPLOAD'],
    [17, '0033', 'INITIALIZE_UPLOAD'],
    [18, '0034', 'DOWNLOAD_BLOCK'],
    [19, '0035', 'END_STRATEGY_DOWNLOAD'],
    [20, '0039', 'READ_ETH_MASTER_DATA'],
    [21, '0040', 'START_PLC'],
    [22, '0041', 'STOP_PLC'],
    [23, '0050', 'MONITOR_PLC'],
    [24, '0058', 'CHECK_PLC'],
    [25, '0070', 'READ_IO_OBJECT'],
    [26, '0071', 'WRITE_IO_OBJECT'],
    [27, '0073', 'GET_STATUS_MODULE']
]

# data MUST be a HEX string
def send_umas_packet(sock, request_id,  message_data=''):
    if data_fix:
        data = (FUNC_ID + session_key + protocol_list[request_id][1] + message_data)
    else:
        data = (FUNC_ID + protocol_list[request_id][1])
    # A Modbus "frame" consists of an Application Data Unit (ADU), 
    # which encapsulates a Protocol Data Unit (PDU)
    # ADU = Address + PDU + Error check.
    # PDU = Function code + Data.

    print("[*] Sending {} request data ...", protocol_list[request_id][2])
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

    print("[*] Receiving {} request response ...", request_id)

    try:
        response = s.recv(1024)
        print("[+] Request response successfully received")
    except Exception as e:
        print("[-] Failed to receive request response properly: {}", e)

    return response
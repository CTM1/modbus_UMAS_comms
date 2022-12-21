from scapy.all import *
import scapy.contrib.modbus as mb
import parser_messages

res_parse_dict = {
    "1" : parser_messages.parse_init_comm_res,
#    "2" : parser_messages.parse_read_id_res,
#    "3" : parser_messages.parse_read_proj_info_res,
#    "4" : parser_messages.parse_read_plc_info_res,
#    "6" : parser_messages.parse_read_card_info_res,
#    "A" : parser_messages.parse_repeat_res,
#    "10": parser_messages.parse_take_plc_res,
#    "11": parser_messages.parse_release_plc_res,
#    "12": parser_messages.parse_keep_alive_res,
}

req_parse_dict = {
    "1": parser_messages.parse_init_comm_req,
#    "2": parser_messages.parse_read_id_req,
#    "3": parser_messages.parse_read_proj_info_req,
#    "4": parser_messages.parse_read_plc_info_req,
#    "6": parser_messages.parse_read_card_info_req,
#    "A": parser_messages.parse_repeat_req,
#    "10": parser_messages.parse_take_plc_req,
#    "11": parser_messages.parse_release_plc_req,
#    "12": parser_messages.parse_keep_alive_req,
}

def parse_pcap(filepath: str):
    print("\n[*] Parsing pcap...")
    pcap = rdpcap(filepath)

    queries     = []
    responses   = []

    previous_request = ""

    for packet in pcap:
        if mb.ModbusPDUReservedFunctionCodeResponse in packet:
            umas_packet = bytes(packet.payload).split(b'Z')[1]
            if "Failed" == previous_request:
                print("[-] Failed to identify request")
            #                    ID               Packet
            responses.append([previous_request, umas_packet])

        if mb.ModbusPDUReservedFunctionCodeRequest in packet:
            umas_packet = bytes(packet.payload).split(b'Z')[1]
            try:
                request = str(umas_packet[4])
            except:
                if umas_packet == b'':
                    request = "Failed"
                else:
                    request = umas_packet[1]

            previous_request = request
            queries.append(umas_packet)
    
    return queries, responses

def print_responses(responses):
    for r in responses:
        try: 
        #                  ID   Packet
            res_parse_dict[r[0]](r[1])
        except KeyError:
            print("Request " + str(r[0]) + " not implemented.")
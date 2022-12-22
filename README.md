# modbus_UMAS_comms
Python program to communicate with a PLC using the UMAS protocol and parse UMAS packets in pcaps.

The project is split in two parts, `parser_*` and `comms_*`. the first one is used for the .pcap parsing and the second one for command-line control.

However, the functions for parsing the .pcaps could equally be used to parse responses in a communication case.

## CLI
`python3 umas_comms.py <IP_ADDR>:<PORT>`

## .pcap parser
`python3 umas_comms.py --pcap <PCAP_FILEPATH>`

# Read PLC info, Monitor PLC, Check PLC, Keep Alive, Read Memory block, Stop PLC, Read Project Info
# Read ID, Read Card Info, Initialize Download, Download Block, End Strategy Download, Upload Block
import scapy
import optparse

def main():

    p = optparse.OptionParser(description='UMAS CLI',
                              prog='comm_umas', version='0.1', usage='usage: comm_umas.py [options] IPAddress')


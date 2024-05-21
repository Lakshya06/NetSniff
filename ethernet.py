#!/usr/bin/env python3

import struct
from ethertype_read import ETHER_TYPE

ETH_P_ALL = 0x03  # to listen all types of packets

def ethernet(data):
    dest, src, ethertype, data = parse_ether_frame(data)
    dest = readable_mac(dest)
    src = readable_mac(src)
    ethertype = ethertype_read(ethertype)

    return (f"[Ethernet - {ethertype}]; Source: {src}; Destination: {dest}; Len: {len(data)}")

def parse_ether_frame(data):
    dest_mac, src_mac, ethertype = struct.unpack('! 6s 6s H', data[:14]) # Parsing raw data packet to get source, dest mac and ethertype
    return dest_mac, src_mac, ethertype, data[14:]

def readable_mac(data): # Making mac form readable
    res = ""
    for i in data:
        res = res + format(i, '02x')
        res = res + ':'
    return res

def ethertype_read(ethertype):
    ether = hex(ethertype)
    res = "UNKNOWN"

    if ethertype in ETHER_TYPE:
        res = ETHER_TYPE[ethertype]
    
    return res



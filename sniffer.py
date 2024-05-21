#!/usr/bin/env python3

import socket
import struct
from ethernet import *

ETH_P_ALL = 0x03  # to listen all types of packets

s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.htons(ETH_P_ALL)) # Create a socket with .AF_PACKET -> To create a socket with low level packet access, send and receive raw data frames .SOCK_RAW -> Raw sockets to access protocols that are not usually allowed
# This will return raw ethernet frame without the last 4 bits checksum: 6 byte dest MAC, 6 byte source MAC, 2 byte ether type, 46-1500 byte Payload

while True:
    raw_data, addr = s.recvfrom(65565) # 65565 is the buffersize to receive
    # dest_mac, src_mac, ethertype, payload = parse_ether_frame(raw_data)
    # print(raw_data[:14])
    # print(f"[ Frame -> Dest: {readable_mac(dest_mac)}; Source: {readable_mac(src_mac)}; EtherType: {hex(ethertype)} ]")
    # print(raw_data[14:])
    frame = ethernet(raw_data)
    print(frame)
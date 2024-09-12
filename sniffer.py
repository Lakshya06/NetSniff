#!/usr/bin/env python3

import socket
import struct
from ethernet import *
from ipv4_frame import *
from extras.colors import *
from udp_segment import *
from tcp_segment import *

ETH_P_ALL = 0x03  # to listen all types of packets
ipv4_id = 0x0800
udp_id = 0x11
tcp_id = 0x06
# print(udp_id)

s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.htons(ETH_P_ALL)) 
# Create a socket with .AF_PACKET -> To create a socket with low level packet access, without any protocol send and receive raw data frames .
# SOCK_RAW -> Raw sockets to access protocols that are not usually allowed
# This will return raw ethernet frame without the last 4 bits checksum: 6 byte dest MAC, 6 byte source MAC, 2 byte ether type, 46-1500 byte Payload

while True:
    raw_data, addr = s.recvfrom(65565) # 65565 is the buffersize to receive

    #Ethernet
    frame, etherype, ether_payload = ethernet(raw_data)
    # print(etherype)
    print(frame+",", end="")

    #ipv4
    if etherype == ipv4_id:
        packet, ipv4_protocol, ipv4_payload = ipv4_frame(ether_payload)
        # print(blue(" └─ " + packet))
        print(packet+",", end="")
        # print(ipv4_protocol)
        # print(ipv4_protocol)

        if ipv4_protocol == udp_id:
            segment, hexdumped_data = udp_segment(ipv4_payload)
            # print(yellow("   └─ " + segment))
            # print(yellow(hexdumped_data))
            print(segment)
        if ipv4_protocol == tcp_id:
            segment, data = tcp_segment(ipv4_payload)
            # print(green("   └─ " + segment))
            # print(green(data))
            print(segment)
    print("\n")
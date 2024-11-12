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

with open("dummyData5.txt", "w") as file:
    pass

f = open("dummyData5.txt", "a")
while True:
    raw_data, addr = s.recvfrom(65565) # 65565 is the buffersize to receive

    #Ethernet
    frame, etherype, ether_payload = ethernet(raw_data)[0]
    frame_to_print  = ethernet(raw_data)[1]
    # print(etherype)
    print(frame_to_print)
    f.write(frame+",")

    #ipv4
    if etherype == ipv4_id:
        packet, ipv4_protocol, ipv4_payload = ipv4_frame(ether_payload)[0]
        packet_to_print = ipv4_frame(ether_payload)[1]
        print(blue(" └─ " + packet_to_print))
        # print(packet_to_print+",", end="")
        f.write(packet+",")
        # print(ipv4_protocol)
        # print(ipv4_protocol)

        if ipv4_protocol == udp_id:
            segment, hexdumped_data = udp_segment(ipv4_payload)[0]
            segment_to_print = udp_segment(ipv4_payload)[1]
            print(yellow("   └─ " + segment))
            print(yellow(hexdumped_data))
            print(segment, end="")
            f.write(segment)
        if ipv4_protocol == tcp_id:
            segment, data = tcp_segment(ipv4_payload)[0]
            segment_to_print = tcp_segment(ipv4_payload)[1]
            print(green("   └─ " + segment_to_print))
            print(green(data))
            # print(segment, end="")
            f.write(segment)
            
    f.write("\n")
    # print("\n")

f.close()
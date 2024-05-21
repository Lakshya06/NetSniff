#!/usr/bin/env python3
import socket
import struct

ETH_P_ALL = 0x03  # to listen all types of packets

def unpack_ether_frame(data):
    dest_mac, src_mac, ethertype = struct.unpack('! 6s 6s H', data[:14]) # Parsing raw data packet to get source, dest mac and ethertype
    return dest_mac, src_mac, ethertype, data[14:]

s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.htons(ETH_P_ALL)) # Create a socket with .AF_PACKET -> To create a socket with low level packet access, send and receive raw data frames .SOCK_RAW -> Raw sockets to access protocols that are not usually allowed
# This will return raw ethernet frame without the last 4 bits checksum: 6 byte dest MAC, 6 byte source MAC, 2 byte ether type, 46-1500 byte Payload

raw_data, addr = s.recvfrom(65565)
dest_mac, src_mac, ethertype, payload = unpack_ether_frame(raw_data)
print(raw_data[:14])
print(f"[Frame - Dest: {dest_mac}; Source: {src_mac}; EtherType: {hex(ethertype)}]")
print(raw_data[14:])

# while True:
    # raw_data, addr = s.recvfrom(65565)
    # print(raw_data)

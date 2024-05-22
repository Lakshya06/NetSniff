#!/usr/bin/env python3

import struct
from etherytype_and_ipv4proto import IP_PROTO

def ipv4_frame(data):
    ipv4_ver_ihl, ipv4_dcp_ecn, ipv4_len, ipv4_id, ipv4_flags_offset, ipv4_ttl, ipv4_protocol, ipv4_checksum, ipv4_src, ipv4_dest, ipv4_extra = parse_ipv4_frame(data)
    ipv4_src = readable_ipv4(ipv4_src) # converting source & dest to readable
    ipv4_dest = readable_ipv4(ipv4_dest)
    ipv4_version = ipv4_ver_ihl >> 4 # to get first four bits, since byte 0 consists of 8 bits and first 4 bits are version and last 4 bits are ihl
    ipv4_ihl = ipv4_ver_ihl & 0b00001111 # anding with bitmask to get last four bits
    ipv4_proto_readable = readable_protocol(ipv4_protocol)

    ipv4_options_len = 0
    if ipv4_ihl > 5:
        ipv4_options_len = (ipv4_ihl - 5) * 4

    ipv4_options = ipv4_extra[:ipv4_options_len]
    ipv4_payload = ipv4_extra[ipv4_options_len:]

    return (f"[ IPV4 - Protocol: {ipv4_protocol} {ipv4_proto_readable}; Source: {ipv4_src}; Destination: {ipv4_dest}]")

def parse_ipv4_frame(data):
    ipv4_ver_ihl, ipv4_dscp_ecn, ipv4_len, ipv4_id, ipv4_flags_offset, ipv4_ttl, ipv4_proto, ipv4_checksum, ipv4_src, ipv4_dest = struct.unpack("! B B H H H B B H 4s 4s", data[:20]) # retreiving all the ipv4 header feilds, 20 bytes, after 20 bytes there is data

    return ipv4_ver_ihl, ipv4_dscp_ecn, ipv4_len, ipv4_id, ipv4_flags_offset, ipv4_ttl, ipv4_proto, ipv4_checksum, ipv4_src, ipv4_dest, data[20:]

def readable_ipv4(data):
    res = ""

    for i in data:
        res += format(i, 'd') # parsing the ipv4 bits into decimal
        res += '.'
    
    return res

def readable_protocol(data):
    proto = hex(data)
    res = "UNKNOWN"

    if data in IP_PROTO: # Converting protocol to redable form if found in dict
        res = IP_PROTO[data]
    
    return res


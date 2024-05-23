#!/usr/bin/env python3

import struct

def udp_segment(data):
    udp_src, udp_dest, udp_len, udp_checksum, udp_extra = parse_udp_segment(data)
    return (f"[ UDP - Source Port: {udp_src}; Destination Port: {udp_dest}; LEN: {udp_len}]")

def parse_udp_segment(data):
    src, dest, lent, checksm = struct.unpack("! H H H H", data[:8])
    return src, dest, lent, checksm, data[8:]
#!/usr/bin/env python3

import struct

def udp_segment(data):
    udp_src, udp_dest, udp_len, udp_checksum, udp_extra = parse_udp_segment(data)
    hexdump_data = hexdump(udp_extra)
    return [(f"{udp_src}, {udp_dest}", hexdump_data), f"[ UDP - Source Port: {udp_src}; Destination Port: {udp_dest}; LEN: {udp_len}]"]
    # return (f"[ UDP - Source Port: {udp_src}; Destination Port: {udp_dest}; LEN: {udp_len}]", hexdump_data)

def parse_udp_segment(data):        # parsing udp segment
    src, dest, lent, checksm = struct.unpack("! H H H H", data[:8])
    return src, dest, lent, checksm, data[8:]

def hexdump(data):
    curr = 0
    end = len(data)
    res = ""

    while curr < end:
        temp_data = data[curr: curr+16] # selecting 16 bytes to transform and save
        res += " "*6

        for i in temp_data:
            res += "%02X " % i      # adding the 16 bits of hex data

        for _ in range(16 - len(temp_data)):
            res += " " * 3
        res += "    "

        for i in temp_data:     # converting hex data into readable string
            if (i >= 32) and (i < 127):     # if it can be redabale (printable chars in the range of [32-127]) convert it to chr
                res += chr(i)
            else:                           # else add '.'
                res += "."

        res += "\n"
        curr += 16

    return res
#!/usr/bin/env python3

import struct

def tcp_segment(data):
    tcp_src, tcp_dest, tcp_seq, tcp_ack_num, tcp_offest_flags, tcp_winsize, tcp_checksum, tcp_urg_ptr, tcp_extra = parse_tcp(data)
    hexdump_data = hexdump(tcp_extra)
    return [(f"{tcp_src}, {tcp_dest}", hexdump_data), f"[ TCP - Source Port: {tcp_src}; Destination Port: {tcp_dest}; LEN: {tcp_winsize}]"]
    # return (f"[ TCP - Source Port: {tcp_src}; Destination Port: {tcp_dest}; LEN: {tcp_winsize}]", hexdump_data)


def parse_tcp(data):
    tcp_src, tcp_dest, tcp_seq, tcp_ack_num, tcp_offest_flags, tcp_winsize, tcp_checksum, tcp_urg_ptr = struct.unpack("! H H I I H H H H", data[:20])       # unpacking the first 19 bits to get header information for tcp segment

    return tcp_src, tcp_dest, tcp_seq, tcp_ack_num, tcp_offest_flags, tcp_winsize, tcp_checksum, tcp_urg_ptr, data[20:]

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

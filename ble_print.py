def print_hex(data):
    hex_data = ""
    for i in list(data):
        hex_data += hex(i) + " "
    return hex_data
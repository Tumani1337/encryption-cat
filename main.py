def encryption_name(name: str) -> int:
    final_num_str = ''
    for i in name:
        final_num_str += str(ord(i))
        final_num_str += '|'
    return final_num_str


def decoding_str(string):
    decoded_str = ''
    last_symbol_index = -1
    for i in range(len(string)):
        if string[i] == "|":
            if last_symbol_index == -1:
                decoded_symbol = chr(int(string[0:i:1]))
                last_symbol_index = i
            else:
                decoded_symbol = chr(int(string[last_symbol_index + 1:i:1]))
                last_symbol_index = i
            decoded_str += decoded_symbol
    return decoded_str


def encryption_num(num: int) -> str:
    return chr(num)
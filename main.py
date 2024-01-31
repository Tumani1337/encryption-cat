def encryption_name(name: str) -> int:
    final_num_str = ''
    for i in name:
        final_num_str += str(ord(i))
        final_num_str += '|'
    return final_num_str
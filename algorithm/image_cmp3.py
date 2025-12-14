from collections import Counter
from bitarray import bitarray

from .huffman_full import (
    build_huffman_tree,
    generate_huffman_code,
    encode_data_to_bitarray,
    decode_data, load_frequency_table
)


def compress_bmp(data: bytes) -> bytes:

    freq_table = Counter(data)

    header = bytearray(b"HUF1")
    k = len(freq_table)
    header += k.to_bytes(2, 'big')

    for sym, freq in freq_table.items():
        header += bytes([sym]) + freq.to_bytes(8, 'big')
    
    root = build_huffman_tree(freq_table)

    code_map = {}
    generate_huffman_code(root, "", code_map)
    payload = encode_data_to_bitarray(data, code_map)

    return bytes(header + payload)


def decompress_bmp(data: bytes) -> bytes:

    freq_table, _, payload_bytes = load_frequency_table(data, from_bytes=True)

    root = build_huffman_tree(freq_table)
    pad_len = payload_bytes[0]

    bits = bitarray()
    bits.frombytes(payload_bytes[1:])

    if pad_len:
        bits = bits[:-pad_len]
    return decode_data(bits.to01(), root)
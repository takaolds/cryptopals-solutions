def fixed_XOR(buffer1, buffer2):
    bytes1 = bytes.fromhex(buffer1)
    bytes2 = bytes.fromhex(buffer2)
    return bytes([a ^ b for a,b in zip(bytes1, bytes2)])

def test1():
    input1 = "1c0111001f010100061a024b53535009181c"
    input2 = "686974207468652062756c6c277320657965"
    output = "746865206b696420646f6e277420706c6179"
    assert fixed_XOR(input1, input2).hex() == output

def main():
    test1()

if __name__ == "__main__":
    main()

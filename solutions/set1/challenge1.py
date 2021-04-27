import base64

def convert_hex_to_b64(val):
    bytes_rep = bytes.fromhex(val);
    return base64.b64encode(bytes_rep)

def test1():
    input_string = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
    output = b'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'
    assert convert_hex_to_b64(input_string) == output 

def main():
    test1()

if __name__ == "__main__":
    main()

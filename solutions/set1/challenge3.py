def main():
    input_string = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
    input_bytes = bytearray.fromhex(input_string)
    for i in range(255):
        result = bytearray("", 'utf-8')
        for j in range(len(input_bytes)):
            result.append(input_bytes[j] ^ i)
        print("{0}: {1}".format(i, result))

if __name__ == "__main__":
    main()

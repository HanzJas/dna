# Python3.11
# Use argument -h for help
import sys
import getopt


def main(argv):
    path = ""
    length = 0
    help_str = "Usage: python3 dna_seq_conv.py [arguments]\nArguments:\
                \n-p\tor\t--path\t\tPath to file\
                \n-l\tor\t--length\tLength of fragment"

# Get arguments from commandline
    try:
        options, arguments = getopt.getopt(argv, "p:l:h",
                                           ["path=",
                                            "length=",
                                            "help"])
    except getopt.GetoptError:
        print('Unknown option argument')
        sys.exit()

# Extract arguments from key:value tupple
    for opt, arg in options:
        if opt in ['-p', '--path']:
            path = arg
        elif opt in ['-l', '--length']:
            if arg.isnumeric():
                length = int(arg)
            else:
                print("Length is not number")
                sys.exit()
        elif opt in ['-h', '--help']:
            print(help_str)
            sys.exit()
    if len(path) == 0 or length <= 0:
        print("Missing argument")
        sys.exit()

    dna_dict = {
        "00": "A",
        "01": "C",
        "10": "G",
        "11": "T"
    }

# Open file (specified in path) and read data
    input_file = open(path, "rb")
    data = input_file.read()
    input_file.close()

# Data processing to get output in required format
    chunk_size = length
    cycle = 1
    while data:
        chunk, data = data[:chunk_size], data[chunk_size:]
        binary_data_element = []
        dna_sequence = ""
        confidence = ""
        for element in chunk:
            binary_data_element = ('{:08b}'.format(element))
            dna_sequence = dna_sequence + (dna_dict[binary_data_element[:2]])
            rest_bits = [binary_data_element[2:]]
            rest_decimal = int(rest_bits[0], 2)
            confidence = confidence + (chr(rest_decimal + 33))
        print(f"@READ_{cycle}")
        print(dna_sequence)
        print(f"+READ_{cycle}")
        print(confidence)
        cycle = cycle + 1


if __name__ == "__main__":
    main(sys.argv[1:])

def decode_readlines(input_file):
    """read input file as lines and decode"""
    try:
        with open(input_file, 'r', encoding ='utf-8') as file:
            #read content of input file as lines and break on each new line
            data = file.readlines()
    except UnicodeDecodeError:
        # If decoding with UTF-8 fails, try with different encodings
        encodings = ['utf-8', 'utf-16', 'latin-1', 'windows-1252', 'gb2312']
        for encoding in encodings:
            try:
                with open(input_file, 'r', encoding=encoding) as file:
                    data = file.readlines()
                # exit loop once file is sucessfully read
                break
            except UnicodeDecodeError:
                print(f'Failed to decode using: {encoding}')
                continue
        else:
            raise ValueError("Unable to decode file with any supported encoding")
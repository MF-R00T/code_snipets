import os
import base64

def decode_base64_filename(encoded_name):
    try:
        #extract first part of file name [0]
        base64_part = encoded_name.split('.')[0]
        decoded_bytes = base64.b64decode(base64_part)
        return decoded_bytes.decode('utf-8')
    except Exception:
        return encoded_name  # Return original if decoding fails

def find_strings_in_files(directory, search_strings):
    # Check if the provided path is a valid directory
    if not os.path.isdir(directory):
        print("Invalid directory")
        return
    
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        
        if os.path.isfile(file_path):
            try:
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
                    content = file.read()
                    # Check if any of the search terms appear in the file content
                    for search_string in search_strings:
                        if search_string in content:
                            decoded_name = decode_base64_filename(filename)
                    print(f"file: {decoded_name} | match: {search_string}")

            except Exception as e:
                print(f"Error reading {filename}: {e}")

# Example usage
directory_path = "path/to/your/directory"
search_terms = ["string1", "string2", "string3"]
find_strings_in_files(directory_path, search_terms)
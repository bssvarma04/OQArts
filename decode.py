def decode(message_file):
    with open(message_file, 'r') as file:
        lines = file.readlines()
    
    decoded_words = [line.split()[1] for line in lines]
    pyramid_height = len(lines)
    decoded_message = ' '.join(decoded_words[:pyramid_height])
    
    return decoded_message.lower().strip()

print(decode('C:\\Users\\bssva\\Downloads\\coding_qual_input.txt'))


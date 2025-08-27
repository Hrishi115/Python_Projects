alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
special_chars = [" ", ".", ",", "!", "?"]

def encode(): 
    message = input("Enter message to encode: ").lower()
    encoded_msg = ""
    for char in message:
        
        if char in special_chars:
            encoded_msg += char
        else:
            pos = alphabets.index(char)
            new_pos = pos+4
            if new_pos < len(alphabets):
                encoded_msg += alphabets[new_pos]
            else: 
                encoded_msg += alphabets[new_pos - len(alphabets)]

    print(encoded_msg)

def decode():
    message = input("Enter message to decode: ").lower()
    decoded_msg = ""
    for char in message:
        if char in special_chars:
            decoded_msg += char
        else:
            pos = alphabets.index(char)
            new_pos = pos-4
            if new_pos < len(alphabets):
                decoded_msg += alphabets[new_pos]
            else: 
                decoded_msg += alphabets[new_pos + len(alphabets)]

    print(decoded_msg)


if __name__ == "__main__":
    choice = input("Encode(E) or Decode(D)? ").lower()
    if choice == "e":
        encode()
    elif choice == "d":
        decode()
    else:
        print("Enter a valid option!")
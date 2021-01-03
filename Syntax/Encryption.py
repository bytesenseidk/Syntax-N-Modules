def encryption(string, step):
    output = ""
    for char in string:
        # Every character has a numeric value,
        # this is how the computer can understand it.
        output += chr(ord(char) - step)
        # We simply change the numeric value of the character,
        # which results in another character.
    return output

def decryption(string, step):
    # Same thing, but reversed
    output = ""
    for char in string:
        output += chr(ord(char) + step)
    return output


if __name__ == "__main__":
    string = "Encrypt me!"
    step = 2
    encrypted = encryption(string, step)
    decrypted = decryption(encrypted, step)
    print(f"Original:  {string}")
    print(f"Encrypted: {encrypted}")
    print(f"Decrypted: {decrypted}")




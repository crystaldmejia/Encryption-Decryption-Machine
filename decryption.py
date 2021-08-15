def decryption():
    
    """
    Take user inputted cipher and convert it to a text message.
    
    Arguments:
    None.
    
    Output:
    `message_decrypt`: A string that represent the decrypted cipher
    
    """
    
    # Create the RSA key pair
    p = 13
    q = 17
    public_key_n = p * q
    phi = (p-1) * (q-1)
    
    public_key_e = 5
    i = 2
    
    private_key = int((i * phi + 1)/public_key_e)
    
    # Get cipher input from the user - input is string, output is list of integers
    cipher = input("Enter the cipher you want to decrypt:").split(",")
    cipher = [int(i) for i in cipher]
    
    
    # Take the cipher and convert it to decrypted values
    decrypt_num = []
    for index in cipher:
        value = (index ** private_key) % public_key_n
        decrypt_num.append(value)
    
    # Convert the decrypted values to letters - output is list of letters
    letters = []
    for index in decrypt_num:
        letter_decrypt = chr(index)
        letters.append(letter_decrypt)
    
    # Combine the letters into a final message - output is string
    message_decrypt = ""
    message_decrypt = message_decrypt.join(letters)
    
    print(message_decrypt)

decryption()
def encryption ():
    
    """
    Take user inputted message and convert it to a cipher.
    
    Arguments:
    None.
    
    Output:
    `encryption`: A list of integers that represent the encrypted message
    
    """
    
    # Create the RSA key pair
    p = 13
    q = 17
    public_key_n = p * q
    phi = (p-1) * (q-1)
    
    public_key_e = 5
    i = 2
    
    private_key = int((i * phi + 1)/public_key_e)

    # Get message input from the user and convert to all caps
    text = input("Enter the message you want to encrypt: ")
    text_upper = text.upper()
    
    # Create a list with the letters from the message converted to cipher
    encryption = []
    for letter in text_upper:
        cipher = (ord(letter) ** public_key_e) % public_key_n
        encryption.append(cipher)
    print(encryption)

encryption()
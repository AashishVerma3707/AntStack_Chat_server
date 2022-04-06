

# Caesar cipher cryptography

def encrypt(message_body,characters):

    all_characters = characters
    encrypted_string = ""
    secret_key=20

    for i in message_body:
        position = all_characters.find(i)
        updated_position = (position+secret_key)%100
        encrypted_string += all_characters[updated_position]

    return encrypted_string


def decrypt(encrypted_string,secret_key,characters):

    all_characters = characters
    decrypted_string = ""

    for i in encrypted_string:
        position = all_characters.find(i)
        updated_position = (position - int(secret_key)) % 100
        decrypted_string += all_characters[updated_position]

    return decrypted_string

def decipher(message, emblem_):
    '''Decipher messages using Seaser (Caeser) algorithm.'''

    VALID_ALPHABETS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    output_text = ""

    for current_character in message:
        output_text += VALID_ALPHABETS[VALID_ALPHABETS.index(
            current_character) - len(emblem_)]

    return(output_text)
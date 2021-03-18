def format_text(text):
    return sorted([letter.lower() for letter in text if letter.isalpha()])


def get_same_letter(text1, text2):
    for letter in text1:
        if letter in text2:
            return letter
    return None


def remove_letter(text, letter):
    if letter in text:
        text.pop(text.index(letter))



def is_blanagram(text1, text2):
    text1_letters = format_text(text1)
    text2_letters = format_text(text2)
    
    if len(text1_letters) != len(text2_letters):
        return False
    
    if text1_letters == text2_letters:
        return True

    iterator = iter(lambda: get_same_letter(text1_letters, text2_letters), None)
    for same_letter in iterator:
        remove_letter(text1_letters, same_letter)
        remove_letter(text2_letters, same_letter)

    return (len(text1_letters) == 1) and (len(text2_letters) == 1)


print(is_blanagram('Justin Timberlake', "I'm a berk but listen"))

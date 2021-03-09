def check_email(string):
    return ' ' not in string and '@' in string and '.' in string[string.find('@') + 1:] and '@.' not in string


def check_email(string):
    if ' ' in string:
        return False
    if '@' not in string:
        return False
    if string.find('.', string.find('@')) == string.find('@') + 1:
        return False
    if string.find('.', string.find('@')) == -1:
        return False
    return True

def check_email(string):
    after_at = string.find("@") + 2
    return string.count("@") == 1 and string[after_at:].count(".") == 1 and string.count(" ") == 0
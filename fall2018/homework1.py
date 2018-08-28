
def convert(text):
    domain = '@gmail.com'
    delimiter = '; '
    separator = ','
    convert_str = ''

    words = text.split(separator)
    for idx, current_word in enumerate(words):
        convert_str += current_word.strip() + domain if idx+1 == len(words) else current_word.strip()+domain+delimiter

    return convert_str
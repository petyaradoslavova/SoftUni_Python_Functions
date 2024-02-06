def camel(string):
    new_list = list(string)
    for index,char in enumerate(new_list):
        if char in ['-','_']:
            new_list[index+1] = new_list[index+1].title()
            new_list.remove(char)
    return ''.join(new_list)


import re

def to_camel_case(text):
    words = re.split(r'[-_]', text)
    words[1:] = list(map(str.capitalize, words[1:]))
    return "".join(words)

# def to_camel_case(text):
#     removed = text.replace('-', ' ').replace('_', ' ').split()
#     if len(removed) == 0:
#         return ''
#     return removed[0]+ ''.join([x.capitalize() for x in removed[1:]])

print(to_camel_case('the_camel_is_here'))
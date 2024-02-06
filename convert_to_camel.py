def camel(string):
    new_list = list(string)
    for index,char in enumerate(new_list):
        if char in ['-','_']:
            new_list[index+1] = new_list[index+1].title()
            new_list.remove(char)
    return ''.join(new_list)


print(to_camel_case('the_camel_is_here'))

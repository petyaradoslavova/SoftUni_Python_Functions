def even_odd_filter(**kwargs):
    new_dirctionary = {}

    for key,value in kwargs.items():

        new_list = []
        if key == 'even':
            new_list = [num for num in value if num % 2 == 0]
        elif key == 'odd':
            new_list = [num for num in value if num % 2 != 0]
        new_dirctionary[key] = new_list

 
    return dict(sorted(new_dirctionary.items() , key=lambda x: -len(x[1])))


print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
    ))

print(even_odd_filter(
    odd=[2, 2, 30, 44, 10, 5],
))

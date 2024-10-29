# # задача 1
# string = input('введите текст: ')
# def string_info (string):
#     f = len(string)
#     b = str (string.lower())
#     c = str (string.upper())
#     tuk = (f, b, c)
#     print(tuk)
# string_info(string)
#
#
# задача № 3
string = input ('введите строку: ', )
list_to_search = ['kaPibara', 'ElefaNt', 'Lion']

def is_contains (string, list_to_search):
    string = string.lower()
    list_to_search = [name.lower() for name in list_to_search]
    if string in list_to_search:
        print(True)
    else:
        print(False)
    return string
    return list_to_search
    count_calls ()
is_contains (string, list_to_search)


calls = 0
def count_calls ():
    global calls
    calls +=1
    return calls
count_calls ()
print(calls)


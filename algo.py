from jap_data import dict_data

def search_dictionary(search_string):
    jap_dict_len  = len(dict_data)
    results = []
    a = len(search_string)
    b = x = 0
    char_asc = 97

    for i in range(1, 26, 3):
        if char_asc > ord(search_string[0]):
            if char_asc > 122:
                char_asc = 122
                break
        else:
            char_asc = char_asc + 3
            if char_asc > 122:
                char_asc = 122

    for i in range(1, jap_dict_len , 100):
        if char_asc < ord(dict_data[i]['romaji'][0]):
            break

    char_asc = chr(char_asc - 4)

    for i in range(i+1, 0, -1):
        b = len(dict_data[i]['romaji'])
        x = 0
        for x in range(b):
            y = 0
            for y in range(a):
                try:
                    if dict_data[i]['romaji'][x+y] != search_string[y]:
                        break
                except:
                    break
                y = y + 1
            if y == a:
                result = { "data": dict_data[i], "index": i }
                results.append(result)
                break
        if char_asc >= dict_data[i]['romaji'][0]:
            break

    return results


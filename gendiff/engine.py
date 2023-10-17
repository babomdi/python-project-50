def convert_to_lower(dictionary):
    for key, value in dictionary.items():
        if isinstance(value, bool):
            dictionary[key] = str(value).lower()
    return dictionary


def generate_diff(data1, data2):
    data1 = convert_to_lower(data1)
    data2 = convert_to_lower(data2)
    result_string = []

    for key, value in data1.items():
        if key in data2 and data1[key] == data2[key]:
            string = f'    {key}: {value}'
            result_string.append(string)
            del data2[key]
        elif key in data2 and data1[key] != data2[key]:
            string1 = f'  - {key}: {value}'
            string2 = f'  + {key}: {data2[key]}'
            result_string.append(string1)
            result_string.append(string2)
            del data2[key]
        else:
            string = f'  - {key}: {value}'
            result_string.append(string)

    if data2:
        for key, value in data2.items():
            string = f'  + {key}: {value}'
            result_string.append(string)

    result_string = sorted(result_string, key=lambda x: x[4])
    result_string.insert(0, '{')
    result_string.append('}\n')

    return '\n'.join(result_string)

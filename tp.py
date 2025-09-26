def dictoutput(inputed_dict):
    inputed_dict = sorted(inputed_dict.items())
    d = ''
    for key in inputed_dict:
        d+=f"{key[0]}: {key[1]}, "
    return d
print(dict(dictoutput({'B': 'B', 'A': 'C'})))
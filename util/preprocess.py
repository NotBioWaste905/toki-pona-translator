from string import punctuation
punctuation += '“' + '”' + '—'
def clear_string(raw: str) -> str:
    new_string = ''
    for i in raw:
        if i not in punctuation:
            new_string += i.lower()
    return new_string

# print(list(punctuation))
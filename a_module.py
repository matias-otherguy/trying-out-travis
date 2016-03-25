def remove_vowels(a_string):
    vowels = set(["a", "e", "i",
                "o", "u", "y" ])
    return ''.join(c for c in a_string if str.lower(c) not in vowels)

def dummy_fun():
    raise(NotImplementedError)

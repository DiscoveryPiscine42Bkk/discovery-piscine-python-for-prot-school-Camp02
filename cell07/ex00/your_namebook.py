def array_of_names(name_dict):

    full_names = []
    keys = list(name_dict.keys())
    i = 0
    
    while i < len(keys):
        first = keys[i].capitalize()
        last = name_dict[keys[i]].capitalize()
        full_names.append(f"{first} {last}")
        i += 1

    return full_names

if __name__ == "__main__":
    names = {
        "jean": "valjean",
        "grace": "hopper",
        "xavier": "niel",
        "fifi": "brindacier"
    }
    
    print(array_of_names(names))
input()
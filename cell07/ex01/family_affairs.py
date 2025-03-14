def find_the_redheads(family_dict):

    redheads = []
    names = list(family_dict.keys())
    i = 0
    
    while i < len(names):
        if family_dict[names[i]].lower() == "red":
            redheads.append(names[i])
        i += 1
    return redheads

if __name__ == "__main__":
    family = {
        "florian": "red",
        "marie": "blond",
        "virginie": "brunette",
        "david": "red",
        "franck": "red"
    }

    print(find_the_redheads(family))
input()
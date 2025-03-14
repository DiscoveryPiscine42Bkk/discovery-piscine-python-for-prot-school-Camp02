def find_the_redheads(family_dict):

    redheads = list(filter(lambda name: family_dict[name].lower() == "red", family_dict))
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
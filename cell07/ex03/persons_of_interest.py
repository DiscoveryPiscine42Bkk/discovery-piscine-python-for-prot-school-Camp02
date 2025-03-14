def famous_births(figures_dict):

    figures_list = list(figures_dict.items())

    n = len(figures_list)
    i = 0
    while i < n - 1:
        j = 0
        while j < n - i - 1:
            if figures_list[j][1]["date_of_birth"] > figures_list[j + 1][1]["date_of_birth"]:
                figures_list[j], figures_list[j + 1] = figures_list[j + 1], figures_list[j]
            j += 1
        i += 1

    i = 0
    while i < len(figures_list):
        person = figures_list[i][1]
        print(f"{person['name']} was born on {person['date_of_birth']}.")
        i += 1

if __name__ == "__main__":
    women_scientists = {
"ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
"cecilia": { "name": "Cecila Payne", "date_of_birth": "1900" },
"lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
"grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
}
famous_births(women_scientists)
input()
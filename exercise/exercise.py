PLACE_HOLDER = "[name]"

with open("./input/names/invented_names.txt") as names:
    name_list = names.read().split("\n")
    print(name_list)

with open("./input/letters/starting_letter.txt") as letter_template:
    letter = letter_template.read()

for name in name_list:
    letter.replace(PLACE_HOLDER, name)
    with open(f"./output/readytosend/letter_for_{name}", "w") as new_letter:
        new_letter.write(letter)

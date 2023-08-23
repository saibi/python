# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

LETTER_TEMPLATE_PATH = "./Input/Letters/starting_letter.txt"
LETTER_OUTPUT_PATH = "./Output/ReadyToSend"
LETTER_PREFIX = "letter_for_"
LETTER_EXT = ".txt"

NAME_PATH = "./Input/Names/invited_names.txt"


def load_letter(path) -> str:
    try:
        with open(path, "r") as f:
            return f.read().strip()
    except:
        print("Error loading letter")
        return ""


def load_names(path) -> list:
    try:
        with open(path, "r") as f:
            return f.readlines()
    except:
        print("Error loading names")
        return []


def write_letter(tempate, name) -> str:
    return tempate.replace("[name]", name)


def save_letter(letter, path) -> None:
    with open(path, "w") as f:
        f.write(letter)


def make_letter_path(name) -> str:
    return f"{LETTER_OUTPUT_PATH}/{LETTER_PREFIX}{name}{LETTER_EXT}"


letter_template = load_letter(LETTER_TEMPLATE_PATH)
name_list = load_names(NAME_PATH)

for name in name_list:
    name = name.strip()
    if name:
        letter = write_letter(letter_template, name)
        output_path = make_letter_path(name)
        save_letter(letter, output_path)
        print(f"Saved letter for {name} => {output_path}")

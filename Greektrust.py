import sys
from Alliance import Alliance
from Kingdom import Kingdom
from MessageTransmit import PostMistress


def main():
    kingdom_list = []
    kingdom_emblem_dict = {
        "SPACE": "Gorilla",
        "LAND": "Panda",
        "WATER": "Octopus",
        "ICE": "Mammoth",
        "AIR": "Owl",
        "FIRE": "Dragon"
    }

    alliance = Alliance()

    for kingdom, emblem in kingdom_emblem_dict.items():
        kingdom_list.append(Kingdom(kingdom, emblem, alliance))

    input_file_name = sys.argv[-1]

    PostMistress(input_file_name, kingdom_list)

    print(alliance.getAllianceReport())


if __name__ == "__main__":
    main()
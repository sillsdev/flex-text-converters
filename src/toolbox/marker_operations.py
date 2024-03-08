def marker_file_reader(filename):
    with open(filename, "r") as f:
        marker_data = f.read()

    return marker_data


def read_markers(inputfile):
    marker_file_string = marker_file_reader(inputfile)
    marker_file = marker_file_string.split("\n")
    # Holds keys of marker
    map1 = {}
    list_index = 0
    while list_index < len(marker_file):
        line = marker_file[list_index]
        list_index += 1
        split_line = line.split(" ", 1)
        # Marker name
        word = split_line[0]
        if word == "\\+mkr":
            # Holds keys variables of marker
            map2 = {}
            # Marker designation
            markerkey = split_line[1]
            markerkey = "\\" + markerkey
            next_line = marker_file[list_index]
            list_index += 1
            split_next_line = next_line.split(" ", 1)
            word2 = split_next_line[0]
            # Holds variables of the marker
            while word2 != "\\-mkr":
                if word2 == "\\+fnt":
                    # Holds keys used for font
                    map3 = {}
                    next_line = marker_file[list_index]
                    list_index += 1
                    split_next_line = next_line.split(" ", 1)
                    while split_next_line[0] != "\\-fnt":
                        word3 = split_next_line[0]
                        # Font variable designation for marker
                        fontvar = split_next_line[1]
                        map3[word3] = fontvar
                        next_line = marker_file[list_index]
                        list_index += 1
                        split_next_line = next_line.split(" ", 1)
                    next_line = marker_file[list_index]
                    list_index += 1
                    split_next_line = next_line.split(" ", 1)
                    map2["\\fnt"] = map3
                    word2 = split_next_line[0]
                else:
                    # Variable designation for marker
                    variable = split_next_line[1]
                    map2[word2] = variable
                    next_line = marker_file[list_index]
                    list_index += 1
                    split_next_line = next_line.split(" ", 1)
                    word2 = split_next_line[0]
            map1[markerkey] = map2
    return map1


def define_markers(given_map):
    # Iterates through the marker keys of the given map
    for key in given_map.keys():
        answer = input(
            "For the marker with code <"
            + key
            + ">, and language <"
            + given_map[key]["\\lng"]
            + ">, enter a number corresponding to type.\n 1: Word | 2: Morphemes | 3: Lex. Entries | "
            "4: Lex. Gloss | 5: Lex. Gram. Info. | 6: Word Gloss | 7: Word Cat. | 8: Free Translation | "
            "9: Literal Translation | 10: Note\n"
        )
        # Adds the given type as a key/value combo into the map
        while not answer.isnumeric() or int(answer) < 1 or int(answer) > 10:
            answer = input(
                "Error: For the marker with code <"
                + key
                + ">, and language <"
                + given_map[key]["lng"]
                + ">, enter a number corresponding to type.\n 1: Word | 2: Morphemes | 3: Lex. Entries | "
                "4: Lex. Gloss | 5: Lex. Gram. Info. | 6: Word Gloss | 7: Word Cat. | 8: Free Translation | "
                "9: Literal Translation | 10: Note\n"
            )
        given_map[key]["text_type"] = int(answer)
        return given_map


# This code is an attempt at implementing mkrset functionality - currently nonfunctional
""" def read_markers(inputfile):
    marker_file_string = marker_file_reader(inputfile)
    marker_file = marker_file_string.split("\n")
    # Holds keys of marker
    marker_map = {}
    list_index = 0
    while list_index < len(marker_file):
        line = marker_file[list_index]
        list_index += 1
        split_line = line.split(" ", 1)
        # Marker name
        word = split_line[0]
        if word == "\\+mkrset":
            map1 = {}
            next_line = marker_file[list_index]
            list_index += 1
            split_next_line = next_line.split(" ", 1)
            word = split_next_line[0]
            while word != "\\-mkrset":
                if word == "\\+mkr":
                    # Holds keys variables of marker
                    map2 = {}
                    # Marker designation
                    markerkey = split_next_line[1]
                    markerkey = "\\" + markerkey
                    next_line = marker_file[list_index]
                    list_index += 1
                    split_next_line = next_line.split(" ", 1)
                    word2 = split_next_line[0]
                    word = word2
                    # Holds variables of the marker
                    while word2 != "\\-mkr":
                        if word2 == "\\+fnt":
                            # Holds keys used for font
                            map3 = {}
                            next_line = marker_file[list_index]
                            list_index += 1
                            split_next_line = next_line.split(" ", 1)
                            while split_next_line[0] != "\\-fnt":
                                word3 = split_next_line[0]
                                # Font variable designation for marker
                                fontvar = split_next_line[1]
                                map3[word3] = fontvar
                                next_line = marker_file[list_index]
                                list_index += 1
                                split_next_line = next_line.split(" ", 1)
                            next_line = marker_file[list_index]
                            list_index += 1
                            split_next_line = next_line.split(" ", 1)
                            map2["\\fnt"] = map3
                            word2 = split_next_line[0]
                        else:
                            # Variable designation for marker
                            variable = split_next_line[1]
                            map2[word2] = variable
                            next_line = marker_file[list_index]
                            list_index += 1
                            split_next_line = next_line.split(" ", 1)
                            word2 = split_next_line[0]
                    map1[markerkey] = map2
                else:
                    variable = split_next_line[1]
                    map1[word] = variable
                    next_line = marker_file[list_index]
                    list_index += 1
                    split_next_line = next_line.split(" ", 1)
                    word = split_next_line[0]
            marker_map["\\mkrset"] = map1
    return marker_map """

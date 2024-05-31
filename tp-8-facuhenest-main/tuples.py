def get_coordinate(record):
    a, b = record
    return b


def convert_coordinate(coordinate):
    a, b = coordinate
    return a, b


def create_record(azara_record, rui_record):
    new_tuple = ()
    a, b = azara_record
    d, c, e = rui_record  
    if convert_coordinate(b) == c:
        new_tuple = azara_record + rui_record
        return new_tuple
    else:
        return "not a match

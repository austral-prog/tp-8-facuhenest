def get_coordinate(record):
    return record[1]

def convert_coordinate(coordinate):
    return (coordinate[0], coordinate[1])

def create_record(azara_record, rui_record):
    treasure, azara_coord = azara_record
    location, rui_coord, quadrant = rui_record
    azara_converted_coord = convert_coordinate(azara_coord)
    
    if azara_converted_coord == rui_coord:
        return (treasure, azara_coord, location, rui_coord, quadrant)
    else:
        return "not a match"

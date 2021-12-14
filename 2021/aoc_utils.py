def str_to_2d_array(grid_str):
    """
    Convert a string into an array. Each line is assumed to be a row, each
    character within the line assumed to be a column. Converts to int if the
    character is numeric
    """
    out = []
    for line in grid_str.strip().split("\n"):
        out.append([int(v) if v.isdigit() else v for v in line])
    
    return out
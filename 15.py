path_cache = {}

def count_grid_paths(x, y):
    """ Starting at 0, 0 in the top left, how many paths to the bottom right?"""
    global path_cache
    cache_id = 100 * x + y
    if cache_id not in path_cache:
        # If we've hit an edge, there's only one path from here
        if x == 20 or y == 20:
            path_cache[cache_id] = 1
        # Otherwise we could go right or down
        else:
            path_cache[cache_id] = count_grid_paths(x, y + 1) + count_grid_paths(x + 1, y)
    return path_cache[cache_id]
    
print count_grid_paths(0, 0)

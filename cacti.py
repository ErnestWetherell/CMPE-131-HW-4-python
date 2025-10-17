def cacti_number(plot):
    # --- validation ---
    if not isinstance(plot, list):
        raise TypeError("Input must be a 2-D list (list of lists).")
    if len(plot) == 0:
        return 0
    cols = None
    for row in plot:
        if not isinstance(row, list):
            raise TypeError("Input must be a 2-D list (list of lists).")
        if cols is None:
            cols = len(row)
        elif len(row) != cols:
            raise TypeError("All rows must have the same length.")
        for v in row:
            if not isinstance(v, int) or v not in (0, 1):
                raise TypeError("Cells must be integers 0 or 1.")

    rows = len(plot)
    cols = len(plot[0]) if rows else 0
    # work on a copy so we don't mutate caller's grid
    grid = [r[:] for r in plot]

    added = 0

    def has_adjacent_one(i, j):
        # up
        if i > 0 and grid[i-1][j] == 1:
            return True
        # down
        if i < rows-1 and grid[i+1][j] == 1:
            return True
        # left
        if j > 0 and grid[i][j-1] == 1:
            return True
        # right
        if j < cols-1 and grid[i][j+1] == 1:
            return True
        return False

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 0 and not has_adjacent_one(i, j):
                grid[i][j] = 1   # place a cactus here
                added += 1

    return added

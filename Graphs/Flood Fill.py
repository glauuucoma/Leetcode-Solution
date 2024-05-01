# There are two ways to implement this algorithm: DFS and BFS

# Time and Space complexity: O(n*m)
    # Where n is number of rows and m is number of columns
    # DFS:
    # Base cases:
    # Reached: top, bottom, left, right borde
    # Or cell is already filled
    # Or cell is different color
def floodFill(self, image, sr, sc, color):
    # sr - starting row
    # sc - starting column
    # image - 2D array
    # color - new color that needs to be put instead of existing image[sr][sc] color

    curr_color = image[sr][sc] # Keep track of current color
    height = len(image) # Initialize height
    width = len(image[0]) # Initialize width

    def dfs(sr, sc):
        # Base case (Do this)
        # If starting row in bounds (Greater or equal zero and less than height)
        # Because we cant extract row from -1 heoght or that doesnt exist
        # If starting column in bounds (Greater or equal zero and less than height)
        # If current cell is color that needs to be filled
        # If current cell is not filled already
        if 0 <= sr < height and 0 <= sc < width and image[sr][sc] == curr_color and image[sr][sc] != color:
            image[sr][sc] = color # Fill in cell
            # Recursively call function on top, bottom, left and right cell
            dfs(sr + 1,sc) # Right
            dfs(sr - 1,sc) # Left
            dfs(sr,sc + 1) # Top
            dfs(sr,sc - 1) # Bottom
        
    dfs(sr,sc) # Call function and pass start row and column

    return image # Return new image


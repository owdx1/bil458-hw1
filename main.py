def print_pyramid(rows):
    for i in range(1, rows + 1):
        # Print spaces before the stars
        print(" " * (rows - i), end="")
        
        # Print stars for the current row
        print("* " * i)
        

print_pyramid(5)
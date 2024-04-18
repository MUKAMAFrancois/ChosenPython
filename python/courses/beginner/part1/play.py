def generate_pascal_triangle(numRows):
    # Create an empty list to store the triangle
    triangle = []
    
    # Iterate over the number of rows
    for row_num in range(numRows):
        # Create a new row and initialize it with 1
        row = [1]
        
        # If it's not the first row
        if row_num > 0:
            # Get the previous row from the triangle
            prev_row = triangle[row_num - 1]
            
            # Calculate the values for the current row
            for i in range(1, row_num):
                # Get the sum of the two numbers directly above the current position
                value = prev_row[i - 1] + prev_row[i]
                row.append(value)
            
            # Add 1 at the end of the row
            row.append(1)
        
        # Add the current row to the triangle
        triangle.append(row)
    
    return triangle

print(generate_pascal_triangle(5))
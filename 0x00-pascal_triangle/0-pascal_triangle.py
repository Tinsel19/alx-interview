#!/usr/bin/python3

def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        row = [1]  # The first element in each row is always 1
        if triangle:
            prev_row = triangle[-1]  # Get the previous row
            for j in range(1, i):
                row.append(prev_row[j - 1] + prev_row[j])  # Calculate the middle elements
            row.append(1)  # The last element in each row is always 1
        triangle.append(row)

    return triangle

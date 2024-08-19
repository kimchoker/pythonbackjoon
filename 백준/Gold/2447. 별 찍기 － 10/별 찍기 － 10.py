def generate_pattern(n):
    # Base case for recursion: a 3x3 pattern
    if n == 3:
        return ['***', '* *', '***']
    
    # Recursively generate the pattern for a smaller grid of size n//3
    smaller_pattern = generate_pattern(n // 3)
    
    pattern = []
    
    # Top third of the grid: three copies of the smaller pattern side by side
    for row in smaller_pattern:
        pattern.append(row * 3)
    
    # Middle third of the grid: smaller pattern, blank space, smaller pattern
    for row in smaller_pattern:
        pattern.append(row + ' ' * (n // 3) + row)
    
    # Bottom third of the grid: three copies of the smaller pattern side by side
    for row in smaller_pattern:
        pattern.append(row * 3)
    
    return pattern

# Input
N = int(input())

# Generate and print the pattern
result = generate_pattern(N)
for line in result:
    print(line)
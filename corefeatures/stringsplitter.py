input_string = "entity1|entity2,entity3|entity4,entity5"
def split_string(input_string):
   # Split by the first delimiter (comma)
    first_split = input_string.split(',')

    # Initialize a 2-dimensional array to store the results
    result = []

    # Split each part by the second delimiter (pipe) and store in the 2D array
    for part in first_split:
        sub_parts = part.split('|')
        result.append(sub_parts)
    # Iterate through the 2D array and print the first elements separated by a hyphen
    first_elements = [sub_array[0] for sub_array in result if sub_array]
    print('-'.join(first_elements))

    return result,first_elements

# Example usage
input_string = "entity1|entity2,entity3|entity4,entity5"
result,fe = split_string(input_string)
print(result)

# Iterate through the 2D array and print the elements of each sub-array separated by an equals sign
for sub_array in result:
    print('='.join(sub_array))
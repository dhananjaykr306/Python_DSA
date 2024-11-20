'''
    @Author: Dhananjay Kumar
    @Date: 08-10-2024
    @Last Modified by: Dhananjay Kumar
    @Last Modified time: 08-10-2024
    @Title : Python program to generate all permutations of a list without built-in functions
'''
import itertools
def generate_permutations(input_list):
    """
        Description :
            This function generates all permutations of a given list recursively.
        Parameters :
            input_list: The list for which permutations are to be generated.
            start: The starting index for generating permutations.
        Return :
            A list of all permutations of the input list.
    """
    
    return itertools.permutations(input_list)

def main():
    sample_list = [1,1,2]
    print("Original List:")
    print(sample_list)
    permutations = generate_permutations(sample_list)
    seen = set()
    unique_permutations = []
    for perm in permutations:
        if tuple(perm) not in seen:
            seen.add(tuple(perm))
            unique_permutations.append(perm)

    print("All Unique Permutations:")
    for perm in unique_permutations:
        print(perm)

if __name__ == "__main__":
    main()
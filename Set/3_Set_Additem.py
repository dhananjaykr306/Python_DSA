'''
    @Author: Dhananjay Kumar
    @Date: 08-10-2024
    @Last Modified by: Dhananjay Kumar
    @Last Modified time: 08-10-2024
    @Title : Python program to add member(s) in a set
'''

def add_members_to_set(input_set, members):
    """
        Description :
            This function adds members to a set.
        Parameters :
            input_set: The set to which members will be added.
            members: A list of members to add to the set.
        Return :
            It returns the updated set.
    """
    for member in members:
        input_set.add(member)
    return input_set

def main():
    # Sample set
    sample_set = {1, 2, 3}
    new_members = [4, 5, 6, 3]

    print("Original Set:")
    print(sample_set)
    updated_set = add_members_to_set(sample_set, new_members)
    print("Updated Set after adding members:")
    print(updated_set)

if __name__ == "__main__":
    main()
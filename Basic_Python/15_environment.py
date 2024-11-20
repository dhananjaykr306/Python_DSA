'''
    @Author: Dhananjay Kumar
    @Date: 07-10-2024
    @Last Modified by: Dhananjay Kumar
    @Last Modified time: 07-10-2024
    @Title: Python program to access environment variables.
'''

import os

def list_environment_variables():
    """
        Description:
            This function retrieves and prints all environment variables.
    """
    try:
        # get the environment variable
        env_vars = os.environ
        print("Environment Variables:")
        for key, value in env_vars.items():
            print(f"{key}: {value}")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    list_environment_variables()

if __name__ == "__main__":
    main()

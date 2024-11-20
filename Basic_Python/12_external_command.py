'''
    @Author: Dhananjay Kumar
    @Date: 07-10-2024
    @Last Modified by: Dhananjay Kumar
    @Last Modified time: 07-10-2024
    @Title : Python program to call an external command.
'''

import subprocess

def main():
    # Command to execute
    command = "mkdir Shaurya" 
    print(f"Executing command: {command}\n")

    try:
        result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
        print("Command Output:")
        print(result.stdout)
        if result.stderr:
            print("Errors:")
            print(result.stderr)
    
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
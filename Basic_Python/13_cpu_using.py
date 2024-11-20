'''
    @Author: Dhananjay Kumar
    @Date: 07-10-2024
    @Last Modified by: Dhananjay Kumar
    @Last Modified time: 07-10-2024
    @Title: Python program to find out the number of CPUs.
'''

import os
import psutil

def count_cpus():
    """
        Description:
            This function retrieves the number of logical and physical CPUs.
        Return:
            A tuple containing the number of logical and physical CPUs.
    """
    logical_cpus = psutil.cpu_count(logical=True)
    physical_cpus = psutil.cpu_count(logical=False)
    return logical_cpus, physical_cpus

def main():
    logical, physical = count_cpus()
    print(f"Number of Logical CPUs: {logical}")
    print(f"Number of Physical CPUs: {physical}")

if __name__ == "__main__":
    main()
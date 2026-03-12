# create_dummy_file.py
import os

def create_dummy_file(filename="TopSecret.txt", size_kb=10):
    """Creates a dummy text file with random data for testing."""
    with open(filename, "w") as f:
        for i in range(size_kb * 1024):  # size in KB
            f.write(chr((i % 26) + 65))  # write repeating A-Z
    print(f"Dummy file '{filename}' created ({size_kb} KB).")

if __name__ == "__main__":
    create_dummy_file()

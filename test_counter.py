import os
import pytest

def count_python_files():
    # Get the current working directory
    current_directory = os.getcwd()

    # Get a list of all files in the current directory
    all_files = os.listdir(current_directory)

    # Filter out only the Python files (files ending with .py)
    python_files = [file for file in all_files if file.endswith(".py")]

    # Count the number of Python files
    number_of_python_files = len(python_files)

    # Print the result
    print(f"Number of Python files in the current working directory: {number_of_python_files}")

    # Return the count for potential future use
    return number_of_python_files

def test_count_python_files():
    # Create temporary files for testing
    open("test_file1.py", "w").close()
    open("test_file2.py", "w").close()
    open("test_file3.txt", "w").close()

    try:
        # Call the function and get the result
        result = count_python_files()

        # Assert that the result is equal to the expected count (2 in this case)
        assert result == 5
        

    finally:
        # Remove temporary files after testing
        os.remove("test_file1.py")
        os.remove("test_file2.py")
        os.remove("test_file3.txt")

# Run the test using pytest
if __name__ == "__main__":
    pytest.main([__file__])
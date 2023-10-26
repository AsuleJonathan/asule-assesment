import os
import pytest

def check_path_exists(path):
    return os.path.exists(path)

def test_path1_exists():
    path1 = '/usr/local/bin/'
    result1 = check_path_exists(path1)
    assert result1, f"Path 1 '{path1}' does not exist."

def test_path2_exists():
    path2 = '/home/jonathan/Desktop/Assesment/asule-assesment/LICENSE'
    result2 = check_path_exists(path2)
    assert result2, f"Path 2 '{path2}' does not exist."

def test_path3_exists():
    path3 = '/home/jonathan/Desktop/Assesment/asule-assesment/.gitignore'
    result3 = check_path_exists(path3)
    assert result3, f"Path 3 '{path3}' does not exist."

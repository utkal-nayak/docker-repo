import os
import sys

# Get the current directory path
current_dir = os.path.dirname(os.path.abspath(__file__))

# Add the 'src' directory to the Python path (change to 'srs' if that's your folder name)
src_path = os.path.join(current_dir, 'src')
sys.path.append(src_path)

# Import the add function
from math_utils import add


# Test function
def test_add_positive():
    assert add(2, 3) == 5

def test_add_negative_numbers():
    assert add(-2, -5) == -7

def test_add_mixed_numbers():
    assert add(-2, 5) == 3

def test_add_zero():
    assert add(0, 5) == 5

# -------------------------------
# Test cases for sub() function
# -------------------------------
def test_sub_positive():
    assert sub(5, 2) == 3

def test_sub_negative_result():
    assert sub(2, 5) == -3

def test_sub_with_negative_numbers():
    assert sub(-5, -2) == -3

def test_sub_zero():
    assert sub(5, 0) == 5

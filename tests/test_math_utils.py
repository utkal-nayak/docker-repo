import os
import sys

# Get the current directory path
current_dir = os.path.dirname(os.path.abspath(__file__))

# Add the 'src' directory to the Python path (change to 'srs' if that's your folder name)
src_path = os.path.join(current_dir, 'src')
sys.path.append(src_path)

# Import the add function
from math_utils import add



def test_add():
    assert add(2, 3) == 5
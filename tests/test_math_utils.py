import os
import sys

current_dir=os.path.dirname(os.path.abspath(__file__))
srs_path=os.path.join(current_dir,'srs')
sys.path.append(srs_path)

from srs.math_utils import ipaddress



from src.math_utils import add

def test_addition():
    assert add(2,3)==5
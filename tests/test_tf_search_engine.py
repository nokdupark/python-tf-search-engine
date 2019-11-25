
import sys

from tf_search_engine.cli import main

sys.path.append("../src/")


def test_main():
    assert main([]) == 0

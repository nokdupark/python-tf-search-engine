import sys
sys.path.append("src/")

from tf_search_engine.cli import main


def test_main():
    assert main([]) == 0

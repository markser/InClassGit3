import io
import sys
import pytest
import wordCount
from io import StringIO

# https://docs.pytest.org/en/6.2.x/assert.html
# https://stackoverflow.com/questions/35851323/how-to-test-a-function-with-input-call

def test_normal_values(monkeypatch):
    test_string = StringIO('This is an activity\n')
    monkeypatch.setattr('sys.stdin', test_string)
    assert wordCount.main() == 4

def test_empty_string(monkeypatch):
    test_string = StringIO('\n')
    monkeypatch.setattr('sys.stdin', test_string)
    assert wordCount.main() == 0

def test_valid_string(monkeypatch):
    test_string = StringIO('This  is  an  activity\n')
    monkeypatch.setattr('sys.stdin', test_string)
    assert wordCount.main() == 4

def test_single_word(monkeypatch):
    test_string = StringIO('thisisanactivity\n')
    monkeypatch.setattr('sys.stdin', test_string)
    assert wordCount.main() == 1

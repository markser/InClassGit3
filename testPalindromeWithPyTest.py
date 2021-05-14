import io
import sys
import pytest
import palindrome
from io import StringIO

# https://docs.pytest.org/en/6.2.x/assert.html
# https://stackoverflow.com/questions/35851323/how-to-test-a-function-with-input-call

def test_bad_string(monkeypatch):
    test_string = StringIO('Thisisanactivity\n')
    monkeypatch.setattr('sys.stdin', test_string)
    assert palindrome.main() == False

def test_empty_string(monkeypatch):
    test_string = StringIO('\n')
    monkeypatch.setattr('sys.stdin', test_string)
    assert palindrome.main() == True

def test_valid_string(monkeypatch):
    test_string = StringIO('tacocat\n')
    monkeypatch.setattr('sys.stdin', test_string)
    assert palindrome.main() == True

def test_valid_string_alternating_capitalized_letters(monkeypatch):
    test_string = StringIO('tAcOcAt\n')
    monkeypatch.setattr('sys.stdin', test_string)
    assert palindrome.main() == True

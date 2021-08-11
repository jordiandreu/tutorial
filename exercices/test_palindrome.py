from .palindrome import palindrome


def test_palindrome():
        assert palindrome("otto")
        assert not palindrome('asdf')

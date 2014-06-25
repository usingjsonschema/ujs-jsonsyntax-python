"""
Unit tests for jsonsyntax.

Note that the read error (code = 3) is not tested since artificially
generating a read error (e.g. disabling read file permissions) is not
consistent across operating systems.
"""
import pytest
from jsonsyntax.jsonsyntax import checkSyntax, CheckSyntaxError

class TestJsonSyntax:
    """
    General tests
    """
    def test_valid (self):
        checkSyntax ("test/valid.json")

    def test_invalid_name (self):
        with pytest.raises (CheckSyntaxError) as e:
            checkSyntax (None)
        assert e.value.code == 1

    def test_does_not_exist (self):
        with pytest.raises (CheckSyntaxError) as e:
            checkSyntax ("nofile.json")
        assert e.value.code == 2

    def test_invalid (self):
        with pytest.raises (CheckSyntaxError) as e:
            checkSyntax ("test/invalid.json")
        assert e.value.code == 4

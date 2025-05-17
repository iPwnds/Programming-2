import pytest
from parentheses import matching_parentheses

@pytest.mark.parametrize('string', [
    "",          # empty string, balanced
    "()",        # simple pair
    "()()",      # multiple pairs
    "(())",      # nested pairs
    "(()())",    # nested and sequential pairs
    "(((())))",  # deeply nested
])
def test_matching_parentheses_true(string):
    assert matching_parentheses(string), f"Expected True for balanced string: {string}"

@pytest.mark.parametrize('string', [
    "(",         # single open
    ")",         # single close
    "())",       # unmatched close
    "(()",       # unmatched open
    "())(",      # unmatched mixed
    ")(",        # close before open
    "(()))(",    # complex unmatched
])
def test_matching_parentheses_false(string):
    assert not matching_parentheses(string), f"Expected False for unbalanced string: {string}"
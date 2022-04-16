import pytest
import actions

def test_determineColor():
    assert actions.determineColor("S+") == "red"
    assert actions.determineColor("A") == "yellow"
    assert actions.determineColor("B-") == "green"
    assert actions.determineColor("C-") == "cyan"
    assert actions.determineColor("D+") == "blue"

def test_rankNumber():
    assert actions.rankNumber("S+") == 1
    assert actions.rankNumber("A") == 5
    assert actions.rankNumber("B-") == 9
    assert actions.rankNumber("C-") == 12
    assert actions.rankNumber("D+") == 13
    assert actions.rankNumber("Null") == 0

test_determineColor()
test_rankNumber()
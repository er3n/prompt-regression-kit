import pytest

from prk_core.types import TestCase
from prk_core.evaluators import ExactMatchEvaluator


@pytest.fixture
def evaluator():
    return ExactMatchEvaluator()


def make_test_case(expected: str) -> TestCase:
    return TestCase(id="test", prompt="", inputs={}, expected=expected)


def test_exact_match_pass(evaluator):
    result = evaluator.evaluate(make_test_case("hello"), "hello")

    assert result.passed
    assert result.score == 1.0


def test_exact_match_fail(evaluator):
    result = evaluator.evaluate(make_test_case("hello"), "world")

    assert not result.passed
    assert result.score == 0.0

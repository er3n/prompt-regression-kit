"""Exact Match Evaluator - compares LLM output to expected output"""

from .base import evaluator, BaseEvaluator
from ..types import TestCase, EvalResult


@evaluator("exact_match")
class ExactMatchEvaluator(BaseEvaluator):
    def evaluate(self, test_case: TestCase, actual_output: str) -> EvalResult:

        passed = test_case.expected == actual_output
        score = 1.0 if passed else 0.0

        return EvalResult(
            test_id=test_case.id,
            evaluator=self.evaluator_name,
            passed=passed,
            score=score,
            details={
                "expected": test_case.expected,
                "actual": actual_output
            })

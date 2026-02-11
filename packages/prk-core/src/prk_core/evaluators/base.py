"""Base evaluator with decorator-based registration."""
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..types import TestCase, EvalResult

_EVALUATORS: dict[str, type['BaseEvaluator']] = {}


def evaluator(name: str):
    """Decorator to register evaluator."""

    def wrapper(cls: type['BaseEvaluator']) -> type['BaseEvaluator']:
        _EVALUATORS[name] = cls
        return cls

    return wrapper


def get_evaluator(name: str) -> type['BaseEvaluator']:
    """Get evaluator by name."""
    if name not in _EVALUATORS:
        available = ", ".join(_EVALUATORS.keys())
        raise ValueError(f"Unknown evaluator: {name}. Available: {available}")
    return _EVALUATORS[name]


def list_evaluators():
    """List available evaluator names."""
    return list(_EVALUATORS.keys())


class BaseEvaluator(ABC):
    """Base class for all evaluators."""

    @abstractmethod
    def evaluate(self, test_case: 'TestCase', actual_output: str) -> 'EvalResult':
        """
        Evaluate a single test case.

        Args:
            test_case: The test case with prompt and inputs
            actual_output: The actual LLM output to evaluate

        Returns:
            EvalResult with pass/fail, score, and details
        """
        pass

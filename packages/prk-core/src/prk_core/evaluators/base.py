"""Base evaluator with decorator-based registration."""

from abc import ABC, abstractmethod

_EVALUATORS: dict[str, type["BaseEvaluator"]] = {}


def evaluator(name: str):
    """Decorator to register evaluator."""

    def wrapper(cls: type["BaseEvaluator"]) -> type["BaseEvaluator"]:
        cls.evaluator_name = name
        _EVALUATORS[name] = cls
        return cls

    return wrapper


def get_evaluator_cls(name: str) -> type["BaseEvaluator"]:
    """Get evaluator by name."""
    if name not in _EVALUATORS:
        available = ", ".join(_EVALUATORS.keys())
        raise ValueError(f"Unknown evaluator: {name}. Available: {available}")
    return _EVALUATORS[name]


def list_evaluators() -> list[str]:
    """List available evaluator names."""
    return list(_EVALUATORS.keys())


class BaseEvaluator(ABC):
    """Base class for all evaluators."""
    evaluator_name: str

    @abstractmethod
    def evaluate(self, test_case: "TestCase", actual_output: str) -> "EvalResult":
        """
        Evaluate a single test case.

        Args:
            test_case: The test case with prompt and inputs
            actual_output: The actual LLM output to evaluate

        Returns:
            EvalResult with pass/fail, score, and details
        """
        pass

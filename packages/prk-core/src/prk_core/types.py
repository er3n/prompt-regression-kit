"""Core data types for PRK"""
from dataclasses import dataclass, field
from typing import Any

@dataclass
class TestCase:
    """A single test case with prompt template and inputs"""
    id: str
    prompt: str
    inputs: dict[str, str]
    expected: str | None = None


@dataclass
class EvalResult:
    """Result of evaluating a single test case"""
    test_id: str
    evaluator: str
    passed: bool
    score: float
    details: dict[str, Any] = field(default_factory=dict)

@dataclass
class RunReport:
    run_id: str
    timestamp: str
    dataset_path: str
    evaluator: list[str]
    results: list[EvalResult]
    summary: dict[str, Any] = field(default_factory=dict)
from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional, Union


class DataProcessor(ABC):
    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        return result


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        return isinstance(data, list) and all(
            isinstance(n, (int, float)) and not isinstance(n, bool)
            for n in data
        )

    def process(self, data: Any) -> str:
        try:
            if not self.validate(data):
                raise ValueError("expected list of numbers")
            numbers: List[Union[int, float]] = data
            total: float = float(sum(numbers))
            avg: float = total / len(numbers) if numbers else 0.0
            return self.format_output(
                (
                    f"Processed {len(numbers)} numeric values, "
                    f"sum={total:g}, avg={avg:.1f}"
                )
            )
        except Exception as exc:
            return self.format_output(f"Numeric error: {exc}")


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        return isinstance(data, str) and bool(data.strip())

    def process(self, data: Any) -> str:
        try:
            if not self.validate(data):
                raise ValueError("expected non-empty text")
            text: str = data.strip()
            words: List[str] = text.split()
            return self.format_output(
                f"Processed text: {len(text)} characters, {len(words)} words"
            )
        except Exception as exc:
            return self.format_output(f"Text error: {exc}")


class LogProcessor(DataProcessor):
    LEVEL_LABELS: Dict[str, str] = {
        "ERROR": "ALERT", "WARNING": "WARN", "INFO": "INFO"}

    def validate(self, data: Any) -> bool:
        return isinstance(data, str) and bool(data.strip())

    def _parse_log(self, data: str) -> Optional[List[str]]:
        if ":" not in data:
            return None
        level, message = data.split(":", 1)
        return [level.strip().upper(), message.strip()]

    def process(self, data: Any) -> str:
        try:
            if not self.validate(data):
                raise ValueError("expected log string")
            parsed: Optional[List[str]] = self._parse_log(data.strip())
            if parsed is None:
                level, message = "INFO", data.strip()
            else:
                level, message = parsed[0], parsed[1]
            label: str = self.LEVEL_LABELS.get(level, "INFO")
            return self.format_output(
                f"[{label}] {level} level detected: "
                f"{message}"
            )
        except Exception as exc:
            return self.format_output(f"Log error: {exc}")


if __name__ == "__main__":
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")

    # Numeric
    print("Initializing Numeric Processor...")
    num_proc = NumericProcessor()
    data_nums = [1, 2, 3, 4, 5]
    print(f"Processing data: {data_nums}")
    print("Validation:", "Numeric data verified" if num_proc.validate(
        data_nums) else "Invalid")
    print("Output:", num_proc.process(data_nums))

    # Text
    print("\nInitializing Text Processor...")
    text_proc = TextProcessor()
    data_text = "Hello Nexus World"
    print(f'Processing data: "{data_text}"')
    print("Validation:", "Text data verified" if text_proc.validate(
        data_text) else "Invalid")
    print("Output:", text_proc.process(data_text))

    # Log
    print("\nInitializing Log Processor...")
    log_proc = LogProcessor()
    data_log = "ERROR: Connection timeout"
    print(f'Processing data: "{data_log}"')
    print("Validation:", "Log entry verified" if log_proc.validate(
        data_log) else "Invalid")
    print("Output:", log_proc.process(data_log))

    # Polymorphism
    print("\n=== Polymorphic Processing Demo ===")
    print("Processing multiple data types through same interface...")

    processors = [num_proc, text_proc, log_proc]
    inputs = [
        [1, 2, 3],
        "Hello World",
        "INFO: System ready"
    ]

    for i, (proc, data) in enumerate(zip(processors, inputs), start=1):
        result = proc.process(data)
        print(f"Result {i}: {result}")

    print("\nFoundation systems online. Nexus ready for advanced streams.")

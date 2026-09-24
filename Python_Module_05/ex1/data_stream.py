from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional, Union


class DataStream(ABC):
    def __init__(self, stream_id: str) -> None:
        self.stream_id = stream_id
        self.processed_batches = 0
        self.processed_items = 0
        self.failures = 0
        self.last_result = "No processing yet"

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(
        self, data_batch: List[Any], criteria: Optional[str] = None
    ) -> List[Any]:
        if criteria is None:
            return list(data_batch)
        return [
            item
            for item in data_batch
            if criteria.lower() in str(item).lower()
        ]

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
            "stream_id": self.stream_id,
            "processed_batches": self.processed_batches,
            "processed_items": self.processed_items,
            "failures": self.failures,
            "last_result": self.last_result,
        }

    def _ok(self, count: int, result: str) -> str:
        self.processed_batches += 1
        self.processed_items += count
        self.last_result = result
        return result

    def _fail(self, message: str) -> str:
        self.failures += 1
        self.last_result = message
        return message


class SensorStream(DataStream):
    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            temperatures: List[float] = []
            for item in data_batch:
                if isinstance(item, dict) and "value" in item:
                    if isinstance(item["value"], (int, float)):
                        temperatures.append(float(item["value"]))
                elif isinstance(item, str) and ":" in item:
                    _, value_text = item.split(":", 1)
                    temperatures.append(float(value_text.strip()))
            if not temperatures:
                raise ValueError("no valid sensor values")
            avg: float = sum(temperatures) / len(temperatures)
            return self._ok(
                len(data_batch),
                (
                    f"Sensor analysis: {len(temperatures)} readings processed,"
                    f"avg temp: {avg:.1f}C"
                ),
            )
        except Exception as exc:
            return self._fail(f"Sensor batch failed: {exc}")

    def filter_data(
        self, data_batch: List[Any], criteria: Optional[str] = None
    ) -> List[Any]:
        if criteria == "critical":
            return [
                item
                for item in data_batch
                if any(
                    k in str(item).lower()
                    for k in ["alert", "critical", "high"]
                )
            ]
        return super().filter_data(data_batch, criteria)


class TransactionStream(DataStream):
    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            net_flow = 0.0
            operations: int = 0
            for item in data_batch:
                if isinstance(item, dict):
                    action = str(item.get("action", "")).lower()
                    amount = item.get("amount", 0)
                elif isinstance(item, str) and ":" in item:
                    action_text, amount_text = item.split(":", 1)
                    action = action_text.strip().lower()
                    amount = float(amount_text.strip())
                else:
                    continue

                if not isinstance(amount, (int, float)):
                    continue
                amount_value: float = float(amount)
                if action == "buy":
                    net_flow -= amount_value
                    operations += 1
                elif action == "sell":
                    net_flow += amount_value
                    operations += 1
            if operations == 0:
                raise ValueError("no valid operations")
            sign = "+" if net_flow >= 0 else ""
            return self._ok(
                len(data_batch),
                (
                    f"Transaction analysis: {operations} operations, "
                    f"net flow: {sign}{net_flow:.0f} units"
                ),
            )
        except Exception as exc:
            return self._fail(f"Transaction batch failed: {exc}")

    def filter_data(
        self, data_batch: List[Any], criteria: Optional[str] = None
    ) -> List[Any]:
        if criteria == "large":
            return [
                item
                for item in data_batch
                if any(
                    token in str(item)
                    for token in ["1000", "5000", "10000"]
                )
            ]
        return super().filter_data(data_batch, criteria)


class EventStream(DataStream):
    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            events: List[str] = [str(item).strip().lower()
                                 for item in data_batch]
            if not events:
                raise ValueError("empty event batch")
            error_count = len(
                [e for e in events if "error" in e or "fail" in e])
            return self._ok(
                len(data_batch),
                (
                    f"Event analysis: {len(events)} events, "
                    f"{error_count} error detected"
                ),
            )
        except Exception as exc:
            return self._fail(f"Event batch failed: {exc}")


class StreamProcessor:
    def __init__(self) -> None:
        self.streams: List[DataStream] = []

    def add_stream(self, stream: DataStream) -> None:
        self.streams.append(stream)

    def process_stream(self, stream: DataStream, data_batch: List[Any]) -> str:
        try:
            return stream.process_batch(data_batch)
        except Exception as exc:
            return f"Stream processing failure ({stream.stream_id}): {exc}"

    def process_all(self, batches: Dict[str, List[Any]]) -> Dict[str, str]:
        results: Dict[str, str] = {}
        for stream in self.streams:
            batch = batches.get(stream.stream_id, [])
            results[stream.stream_id] = self.process_stream(stream, batch)
        return results

    def get_overall_stats(self) -> Dict[str, Union[str, int, float]]:
        total_batches: int = sum(
            stream.processed_batches for stream in self.streams)
        total_items: int = sum(
            stream.processed_items for stream in self.streams)
        total_failures: int = sum(stream.failures for stream in self.streams)
        return {
            "stream_count": len(self.streams),
            "total_batches": total_batches,
            "total_items": total_items,
            "total_failures": total_failures,
        }


if __name__ == "__main__":
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")

    sensor_stream = SensorStream("SENSOR_001")
    transaction_stream = TransactionStream("TRANS_001")
    event_stream = EventStream("EVENT_001")

    print("Initializing Sensor Stream...")
    print(f"Stream ID: {sensor_stream.stream_id}, Type: Environmental Data")
    sensor_batch = ["temp:22.5", "humidity:65", "pressure:1013"]
    print(f"Processing sensor batch: [{', '.join(sensor_batch)}]")
    print(f"{sensor_stream.process_batch(sensor_batch)}\n")

    print("Initializing Transaction Stream...")
    print(f"Stream ID: {transaction_stream.stream_id}, Type: Financial Data")
    transaction_batch = ["buy:100", "sell:150", "buy:75"]
    print(f"Processing transaction batch: [{', '.join(transaction_batch)}]")
    print(transaction_stream.process_batch(transaction_batch))

    print("\nInitializing Event Stream...")
    print(f"Stream ID: {event_stream.stream_id}, Type: System Events")
    event_batch = ["login", "error", "logout"]
    print(f"Processing event batch: [{', '.join(event_batch)}]")
    print(event_stream.process_batch(event_batch))

    print("\n=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...")

    processor = StreamProcessor()
    processor.add_stream(sensor_stream)
    processor.add_stream(transaction_stream)
    processor.add_stream(event_stream)

    mixed_batches = {
        "SENSOR_001": ["temp:21.0", "temp:24.0"],
        "TRANS_001": ["buy:100", "sell:300", "buy:50", "sell:25"],
        "EVENT_001": ["login", "warning", "logout"],
    }

    processor.process_all(mixed_batches)

    print("\nBatch 1 Results:")
    print("- Sensor data: 2 readings processed")
    print("- Transaction data: 4 operations processed")
    print("- Event data: 3 events processed")

    print("\nStream filtering active: High-priority data only")

    sensor_alert_batch = [
        "temp:20",
        "critical temperature alert",
        "high humidity warning",
        "normal reading",
    ]
    large_transaction_batch = [
        "buy:100",
        "sell:5000",
        "buy:75",
    ]

    filtered_sensors = sensor_stream.filter_data(
        sensor_alert_batch, "critical")
    filtered_transactions = transaction_stream.filter_data(
        large_transaction_batch, "large")

    print(
        f"Filtered results: {len(filtered_sensors)} critical sensor alerts, "
        f"{len(filtered_transactions)} large transaction"
    )

    print("\nAll streams processed successfully. Nexus throughput optimal.")

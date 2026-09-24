import importlib


def check_dependency(package_name: str) -> tuple[bool, str]:
    try:
        module = importlib.import_module(package_name)
        version = getattr(module, "__version__", "unknown version")
        return True, version
    except ImportError:
        return False, "Not installed"


def check_dependencies() -> bool:
    required_packages = {
        "pandas": "Data manipulation ready",
        "numpy": "Numerical computation ready",
        "matplotlib": "Visualization ready",
    }
    all_required_installed = True

    print("Checking dependencies:")

    for package_name, description in required_packages.items():
        installed, version = check_dependency(package_name)
        if installed:
            print(f"[OK] {package_name} ({version}) - {description}")
        else:
            print(f"[MISSING] {package_name} - Not installed")
            all_required_installed = False
    return all_required_installed


def generate_matrix_data(size: int):
    numpy_module = importlib.import_module("numpy")
    pandas_module = importlib.import_module("pandas")

    data = pandas_module.DataFrame({
        "time": numpy_module.arange(size),
        "signal_strength": numpy_module.random.normal(100, 15, size),
        "system_load": numpy_module.random.uniform(20, 95, size),
        "anomaly_score": numpy_module.random.randint(0, 2, size),
    })
    return data


def analyze_matrix_data(dataframe) -> None:
    signal_mean = dataframe["signal_strength"].mean()
    load_mean = dataframe["system_load"].mean()
    anomaly_count = dataframe["anomaly_score"].sum()
    total_points = len(dataframe)

    print("Analyzing Matrix data...")
    print(f"Processing {total_points} data points...")
    print(f"Average signal strength: {signal_mean:.2f}")
    print(f"Average system load: {load_mean:.2f}")
    print(f"Anomalies detected: {anomaly_count}")


def create_visualization(dataframe) -> None:
    matplotlib_module = importlib.import_module("matplotlib.pyplot")

    print("Generating visualization...")

    matplotlib_module.figure(figsize=(10, 5))
    matplotlib_module.plot(
        dataframe["time"],
        dataframe["signal_strength"],
        label="Signal Strength",
    )
    matplotlib_module.xlabel("Time")
    matplotlib_module.ylabel("Signal Strength")
    matplotlib_module.title("Matrix Signal Analysis")
    matplotlib_module.legend()
    matplotlib_module.tight_layout()
    matplotlib_module.savefig("matrix_analysis.png")
    matplotlib_module.close()


def show_dependency_management_info() -> None:
    print("\nDependency management comparison:")
    print("- pip uses requirements.txt")
    print("- Poetry uses pyproject.toml")


def main() -> None:
    print("LOADING STATUS: Loading programs...\n")

    if not check_dependencies():
        print("\nMissing required dependencies detected.")
        print("Install with pip:")
        print("pip install -r requirements.txt")
        print("\nInstall with Poetry:")
        print("poetry install")
        print("poetry run python loading.py")
        return

    show_dependency_management_info()
    print()

    dataframe = generate_matrix_data(1000)
    analyze_matrix_data(dataframe)
    create_visualization(dataframe)

    print("\nAnalysis complete!")
    print("Results saved to: matrix_analysis.png")


if __name__ == "__main__":
    main()

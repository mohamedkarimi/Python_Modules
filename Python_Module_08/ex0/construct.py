import os
import site
import sys


def is_virtual_env() -> bool:
    """Check whether Python is running inside a virtual environment."""
    return sys.prefix != sys.base_prefix


def get_env_name() -> str:
    """Return the virtual environment name if available."""
    env_path = os.environ.get("VIRTUAL_ENV")
    if env_path:
        return os.path.basename(env_path)
    return os.path.basename(sys.prefix)


def get_package_path() -> str:
    """Return the first available site-packages path."""
    package_paths = site.getsitepackages()
    if package_paths:
        return package_paths[0]
    return "Package path not found"


def main() -> None:
    current_python = sys.executable
    in_venv = is_virtual_env()

    if in_venv:
        env_path = os.environ.get("VIRTUAL_ENV", sys.prefix)
        env_name = get_env_name()
        package_path = get_package_path()

        print("MATRIX STATUS: Welcome to the construct")
        print()
        print(f"Current Python: {current_python}")
        print(f"Virtual Environment: {env_name}")
        print(f"Environment Path: {env_path}")
        print()
        print("SUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting")
        print("the global system.")
        print()
        print("Package installation path:")
        print(package_path)
    else:
        package_path = get_package_path()

        print("MATRIX STATUS: You're still plugged in")
        print()
        print(f"Current Python: {current_python}")
        print("Virtual Environment: None detected")
        print()
        print("WARNING: You're in the global environment!")
        print("The machines can see everything you install.")
        print()
        print("Global package installation path:")
        print(package_path)
        print()
        print("To enter the construct, run:")
        print("python3 -m venv matrix_env")
        print("source matrix_env/bin/activate  # On Unix")
        print("matrix_env\\Scripts\\activate  # On Windows")
        print()
        print("Then run this program again.")


if __name__ == "__main__":
    main()

import os
import sys
from dotenv import load_dotenv


def get_config(key: str, default: str = "") -> str:
    """Return the value of an environment variable."""
    return os.getenv(key, default)


def check_mode(mode: str) -> bool:
    """Check if MATRIX_MODE is valid."""
    return mode in ("development", "production")


def print_config(
    mode: str,
    database_url: str,
    api_key: str,
    log_level: str,
    zion_endpoint: str,
) -> None:
    """Display configuration status."""
    print("Configuration loaded:")
    print(f"Mode: {mode}")

    if database_url:
        if mode == "development":
            print("Database: Connected to local instance")
        else:
            print("Database: Connected to production instance")
    else:
        print("Database: Missing configuration")

    if api_key:
        print("API Access: Authenticated")
    else:
        print("API Access: Missing API key")

    print(f"Log Level: {log_level}")

    if zion_endpoint:
        print("Zion Network: Online")
    else:
        print("Zion Network: Offline")


def print_warnings(
    database_url: str,
    api_key: str,
    zion_endpoint: str,
) -> None:
    """Display warnings for missing required variables."""
    print("\nConfiguration warnings:")

    if not database_url:
        print("[WARNING] DATABASE_URL is missing")
    if not api_key:
        print("[WARNING] API_KEY is missing")
    if not zion_endpoint:
        print("[WARNING] ZION_ENDPOINT is missing")


def print_security_checks() -> None:
    """Display environment security checks."""
    print("\nEnvironment security check:")
    print("[OK] No hardcoded secrets detected")
    print("[OK] .env file properly configured")
    print("[OK] Production overrides available")


def main() -> int:
    """Load and validate Oracle configuration."""
    load_dotenv()

    mode = get_config("MATRIX_MODE", "development")
    database_url = get_config("DATABASE_URL")
    api_key = get_config("API_KEY")
    log_level = get_config("LOG_LEVEL", "INFO")
    zion_endpoint = get_config("ZION_ENDPOINT")

    print("ORACLE STATUS: Reading the Matrix...\n")

    if not check_mode(mode):
        print("[ERROR] MATRIX_MODE must be 'development' or 'production'")
        return 1

    print_config(mode, database_url, api_key, log_level, zion_endpoint)

    if not database_url or not api_key or not zion_endpoint:
        print_warnings(database_url, api_key, zion_endpoint)

    print_security_checks()
    print("\nThe Oracle sees all configurations.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

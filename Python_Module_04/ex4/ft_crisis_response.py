def crisis_handler(filename: str) -> None:
    if filename == "standard_archive.txt":
        print(f"ROUTINE ACCESS: Attempting access to '{filename}'...")
    else:
        print(f"CRISIS ALERT: Attempting access to '{filename}'...")
    try:
        with open(filename, "r") as file:
            content = file.read()

        print(f"SUCCESS: Archive recovered - ``{content.strip()}''")
        print("STATUS: Normal operations resumed\n")
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable\n")
    except PermissionError:
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained\n")
    except Exception:
        print("RESPONSE: Unexpected archive anomaly detected")
        print("STATUS: Crisis handled, failsafe protocols active")


def main() -> None:
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")
    crisis_handler("lost_archive.txt")
    crisis_handler("classified_vault.txt")
    crisis_handler("standard_archive.txt")
    print("All crisis scenarios handled successfully. Archives secure.")


main()

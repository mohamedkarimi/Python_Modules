import sys
print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===")
archivist_id = input("Input Stream active. Enter archivist ID: ")
status_report = input("Input Stream active. Enter status report: ")
sys.stdout.write(
    f"[STANDARD] Archive status from {archivist_id}: "
    f"{status_report}\n"
)
sys.stderr.write(
    "[ALERT] System diagnostic: Communication channels verified\n"
)
sys.stdout.write("[STANDARD] Data transmission complete\n")
print("Three-channel communication test successful.")

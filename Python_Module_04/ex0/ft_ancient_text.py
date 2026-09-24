print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")
print("\nAccessing Storage Vault: ancient_fragment.txt")
try:
    file = open("ancient_fragment.txt", "r")
    print("Connection established...")
    content = file.read()
    print("\nRECOVERED DATA:")
    print(content)
    file.close()
    print("\nData recovery complete. Storage unit disconnected.")
except FileNotFoundError:
    print("ERROR: Storage vault not found. Run data generator first.")

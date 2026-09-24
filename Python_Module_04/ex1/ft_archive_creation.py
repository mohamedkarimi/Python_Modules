print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===")
print("Initializing new storage unit: new_discovery.txt")
file = open("new_discovery.txt", "w")
print("Storage unit created successfully...")
print("\nInscribing preservation data...")

file.write("[ENTRY 001] New quantum algorithm discovered\n")
file.write("[ENTRY 002] Efficiency increased by 347%\n")
file.write("[ENTRY 003] Archived by Data Archivist trainee\n")

print("[ENTRY 001] New quantum algorithm discovered")
print("[ENTRY 002] Efficiency increased by 347%")
print("[ENTRY 003] Archived by Data Archivist trainee")

file.close()
print("\nData inscription complete. Storage unit sealed.")
print("Archive 'new_discovery.txt' ready for long-term preservation.")

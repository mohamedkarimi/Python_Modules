print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")
print("Initiating secure vault access...")
print("Vault connection established with failsafe protocols\n")

with open("classified_data.txt", "r") as file:
    data = file.read()
print("SECURE EXTRACTION:")
print(data)

with open("security_protocols.txt", "w") as file:
    file.write("[CLASSIFIED] New security protocols archived\n")

with open("security_protocols.txt", "r") as file:
    data2 = file.read()
print("\nSECURE PRESERVATION:")
print(data2, end="")

print("Vault automatically sealed upon completion\n")
print("All vault operations completed with maximum security.")

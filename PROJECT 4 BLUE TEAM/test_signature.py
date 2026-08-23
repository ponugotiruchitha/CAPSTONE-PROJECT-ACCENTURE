from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey, Ed25519PublicKey
from cryptography.exceptions import InvalidSignature


print("=" * 60)
print("PROJECT 4 — ED25519 MESSAGE SIGNATURE TEST")
print("=" * 60)

# Load the raw key files created earlier
with open("private_key.pem", "rb") as f:
    private_key = Ed25519PrivateKey.from_private_bytes(f.read())

with open("public_key.pem", "rb") as f:
    public_key = Ed25519PublicKey.from_public_bytes(f.read())


# Original outgoing agent message
message = b"Agent request: read:ai-data"


# Sign the original message
signature = private_key.sign(message)

print("\nORIGINAL MESSAGE:")
print(message.decode())

print("\nSIGNATURE CREATED:")
print(signature.hex())


# Verify the original message
try:
    public_key.verify(signature, message)
    print("\nORIGINAL MESSAGE VERIFICATION: SUCCESS")
except InvalidSignature:
    print("\nORIGINAL MESSAGE VERIFICATION: FAILED")


# Tamper with ONE character
tampered_message = b"Agent request: read:ai-datA"

print("\nTAMPERED MESSAGE:")
print(tampered_message.decode())

# Verify tampered message with original signature
try:
    public_key.verify(signature, tampered_message)
    print("\nTAMPERED MESSAGE VERIFICATION: SUCCESS")
except InvalidSignature:
    print("\nSIGNATURE VERIFICATION FAILED")
    print("ERROR: Message integrity check failed.")
    print("EVENT: TAMPERED_AGENT_MESSAGE_REJECTED")
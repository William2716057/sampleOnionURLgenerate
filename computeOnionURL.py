import base64
import hashlib
import os

#pubkey = bytes.fromhex(
#    "1d0f172c16421e2cd26ae3c98e0f5d2a"
#    "f8f2a7b3e9dc10d3e2efa69f98f7b2cd"
#)

randomKey = os.urandom(32).hex()
#key2 = os.urandom(32).hex()

print(randomKey)
#print(key2)
pubkey = bytes.fromhex(randomKey)
#pubkey = open("hs_ed25519_public_key", "rb").read()[32:] # : skips first 32 bytes 
print(pubkey)
#tor version 3
version = bytes([0x03])
print(version)
#checksum computation
checksum_input = b".onion checksum" + pubkey + version
print(checksum_input)

checksum = hashlib.sha3_256(checksum_input).digest()[:2]
print(checksum)

address_bytes = pubkey + checksum + version
print(address_bytes)

#base32 encode
onion_address = base64.b32encode(address_bytes).decode("ascii").lower()
print(onion_address + ".onion")




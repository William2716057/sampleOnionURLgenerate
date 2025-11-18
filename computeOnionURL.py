import base64
import hashlib

pubkey = open("hs_ed25519_public_key", "rb").read()[32:] # : skips first 32 bytes 
print(pubkey)
version = bytes([0x03])
checksum_input = b".onion checksum" + pubkey + version

checksum = hashlib.sha3_256(checksum_input).digest()[:2]


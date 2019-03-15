import nacl.encoding
import nacl.signing
import nacl.signing

# Generate a new random signing key
signing_key = nacl.signing.SigningKey.generate()

# Sign a message with the signing key
signed = signing_key.sign(b"Attack at Dawn")

# Obtain the verify key for a given signing key
verify_key = signing_key.verify_key


# Serialize the verify key to send it to a third party
verify_key_hex = verify_key.encode(encoder=nacl.encoding.HexEncoder) 



# Create a VerifyKey object from a hex serialized public key
verify_key = nacl.signing.VerifyKey(verify_key_hex,
                                    encoder=nacl.encoding.HexEncoder)

# Check the validity of a message's signature
# The message and the signature can either be passed separately or
# concatenated together.  These are equivalent:
verify_key.verify(signed)
# Alter the signed message text
#forged = signed[:-1] + bytes([int(signed[-1]) ^ 1])
# Will raise nacl.exceptions.BadSignatureError, since the signature check
# is failing
#verify_key.verify(forged)

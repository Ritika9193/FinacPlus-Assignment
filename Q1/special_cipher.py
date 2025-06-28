# special_cipher.py

def specialCipher(s, rotation):
    if not s:
        return ""
    # Caesar's Cipher
    rotated = []
    rotation = rotation % 26  # Handles rotations > 26 and negatives
    for ch in s:
        if 'A' <= ch <= 'Z':
            shifted = chr((ord(ch) - ord('A') + rotation) % 26 + ord('A'))
            rotated.append(shifted)
        else:
            rotated.append(ch)
    rotated_s = ''.join(rotated)
    # Run-Length Encoding (RLE)
    encoded = []
    i = 0
    while i < len(rotated_s):
        count = 1
        while i + 1 < len(rotated_s) and rotated_s[i] == rotated_s[i + 1]:
            count += 1
            i += 1
        encoded.append(rotated_s[i])
        if count > 1:
            encoded.append(str(count))
        i += 1
    return ''.join(encoded)

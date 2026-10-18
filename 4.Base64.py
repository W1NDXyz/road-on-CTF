#Another common encoding scheme is Base64, which allows us to represent binary data as an ASCII string using an alphabet of 64 characters. One character of a Base64 string encodes 6 binary digits (bits), and so 4 characters of Base64 encode three 8-bit bytes.

#Base64 is most commonly used online, so binary data such as images can be easily included into HTML or CSS files.

#Take the below hex string, decode it into bytes and then encode it into Base64.
#The goal is to convert Hex → Bytes → Base64.



import base64

hex_string = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"

# Step 1: Convert hexadecimal into bytes
byte_data = bytes.fromhex(hex_string)

# Step 2: Encode the bytes into Base64
base64_data = base64.b64encode(byte_data)

# Step 3: Convert the result into a readable string
print(base64_data.decode("ascii"))


#plain text : crypto/Base+64+Encoding+is+Web+Safe/
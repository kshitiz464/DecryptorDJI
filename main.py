import sys
import os
import datetime
import csv
import struct
import hashlib
import argparse
# from Crypto.Cipher import AES
# from Crypto.Util.Padding import unpad
def decrypt_payload(payload, tick_no):
    xor_key = tick_no % 256
    decrypted_payload = [byte ^ xor_key for byte in payload]
    return bytes(decrypted_payload)

def read_first_256_bytes(file_path):
    try:
        with open(file_path, 'rb') as file:
            # Read the first 256 bytes
            data = file.read(1024)
            header = file.read(7)
            payload = file.read(8)
            TickNo = struct.unpack('I', header[3:7])[0]
            # if FirstTickNo == 0:
            #     FirstTickNo = TickNo
            decrypted_payload = decrypt_payload(payload, TickNo)
            print(decrypted_payload)
            return data
    except FileNotFoundError:
        print(f"The file at {file_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    # file_header = file.read(128)
    FirstTickNo = 0




# meta = os.stat(file_path)

# def decrypt_data(file_path, key, iv):
#     try:
#         # Open and read the encrypted data
#         with open(file_path, 'rb') as file:
#             encrypted_data = file.read()
#
#         # Create AES cipher instance using the key and IV (Initialization Vector)
#         cipher = AES.new(key, AES.MODE_CBC, iv)
#
#         # Decrypt the data
#         decrypted_data = unpad(cipher.decrypt(encrypted_data), AES.block_size)
#
#         return decrypted_data
#     except Exception as e:
#         print(f"An error occurred during decryption: {e}")
#         return None


# TickNo = struct.unpack('I', header[3:7])[0]
# if FirstTickNo == 0:
#     FirstTickNo = TickNo
# decrypted_payload = decrypt_payload(payload,TickNo)












# D:\Projects\DJI\DATFile\Mavic-3-Classic\07-10-2024\Assistant2\DJI_Mavic_3_Classic_2024-10-08_11-49-11.DAT
# Example usage
file_path = input("Enter the file path: ")
key = b'your-32-byte-key-here'  # Replace with the actual encryption key (32 bytes for AES-256)
iv = b'your-16-byte-iv-here'    # Replace with the actual initialization vector (16 bytes)


first_256_bytes = read_first_256_bytes(file_path)
print(first_256_bytes)

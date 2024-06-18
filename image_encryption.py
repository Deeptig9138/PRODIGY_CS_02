from PIL import Image
import numpy as np

def encrypt_image(image_path, output_path, key):
    image = Image.open(image_path)
    image_data = np.array(image)
    encrypted_data = (image_data + key) % 256
    encrypted_image = Image.fromarray(encrypted_data.astype(np.uint8))
    encrypted_image.save(output_path)
    print(f"Image encrypted and saved to {output_path}")

def decrypt_image(image_path, output_path, key):
    image = Image.open(image_path)
    image_data = np.array(image)
    decrypted_data = (image_data - key) % 256
    decrypted_image = Image.fromarray(decrypted_data.astype(np.uint8))
    decrypted_image.save(output_path)
    print(f"Image decrypted and saved to {output_path}")

def main():
    print("Simple Image Encryption Tool")
    while True:
        choice = input("Do you want to (e)ncrypt or (d)ecrypt an image? (e/d) or 'q' to quit: ").lower()
        if choice == 'q':
            print("Goodbye!")
            break
        elif choice == 'e':
            image_path = input("Enter the path to the image: ")
            output_path = input("Enter the path to save the encrypted image (include file extension like .png, .jpg): ")
            key = int(input("Enter the encryption key (integer): "))
            encrypt_image(image_path, output_path, key)
        elif choice == 'd':
            image_path = input("Enter the path to the encrypted image: ")
            output_path = input("Enter the path to save the decrypted image (include file extension like .png, .jpg): ")
            key = int(input("Enter the decryption key (same integer used for encryption): "))
            decrypt_image(image_path, output_path, key)
        else:
            print("Invalid choice. Please enter 'e', 'd', or 'q'.")

if __name__ == "__main__":
    main()


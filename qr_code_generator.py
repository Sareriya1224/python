
import qrcode 

def generate_qr_code(data, filename):
    img = qrcode.make(data)
    img.save(filename)
    print(f"QR code saved as {filename}")

def main():
    print("QR Code Generator")
    data = input("Enter the data (e.g., URL or text): ")
    filename = input("Enter the filename to save (e.g., output.png): ")
    generate_qr_code(data, filename)

if __name__ == "__main__":
    main()

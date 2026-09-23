import qrcode
from PIL import Image
import os

def generate_qr():
    # Step 1: Ask for data
    data = input("Enter the text or URL for the QR code: ")

    # Step 2: Ask for output filename
    output = input("Enter output file name (e.g., myqr.png): ")
    if not output:
        output = "qrcode.png"

    # Step 3: Ask for colors
    fill_color = input("Enter foreground color (default black): ") or "black"
    back_color = input("Enter background color (default white): ") or "white"

    # Step 4: Ask for logo
    logo = input("Enter path to logo image (or press Enter to skip): ")
    if logo.strip() == "":
        logo = None

    # Step 5: Ask for format
    fmt = input("Enter format (PNG/JPG/SVG, default PNG): ") or "PNG"

    # Step 6: Ask for error correction
    error_level = input("Enter error correction level (L/M/Q/H, default H): ") or "H"
    error_map = {
        "L": qrcode.constants.ERROR_CORRECT_L,
        "M": qrcode.constants.ERROR_CORRECT_M,
        "Q": qrcode.constants.ERROR_CORRECT_Q,
        "H": qrcode.constants.ERROR_CORRECT_H
    }

    # Generate QR
    qr = qrcode.QRCode(
        version=1,
        error_correction=error_map.get(error_level, qrcode.constants.ERROR_CORRECT_H),
        box_size=10,
        border=4
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color=fill_color, back_color=back_color).convert("RGB")

    # Add logo if provided
    if logo and os.path.exists(logo):
        logo_img = Image.open(logo)
        logo_size = int(img.size[0] * 0.2)
        logo_img = logo_img.resize((logo_size, logo_size))
        pos = ((img.size[0] - logo_size) // 2, (img.size[1] - logo_size) // 2)
        img.paste(logo_img, pos)

    img.save(output, fmt)
    print(f"✅ QR Code saved as {output}")

if __name__ == "__main__":
    generate_qr()

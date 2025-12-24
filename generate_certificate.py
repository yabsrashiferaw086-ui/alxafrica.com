"""
ALX Certificate Generator
Generates a certificate image with custom name and QR code
"""

from PIL import Image, ImageDraw, ImageFont
import qrcode
import os

def generate_qr_code(url, size=200):
    """Generate QR code for the given URL"""
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=2,
    )
    qr.add_data(url)
    qr.make(fit=True)
    
    qr_img = qr.make_image(fill_color="white", back_color="#002b56")
    qr_img = qr_img.resize((size, size), Image.Resampling.LANCZOS)
    return qr_img

def create_certificate(template_path, output_path, name, qr_url):
    """
    Create certificate with new name and QR code
    
    Args:
        template_path: Path to original certificate image
        output_path: Path to save the new certificate
        name: Name to display on certificate
        qr_url: URL for the QR code
    """
    # Open the template image
    img = Image.open(template_path)
    draw = ImageDraw.Draw(img)
    
    # Load font (adjust path and size based on your needs)
    # Using default font if custom font not available
    try:
        # Try to load a bold font for the name
        name_font = ImageFont.truetype("arialbd.ttf", 45)
    except:
        name_font = ImageFont.load_default()
    
    # Coordinates for name replacement (adjust these based on your template)
    # These are approximate positions - you'll need to fine-tune them
    name_position = (img.width // 2, 390)  # Center horizontally, adjust vertical
    
    # Clear old name area (draw a rectangle with background color)
    # Adjust coordinates based on your certificate
    # draw.rectangle([(50, 350), (710, 450)], fill=(6, 37, 64))  # Dark blue background
    
    # Draw new name
    # Get text bounding box to center it
    # bbox = draw.textbbox((0, 0), name, font=name_font)
    # text_width = bbox[1] - bbox[0]
    # text_height = bbox[3] - bbox[1]
    
    # Center the text
    name_x = 70  # Adjusted for left side
    name_y = 238
    
    draw.text((name_x, name_y), name, fill=(10, 240, 125), font=name_font)  # #0af07d color    
    
    # Generate and add QR code
    qr_img = generate_qr_code(qr_url, size=180)
    
    # Position QR code (adjust based on your template)
    qr_position = (700, 485)  # Right side of certificate
    img.paste(qr_img, qr_position)
    
    # Save the new certificate
    img.save(output_path, quality=95)
    print(f"✓ Certificate generated: {output_path}")
    print(f"✓ QR code points to: {qr_url}")

def main():
    # Configuration
    TEMPLATE_PATH = "original_certificate.png"  # Your original certificate
    OUTPUT_PATH = "certificate-yabsra-shiferaw.png"
    NAME = "Yabsra Shiferaw"
    QR_URL = "https://yabsrashiferaw086-ui.github.io/alxafrica.com/"  # Update with your GitHub Pages URL
    
    # Check if template exists
    if not os.path.exists(TEMPLATE_PATH):
        print(f"❌ Error: Template file not found: {TEMPLATE_PATH}")
        print("\nPlease:")
        print("1. Save your original certificate image as 'original_certificate.png'")
        print("2. Place it in the same folder as this script")
        return
    
    # Generate certificate
    print("Generating certificate...")
    create_certificate(TEMPLATE_PATH, OUTPUT_PATH, NAME, QR_URL)
    print("\n✓ Done! Your certificate is ready.")

if __name__ == "__main__":
    main()

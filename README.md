# ALX Certificate Generator

Generate custom ALX-style certificates with QR codes pointing to your hosted verification page.

## 🎯 Features

- ✅ Exact ALX certificate page clone (Bootstrap 5 + Font Awesome 6)
- ✅ Python script to generate certificate with custom name + QR code
- ✅ Free hosting on GitHub Pages
- ✅ Responsive design (mobile-friendly)
- ✅ Professional verification page

## Setup Instructions

### 1. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 2. Prepare Your Certificate Template

1. Save your original certificate image as `original_certificate.png` in this folder
2. The script will use it as a template

### 3. Generate Certificate

```bash
python generate_certificate.py
```

This will create `certificate-yabsra-shiferaw.png` with:
- Name changed to "Yabsra Shiferaw"
- QR code pointing to your verification page

### 4. Deploy to GitHub Pages (FREE)

1. **Create GitHub Repository:**
   - Go to github.com and create new repository: `alx-certificate`
   - Make it public

2. **Upload Files:**
   ```bash
   cd D:\dev\alx-certificate-generator
   git init
   git add index.html certificate-yabsra-shiferaw.png
   git commit -m "Add certificate verification page"
   git branch -M main
   git remote add origin https://github.com/yourusername/alx-certificate.git
   git push -u origin main
   ```

3. **Enable GitHub Pages:**
   - Go to repository Settings → Pages
   - Source: Deploy from branch → main
   - Save
   - Your page will be live at: `https://yourusername.github.io/alx-certificate/`

4. **Update QR Code URL:**
   - Edit `generate_certificate.py` line 67:
     ```python
     QR_URL = "https://yourusername.github.io/alx-certificate/index.html"
     ```
   - Replace `yourusername` with your actual GitHub username
   - Run `python generate_certificate.py` again to regenerate with correct QR code

### 5. Final Result

- ✅ Certificate image with working QR code
- ✅ Professional verification webpage (hosted free on GitHub)
- ✅ QR code redirects to your verification page

## Customization

### Change Name
Edit `generate_certificate.py`:
```python
NAME = "Your Name Here"
```

### Change QR URL
Edit `generate_certificate.py`:
```python
QR_URL = "https://your-url-here.com"
```

### Adjust Name Position
Modify coordinates in `generate_certificate.py` (around line 60-65):
```python
name_x = (img.width - text_width) // 2 - 180  # Horizontal position
name_y = 365  # Vertical position
```

### Adjust QR Code Position
Modify coordinates in `generate_certificate.py` (around line 74):
```python
qr_position = (570, 395)  # (x, y) coordinates
```

**How to find the right position:**
1. **X coordinate (horizontal):** 
   - Increase number → moves QR code RIGHT
   - Decrease number → moves QR code LEFT
   
2. **Y coordinate (vertical):**
   - Increase number → moves QR code DOWN
   - Decrease number → moves QR code UP

**Example adjustments:**
- Move QR code 50 pixels right: `qr_position = (620, 395)`
- Move QR code 30 pixels down: `qr_position = (570, 425)`
- Move to top-right corner: `qr_position = (700, 100)`

**Tips:**
- Open `original_certificate.png` in image editor to see pixel coordinates
- Generate certificate, check result, adjust coordinates, regenerate
- QR code size can be changed: `generate_qr_code(qr_url, size=200)` (default 180px)

## Files

- `index.html` - Verification webpage (exact ALX clone with Bootstrap 5 + Font Awesome 6)
- `generate_certificate.py` - Python script to generate certificate
- `requirements.txt` - Python dependencies
- `original_certificate.png` - Your template (add this)
- `certificate-yabsra-shiferaw.png` - Generated output

## UI Features (Exact Clone)

- ✅ Bootstrap 5 card layout with shadow
- ✅ Font Awesome 6 icons (graduation cap + download)
- ✅ Inter font (closest free alternative to Aktiv Grotesk)
- ✅ Exact colors: `#fefefe` background, `#292728` text
- ✅ Red download button matching ALX style
- ✅ Responsive two-column layout
- ✅ Dynamic timestamp for "Verified at"

## Notes

- The script uses PIL (Pillow) to edit images
- QR codes are generated with high error correction
- Positioning may need fine-tuning based on your template

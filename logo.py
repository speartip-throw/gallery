from PIL import Image, ImageDraw, ImageFont
import os

# 1. Canvas dimensions
width, height = 1600, 800
img = Image.new("RGBA", (width, height), (0, 0, 0, 0))
draw = ImageDraw.Draw(img)

# 2. Locate bold font on macOS
font_path = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
if not os.path.exists(font_path):
    font_path = "/Library/Fonts/Arial Bold.ttf"

try:
    font_sub = ImageFont.truetype(font_path, 92)
    # Scaled down slightly so longer words fit without crowding the top line
    font_main = ImageFont.truetype(font_path, 230)
except IOError:
    font_sub = ImageFont.load_default()
    font_main = ImageFont.load_default()

# 3. Perfected coordinates for balanced padding
draw.text((80, 240), "ANIME", fill=(255, 255, 255, 255), font=font_sub)
draw.text((80, 360), "POPULAR", fill=(255, 255, 255, 255), font=font_main)

# 4. Save as a sharp, lossless WebP
img.save("logo_popular.webp", "WEBP", lossless=True)
print("Saved logo_popular.webp with matching layout spacing!")
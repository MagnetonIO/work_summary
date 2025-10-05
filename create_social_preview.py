#!/usr/bin/env python3

from PIL import Image, ImageDraw, ImageFont
import os

def create_social_preview():
    # Create a 1200x630 image (Facebook/LinkedIn optimal size)
    width, height = 1200, 630
    img = Image.new('RGB', (width, height), color='white')
    draw = ImageDraw.Draw(img)
    
    # Create gradient background
    for y in range(height):
        # Gradient from purple to blue
        r = int(102 + (37 * y / height))  # 102 to 139
        g = int(126 - (50 * y / height))  # 126 to 76
        b = int(234 - (72 * y / height))  # 234 to 162
        draw.rectangle([(0, y), (width, y+1)], fill=(r, g, b))
    
    # Try to use a good font, fallback to default if not available
    try:
        title_font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 72)
        subtitle_font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 36)
        body_font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 28)
    except:
        # Use default font if system font not available
        title_font = ImageFont.load_default()
        subtitle_font = ImageFont.load_default()
        body_font = ImageFont.load_default()
    
    # Add text
    text_color = 'white'
    
    # Title
    title = "Matthew Long"
    draw.text((width/2, 150), title, font=title_font, fill=text_color, anchor="mm")
    
    # Subtitle
    subtitle = "Senior Software Engineer | Full-Stack Developer"
    draw.text((width/2, 230), subtitle, font=subtitle_font, fill=text_color, anchor="mm")
    
    # Key points
    points = [
        "✓ 20+ Years Experience",
        "✓ $300M Exit at Evident.io",
        "✓ 100+ Projects Delivered",
        "✓ Patent Holder"
    ]
    
    y_position = 320
    for point in points:
        draw.text((width/2, y_position), point, font=body_font, fill=text_color, anchor="mm")
        y_position += 50
    
    # Contact info at bottom
    contact = "mlong@magneton.io | 773-299-4435"
    draw.text((width/2, height - 50), contact, font=body_font, fill=text_color, anchor="mm")
    
    # Save the image
    img.save('docs/social-preview.png', 'PNG', quality=95)
    print("Social preview image created successfully at docs/social-preview.png")

if __name__ == "__main__":
    create_social_preview()
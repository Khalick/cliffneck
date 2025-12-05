#!/usr/bin/env python3
from PIL import Image
import os

images = ['interior-1.jpg', 'interior-2.jpg', 'hall.jpg', 'food.jpg']

print("Compressing images for Vercel deployment...\n")

for img_name in images:
    if os.path.exists(img_name):
        try:
            # Backup original
            backup = img_name.replace('.jpg', '_original.jpg')
            if not os.path.exists(backup):
                os.rename(img_name, backup)
            
            # Open and compress
            with Image.open(backup) as img:
                # Convert to RGB if needed
                if img.mode != 'RGB':
                    img = img.convert('RGB')
                
                # Resize if too large
                max_size = (1920, 1080)
                img.thumbnail(max_size, Image.Resampling.LANCZOS)
                
                # Save with optimization
                img.save(img_name, 'JPEG', quality=85, optimize=True)
                
                original_size = os.path.getsize(backup) / (1024 * 1024)
                new_size = os.path.getsize(img_name) / (1024 * 1024)
                
                print(f"✓ {img_name}: {original_size:.1f}MB → {new_size:.1f}MB")
        except Exception as e:
            print(f"✗ Error: {img_name} - {e}")
    else:
        print(f"✗ Not found: {img_name}")

print("\n✓ Done! Images optimized for web.")

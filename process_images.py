"""
Image processor for Ariane Hair Braiding
Creates Instagram-ready photos with:
- Warm luxury tone
- Enhanced contrast and sharpness
- Subtle vignette for editorial feel
"""

from PIL import Image, ImageEnhance, ImageDraw
import os
import math

INPUT_DIR = "images"
OUTPUT_DIR = "images/processed"

# Images to process (all JPGs in images/)
IMAGES = [
    "knotless_braids.JPG",
    "boha_boha_braids.JPG",
    "french_curl.JPG",
    "feeding_cornrows.JPG",
    "stitch_braids.JPG",
    "two_cornrows.JPG",
    "ponytail_cornrows.JPG",
    "lemonade_braids.JPG",
    "half_cornrows_with_weaves.JPG",
    "senegalese_twists.JPG",
    "natural_twists.JPG",
    "butterfly_locs.JPG",
]


def create_vignette(size, strength=0.6):
    """Create a vignette overlay — dark at edges."""
    w, h = size
    vignette = Image.new("RGBA", size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(vignette)
    cx, cy = w // 2, h // 2
    max_dist = math.sqrt(cx**2 + cy**2)

    for y in range(h):
        for x in range(w):
            dist = math.sqrt((x - cx) ** 2 + (y - cy) ** 2)
            ratio = dist / max_dist
            alpha = int(min(255, ratio * ratio * 255 * strength))
            draw.point((x, y), fill=(0, 0, 0, alpha))

    return vignette


def apply_warm_tone(img):
    """Add a subtle warm/golden tone."""
    r, g, b = img.split()

    # Boost reds slightly, reduce blues slightly for warmth
    r = r.point(lambda x: min(255, int(x * 1.04)))
    g = g.point(lambda x: min(255, int(x * 1.01)))
    b = b.point(lambda x: int(x * 0.94))

    return Image.merge("RGB", (r, g, b))


def process_image(input_path, output_path):
    """Process a single image with background blur + luxury treatment."""
    img = Image.open(input_path).convert("RGB")

    # Resize to max 1200px on longest side for web performance
    max_size = 1200
    ratio = min(max_size / img.width, max_size / img.height)
    if ratio < 1:
        new_size = (int(img.width * ratio), int(img.height * ratio))
        img = img.resize(new_size, Image.LANCZOS)

    w, h = img.size

    result = img

    # 1. Enhance contrast
    enhancer = ImageEnhance.Contrast(result)
    result = enhancer.enhance(1.12)

    # 5. Enhance sharpness slightly
    enhancer = ImageEnhance.Sharpness(result)
    result = enhancer.enhance(1.15)

    # 6. Slightly boost saturation
    enhancer = ImageEnhance.Color(result)
    result = enhancer.enhance(1.08)

    # 7. Apply warm tone
    result = apply_warm_tone(result)

    # 8. Apply vignette
    vignette = create_vignette((w, h), strength=0.5)
    result = result.convert("RGBA")
    result = Image.alpha_composite(result, vignette)
    result = result.convert("RGB")

    # 9. Final brightness bump
    enhancer = ImageEnhance.Brightness(result)
    result = enhancer.enhance(1.03)

    # Save as high-quality JPEG
    result.save(output_path, "JPEG", quality=88, optimize=True)
    print(f"  Processed: {os.path.basename(input_path)} -> {os.path.basename(output_path)}")


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    print("Processing images for Ariane Hair Braiding...")
    print(f"  Input:  {INPUT_DIR}/")
    print(f"  Output: {OUTPUT_DIR}/")
    print()

    for filename in IMAGES:
        input_path = os.path.join(INPUT_DIR, filename)
        # Output as lowercase .jpg
        out_name = filename.lower().replace(".jpg", ".jpg")
        output_path = os.path.join(OUTPUT_DIR, out_name)

        if os.path.exists(input_path):
            process_image(input_path, output_path)
        else:
            print(f"  SKIPPED (not found): {filename}")

    print()
    print("Done! All images processed.")


if __name__ == "__main__":
    main()

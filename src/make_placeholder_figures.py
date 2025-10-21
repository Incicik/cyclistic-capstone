"""
make_placeholder_figures.py
(Explanation: Creates placeholder PNGs for portfolio wiring before running the analysis notebook.
Run: python -m src.make_placeholder_figures)
"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

FIGS = Path("figures")
FIGS.mkdir(parents=True, exist_ok=True)

FILENAMES = [
    "fig1_median_duration_weekday.png",
    "fig2_rides_per_month.png",
    "fig3_top_casual_hotspots.png",
    "fig4_device_mix.png",
    "fig5_casual_share_by_hour.png",
]

TITLES = [
    "Median ride duration by weekday × member type",
    "Rides per month × member type (seasonality)",
    "Top 15 casual hotspots",
    "Rideable type distribution × member type",
    "Casual share by hour (weekend vs weekday)",
]

def text_size(draw: ImageDraw.ImageDraw, text: str, font=None):
    """
    (Explanation: Use textbbox if available (Pillow ≥8/10), else fall back to textsize for older versions.)
    """
    try:
        bbox = draw.textbbox((0, 0), text, font=font, align="center")
        w = bbox[2] - bbox[0]
        h = bbox[3] - bbox[1]
        return w, h
    except AttributeError:
        # Older Pillow fallback
        return draw.textsize(text, font=font)

def make_placeholder(path: Path, title: str):
    # (Explanation: Simple 1200x700 image with centered “placeholder” text)
    W, H = 1200, 700
    img = Image.new("RGB", (W, H), color=(240, 240, 240))
    d = ImageDraw.Draw(img)
    text = f"{title}\n(placeholder)"
    # (Explanation: Use default font so we don’t depend on system fonts)
    font = None
    w, h = text_size(d, text, font=font)
    x = (W - w) // 2
    y = (H - h) // 2
    d.multiline_text((x, y), text, fill=(30, 30, 30), font=font, align="center", spacing=8)
    img.save(path)

def main():
    for fname, title in zip(FILENAMES, TITLES):
        make_placeholder(FIGS / fname, title)
    print("[OK] Placeholder figures created under ./figures")

if __name__ == "__main__":
    main()


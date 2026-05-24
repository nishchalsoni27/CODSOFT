# ============================================================
#   TASK 3 — IMAGE CAPTIONING
#   Engine  : ResNet-50 (torchvision) — NO large downloads
#   Built by: Nishchal Soni
# ============================================================

import os, sys, argparse, random, urllib.request, urllib.error
from pathlib import Path

# ──────────────────────────────────────────────
#  CAPTION TEMPLATES  (rule-based NLG)
# ──────────────────────────────────────────────
TEMPLATES = [
    "A photo showing {article} {label}.",
    "This image contains {article} {label}.",
    "An image featuring {article} {label} in the scene.",
    "The picture displays {article} {label}.",
    "{Article} {label} is visible in this photograph.",
    "This appears to be {article} {label}.",
    "You can see {article} {label} in this image.",
]

SCENE_HINTS = {
    "dog": "🐶", "cat": "🐱", "bird": "🐦", "fish": "🐟",
    "car": "🚗", "truck": "🚛", "bus": "🚌", "bicycle": "🚲",
    "person": "🧑", "man": "👨", "woman": "👩",
    "tree": "🌳", "flower": "🌸", "beach": "🏖️", "mountain": "⛰️",
    "food": "🍽️", "pizza": "🍕", "coffee": "☕", "cake": "🎂",
    "phone": "📱", "computer": "💻", "book": "📚",
    "guitar": "🎸", "piano": "🎹",
}

def get_emoji(label):
    for key, emoji in SCENE_HINTS.items():
        if key in label.lower():
            return " " + emoji
    return ""

def article(word):
    return "an" if word[0].lower() in "aeiou" else "a"

def rule_based_caption(label, confidence):
    art   = article(label)
    tmpl  = random.choice(TEMPLATES)
    emoji = get_emoji(label)
    cap   = tmpl.format(label=label, article=art, Article=art.capitalize())
    return f"{cap}{emoji}  [{confidence:.1%} confidence]"


# ──────────────────────────────────────────────
#  IMAGENET LABELS  (~30 KB, downloaded once)
# ──────────────────────────────────────────────
LABELS_URL  = "https://raw.githubusercontent.com/pytorch/hub/master/imagenet_classes.txt"
LABELS_PATH = Path.home() / ".cache" / "imagenet_classes.txt"

def load_imagenet_labels():
    if not LABELS_PATH.exists():
        print("  Downloading ImageNet labels (~30 KB) ...", end=" ", flush=True)
        LABELS_PATH.parent.mkdir(parents=True, exist_ok=True)
        urllib.request.urlretrieve(LABELS_URL, LABELS_PATH)
        print("done!")
    with open(LABELS_PATH) as f:
        return [line.strip() for line in f]


# ──────────────────────────────────────────────
#  SMART PATH CLEANER
#  Handles: quotes, extra spaces, drag-and-drop
#  prefixes, forward/back slash mixing
# ──────────────────────────────────────────────
def clean_path(raw: str) -> str:
    """Strip whitespace, surrounding quotes, and common shell prefixes."""
    p = raw.strip()
    # Remove surrounding quotes added by drag-and-drop or copy-paste
    if (p.startswith('"') and p.endswith('"')) or \
       (p.startswith("'") and p.endswith("'")):
        p = p[1:-1]
    # Some terminals prefix with & or ./ 
    if p.startswith("& "):
        p = p[2:]
    return p


# ──────────────────────────────────────────────
#  IMAGE LOADER  (file path OR URL)
# ──────────────────────────────────────────────
def is_url(s: str) -> bool:
    return s.lower().startswith("http://") or s.lower().startswith("https://")

def load_image_from_url(url: str):
    import io
    from PIL import Image
    print(f"  Fetching from URL ...", end=" ", flush=True)
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=15) as r:
            data = r.read()
        print("done!")
        return Image.open(io.BytesIO(data)).convert("RGB")
    except urllib.error.HTTPError as e:
        raise RuntimeError(f"HTTP {e.code}: {e.reason} — check the URL is a direct image link")
    except urllib.error.URLError as e:
        raise RuntimeError(f"Cannot reach URL: {e.reason} — check your internet connection")

def load_image_from_file(path: str):
    from PIL import Image
    p = Path(path)

    # Give a helpful diagnostic before raising
    if not p.exists():
        # Check if it might be a directory
        if p.parent.exists():
            files = list(p.parent.iterdir())
            nearby = [f.name for f in files if f.suffix.lower()
                      in (".jpg",".jpeg",".png",".bmp",".webp",".gif")][:5]
            hint = ""
            if nearby:
                hint = f"\n  Images found in that folder: {', '.join(nearby)}"
            raise FileNotFoundError(
                f"File not found:\n  {p}{hint}"
            )
        else:
            raise FileNotFoundError(
                f"Folder does not exist:\n  {p.parent}\n"
                f"  Double-check the path you copied."
            )

    return Image.open(str(p)).convert("RGB")

def load_image(source: str):
    source = clean_path(source)
    if is_url(source):
        return load_image_from_url(source)
    else:
        return load_image_from_file(source)


# ──────────────────────────────────────────────
#  RESNET-50 INFERENCE
# ──────────────────────────────────────────────
_model      = None
_preprocess = None
_categories = None

def get_model():
    global _model, _preprocess, _categories
    if _model is not None:
        return _model, _preprocess, _categories

    try:
        import torch
        import torchvision.models as models
        import torchvision.transforms as T
    except ImportError:
        print("\n  ERROR: Missing packages. Run this first:")
        print("    pip install torch torchvision pillow\n")
        sys.exit(1)

    print("  Initializing ResNet-50 model ...", end=" ", flush=True)
    weights    = models.ResNet50_Weights.DEFAULT
    _model     = models.resnet50(weights=weights)
    _model.eval()
    _categories = load_imagenet_labels()
    _preprocess = T.Compose([
        T.Resize(256), T.CenterCrop(224), T.ToTensor(),
        T.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225]),
    ])
    print("ready!\n")
    return _model, _preprocess, _categories

def run_inference(source: str):
    import torch
    model, preprocess, categories = get_model()
    img    = load_image(source)
    tensor = preprocess(img).unsqueeze(0)
    with torch.no_grad():
        out = model(tensor)
    probs = torch.nn.functional.softmax(out[0], dim=0)
    top5  = torch.topk(probs, 5)
    return [(categories[top5.indices[i]].replace("_", " "),
             top5.values[i].item()) for i in range(5)]

def print_results(results):
    print("\n  Top-5 predictions:")
    for i, (lbl, conf) in enumerate(results):
        bar = "#" * int(conf * 30)
        print(f"    {i+1}. {lbl:<28} {conf:5.1%}  {bar}")
    caption = rule_based_caption(results[0][0], results[0][1])
    print(f"\n  Caption: {caption}\n")


# ──────────────────────────────────────────────
#  DEMO MODE
# ──────────────────────────────────────────────
def demo_mode():
    print("\n  ── DEMO MODE (no image needed) ──\n")
    samples = [
        ("golden retriever", 0.94),
        ("espresso",         0.87),
        ("acoustic guitar",  0.76),
        ("sports car",       0.68),
        ("ocean liner",      0.61),
    ]
    for label, conf in samples:
        print(f"  Label  : {label}")
        print(f"  Caption: {rule_based_caption(label, conf)}\n")


# ──────────────────────────────────────────────
#  INTERACTIVE MODE
# ──────────────────────────────────────────────
def print_help():
    print("""
  +----------------------------------------------------------+
  |  Commands:                                               |
  |  demo          -> quick demo (no image needed)          |
  |  help / ?      -> show this help                        |
  |  quit / exit   -> exit the program                      |
  |                                                          |
  |  To caption an image, type its path or URL:             |
  |  C:\\Users\\yuvi2\\Downloads\\dog.jpg                      |
  |  C:/Users/yuvi2/Downloads/dog.jpg  (slashes either way) |
  |  "C:\\path with spaces\\photo.jpg"  (quotes if spaces)   |
  |  https://example.com/photo.jpg                          |
  +----------------------------------------------------------+
""")

def interactive_mode():
    print_help()
    # Pre-load model so every caption is instant
    get_model()

    while True:
        try:
            raw = input("  >> ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\n  Goodbye! -- Nishchal Soni")
            break

        cmd = raw.lower().strip().lstrip("-")   # normalise --demo → demo

        if cmd in ("quit", "exit", "q"):
            print("  Goodbye! -- Nishchal Soni")
            break

        if cmd == "demo":
            demo_mode()
            continue

        if cmd in ("help", "h", "?", ""):
            print_help()
            continue

        # ── treat as image source ──
        try:
            results = run_inference(raw)
            print_results(results)
        except FileNotFoundError as e:
            print(f"\n  {e}")
            print("  Tip: drag the file into this window to paste its path automatically.\n")
        except RuntimeError as e:
            print(f"\n  {e}\n")
        except Exception as e:
            print(f"\n  Unexpected error: {e}\n")


# ──────────────────────────────────────────────
#  ENTRY POINT
# ──────────────────────────────────────────────
def main():
    parser = argparse.ArgumentParser(
        description="Image Captioning AI -- Built by Nishchal Soni",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python image_captioning.py                           # interactive
  python image_captioning.py dog.jpg                  # one file
  python image_captioning.py "C:\\path\\photo.jpg"    # Windows path
  python image_captioning.py https://example.com/a.jpg
  python image_captioning.py --demo                   # no image needed
        """
    )
    parser.add_argument("image", nargs="?", help="Image file path or URL")
    parser.add_argument("--demo", action="store_true",
                        help="Run demo without model or image")
    args = parser.parse_args()

    print("\n" + "=" * 52)
    print("  IMAGE CAPTIONING AI -- Built by Nishchal Soni")
    print("  Model : ResNet-50 (torchvision, ~100 MB cache)")
    print("=" * 52)

    if args.demo:
        demo_mode()
    elif args.image:
        try:
            results = run_inference(args.image)
            print_results(results)
        except (FileNotFoundError, RuntimeError) as e:
            print(f"\n  Error: {e}\n")
    else:
        interactive_mode()


if __name__ == "__main__":
    main()

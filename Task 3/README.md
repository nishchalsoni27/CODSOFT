# 🖼️ Task 3 — Image Captioning AI
**Built by: Nishchal Soni**

An Image Captioning system that uses **ResNet-50** (a deep Convolutional Neural Network pretrained on ImageNet) to extract visual features from images, then generates natural English captions using a **rule-based Natural Language Generation (NLG)** template engine — combining Computer Vision and NLP exactly as the task requires.

> ✅ No Hugging Face Hub. No 1 GB downloads. Works offline after first run.

---

## 🧠 How It Works

```
Your Image (file or URL)
        │
        ▼
┌─────────────────────────┐
│   ResNet-50 (CNN)       │  ← Pre-trained on 1.2M ImageNet images
│   Feature Extraction    │    Recognises 1000 object categories
└──────────┬──────────────┘
           │  Top-5 class predictions + confidence scores
           ▼
┌─────────────────────────┐
│   Rule-Based NLG        │  ← Selects grammar-correct template
│   Caption Generator     │    Adds emoji hints for known objects
└──────────┬──────────────┘
           │
           ▼
  ✅ "This image contains a golden retriever. 🐶 [94.0% confidence]"
```

### Key concepts used
| Concept | Detail |
|---|---|
| **CNN (ResNet-50)** | 50-layer residual network; extracts deep visual features |
| **Transfer Learning** | Uses ImageNet pre-trained weights — no training needed |
| **Softmax** | Converts raw scores to probabilities across 1000 classes |
| **Top-K prediction** | Returns the 5 most likely labels with confidence |
| **Rule-based NLG** | Fills caption templates with correct grammar (a/an, emoji) |

---

## 📦 Installation

### Requirements
- Python 3.7+
- pip packages:

```bash
pip install torch torchvision pillow
```

> **First run** downloads ResNet-50 weights (~100 MB) into `~/.cache/torch/` and ImageNet labels (~30 KB). Every run after that is instant — no internet needed.

---

## 🚀 How to Run

### Mode 1 — Interactive (recommended for beginners)
Type image paths or URLs one by one:
```bash
python image_captioning.py
```
```
  Image path / URL: C:\Users\yuvi2\Downloads\dog.jpg
  Image path / URL: https://upload.wikimedia.org/wikipedia/commons/a/a7/Camponotus_flavomarginatus_ant.jpg
  Image path / URL: quit
```

### Mode 2 — Single image file
```bash
python image_captioning.py photo.jpg
python image_captioning.py C:\Users\yuvi2\Downloads\cat.png
```

### Mode 3 — Image from URL
```bash
python image_captioning.py https://example.com/image.jpg
```

### Mode 4 — Demo (no image or model needed)
```bash
python image_captioning.py --demo
```

### Help
```bash
python image_captioning.py --help
```

---

## 🖥️ Example Output

### Single image
```
====================================================
  IMAGE CAPTIONING AI — Built by Nishchal Soni
  Model : ResNet-50 (torchvision, ~100 MB cache)
====================================================

  Loading ResNet-50 (cached after first run) … ready ✅

  Top-5 predictions:
    1. golden retriever          94.0%  ██████████████████████████████
    2. Labrador retriever         3.2%  █
    3. kuvasz                     1.1%  
    4. clumber                    0.9%  
    5. Sussex spaniel             0.4%  

  ✅ Caption: This image contains a golden retriever. 🐶  [94.0% confidence]
```

### Demo mode
```
  Label  : espresso
  Caption: The picture displays an espresso. ☕  [87.0% confidence]

  Label  : acoustic guitar
  Caption: This appears to be an acoustic guitar. 🎸  [76.0% confidence]
```

---

## 📁 File Structure

```
image_captioning.py
│
├── TEMPLATES[]           — 7 caption sentence templates
├── SCENE_HINTS{}         — label → emoji mapping (20+ categories)
├── article()             — picks "a" or "an" grammatically
├── get_emoji()           — matches label to relevant emoji
├── rule_based_caption()  — fills template with label + confidence
│
├── load_imagenet_labels()— downloads 1000 class names (~30 KB, once)
├── load_image()          — opens image from file path OR URL
├── caption_image()       — full pipeline: load → infer → caption
│
├── interactive_mode()    — loads model once, captions many images
├── demo_mode()           — runs without model or image files
└── main()                — CLI argument parser & entry point
```

---

## 🗂️ Supported Image Formats

| Format | Extensions |
|---|---|
| JPEG | `.jpg`, `.jpeg` |
| PNG | `.png` |
| BMP | `.bmp` |
| WebP | `.webp` |
| GIF | `.gif` (first frame) |

---

## ⚡ Performance Tips

- **Interactive mode** is fastest for multiple images — the model loads only once and captions every image you type in.
- **Cached weights** mean the second run is much faster than the first.
- Images can be any size — they are automatically resized to 224×224 for the model.

---

## ❓ Troubleshooting

| Problem | Fix |
|---|---|
| `ModuleNotFoundError: PIL` | `pip install pillow` |
| `ModuleNotFoundError: torch` | `pip install torch torchvision` |
| `FileNotFoundError` | Check the file path — use full path if needed |
| `urllib.error` on labels | Check internet connection for first run |
| Slow first run | Normal — ResNet-50 weights (~100 MB) download once |

---

## 💡 Key Concepts Learned

- **Convolutional Neural Networks** — how ResNet-50 sees images layer by layer
- **Residual connections** — why ResNet-50 trains deeper than earlier CNNs
- **Transfer Learning** — reusing ImageNet weights without retraining
- **Softmax & Top-K** — converting raw scores to ranked probabilities
- **Rule-based NLG** — generating grammatically correct captions from structured data
- **CV + NLP pipeline** — linking vision output to language generation

---

## 🛠️ Customisation Ideas

- Add more templates to `TEMPLATES[]` for more varied captions
- Extend `SCENE_HINTS{}` with more emoji mappings
- Add a **GUI** with `tkinter` or a web UI with `Flask`/`Streamlit`
- Process an **entire folder** of images in batch
- Save captions to a `.csv` or `.json` report file

---

## 📋 Quick Reference Card

```
python image_captioning.py                  → interactive mode
python image_captioning.py image.jpg        → caption one file
python image_captioning.py https://...      → caption from URL
python image_captioning.py --demo           → demo, no model needed
python image_captioning.py --help           → show all options
```

---

*Task 3 — AI Internship Project | Built by Nishchal Soni*

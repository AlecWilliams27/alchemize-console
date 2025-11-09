<!-- Banner -->
<p align="center">
  <img src="assets/banner_alchemize.png" alt="Alchemize – Emotional Transmutation Console" width="100%" />
</p>

<h1 align="center">🧪 Alchemize — Emotional Transmutation Console</h1>
<p align="center">
  Turn emotions into <b>gold</b> right from your terminal. Shadow → purpose. Light → momentum.
</p>

<p align="center">
  <!-- Badges -->
  <a href="https://www.python.org/"><img alt="Python" src="https://img.shields.io/badge/Python-3.8%2B-3776AB?logo=python&logoColor=white"></a>
  <img alt="Platform" src="https://img.shields.io/badge/Platform-macOS%20%7C%20Windows%20%7C%20Linux-555">
  <img alt="License" src="https://img.shields.io/badge/License-MIT-green">
  <img alt="Type" src="https://img.shields.io/badge/Type-CLI-blue">
  <img alt="Made with Love" src="https://img.shields.io/badge/Made%20with-%F0%9F%92%9C-ff69b4">
</p>

<p align="center">
  <a href="#-demo">Demo</a> •
  <a href="#-features">Features</a> •
  <a href="#-installation">Installation</a> •
  <a href="#%EF%B8%8F-usage">Usage</a> •
  <a href="#-concept">Concept</a> •
  <a href="#-roadmap">Roadmap</a>
</p>

---

## ✨ Overview
**Alchemize** is a Python-based CLI that guides you through an animated, color-coded journey to transform (🌑 Shadow) or amplify (🌞 Light) emotions.  
It blends UX storytelling, ANSI styling, and timed progress to create a cinematic, meditative terminal experience.

- 🌑 **Shadow Mode**: pain → purpose • fear → courage • doubt → confidence • anger → focus  
- 🌞 **Light Mode**: joy → gratitude • love → compassion • peace → clarity • gratitude → abundance • confidence → momentum • hope → direction  

---

## 🎥 Demo
Add a short GIF to bring it to life:
```text
<p align="center"> <img src="assets/alchemy_demo.gif" alt="Alchemize demo" width="85%"/> </p>

⭐ Features
Animated progress bars + smooth typing effects
Shadow vs Light detection with themed banners
Built-in synonym mapping (“hurt” → pain, “happy” → joy, etc.)
Quick menu shortcuts: m (menu), q (quit)
Adjustable speed coefficient for animation pacing

⚙️ Installation
# Option A: Install directly from the folder
pip install .

# Option B: Editable (development) install
pip install -e .
Requires Python 3.8+.
On macOS, use python3 and optionally a virtual environment.

🧭 Project Structure
alchemize/
├─ alchemize/
│  ├─ __init__.py
│  └─ __main__.py
├─ README.md
├─ pyproject.toml
└─ assets/
   ├─ banner_alchemize.png   # top banner (recommended 2000x500)
   └─ alchemy_demo.gif       # short looping demo

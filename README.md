# 🔥 Fire & Ice — Magic Hand Particle System ❄️

<div align="center">

<img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=22&pause=1000&color=FF4500&center=true&vCenter=true&width=600&lines=Real-time+Hand+Tracking+Particle+Magic;Left+Hand+%3D+FIRE+%F0%9F%94%A5;Right+Hand+%3D+ICE+%E2%9D%84%EF%B8%8F;Both+Hands+%3D+FUSION+%E2%9A%A1" alt="Typing SVG" />

<br/>

![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-4.7%2B-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)
![MediaPipe](https://img.shields.io/badge/MediaPipe-0.10.8-FF6F00?style=for-the-badge&logo=google&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-Latest-013243?style=for-the-badge&logo=numpy&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-22C55E?style=for-the-badge)
![Stars](https://img.shields.io/github/stars/upendra8690/fire-ice-write?style=for-the-badge&color=FFD700)

<br/>

> **Left Hand = 🔥 FIRE · Right Hand = ❄️ ICE · Both Hands Close = ⚡ FUSION**
>
> *6,000 real-time particles. Zero game engine. Pure Python.*

</div>

---

## 🎬 Demo

<div align="center">

https://github.com/upendra8690/fire-ice-write/assets/Fire_Ice_BANGER.mp4

> 🎵 *Fire & Ice Magic — real-time hand tracking with epic BGM*

</div>

---

## ✨ What Makes This Special

| Feature | Description |
|---|---|
| 🔥 **Fire mode** | Left hand → 6,000 blazing particles with upward drift physics |
| ❄️ **Ice mode** | Right hand → shimmering crystalline particles with lateral shimmer |
| ⚡ **Fusion mode** | Bring both hands within 180px → epic dual-spiral collision |
| ✍️ **Air drawing** | Point index finger → draw glowing trails that persist on screen |
| 💥 **Fist explode** | Close your fist → particles blast outward dramatically |
| 🌌 **Star field** | 300 twinkling ambient stars in the background (toggle `B`) |
| 🎨 **3 live themes** | Switch colour palettes on the fly — keys `1`, `2`, `3` |
| 📸 **Screenshots** | Save any frame with `S` → auto-saved to `screenshots/` folder |
| ⛶ **Fullscreen** | Instant fullscreen with `F` |
| ⏱️ **Live HUD** | Real-time FPS counter, session timer, per-hand gesture labels |

---

## 🚀 Quick Start

```bash
# 1. Clone the repo
git clone https://github.com/upendra8690/fire-ice-write.git
cd fire-ice-write

# 2. Create a virtual environment
python -m venv venv
.\venv\Scripts\Activate.ps1   # Windows
# source venv/bin/activate    # macOS / Linux

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run it!
python main.py
```

> ⚠️ **Important:** Use exactly `mediapipe==0.10.8` + `protobuf==3.20.3` for stability.

---

## 🎮 Controls

```
┌──────────────────────────────────────────────────────┐
│  GESTURE               │  ACTION                     │
├────────────────────────┼─────────────────────────────┤
│  Left hand in frame    │  🔥 Fire particles          │
│  Right hand in frame   │  ❄️  Ice particles           │
│  Both hands close      │  ⚡ Fusion mode             │
│  Point index finger    │  ✍️  Air-draw glowing trails │
│  Close fist            │  💥 Explode particles       │
│  Open palm             │  🌀 Calm orbit mode         │
├────────────────────────┼─────────────────────────────┤
│  Q                     │  Quit                       │
│  R                     │  Reset particles & canvas   │
│  S                     │  Save screenshot            │
│  F                     │  Toggle fullscreen          │
│  B                     │  Toggle star-field          │
│  1 / 2 / 3             │  Switch colour theme        │
└──────────────────────────────────────────────────────┘
```

---

## 🛠️ How It Works

```
📷 Webcam Frame
      │
      ▼
🤖 MediaPipe Hands ──► 21 landmark points per hand
      │
      ▼
👋 Gesture Classifier ──► write / fist / open / neutral
      │
      ▼
⚛️  Particle System (6,000 particles)
      ├── Orbit force    → particles spiral around hand
      ├── Shell force    → maintains ideal orbit radius
      ├── Element drift  → fire rises UP, ice shimmers SIDEWAYS
      ├── Comet tails    → 4-frame position history per particle
      └── Fusion mode    → dual-hand spiral collision
      │
      ▼
🖼️  Layer Compositing
      ├── Dark camera feed  (30% brightness)
      ├── Star field layer  (300 twinkling stars)
      ├── Canvas layer      (persistent air-drawn trails)
      └── Particle layer    (main glow)
      │
      ▼
📊 HUD Overlay ──► Final output window
```

---

## 📦 Requirements

```
opencv-python
mediapipe==0.10.8
numpy
protobuf==3.20.3
```

---

## 🔧 Troubleshooting

| Problem | Solution |
|---|---|
| `ModuleNotFoundError: cv2` | Run `pip install opencv-python` inside your **venv** |
| `module 'mediapipe' has no attribute 'solutions'` | Run `pip install mediapipe==0.10.8 protobuf==3.20.3` |
| Camera not found | Try `cv2.VideoCapture(1)` if you have multiple cameras |
| Low FPS | Reduce `PARTICLE_COUNT` in `main.py` to `3000` |

---

## 👨‍💻 Author

<div align="center">

**Mopuru Upendra Reddy**

[![GitHub](https://img.shields.io/badge/GitHub-upendra8690-181717?style=for-the-badge&logo=github)](https://github.com/upendra8690)

*"Built with Python, physics math, and zero game engines."*

</div>

---

## 🙏 Acknowledgements

- [MediaPipe](https://mediapipe.dev/) by Google — real-time hand landmark detection
- [OpenCV](https://opencv.org/) — computer vision and rendering

---

<div align="center">

⭐ **If this project impressed you, drop a star!** ⭐

</div>

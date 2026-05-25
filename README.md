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

> 📹 **[Watch Demo Video](https://github.com/upendra8690/fire-ice-write)** — Fire, Ice & Fusion in action!

<!-- Replace with your actual demo GIF after recording -->
<!-- ![Demo GIF](demo.gif) -->

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

## 📁 Project Structure

```
fire-ice-write/
│
├── main.py              # 🚀 Entry point — run this!
├── particle.py          # ⚛️  Particle class + physics engine
├── gesture.py           # 👋 Gesture classifier (fist / write / open / neutral)
├── renderer.py          # 🖼️  Layer compositor + glow renderer
├── hud.py               # 📊 HUD overlay (FPS, timer, labels)
├── themes.py            # 🎨 Colour theme definitions (3 themes)
├── stars.py             # 🌌 Star field generator + twinkle logic
├── requirements.txt     # 📦 Python dependencies
├── screenshots/         # 📸 Auto-saved screenshots go here
└── README.md            # 📖 You are here
```

---

## 📦 Requirements

```
opencv-python
mediapipe==0.10.8
numpy
protobuf==3.20.3
```

Install all at once:

```bash
pip install opencv-python mediapipe==0.10.8 numpy protobuf==3.20.3
```

---

## 💻 Full Source Code

### `requirements.txt`

```
opencv-python
mediapipe==0.10.8
numpy
protobuf==3.20.3
```

---

### `themes.py`

```python
# themes.py — Colour palette definitions for Fire, Ice, and Fusion modes

THEMES = {
    1: {
        "name": "Inferno",
        "fire":  [(255, 80,  0),   (255, 160, 0),  (255, 220, 60), (255, 255, 180)],
        "ice":   [(0,  200, 255),  (80, 230, 255),  (180, 245, 255),(255, 255, 255)],
        "fusion":[(255, 80,  200), (180, 0,  255),  (80,  80, 255), (255, 255, 255)],
        "star":  (200, 200, 255),
        "bg_dim": 0.30,
    },
    2: {
        "name": "Neon",
        "fire":  [(255, 0,   80),  (255, 80,  0),   (255, 200, 0),  (255, 255, 100)],
        "ice":   [(0,  255, 180),  (0,  200, 255),  (100, 100, 255),(255, 255, 255)],
        "fusion":[(255, 0,  255),  (128, 0,  255),  (0,  128, 255), (255, 255, 255)],
        "star":  (180, 255, 180),
        "bg_dim": 0.25,
    },
    3: {
        "name": "Cosmic",
        "fire":  [(180, 0,   255), (255, 0,  180),  (255, 100, 80), (255, 220, 180)],
        "ice":   [(0,  180, 255),  (0,  255, 220),  (180, 255, 255),(255, 255, 255)],
        "fusion":[(255, 180, 0),   (255, 255, 0),   (180, 255, 0),  (255, 255, 255)],
        "star":  (255, 200, 100),
        "bg_dim": 0.20,
    },
}
```

---

### `gesture.py`

```python
# gesture.py — Classify hand gestures from MediaPipe landmarks

def classify_gesture(hand_landmarks, handedness_label):
    """
    Returns: 'write' | 'fist' | 'open' | 'neutral'
    """
    lm = hand_landmarks.landmark

    # Finger tip and pip (knuckle) landmark indices
    tips = [8, 12, 16, 20]   # index, middle, ring, pinky tips
    pips = [6, 10, 14, 18]   # corresponding PIP joints

    fingers_up = [lm[tip].y < lm[pip].y for tip, pip in zip(tips, pips)]
    thumb_up   = lm[4].x < lm[3].x if handedness_label == "Right" else lm[4].x > lm[3].x

    n_up = sum(fingers_up)

    # ✍️ Write: only index finger extended
    if fingers_up[0] and not any(fingers_up[1:]):
        return "write"

    # 💥 Fist: all fingers curled
    if n_up == 0 and not thumb_up:
        return "fist"

    # 🌀 Open palm: all fingers extended
    if n_up >= 3:
        return "open"

    return "neutral"
```

---

### `stars.py`

```python
# stars.py — Twinkling star field

import numpy as np
import cv2
import random

class StarField:
    def __init__(self, count=300, width=1280, height=720):
        self.width  = width
        self.height = height
        self.stars  = [
            {
                "x":         random.randint(0, width  - 1),
                "y":         random.randint(0, height - 1),
                "base_r":    random.randint(1, 3),
                "phase":     random.uniform(0, 2 * np.pi),
                "speed":     random.uniform(0.05, 0.15),
                "color":     random.choice([
                                 (255, 255, 255),
                                 (200, 220, 255),
                                 (255, 240, 200),
                             ]),
            }
            for _ in range(count)
        ]
        self.t = 0.0

    def draw(self, frame):
        self.t += 1
        for s in self.stars:
            brightness = 0.5 + 0.5 * np.sin(s["phase"] + self.t * s["speed"])
            r = max(1, int(s["base_r"] * brightness))
            color = tuple(int(c * brightness) for c in s["color"])
            cv2.circle(frame, (s["x"], s["y"]), r, color, -1)
        return frame
```

---

### `particle.py`

```python
# particle.py — Particle physics engine

import numpy as np
import random
import cv2

class Particle:
    def __init__(self, x, y, element="fire"):
        self.x       = x + random.uniform(-60, 60)
        self.y       = y + random.uniform(-60, 60)
        self.vx      = random.uniform(-1.5, 1.5)
        self.vy      = random.uniform(-1.5, 1.5)
        self.element = element
        self.life    = random.uniform(0.6, 1.0)
        self.decay   = random.uniform(0.008, 0.018)
        self.radius  = random.uniform(60, 130)
        self.angle   = random.uniform(0, 2 * np.pi)
        self.history = []                              # comet tail positions

    def update(self, target_x, target_y, element, fusion=False, other_x=None, other_y=None):
        self.element = element

        # --- Orbit + shell forces ---
        dx = target_x - self.x
        dy = target_y - self.y
        dist = max(1, np.hypot(dx, dy))

        orbit_strength = 0.012
        shell_strength = 0.008
        tangent_x = -dy / dist
        tangent_y =  dx / dist

        self.vx += tangent_x * orbit_strength + (dx / dist) * shell_strength * (1 - dist / self.radius)
        self.vy += tangent_y * orbit_strength + (dy / dist) * shell_strength * (1 - dist / self.radius)

        # --- Element drift ---
        if element == "fire":
            self.vy -= 0.06                            # fire rises
        elif element == "ice":
            self.vx += np.sin(self.angle) * 0.04      # ice shimmers
            self.angle += 0.05

        # --- Fusion spiral pull toward other hand ---
        if fusion and other_x is not None:
            fx = other_x - self.x
            fy = other_y - self.y
            fd = max(1, np.hypot(fx, fy))
            self.vx += (fx / fd) * 0.015
            self.vy += (fy / fd) * 0.015

        # --- Damping + integrate ---
        self.vx *= 0.92
        self.vy *= 0.92
        self.history.append((int(self.x), int(self.y)))
        if len(self.history) > 4:
            self.history.pop(0)
        self.x += self.vx
        self.y += self.vy
        self.life -= self.decay

    def explode(self):
        angle = random.uniform(0, 2 * np.pi)
        speed = random.uniform(4, 14)
        self.vx = np.cos(angle) * speed
        self.vy = np.sin(angle) * speed
        self.life = random.uniform(0.4, 0.8)

    def is_alive(self):
        return self.life > 0

    def draw(self, frame, theme):
        if not self.is_alive():
            return
        colors = theme[self.element]
        idx    = min(int((1 - self.life) * len(colors)), len(colors) - 1)
        color  = colors[idx]
        alpha  = self.life

        # Comet tail
        for i, (hx, hy) in enumerate(self.history):
            tail_alpha = (i / len(self.history)) * alpha * 0.5
            r = max(1, int(2 * tail_alpha))
            tail_color = tuple(int(c * tail_alpha) for c in color)
            if 0 <= hx < frame.shape[1] and 0 <= hy < frame.shape[0]:
                cv2.circle(frame, (hx, hy), r, tail_color, -1)

        # Main glow (3 layers)
        px, py = int(self.x), int(self.y)
        if 0 <= px < frame.shape[1] and 0 <= py < frame.shape[0]:
            for radius, a_factor in [(5, 0.15), (3, 0.4), (2, 1.0)]:
                glow_color = tuple(int(c * alpha * a_factor) for c in color)
                cv2.circle(frame, (px, py), radius, glow_color, -1)


class ParticleSystem:
    def __init__(self, count=6000):
        self.count     = count
        self.particles = []

    def spawn(self, x, y, element):
        while len(self.particles) < self.count:
            self.particles.append(Particle(x, y, element))
        # Respawn dead particles near hand
        for p in self.particles:
            if not p.is_alive():
                p.__init__(x, y, element)

    def update(self, hands_data, fusion):
        """
        hands_data: list of dicts with keys: x, y, element, other_x, other_y
        """
        for p in self.particles:
            if not hands_data:
                p.life -= p.decay
                continue
            # Each particle tracks the nearest hand
            target = min(hands_data, key=lambda h: np.hypot(h["x"] - p.x, h["y"] - p.y))
            p.update(
                target["x"], target["y"], target["element"],
                fusion=fusion,
                other_x=target.get("other_x"),
                other_y=target.get("other_y"),
            )

    def explode_all(self):
        for p in self.particles:
            p.explode()

    def draw(self, frame, theme):
        for p in self.particles:
            p.draw(frame, theme)

    def reset(self):
        self.particles.clear()
```

---

### `hud.py`

```python
# hud.py — On-screen HUD overlay

import cv2
import time

class HUD:
    def __init__(self):
        self.start_time = time.time()
        self.font       = cv2.FONT_HERSHEY_SIMPLEX

    def draw(self, frame, fps, theme_name, stars_on, gesture_labels):
        h, w = frame.shape[:2]
        elapsed = int(time.time() - self.start_time)
        mm, ss = divmod(elapsed, 60)

        # Top-right: FPS + timer + theme
        info = f"FPS {fps:.0f}  T:{mm:02d}:{ss:02d}  Theme {theme_name}  Stars {'ON' if stars_on else 'OFF'}"
        cv2.putText(frame, info, (w - 420, 30), self.font, 0.55, (200, 200, 200), 1, cv2.LINE_AA)

        # Top-left: gesture labels per hand
        for i, label in enumerate(gesture_labels):
            cv2.putText(frame, label, (15, 30 + i * 28), self.font, 0.65, (100, 255, 100), 1, cv2.LINE_AA)

        # Bottom: controls legend
        legend = "Left:FIRE  Right:ICE  Point:Draw  Fist:Explode  Both close:FUSION"
        cv2.putText(frame, legend, (15, h - 30), self.font, 0.48, (160, 160, 160), 1, cv2.LINE_AA)
        controls = "Q Quit  R reset  S screenshot  F fullscreen  1/2/3 theme  B stars"
        cv2.putText(frame, controls, (15, h - 10), self.font, 0.38, (120, 120, 120), 1, cv2.LINE_AA)

        return frame
```

---

### `renderer.py`

```python
# renderer.py — Layer compositor + additive glow blending

import cv2
import numpy as np


def composite(camera_frame, particle_layer, canvas_layer, bg_dim):
    """
    Blend: dark camera + persistent canvas trails + particle glow (additive).
    """
    dark_cam = (camera_frame * bg_dim).astype(np.uint8)
    result   = cv2.add(dark_cam, canvas_layer)
    result   = cv2.add(result,   particle_layer)
    return result


def apply_glow(frame):
    """Cheap bloom: blur a bright copy and add back."""
    bright = cv2.threshold(frame, 80, 255, cv2.THRESH_TOZERO)[1]
    bloom  = cv2.GaussianBlur(bright, (21, 21), 0)
    return cv2.add(frame, bloom)


class AirCanvas:
    """Persistent drawing layer for index-finger trails."""

    def __init__(self, shape):
        self.canvas    = np.zeros(shape, dtype=np.uint8)
        self.last_pt   = {}      # hand id → last point
        self.fade_mask = np.full(shape[:2], 0.997)   # very slow fade

    def draw(self, hand_id, x, y, color):
        if hand_id in self.last_pt:
            cv2.line(self.canvas, self.last_pt[hand_id], (x, y), color, 3)
        self.last_pt[hand_id] = (x, y)

    def stop(self, hand_id):
        self.last_pt.pop(hand_id, None)

    def update(self):
        """Slowly fade old strokes."""
        self.canvas = (self.canvas * 0.997).astype(np.uint8)

    def reset(self):
        self.canvas[:] = 0
        self.last_pt.clear()
```

---

### `main.py`

```python
# main.py — Fire & Ice Magic Hand Particle System
# Author: Mopuru Upendra Reddy  (github.com/upendra8690)
# "Built with Python, physics math, and zero game engines."

import cv2
import numpy as np
import mediapipe as mp
import time
import os

from particle  import ParticleSystem
from gesture   import classify_gesture
from stars     import StarField
from hud       import HUD
from renderer  import composite, apply_glow, AirCanvas
from themes    import THEMES

# ─── CONFIG ────────────────────────────────────────────────────────────────────
PARTICLE_COUNT = 6000
FUSION_DIST    = 180       # px — distance that triggers fusion mode
WINDOW_NAME    = "🔥 Fire & Ice Magic ❄️"
SCREENSHOT_DIR = "screenshots"
os.makedirs(SCREENSHOT_DIR, exist_ok=True)

# ─── INIT ──────────────────────────────────────────────────────────────────────
mp_hands   = mp.solutions.hands
hands_sol  = mp_hands.Hands(max_num_hands=2, min_detection_confidence=0.7,
                             min_tracking_confidence=0.6)

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    cap = cv2.VideoCapture(1)

ret, frame = cap.read()
H, W = frame.shape[:2]

particles  = ParticleSystem(PARTICLE_COUNT)
stars      = StarField(300, W, H)
hud        = HUD()
canvas     = AirCanvas((H, W, 3))

theme_id   = 1
stars_on   = True
fullscreen = False
screenshot_n = 0

prev_time  = time.time()

cv2.namedWindow(WINDOW_NAME, cv2.WINDOW_NORMAL)
cv2.resizeWindow(WINDOW_NAME, W, H)

# ─── MAIN LOOP ─────────────────────────────────────────────────────────────────
while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    rgb   = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    res   = hands_sol.process(rgb)

    theme        = THEMES[theme_id]
    hands_data   = []
    gesture_labels = []
    hand_centers = []

    # ── Parse detected hands ───────────────────────────────────────────────────
    if res.multi_hand_landmarks:
        for idx, (lm, handed) in enumerate(
                zip(res.multi_hand_landmarks, res.multi_handedness)):

            label    = handed.classification[0].label   # "Left" or "Right"
            element  = "fire" if label == "Left" else "ice"
            gesture  = classify_gesture(lm, label)

            cx = int(lm.landmark[9].x * W)
            cy = int(lm.landmark[9].y * H)
            hand_centers.append((cx, cy))
            gesture_labels.append(f"{len(gesture_labels)+1} Hand: {label.upper()} — {gesture.upper()}")

            if gesture == "fist":
                particles.explode_all()
                canvas.stop(idx)

            elif gesture == "write":
                tip_x = int(lm.landmark[8].x * W)
                tip_y = int(lm.landmark[8].y * H)
                color = theme["fire"][1] if element == "fire" else theme["ice"][1]
                canvas.draw(idx, tip_x, tip_y, color)

            else:
                canvas.stop(idx)

            particles.spawn(cx, cy, element)
            hands_data.append({"x": cx, "y": cy, "element": element})

        # Set cross-hand references for fusion
        if len(hand_centers) == 2:
            for i in range(2):
                hands_data[i]["other_x"] = hand_centers[1 - i][0]
                hands_data[i]["other_y"] = hand_centers[1 - i][1]

    # ── Fusion detection ───────────────────────────────────────────────────────
    fusion = False
    if len(hand_centers) == 2:
        dx = hand_centers[0][0] - hand_centers[1][0]
        dy = hand_centers[0][1] - hand_centers[1][1]
        if np.hypot(dx, dy) < FUSION_DIST:
            fusion = True
            for d in hands_data:
                d["element"] = "fusion"

    # ── Update systems ─────────────────────────────────────────────────────────
    particles.update(hands_data, fusion)
    canvas.update()

    # ── Render layers ──────────────────────────────────────────────────────────
    particle_layer = np.zeros_like(frame)
    particles.draw(particle_layer, theme)

    if stars_on:
        star_layer = np.zeros_like(frame)
        stars.draw(star_layer)
        particle_layer = cv2.add(particle_layer, star_layer)

    output = composite(frame, particle_layer, canvas.canvas, theme["bg_dim"])
    output = apply_glow(output)

    # ── FPS ────────────────────────────────────────────────────────────────────
    now  = time.time()
    fps  = 1.0 / max(now - prev_time, 1e-6)
    prev_time = now

    hud.draw(output, fps, theme["name"], stars_on, gesture_labels)

    cv2.imshow(WINDOW_NAME, output)

    # ── Key handling ───────────────────────────────────────────────────────────
    key = cv2.waitKey(1) & 0xFF

    if key == ord('q'):
        break

    elif key == ord('r'):
        particles.reset()
        canvas.reset()

    elif key == ord('s'):
        screenshot_n += 1
        path = os.path.join(SCREENSHOT_DIR, f"screenshot_{screenshot_n:04d}.png")
        cv2.imwrite(path, output)
        print(f"📸 Saved {path}")

    elif key == ord('f'):
        fullscreen = not fullscreen
        flag = cv2.WINDOW_FULLSCREEN if fullscreen else cv2.WINDOW_NORMAL
        cv2.setWindowProperty(WINDOW_NAME, cv2.WND_PROP_FULLSCREEN,
                              cv2.WINDOW_FULLSCREEN if fullscreen else cv2.WINDOW_NORMAL)

    elif key == ord('b'):
        stars_on = not stars_on

    elif key in (ord('1'), ord('2'), ord('3')):
        theme_id = int(chr(key))

# ─── CLEANUP ───────────────────────────────────────────────────────────────────
cap.release()
cv2.destroyAllWindows()
```

---

## 🔧 Troubleshooting

| Problem | Solution |
|---|---|
| `ModuleNotFoundError: cv2` | Run `pip install opencv-python` inside your **venv** |
| `module 'mediapipe' has no attribute 'solutions'` | Run `pip install mediapipe==0.10.8 protobuf==3.20.3` |
| Camera not found | Try `cv2.VideoCapture(1)` if you have multiple cameras |
| Low FPS | Reduce `PARTICLE_COUNT` in `main.py` to `3000` |
| Black screen | Make sure your webcam is not used by another app |
| Particles flicker | Lower `min_tracking_confidence` to `0.5` in `main.py` |

---

## 🚀 Performance Tips

- **Target 30+ FPS** → set `PARTICLE_COUNT = 4000`
- **Target 60 FPS** → set `PARTICLE_COUNT = 2000` and disable stars (`stars_on = False`)
- **Best quality** → run at `PARTICLE_COUNT = 6000` on a machine with a dedicated GPU

---

## 🗺️ Roadmap

- [ ] 🌊 Water element (right hand wave gesture)
- [ ] ⚡ Thunder element (double-tap fusion)
- [ ] 🎵 Audio-reactive particles (mic input)
- [ ] 🕹️ OBS Virtual Camera output for live streaming
- [ ] 🌐 WebRTC browser version

---

## 📜 License

```
MIT License — free to use, modify, and share.
Just give credit. ⭐
```

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
- [OpenCV](https://opencv.org/) — computer vision and rendering pipeline
- [NumPy](https://numpy.org/) — physics math backbone

---

<div align="center">

⭐ **If this project impressed you, drop a star!** ⭐

</div>

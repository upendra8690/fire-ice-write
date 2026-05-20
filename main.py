"""
╔══════════════════════════════════════════════════════════════╗
║         🔥 FIRE & ICE — Magic Hand Particle System ❄️         ║
║         Enhanced Edition — by Mopuru Upendra Reddy        ║
╚══════════════════════════════════════════════════════════════╝
Controls:
  • Left Hand  → FIRE particles (red/orange/yellow)
  • Right Hand → ICE particles  (blue/cyan/white)
  • Point index finger → WRITING mode (draw glowing trails)
  • Both hands together → FUSION mode (epic spiral collision!)
  • Q → quit   R → reset   S → screenshot   F → fullscreen
  • 1/2/3 → Switch themes   B → toggle background star-field
"""

import cv2
import mediapipe as mp
import numpy as np
import math
import random
import time
import os

# ──────────────────────────────────────────────
#  TUNING CONSTANTS
# ──────────────────────────────────────────────
PARTICLE_COUNT   = 6000
HAND_RADIUS      = 180
IDEAL_ORBIT_R    = 80
ORBIT_FORCE      = 0.75
REPEL_FORCE      = 0.015
NOISE_F          = 1.0
DAMPING          = 0.90
HAND_DAMPING     = 0.90
MAX_SPEED        = 6.0
HAND_SPEED       = 15.0
SMOOTH           = 0.18
TRAIL_FADE       = 0.85
CANVAS_FADE      = 0.99
CAM_BRIGHTNESS   = 0.30
SCREENSHOT_DIR   = "screenshots"

# ──────────────────────────────────────────────
#  COLOUR PALETTES (BGR format)
# ──────────────────────────────────────────────

# Theme 1 — Classic (default)
FIRE_PALETTES = {
    1: [(100,180,255),(80,120,255),(40,60,255),(20,40,220),(200,240,255)],  # deep fire
    2: [(0,150,255),(0,100,200),(0,200,255),(0,80,180),(50,220,255)],       # orange nova
    3: [(50,50,255),(30,30,200),(150,80,255),(200,100,255),(255,200,255)],  # purple plasma
}
ICE_PALETTES = {
    1: [(255,255,255),(255,240,240),(255,220,150),(255,120,120),(250,200,100)],  # classic ice
    2: [(255,230,100),(255,255,200),(200,255,255),(150,240,255),(255,255,255)],  # arctic white
    3: [(255,200,150),(255,170,80),(200,220,255),(180,255,255),(255,255,255)],   # glacier
}
FUSION_PALETTE = [
    (100,255,200),(50,255,150),(200,200,255),(255,100,200),(255,200,100),
]

mp_hands = mp.solutions.hands
PALM_IDS = [0, 5, 9, 13, 17]


# ──────────────────────────────────────────────
#  HELPER — gesture recognition
# ──────────────────────────────────────────────

def is_index_pointing(lm):
    index_up  = lm[8].y  < lm[6].y
    mid_down  = lm[12].y > lm[10].y
    ring_down = lm[16].y > lm[14].y
    pink_down = lm[20].y > lm[18].y
    return index_up and mid_down and ring_down and pink_down


def is_fist(lm):
    tips = [8, 12, 16, 20]
    pips = [6, 10, 14, 18]
    return all(lm[t].y > lm[p].y for t, p in zip(tips, pips))


def is_open_palm(lm):
    tips = [8, 12, 16, 20]
    mcps = [5,  9, 13, 17]
    return all(lm[t].y < lm[m].y for t, m in zip(tips, mcps))


def get_hand_gesture(lm):
    if is_index_pointing(lm):
        return "write"
    if is_fist(lm):
        return "fist"
    if is_open_palm(lm):
        return "open"
    return "neutral"


# ──────────────────────────────────────────────
#  STAR FIELD (ambient background)
# ──────────────────────────────────────────────

class Star:
    def __init__(self, W, H):
        self.W, self.H = W, H
        self.x = random.uniform(0, W)
        self.y = random.uniform(0, H)
        self.r = random.uniform(0.3, 1.5)
        self.phase = random.uniform(0, math.pi*2)
        self.speed = random.uniform(0.01, 0.04)
        self.base  = random.uniform(0.2, 0.6)

    def draw(self, frame):
        a = self.base + math.sin(self.phase) * 0.3
        self.phase += self.speed
        b = int(a * 255)
        cv2.circle(frame, (int(self.x), int(self.y)), int(self.r), (b, b, b), -1, cv2.LINE_AA)


# ──────────────────────────────────────────────
#  PARTICLE
# ──────────────────────────────────────────────

class Particle:
    def __init__(self, W, H, theme=1):
        self.W, self.H  = W, H
        self.theme      = theme
        self.element    = None
        self.color      = (255, 255, 255)
        self.fusion     = False
        self._spawn()

    def _spawn(self):
        self.x  = random.uniform(0, self.W)
        self.y  = random.uniform(0, self.H)
        self.vx = random.gauss(0, 0.6)
        self.vy = random.gauss(0, 0.6)
        self.size           = random.uniform(0.8, 2.2)
        self.original_alpha = random.uniform(0.6, 1.0)
        self.alpha_base     = self.original_alpha
        self.drift_ang      = random.uniform(0, math.pi*2)
        self.drift_rot      = random.uniform(0.005, 0.020) * random.choice([1,-1])
        self.twinkle        = random.uniform(0, math.pi*2)
        self.twinkle_sp     = random.uniform(0.04, 0.12)
        self.life           = 1.0   # used in burst mode
        self.tail           = []    # last N positions for comet tail

    def update(self, hands_info, fusion_active=False):
        self.twinkle   += self.twinkle_sp
        self.drift_ang += self.drift_rot

        if not hands_info:
            self.alpha_base = 0.0
            self.vx *= 0.5
            self.vy *= 0.5
            return False, 0.0

        self.alpha_base = self.original_alpha

        # Find closest hand
        best_d, best_hand = float('inf'), None
        for h in hands_info:
            tx, ty = (h['tip'] if h['gesture'] == 'write' else h['pos'])
            d = math.hypot(self.x - tx, self.y - ty)
            if d < best_d:
                best_d, best_hand = d, h

        tx, ty = (best_hand['tip'] if best_hand['gesture'] == 'write' else best_hand['pos'])
        dx = self.x - tx
        dy = self.y - ty
        d  = math.hypot(dx, dy) or 0.001

        # Assign element / colour
        new_elem = 'Fusion' if fusion_active else best_hand['element']
        if self.element != new_elem:
            self.element = new_elem
            if fusion_active:
                self.color = random.choice(FUSION_PALETTE)
            else:
                palette = FIRE_PALETTES[self.theme] if new_elem == 'Fire' else ICE_PALETTES[self.theme]
                self.color = random.choice(palette)
        self.fusion = fusion_active

        is_writing = (best_hand['gesture'] == 'write')
        is_fist_g  = (best_hand['gesture'] == 'fist')

        snap_r       = HAND_RADIUS * (0.4 if is_writing else 1.2)
        orbit_r      = IDEAL_ORBIT_R * (0.1 if is_writing else (2.0 if fusion_active else 1.0))
        logic_r      = HAND_RADIUS  * (0.5 if is_writing else 1.5)

        # Snap distant particles
        if d > snap_r:
            ang = random.uniform(0, math.pi*2)
            r_new = random.uniform(0, snap_r * 0.8)
            self.x = tx + math.cos(ang) * r_new
            self.y = ty + math.sin(ang) * r_new
            dx = self.x - tx
            dy = self.y - ty
            d  = math.hypot(dx, dy) or 0.001

        fx, fy     = 0.0, 0.0
        near_hand  = False

        if d < logic_r:
            near_hand = True
            nx, ny = dx/d, dy/d
            tx2, ty2 = -ny, nx

            t_str = ORBIT_FORCE * (1.0 - d/logic_r)
            if is_writing:    t_str *= 3.0
            if fusion_active: t_str *= 2.0
            fx += tx2 * t_str * 9.0
            fy += ty2 * t_str * 9.0

            shell_err = orbit_r - d
            rep = REPEL_FORCE * (5.0 if is_writing else 1.0)
            fx += nx * shell_err * rep
            fy += ny * shell_err * rep

            # Element-specific drift
            if self.element == 'Fire':
                fy -= 0.8          # fire rises
            elif self.element == 'Ice':
                fy += 0.4          # ice settles
                fx += random.gauss(0, 0.3)   # icy shimmer
            elif self.element == 'Fusion':
                ang2 = math.atan2(dy, dx) + 0.08
                fx += math.cos(ang2) * 1.5
                fy += math.sin(ang2) * 1.5

            # Fist = explode outward!
            if is_fist_g:
                fx += nx * 4.0
                fy += ny * 4.0

        fx += random.gauss(0, NOISE_F)
        fy += random.gauss(0, NOISE_F)

        self.vx += fx
        self.vy += fy

        damp = HAND_DAMPING if near_hand else DAMPING
        if is_writing:    damp *= 0.80
        if fusion_active: damp *= 0.85
        self.vx *= damp
        self.vy *= damp

        spd = math.hypot(self.vx, self.vy)
        cap = HAND_SPEED if near_hand else MAX_SPEED
        if spd > cap:
            self.vx = self.vx/spd * cap
            self.vy = self.vy/spd * cap

        # Comet tail
        self.tail.append((int(self.x), int(self.y)))
        if len(self.tail) > 4:
            self.tail.pop(0)

        self.x += self.vx
        self.y += self.vy

        return near_hand, spd

    def draw(self, layer, near_hand, spd):
        if self.alpha_base <= 0.01:
            return
        ix, iy = int(self.x), int(self.y)
        if not (0 <= ix < self.W and 0 <= iy < self.H):
            return

        twinkle  = 0.6 + math.sin(self.twinkle) * 0.4
        spd_frac = min(spd / HAND_SPEED, 1.0)
        a        = self.alpha_base * twinkle
        r        = max(1, int(self.size * (1.0 + spd_frac * 0.8)))

        # Comet tail
        if len(self.tail) >= 2:
            for i in range(len(self.tail)-1):
                ta = a * (i / len(self.tail)) * 0.4
                tc = tuple(int(c * ta * 0.3) for c in self.color)
                cv2.line(layer, self.tail[i], self.tail[i+1], tc, 1, cv2.LINE_AA)

        # Glow rings
        outer = tuple(int(c * a * 0.15) for c in self.color)
        mid   = tuple(int(c * a * 0.45) for c in self.color)
        core  = tuple(int(c * a)        for c in self.color)

        # Extra large aura for fusion
        if self.fusion:
            aura = tuple(int(c * a * 0.08) for c in self.color)
            cv2.circle(layer, (ix, iy), r*5, aura,  -1, cv2.LINE_AA)

        cv2.circle(layer, (ix, iy), r*3, outer, -1, cv2.LINE_AA)
        cv2.circle(layer, (ix, iy), r*2, mid,   -1, cv2.LINE_AA)
        cv2.circle(layer, (ix, iy), r,   core,  -1, cv2.LINE_AA)


# ──────────────────────────────────────────────
#  HUD overlay helpers
# ──────────────────────────────────────────────

def draw_rounded_rect(img, x1, y1, x2, y2, color, alpha=0.45, radius=12):
    overlay = img.copy()
    cv2.rectangle(overlay, (x1+radius, y1), (x2-radius, y2), color, -1)
    cv2.rectangle(overlay, (x1, y1+radius), (x2, y2-radius), color, -1)
    for cx, cy in [(x1+radius, y1+radius),(x2-radius, y1+radius),
                   (x1+radius, y2-radius),(x2-radius, y2-radius)]:
        cv2.circle(overlay, (cx, cy), radius, color, -1)
    cv2.addWeighted(overlay, alpha, img, 1-alpha, 0, img)


def put_text_shadow(img, text, pos, font, scale, color, thick=1):
    sx, sy = pos[0]+1, pos[1]+1
    cv2.putText(img, text, (sx, sy), font, scale, (0,0,0), thick+1, cv2.LINE_AA)
    cv2.putText(img, text, pos,      font, scale, color,   thick,   cv2.LINE_AA)


# ──────────────────────────────────────────────
#  MAIN
# ──────────────────────────────────────────────

def main():
    os.makedirs(SCREENSHOT_DIR, exist_ok=True)

    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH,  1280)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

    ret, probe = cap.read()
    if not ret:
        print("Camera not found. Check connection.")
        return

    H, W = probe.shape[:2]
    print(f"Camera: {W}x{H}")
    print("✨  Fire & Ice Magic — ENHANCED EDITION  ✨")
    print("Left: FIRE  |  Right: ICE  |  Both close: FUSION")
    print("Point index → draw  |  Fist → explode  |  Open palm → orbit")
    print("Q quit  R reset  S screenshot  F fullscreen  1/2/3 theme  B stars")

    theme        = 1
    show_stars   = True
    fullscreen   = False
    screenshot_n = 0
    fps_t        = time.time()
    fps_val      = 0.0
    frame_count  = 0
    session_start= time.time()

    particles      = [Particle(W, H, theme) for _ in range(PARTICLE_COUNT)]
    particle_layer = np.zeros((H, W, 3), dtype=np.uint8)
    canvas_layer   = np.zeros((H, W, 3), dtype=np.uint8)
    stars          = [Star(W, H) for _ in range(300)]
    star_layer     = np.zeros((H, W, 3), dtype=np.uint8)
    smooth_hands   = []

    hands_model = mp_hands.Hands(
        max_num_hands=2,
        model_complexity=1,
        min_detection_confidence=0.65,
        min_tracking_confidence=0.60,
    )

    cv2.namedWindow("Fire & Ice Magic", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Fire & Ice Magic", W, H)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1)
        frame_count += 1

        # FPS
        now = time.time()
        if now - fps_t >= 0.5:
            fps_val = frame_count / (now - fps_t)
            frame_count = 0
            fps_t = now

        # ── Hand detection ──
        rgb     = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands_model.process(rgb)

        raw_hands = []
        if results.multi_hand_landmarks and results.multi_handedness:
            for hand_lm, handedness in zip(results.multi_hand_landmarks, results.multi_handedness):
                label   = handedness.classification[0].label
                element = 'Fire' if label == 'Left' else 'Ice'
                lm      = hand_lm.landmark

                sx = sum(lm[i].x * W for i in PALM_IDS) / len(PALM_IDS)
                sy = sum(lm[i].y * H for i in PALM_IDS) / len(PALM_IDS)
                tx = lm[8].x * W
                ty = lm[8].y * H

                gesture = get_hand_gesture(lm)
                raw_hands.append({'pos':[sx,sy], 'tip':[tx,ty],
                                  'gesture':gesture, 'element':element})

        # ── Smooth hands ──
        new_smooth = []
        for raw in raw_hands:
            best_s, best_d2 = None, float('inf')
            for s in smooth_hands:
                if s['element'] == raw['element']:
                    d2 = math.hypot(s['pos'][0]-raw['pos'][0], s['pos'][1]-raw['pos'][1])
                    if d2 < best_d2:
                        best_d2, best_s = d2, s

            if best_s and best_d2 < 300:
                sp = [best_s['pos'][0] + (raw['pos'][0]-best_s['pos'][0])*SMOOTH,
                      best_s['pos'][1] + (raw['pos'][1]-best_s['pos'][1])*SMOOTH]
                tp = [best_s['tip'][0] + (raw['tip'][0]-best_s['tip'][0])*SMOOTH,
                      best_s['tip'][1] + (raw['tip'][1]-best_s['tip'][1])*SMOOTH]
                new_smooth.append({'pos':sp,'tip':tp,'gesture':raw['gesture'],'element':raw['element']})

                # Draw glowing trail when writing
                if raw['gesture'] == 'write' and best_s['gesture'] == 'write':
                    c_glow = FIRE_PALETTES[theme][2] if raw['element']=='Fire' else ICE_PALETTES[theme][2]
                    pt1 = (int(best_s['tip'][0]), int(best_s['tip'][1]))
                    pt2 = (int(tp[0]), int(tp[1]))
                    cv2.line(canvas_layer, pt1, pt2, c_glow, 18, cv2.LINE_AA)
                    cv2.line(canvas_layer, pt1, pt2, (255,255,255), 6, cv2.LINE_AA)
            else:
                new_smooth.append(raw)

        smooth_hands = new_smooth

        # ── Fusion detection ──
        fusion_active = False
        if len(smooth_hands) == 2:
            d_hands = math.hypot(smooth_hands[0]['pos'][0]-smooth_hands[1]['pos'][0],
                                  smooth_hands[0]['pos'][1]-smooth_hands[1]['pos'][1])
            fusion_active = d_hands < 180

        # ── Fade layers ──
        canvas_layer   = (canvas_layer   * CANVAS_FADE).astype(np.uint8)
        particle_layer = (particle_layer * TRAIL_FADE ).astype(np.uint8)

        # ── Update & draw particles ──
        n_hands = len(smooth_hands)
        for i, p in enumerate(particles):
            p.theme = theme
            assigned = [smooth_hands[i % n_hands]] if n_hands > 0 else []
            near, spd = p.update(assigned, fusion_active)
            p.draw(particle_layer, near, spd)

        # ── Stars ──
        if show_stars:
            star_layer[:] = 0
            for s in stars:
                s.draw(star_layer)

        # ── Compose final frame ──
        dark_cam = cv2.convertScaleAbs(frame, alpha=CAM_BRIGHTNESS, beta=0)
        if show_stars:
            dark_cam = cv2.add(dark_cam, star_layer)
        combo  = cv2.add(dark_cam, canvas_layer)
        output = cv2.add(combo,    particle_layer)

        # ── FUSION vignette flash ──
        if fusion_active:
            t_pulse = math.sin(time.time() * 8) * 0.5 + 0.5
            vign = np.zeros((H, W, 3), dtype=np.uint8)
            cy, cx = H//2, W//2
            for vy in range(0, H, 4):
                for vx in range(0, W, 4):
                    dist = math.hypot(vx-cx, vy-cy) / math.hypot(cx, cy)
                    if dist > 0.6:
                        alpha = min(1.0, (dist-0.6)/0.4) * t_pulse * 0.4
                        vign[vy,vx] = (int(100*alpha), int(200*alpha), int(100*alpha))
            output = cv2.add(output, cv2.blur(vign,(21,21)))

        # ── HUD ──
        elapsed = int(time.time() - session_start)
        mm, ss  = divmod(elapsed, 60)

        # Top bar
        draw_rounded_rect(output, 8, 8, 340, 52, (10,10,10), alpha=0.55)

        n = len(smooth_hands)
        if   n == 0:         label, lc = "No Hands Detected", (80,80,80)
        elif n == 1:         label, lc = f"1 Hand: {smooth_hands[0]['element']}", (80,220,80)
        elif fusion_active:  label, lc = "⚡ FUSION MODE ⚡", (80,255,180)
        else:                label, lc = "Both Hands Active", (80,220,200)

        if n > 0:
            gestures = " | ".join(h['gesture'].upper() for h in smooth_hands)
            put_text_shadow(output, gestures, (16, 46), cv2.FONT_HERSHEY_SIMPLEX, 0.42, (180,180,180))

        put_text_shadow(output, label, (16, 32), cv2.FONT_HERSHEY_SIMPLEX, 0.7, lc, 1)

        # Top-right info
        draw_rounded_rect(output, W-220, 8, W-8, 52, (10,10,10), alpha=0.55)
        put_text_shadow(output, f"FPS {fps_val:.0f}  T:{mm:02d}:{ss:02d}", (W-212, 32),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.55, (200,200,200))
        put_text_shadow(output, f"Theme {theme}  Stars {'ON' if show_stars else 'OFF'}", (W-212, 46),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.40, (130,130,130))

        # Bottom bar
        draw_rounded_rect(output, 8, H-56, W-8, H-8, (10,10,10), alpha=0.45)
        put_text_shadow(output,
            "Left:FIRE  Right:ICE  Point:Draw  Fist:Explode  Both close:FUSION",
            (16, H-36), cv2.FONT_HERSHEY_SIMPLEX, 0.50, (220,220,220))
        put_text_shadow(output,
            "Q quit  R reset  S screenshot  F fullscreen  1/2/3 theme  B stars",
            (16, H-16), cv2.FONT_HERSHEY_SIMPLEX, 0.40, (100,100,100))

        cv2.imshow("Fire & Ice Magic", output)

        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break
        elif key == ord('r'):
            particles      = [Particle(W, H, theme) for _ in range(PARTICLE_COUNT)]
            particle_layer = np.zeros((H, W, 3), dtype=np.uint8)
            canvas_layer   = np.zeros((H, W, 3), dtype=np.uint8)
            print("🔄 Reset!")
        elif key == ord('s'):
            fname = os.path.join(SCREENSHOT_DIR, f"fireice_{int(time.time())}.png")
            cv2.imwrite(fname, output)
            screenshot_n += 1
            print(f"📸 Screenshot saved: {fname}")
        elif key == ord('f'):
            fullscreen = not fullscreen
            flag = cv2.WINDOW_FULLSCREEN if fullscreen else cv2.WINDOW_NORMAL
            cv2.setWindowProperty("Fire & Ice Magic", cv2.WND_PROP_FULLSCREEN, flag)
        elif key == ord('b'):
            show_stars = not show_stars
            print(f"⭐ Stars {'ON' if show_stars else 'OFF'}")
        elif key in (ord('1'), ord('2'), ord('3')):
            theme = int(chr(key))
            for p in particles:
                p.theme   = theme
                p.element = None   # force palette reassign
            print(f"🎨 Theme {theme}")

    cap.release()
    hands_model.close()
    cv2.destroyAllWindows()
    print(f"\n✅ Session ended. Screenshots saved: {screenshot_n}")


if __name__ == "__main__":
    main()
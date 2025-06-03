from moviepy.editor import *
import os

# Configuration
video_size = (1080, 1080)
duration = 20  # in seconds
logo_path = "FUSIKABDJ+noir-9aba294e-1920w.webp"
font = "Arial-Bold"

# Scene 1: Dramatic fade-in of logo with zoom-in effect
scene1_logo = (
    ImageClip(logo_path)
    .resize(height=400)
    # .resize(3)  # ×3 la taille actuelle
    .set_position("center")
    .fadein(1.2)
    .resize(lambda t: 1 + 0.02 * t)  # subtle zoom-in
    .set_duration(4)
    .on_color(size=video_size, color=(0, 0, 0), pos="center")
)

# Scene 2: Text drop effect for "FUSIKABDJ - DJ & Show Lights"
headline = (
    TextClip("FUSIKAB DJ", fontsize=100, color="white", font=font)
    .set_position(("center", "center"))
    .set_duration(3.5)
    .fadein(0.5)
)

subline = (
    TextClip("DJ & Show Lights", fontsize=50, color="white", font=font)
    .set_position(("center", 650))
    .set_duration(3.5)
    .fadein(0.8)
)

scene2_bg = ColorClip(size=video_size, color=(0, 0, 0), duration=1.5)
scene2 = CompositeVideoClip([scene2_bg, headline, subline])

# Scene 3: Call to action + Instagram
call_text = (
    TextClip("Dispo pour vos événements", fontsize=65, color="white", font=font)
    .set_position(("center", 400))
    .set_duration(4)
    .fadein(0.8)
)

insta = (
    TextClip("@fusikabdj", fontsize=60, color="white", font=font)
    .set_position(("center", 850))
    .set_duration(4)
    .fadein(1.0)
)

scene3_bg = ColorClip(size=video_size, color=(0, 0, 0), duration=2)
scene3 = CompositeVideoClip([scene3_bg, call_text, insta])

# Final scene: Flash logo (again) with pulse effect
scene4_logo = (
    ImageClip(logo_path)
    .resize(height=400)
    # .resize(3)  # ×3 la taille actuelle
    .set_duration(3.5)
    .fadein(0.3)
    .resize(lambda t: 1.05 + 0.02 * (t % 0.5))  # pulse effect
    .set_position("center")
    .on_color(size=video_size, color=(0, 0, 0), pos="center")
)

# Combine with transitions
final_clip = concatenate_videoclips(
    [
        scene1_logo,
        scene2.crossfadein(1),
        scene3.crossfadein(1),
        scene4_logo.crossfadein(1),
    ],
    method="compose"
)

# Export
output_path = "FUSIKABDJ_Instagram_SexyPromo.mp4"
final_clip.write_videofile(output_path, fps=24, codec="libx264")

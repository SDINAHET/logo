from moviepy.editor import *
from moviepy.video.fx.all import fadein, fadeout
import numpy as np


# Chemins des médias
logo_yalla = "logo_yalla_raqasa_fond_inverse.png"
logo_fusikab = "FUSIKABDJ+noir-9aba294e-1920w.webp"
fusion_image = "fusion_finale.png"  # à créer plus tard si souhaité
music_path = "Loreen - Tattoo.mp3"

# Configuration
video_size = (1080, 1080)
duration_each = 4
font = "DejaVu-Sans-Bold"

# Texte sous forme d’images à créer dynamiquement
text_slides = [
    ("Un souffle venu d’Orient…", 65),
    ("… rencontre la puissance du son et de la lumière.", 60),
    ("✨ Yalla Raqasa ✨\nDanse orientale passionnée\nSpectacles, cours & événements", 55),
    ("🎧 DJ FUSIKAB 🎧\nAmbiance & shows lumière\nMariages, galas, soirées", 55),
    ("📍 Montfort-sur-Meu\n📅 14 juin 2025\n💃 Show oriental – 🎧 DJ Set", 55),
    ("📞 06 52 32 53 57\n🌐 www.fusikabdj.fr\n📸 @fusikabdj", 55),
    ("📵 Merci d’éteindre vos téléphones…\nSinon DJ FUSIKAB les connecte à ses platines 🎧📲💥", 50),
    ("Le spectacle commence maintenant !", 65)
]

def generate_text_clip(text, fontsize=50, duration=4):
    return TextClip(text, fontsize=fontsize, font=font, color="white", size=video_size, method='caption', align='center')\
        .set_duration(duration).fadein(1).fadeout(1).set_position("center")\
        .on_color(size=video_size, color=(0, 0, 0), col_opacity=1)

# Générer clips de texte
text_clips = [generate_text_clip(txt, fs, duration_each) for txt, fs in text_slides]

# Logo Yalla
logo1 = ImageClip(logo_yalla).resize(height=700).set_duration(duration_each).set_position("center").fadein(1).fadeout(1)

# Logo Fusikab
logo2 = ImageClip(logo_fusikab).resize(height=700).set_duration(duration_each).set_position("center").fadein(1).fadeout(1)

# Compte à rebours
countdown = concatenate_videoclips([
    TextClip(str(i), fontsize=120, font=font, color="white", method="caption")
    .set_duration(1).set_position("center").on_color(size=video_size, color=(0, 0, 0))
    for i in range(10, 0, -1)
])

# Logo final pulsant
pulse = ImageClip(logo_fusikab).set_duration(6).resize(lambda t: 1 + 0.05 * np.sin(2 * np.pi * t))\
    .set_position("center").on_color(size=video_size, color=(0, 0, 0))

# Enchaînement des scènes
final_video = concatenate_videoclips([
    logo1,
    text_clips[0],
    logo2,
    text_clips[1],
    text_clips[2],
    text_clips[3],
    text_clips[4],
    text_clips[5],
    text_clips[6],
    countdown,
    text_clips[7],
    pulse
], method="compose")

# Ajouter musique de fond
audio = AudioFileClip(music_path).subclip(0, final_video.duration)
final_video = final_video.set_audio(audio)

# Export
output_path = "VIDEO_FINAL_DIAPO_FUSIKAB_YALLA.mp4"
final_video.write_videofile(output_path, fps=24, codec="libx264", audio_codec="aac")

from moviepy.editor import *
from moviepy.video.fx.all import fadein, fadeout
import numpy as np

# Fichiers
logo_yalla = "logo_yalla_raqasa_fond_inverse.png"
logo_fusikab = "FUSIKABDJ+noir-9aba294e-1920w.webp"
pool_logo = "pool_logo.png"
# music_path = "Loreen - Tattoo.mp3"
music_path = "fixed_music.mp3"


# Paramètres
video_size = (1080, 1080)
duration_each = 4
# font = "DejaVu-Sans-Bold"
font = "Noto Color Emoji"

# Slides texte
text_slides = [
    ("Un souffle venu d’Orient...", 65),
    ("... rencontre la puissance du son et de la lumière", 60),
    ("✨Yalla Raqasa ✨\nDanse orientale envoûtante\nSpectacles, cours et animations en Ille-et-Vilaine", 55),
    ("🎧DJ FUSIKAB 🎧\nLumières, ambiance, mix sur mesure\nMariages, soirées, galas", 55),
    ("📍Montfort-sur-Meu\n📅 Samedi 14 juin 2025 – 20h\n💃 Spectacle oriental – 🎧 DJ Set live", 55),
    ("📞06 52 32 53 57\n🌐 www.fusikabdj.fr\n📸 @fusikabdj", 55),
    ("📵Merci de mettre vos téléphones en silencieux 🙃\nSinon DJ FUSIKAB les connecte à ses platines ! 🎧📲💥", 50),
    ("🎭Le spectacle commence... maintenant !", 65)
]

def generate_text_clip(text, fontsize=50, duration=4):
    return TextClip(
        text, fontsize=fontsize, font=font, color="white",
        size=video_size, method='caption', align='center'
    ).set_duration(duration).fadein(1).fadeout(1).set_position("center")\
     .on_color(size=video_size, color=(0, 0, 0), col_opacity=1)

# Clips texte
text_clips = [generate_text_clip(txt, fs, duration_each) for txt, fs in text_slides]

# Logos
logo1 = ImageClip(logo_yalla).resize(height=700).set_duration(duration_each).set_position("center").fadein(1).fadeout(1)
logo2 = ImageClip(logo_fusikab).resize(height=1000).set_duration(duration_each).set_position("center").fadein(1).fadeout(1)

# Compte à rebours
countdown = concatenate_videoclips([
    TextClip(str(i), fontsize=120, font=font, color="white", method="caption")
    .set_duration(1).set_position("center").on_color(size=video_size, color=(0, 0, 0))
    for i in range(5, 0, -1)
])

# Logo pulsant final
pulse = ImageClip(logo_fusikab).set_duration(4)\
    .resize(lambda t: 1 + 0.05 * np.sin(2 * np.pi * t))\
    .resize(height=1000)\
    .set_position("center")\
    .on_color(size=video_size, color=(0, 0, 0))

# Pool logo avec délai visuel
pause = ColorClip(size=video_size, color=(0, 0, 0)).set_duration(1)
pool = ImageClip(pool_logo).resize(height=1100).set_duration(20).fadein(1).fadeout(1).set_position("center")\
    .on_color(size=video_size, color=(0, 0, 0))

# Montage final
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
    pulse,
    pause,
    pool
], method="compose")

# Musique
audio = AudioFileClip(music_path)
final_video = final_video.set_audio(audio.set_duration(final_video.duration))

# Export
output_path = "VIDEO_FINAL_FUSIKAB_YALLA_PRO.mp4"
final_video.write_videofile(output_path, fps=24, codec="libx264", audio_codec="aac")

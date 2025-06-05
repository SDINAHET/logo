from moviepy.editor import *
import os

# Configuration générale
video_size = (1080, 1080)
font = "Arial-Bold"
logo_fusikab = "FUSIKABDJ+noir-9aba294e-1920w.webp"
logo_yalla = "logo_yalla_raqasa_fond_inverse.png"
output_path = "EVENT_5MIN_FUSIKAB_YALLA_2025.mp4"

# Fonction pour créer un TextClip stylisé
def styled_text(txt, fontsize=50, duration=4, y=900):
    return TextClip(txt, fontsize=fontsize, font=font, color="white", method="caption")\
        .set_position(("center", y)).set_duration(duration).fadein(1)

# Scene 1 – Intro mystique avec logo Yalla
scene1 = ImageClip(logo_yalla).resize(height=400).set_position("center")\
    .fadein(2).resize(lambda t: 1 + 0.05 * t).set_duration(8)\
    .on_color(size=video_size, color=(0, 0, 0))

scene1_txt = styled_text("Un souffle venu d’Orient…", fontsize=50, duration=6)
scene1_final = CompositeVideoClip([scene1, scene1_txt])

# Scene 2 – Énergie DJ Fusikab
scene2_logo = ImageClip(logo_fusikab).resize(height=400).set_position("center")\
    .fadein(1.5).resize(lambda t: 1 + 0.08 * t).set_duration(8)\
    .on_color(size=video_size, color=(0, 0, 0))

scene2_txt = styled_text("… rencontre la puissance du son et de la lumière.", fontsize=45, duration=7)
scene2_final = CompositeVideoClip([scene2_logo, scene2_txt])

# Scene 3 – Logos côte à côte
logo1 = ImageClip(logo_fusikab).resize(height=300).set_position(("left", "center"))
logo2 = ImageClip(logo_yalla).resize(height=300).set_position(("right", "center"))
fusion_txt = styled_text("FUSIKAB × Yalla Raqasa", fontsize=60, duration=8, y=850)
scene3 = CompositeVideoClip([logo1, logo2, fusion_txt]).set_duration(10).on_color(size=video_size, color=(0, 0, 0))

# Scene 4 – Détails de l'événement
event_lines = [
    "📍 Montfort-sur-Meu",
    "📅 14 juin 2025",
    "💃 Danse orientale – 💡 Show lumière – 🎧 DJ Set"
]
event_clips = [
    TextClip(line, fontsize=50, font=font, color="white", method="caption")
    .set_position(("center", 350 + i * 100)).set_duration(6).fadein(1)
    for i, line in enumerate(event_lines)
]
scene4 = CompositeVideoClip(event_clips).set_duration(12).on_color(size=video_size, color=(0, 0, 0))

# Scene 5 – Slogans sensoriels
slogans = [
    "🎵 Des basses envoûtantes",
    "💃 Des danses captivantes",
    "✨ Une nuit inoubliable"
]
slogan_clips = [
    styled_text(text, fontsize=55, duration=5, y=850)
    for text in slogans
]
scene5 = concatenate_videoclips(slogan_clips).on_color(size=video_size, color=(0, 0, 0))

# Scene 6 – Countdown (10 → 0)
countdown_clips = [
    TextClip(str(i), fontsize=130, font=font, color="white", method="caption")
    .set_duration(1).set_position("center")
    for i in range(10, 0, -1)
]
scene6 = concatenate_videoclips(countdown_clips).on_color(size=video_size, color=(0, 0, 0))

# Scene 7 – Coordonnées
contacts = [
    "@fusikabdj",
    "www.fusikabdj.fr",
    "📞 06 52 32 53 57"
]
contact_clips = [
    styled_text(txt, fontsize=50, duration=6, y=400 + i * 100)
    for i, txt in enumerate(contacts)
]
scene7_logo = ImageClip(logo_fusikab).resize(height=300).set_position(("center", 100)).set_duration(10).fadein(1)
scene7 = CompositeVideoClip([scene7_logo] + contact_clips).set_duration(10).on_color(size=video_size, color=(0, 0, 0))

# Scene 8 – Rappel humour silencieux
silence_txt = [
    "📵 Merci d’éteindre vos téléphones…",
    "…ou au moins les mettre en mode silencieux 🙃",
    "Sinon DJ FUSIKAB pourrait les connecter à ses platines 🎧📲💥"
]
silence_clips = [
    styled_text(line, fontsize=45, duration=4, y=850)
    for line in silence_txt
]
scene8 = concatenate_videoclips(silence_clips).on_color(size=video_size, color=(0, 0, 0))

# Scene 9 – Clôture finale
scene9_txt = styled_text("14 juin 2025 – Le spectacle commence maintenant…", fontsize=50, duration=10, y=900)
scene9 = CompositeVideoClip([scene9_txt]).on_color(size=video_size, color=(0, 0, 0))

# Scene 10 – Logos en pulsation lente (bouclés)
pulse = ImageClip(logo_fusikab).resize(height=350).set_position("center").fadein(2)\
    .resize(lambda t: 1.01 + 0.01 * (t % 2)).set_duration(20).on_color(size=video_size, color=(0, 0, 0))
scene10 = pulse

# Compilation finale des scènes (~5 minutes)
final_clip = concatenate_videoclips([
    scene1_final, scene2_final, scene3, scene4,
    scene5, scene6, scene7, scene8, scene9, scene10
], method="compose")

# Export vidéo
final_clip.write_videofile(output_path, fps=24, codec="libx264")


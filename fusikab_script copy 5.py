from moviepy.editor import *

# Configuration générale
video_size = (1080, 1080)
font = "DejaVu-Sans-Bold"
logo_fusikab = "FUSIKABDJ+noir-9aba294e-1920w.webp"
logo_yalla = "logo_yalla_raqasa_fond_inverse.png"
logo_pool = "pool_logo.png"
output_path = "EVENT_CORRIGE_FUSIKAB_YALLA_2025.mp4"

# Fonction texte stylisé avec fond semi-transparent
def styled_text(txt, fontsize=50, duration=4, y=900):
    txt_clip = TextClip(txt, fontsize=fontsize, font=font, color="white", method="caption", size=(video_size[0] - 100, None), align="center")
    bg = ColorClip(size=(txt_clip.w + 40, txt_clip.h + 20), color=(0, 0, 0)).set_opacity(0.6)
    bg = bg.set_position(("center", y - 10)).set_duration(duration)
    return CompositeVideoClip([bg, txt_clip.set_position(("center", y))]).set_duration(duration).fadein(1)

# Scène : logo centré avec texte en bas
def scene_logo_with_text(logo_path, text, text_y=950, logo_height=700, duration=8):
    logo = ImageClip(logo_path).resize(height=logo_height).set_position("center").set_duration(duration).fadein(1)
    text_clip = styled_text(text, fontsize=65, duration=duration, y=text_y)
    return CompositeVideoClip([logo, text_clip]).on_color(size=video_size, color=(0, 0, 0)).set_duration(duration)

# Scene 1
scene1 = scene_logo_with_text(logo_yalla, "Un souffle venu d’Orient…")

# Scene 2
scene2 = scene_logo_with_text(logo_fusikab, "… rencontre la puissance du son et de la lumière.")

# Scene 3 : Présentation Yalla
scene3_logo = ImageClip(logo_yalla).resize(height=400).set_position(("center", 100)).set_duration(10)
desc_yalla = [
    "✨ Yalla Raqasa ✨",
    "Danse orientale passionnée en Ille-et-Vilaine",
    "Spectacles, cours & événements"
]
scene3_texts = [styled_text(txt, fontsize=55 - i*5, duration=10, y=500 + i*100) for i, txt in enumerate(desc_yalla)]
scene3 = CompositeVideoClip([scene3_logo] + scene3_texts).on_color(size=video_size, color=(0, 0, 0))

# Scene 4 : Présentation FUSIKAB
scene4_logo = ImageClip(logo_fusikab).resize(height=400).set_position(("center", 100)).set_duration(10)
desc_fusikab = [
    "🎧 DJ FUSIKAB 🎧",
    "Ambiance & shows lumière sur mesure",
    "Animations, mariages, soirées"
]
scene4_texts = [styled_text(txt, fontsize=55 - i*5, duration=10, y=500 + i*100) for i, txt in enumerate(desc_fusikab)]
scene4 = CompositeVideoClip([scene4_logo] + scene4_texts).on_color(size=video_size, color=(0, 0, 0))

# Scene 5 : Fusion des deux logos
logo1 = ImageClip(logo_fusikab).resize(height=450).set_position(("left", "center")).set_duration(10)
logo2 = ImageClip(logo_yalla).resize(height=450).set_position(("right", "center")).set_duration(10)
fusion_txt = styled_text("FUSIKAB × Yalla Raqasa", fontsize=65, duration=10, y=950)
scene5 = CompositeVideoClip([logo1, logo2, fusion_txt]).on_color(size=video_size, color=(0, 0, 0))

# Scene 6 : Infos événement
event_lines = [
    "📍 Montfort-sur-Meu",
    "📅 14 juin 2025",
    "💃 Danse orientale – 💡 Show lumière – 🎧 DJ Set",
    "📸 @yalla.raqasa"
]
scene6 = CompositeVideoClip([
    styled_text(txt, fontsize=55, duration=12, y=350 + i*100)
    for i, txt in enumerate(event_lines)
]).on_color(size=video_size, color=(0, 0, 0)).set_duration(12)

# Scene 7 : Slogans sensoriels
slogans = [
    "🎵 Des basses envoûtantes",
    "💃 Des danses captivantes",
    "✨ Une nuit inoubliable"
]
scene7 = concatenate_videoclips([
    styled_text(text, fontsize=60, duration=5, y=900)
    for text in slogans
]).on_color(size=video_size, color=(0, 0, 0))

# Scene 8 : Infos publiques (logo pool + contact)
icon = ImageClip(logo_pool).resize(height=150).set_position(("center", 100)).set_duration(10)
pub_lines = [
    "📞 06 52 32 53 57",
    "🌐 www.fusikabdj.fr",
    "📸 @fusikabdj"
]
pub_texts = [styled_text(txt, fontsize=55, duration=10, y=450 + i*100) for i, txt in enumerate(pub_lines)]
scene8 = CompositeVideoClip([icon] + pub_texts).on_color(size=video_size, color=(0, 0, 0))

# Scene 9 : Message humour téléphone
silence_txt = [
    "📵 Merci d’éteindre vos téléphones…",
    "… ou au moins les mettre en mode silencieux 🙃",
    "Sinon DJ FUSIKAB pourrait les connecter à ses platines 🎧📲💥"
]
scene9 = concatenate_videoclips([
    styled_text(line, fontsize=50, duration=4, y=850)
    for line in silence_txt
]).on_color(size=video_size, color=(0, 0, 0))

# Scene 10 : Compte à rebours
scene10 = concatenate_videoclips([
    TextClip(str(i), fontsize=140, font=font, color="white", method="caption")
    .set_duration(1).set_position("center")
    for i in range(10, 0, -1)
]).on_color(size=video_size, color=(0, 0, 0))

# Scene 11 : lancement show
scene11_txt = styled_text("14 juin 2025 – Le spectacle commence maintenant !", fontsize=65, duration=10, y=900)
scene11 = CompositeVideoClip([scene11_txt]).on_color(size=video_size, color=(0, 0, 0))

# Scene 12 : logo final pulsant
scene12 = ImageClip(logo_fusikab).resize(2).set_position("center")\
    .fadein(2).resize(lambda t: 1.02 + 0.01 * (t % 2))\
    .set_duration(20).on_color(size=video_size, color=(0, 0, 0))

# Compilation finale
final_clip = concatenate_videoclips([
    scene1, scene2,
    scene3, scene4, scene5,
    scene6, scene7, scene8,
    scene9, scene10, scene11,
    scene12
], method="compose")

# Export de la vidéo corrigée
final_clip.write_videofile(output_path, fps=24, codec="libx264")

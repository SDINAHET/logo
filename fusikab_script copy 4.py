from moviepy.editor import *
import os

# Configuration générale
video_size = (1080, 1080)
font = "Arial-Bold"
logo_fusikab = "FUSIKABDJ+noir-9aba294e-1920w.webp"
logo_yalla = "logo_yalla_raqasa_fond_inverse.png"
logo_pool = "pool_logo.png"
output_path = "EVENT_5MIN_FUSIKAB_YALLA_2025.mp4"

# Fonction texte stylisé
def styled_text(txt, fontsize=50, duration=4, y=900):
    return TextClip(txt, fontsize=fontsize, font=font, color="white", method="caption")\
        .set_position(("center", y)).set_duration(duration).fadein(1)

# Scene 1 : Yalla Raqasa grand
scene1_logo = ImageClip(logo_yalla).resize(1).set_position("center")\
    .fadein(2).set_duration(8).on_color(size=video_size, color=(0, 0, 0))
scene1_txt = styled_text("Un souffle venu d’Orient…", fontsize=65, duration=7, y=950)
scene1_final = CompositeVideoClip([scene1_logo, scene1_txt])

# Scene 2 : FUSIKABDJ grand
scene2_logo = ImageClip(logo_fusikab).resize(1).set_position("center")\
    .fadein(1.5).set_duration(8).on_color(size=video_size, color=(0, 0, 0))
scene2_txt = styled_text("… rencontre la puissance du son et de la lumière.", fontsize=60, duration=7, y=950)
scene2_final = CompositeVideoClip([scene2_logo, scene2_txt])

# Scene 3 : Présentation Yalla
scene3_logo = ImageClip(logo_yalla).resize(1).set_position(("center", 200))
desc_yalla = [
    "✨ Yalla Raqasa ✨",
    "Une association de danse orientale passionnée",
    "Spectacles, cours et événements en Ille-et-Vilaine"
]
scene3_texts = [styled_text(txt, fontsize=60 - i*10, duration=6, y=500 + i*80) for i, txt in enumerate(desc_yalla)]
scene3 = CompositeVideoClip([scene3_logo] + scene3_texts).set_duration(10).on_color(size=video_size, color=(0, 0, 0))

# Scene 4 : Présentation FUSIKAB
scene4_logo = ImageClip(logo_fusikab).resize(1).set_position(("center", 200))
desc_fusikab = [
    "🎧 DJ FUSIKAB 🎧",
    "Ambiance & shows lumière sur mesure",
    "Animations, soirées, mariages & galas"
]
scene4_texts = [styled_text(txt, fontsize=60 - i*10, duration=6, y=500 + i*80) for i, txt in enumerate(desc_fusikab)]
scene4 = CompositeVideoClip([scene4_logo] + scene4_texts).set_duration(10).on_color(size=video_size, color=(0, 0, 0))

# Scene 5 : Logos fusion
logo1 = ImageClip(logo_fusikab).resize(1).set_position(("left", "center"))
logo2 = ImageClip(logo_yalla).resize(1).set_position(("right", "center"))
fusion_txt = styled_text("FUSIKAB × Yalla Raqasa", fontsize=70, duration=8, y=900)
scene5 = CompositeVideoClip([logo1, logo2, fusion_txt]).set_duration(10).on_color(size=video_size, color=(0, 0, 0))

# Scene 6 : Infos événement
event_lines = [
    "📍 Montfort-sur-Meu",
    "📅 14 juin 2025",
    "💃 Danse orientale – 💡 Show lumière – 🎧 DJ Set"
    "📸 @yalla.raqasa"
]
scene6_clips = [
    styled_text(line, fontsize=65, duration=7, y=400 + i * 100)
    for i, line in enumerate(event_lines)
]
scene6 = CompositeVideoClip(scene6_clips).set_duration(12).on_color(size=video_size, color=(0, 0, 0))

# Scene 7 : Slogans sensoriels
slogans = [
    "🎵 Des basses envoûtantes",
    "💃 Des danses captivantes",
    "✨ Une nuit inoubliable"
]
scene7 = concatenate_videoclips([
    styled_text(text, fontsize=65, duration=5, y=900)
    for text in slogans
]).on_color(size=video_size, color=(0, 0, 0))

# Scene 8 : Infos publiques (pause/entracte)
pub_lines = [
    "📞 06 52 32 53 57",
    "🌐 www.fusikabdj.fr",
    "📸 @fusikabdj"
]
icons = [ImageClip(logo_pool).resize(1).set_position(("center", 100)).set_duration(10)]
pub_texts = [styled_text(txt, fontsize=60, duration=10, y=450 + i*100) for i, txt in enumerate(pub_lines)]
scene8 = CompositeVideoClip(icons + pub_texts).on_color(size=video_size, color=(0, 0, 0)).set_duration(10)

# Scene 9 : Message humour téléphone
silence_txt = [
    "📵 Merci d’éteindre vos téléphones…",
    "…ou au moins les mettre en mode silencieux 🙃",
    "Sinon DJ FUSIKAB pourrait les connecter à ses platines 🎧📲💥"
]
scene9 = concatenate_videoclips([
    styled_text(line, fontsize=55, duration=4, y=850)
    for line in silence_txt
]).on_color(size=video_size, color=(0, 0, 0))

# Scene 10 : Compte à rebours
scene10 = concatenate_videoclips([
    TextClip(str(i), fontsize=140, font=font, color="white", method="caption")
    .set_duration(1).set_position("center")
    for i in range(10, 0, -1)
]).on_color(size=video_size, color=(0, 0, 0))

# Scene 11 : lancement show
scene11_txt = styled_text("14 juin 2025 – Le spectacle commence maintenant !", fontsize=70, duration=10, y=900)
scene11 = CompositeVideoClip([scene11_txt]).on_color(size=video_size, color=(0, 0, 0))

# Scene 12 : logo pulsant final
scene12 = ImageClip(logo_fusikab).resize(2).set_position("center")\
    .fadein(2).resize(lambda t: 1.02 + 0.01 * (t % 2))\
    .set_duration(20).on_color(size=video_size, color=(0, 0, 0))

# Compilation finale
final_clip = concatenate_videoclips([
    scene1_final, scene2_final,
    scene3, scene4, scene5,
    scene6, scene7, scene8,
    scene9, scene10, scene11,
    scene12
], method="compose")

# Export
final_clip.write_videofile(output_path, fps=24, codec="libx264")

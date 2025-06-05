# logo





./setup_fusikab_env.sh


source venv_fusikab/bin/activate

python3 fusikab_script.py




AttributeError: module 'PIL.Image' has no attribute 'ANTIALIAS'

pip uninstall pillow
pip install "pillow==8.4.0"

python3 fusikab_script.py



sudo apt update
sudo apt install imagemagick

python3 fusikab_script.py

deactivate






ffmpeg -i "Loreen - Tattoo.mp3" -ar 44100 -ac 2 -b:a 192k fixed_music.mp3
pip freeze > requirements.txt

certifi==2025.4.26
charset-normalizer==3.4.2
decorator==4.4.2
idna==3.10
imageio==2.37.0
imageio-ffmpeg==0.6.0
moviepy==1.0.3
numpy==2.2.6
Pillow==8.4.0
proglog==0.1.12
requests==2.32.3
tqdm==4.67.1
urllib3==2.4.0

import os
import requests
import zipfile
import shutil
import subprocess
from tqdm import tqdm

GAME_FOLDER = os.path.join(os.getenv("APPDATA"), "Miga")
GAME_URL = "https://github.com/KOLBEEV/Miga/raw/main/dist/miga/miga.zip"
VERSION_URL = "https://github.com/KOLBEEV/Miga/raw/main/dist/miga/version.txt"
GAME_EXE = os.path.join(GAME_FOLDER, "miga.exe")
TMP_ZIP = os.path.join(GAME_FOLDER, "miga_temp.zip")
LOCAL_VERSION = os.path.join(GAME_FOLDER, "version.txt")

def get_remote_version():
    try:
        response = requests.get(VERSION_URL)
        response.raise_for_status()
        return response.text.strip()
    except Exception as e:
        print("Не удалось получить версию:", e)
        return None

def get_local_version():
    if not os.path.exists(LOCAL_VERSION):
        return None
    with open(LOCAL_VERSION, 'r') as f:
        return f.read().strip()

def download_game():
    os.makedirs(GAME_FOLDER, exist_ok=True)
    print("Скачивание игры...")

    with requests.get(GAME_URL, stream=True) as r:
        total = int(r.headers.get('content-length', 0))
        with open(TMP_ZIP, 'wb') as f, tqdm(
            desc="Загрузка",
            total=total,
            unit='B',
            unit_scale=True,
            unit_divisor=1024
        ) as bar:
            for chunk in r.iter_content(chunk_size=1024):
                f.write(chunk)
                bar.update(len(chunk))
    print("Скачано.")

def extract_game():
    print("Распаковка...")
    with zipfile.ZipFile(TMP_ZIP, 'r') as zip_ref:
        zip_ref.extractall(GAME_FOLDER)
    os.remove(TMP_ZIP)
    print("Готово.")

def save_version(version):
    with open(LOCAL_VERSION, 'w') as f:
        f.write(version)

def launch_game():
    print("Запуск игры...")
    subprocess.Popen(GAME_EXE)
    print("Игра запущена.")

if __name__ == "__main__":
    remote_version = get_remote_version()
    local_version = get_local_version()

    if remote_version and remote_version != local_version or not os.path.exists(GAME_EXE):
        print("Обнаружена новая версия." if remote_version != local_version else "Игра не установлена.")
        download_game()
        extract_game()
        if remote_version:
            save_version(remote_version)
    else:
        print("Игра актуальна.")

    launch_game()

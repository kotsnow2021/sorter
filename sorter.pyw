import shutil
import os
import time
from config import *

def find_files(target_extensions):
    target_extensions = target_extensions
    files_for_move = [
        file for file in os.listdir(DOWNLOADS_PATH)
        if os.path.splitext(file)[1].lower() in target_extensions
        and os.path.isfile(os.path.join(DOWNLOADS_PATH, file))
    ]
    if files_for_move:
        if target_extensions == TEXT_EXTENTIONS:
            sorter_files(files_for_move, TEXTS_PATH)
        elif target_extensions == IMAGES_EXTANTIONS:
            sorter_files(files_for_move, IMAGES_PATH)
        elif target_extensions == APP_EXTANTIONS:
            sorter_files(files_for_move, APPS_PATH)
        elif target_extensions == ARCHIVE_EXTANTIOS:
            sorter_files(files_for_move, ARCHIVE_PATH)
        elif target_extensions == MUSIC_EXTANTIONS:
            sorter_files(files_for_move, MUSIC_PATH)
        elif target_extensions == PDF_EXTENSIONS:
            sorter_files(files_for_move, PDF_PATH)
        elif target_extensions == JAR_EXTENTIONS:
            sorter_files(files_for_move, JAR_PATH)
        elif target_extensions == VIDEOS_EXTENTIONS:
            sorter_files(files_for_move, VIDEOS_PATH)

def sorter_files(files_for_move, move_path):
    for file in files_for_move:
        src = os.path.join(DOWNLOADS_PATH, file)
        dst = os.path.join(move_path, file)

        try:
            shutil.move(src, dst)
        except Exception as e:
            print(f"Произошла ошибка при перемещении {file}: {e}")

while True:
    for extantions in EXTENTIONS_LIST:
        find_files(extantions)
    time.sleep(5)

import shutil
import os
import time
from config import *

def find_files(target_EXTENTIONS):
    target_EXTENTIONS = target_EXTENTIONS
    files_for_move = [
        file for file in os.listdir(DOWNLOADS_PATH)
        if os.path.splitext(file)[1].lower() in target_EXTENTIONS
        and os.path.isfile(os.path.join(DOWNLOADS_PATH, file))
    ]
    if files_for_move:
        if target_EXTENTIONS == TEXT_EXTENTIONS:
            sorter_files(files_for_move, TEXTS_PATH)
        elif target_EXTENTIONS == IMAGES_EXTENTIONS:
            sorter_files(files_for_move, IMAGES_PATH)
        elif target_EXTENTIONS == APP_EXTENTIONS:
            sorter_files(files_for_move, APPS_PATH)
        elif target_EXTENTIONS == ARCHIVE_EXTANTIOS:
            sorter_files(files_for_move, ARCHIVE_PATH)
        elif target_EXTENTIONS == MUSIC_EXTENTIONS:
            sorter_files(files_for_move, MUSIC_PATH)
        elif target_EXTENTIONS == PDF_EXTENTIONS:
            sorter_files(files_for_move, PDF_PATH)
        elif target_EXTENTIONS == JAR_EXTENTIONS:
            sorter_files(files_for_move, JAR_PATH)
        elif target_EXTENTIONS == VIDEOS_EXTENTIONS:
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
    for EXTENTIONS in EXTENTIONS_LIST:
        find_files(EXTENTIONS)
    time.sleep(5)

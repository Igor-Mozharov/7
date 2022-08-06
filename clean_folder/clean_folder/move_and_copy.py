import sys
import os
import shutil
from pathlib import Path
from funk_normalize import normalize

extension_dict = {
    'images': ['jpeg', 'jpg', 'svg', 'png'],
    'video': ['avi', 'mp4', 'mov', 'mkv'],
    'documents': ['doc', 'docx', 'txt', 'pdf', 'xlsx', 'pptx'],
    'audio': ['mp3', 'ogg', 'wav', 'amr'],
    'archives': ['zip', 'tar', 'gz'],
    'unknown': []
}

main_directory = Path('C:\\SORT_FOLDER\\')
if not os.path.isdir(main_directory):
    os.makedirs(main_directory)


def find_format(file):
    for suf in extension_dict:
        if file.name.split('.')[-1] in extension_dict[suf]:
            dir_img = main_directory / suf
            dir_img.mkdir(exist_ok=True)
            name = file.name.replace(file.name.split(
                '.')[0], normalize(file.name.split('.')[0]))
            file.replace(dir_img.joinpath(name))
            return True
    return False


def sort_folder(path):
    folder = Path(path)
    for file in folder.iterdir():
        if file.is_dir():
            if file.name in ('audio', 'video', 'documents', 'images', 'archives', 'unknown'):
                continue
            sort_folder(file)
            if not os.listdir(file):
                os.rmdir(file)
        else:
            if find_format(file) == False:
                dir_unk = main_directory / 'unknown'
                dir_unk.mkdir(exist_ok=True)
                name = file.name.replace(file.name.split(
                    '.')[0], normalize(file.name.split('.')[0]))
                file.replace(dir_unk.joinpath(name))


def unpack_arc():
    arch_dir = Path(main_directory / 'archives')
    if os.path.exists(arch_dir):
        for arc in arch_dir.iterdir():
            try:
                shutil.unpack_archive(arc, arch_dir / arc.name.split('.')[0])
            except:
                pass


def show_unknown_extension(path):
    unknown_ext = set()
    folder = Path(path)
    for f in folder.iterdir():
        unknown_ext.add(f.name.split('.')[1])
    return f' ALL UNKNOWN EXTENSION IS : {unknown_ext}'


def show_all_known_extensions(path):
    all_known_ext = set()
    path = Path(path)
    for root, dirs, files in os.walk(path):
        for f in files:
            all_known_ext.add(f.split('.')[1])
    return f' ALL KNOWN EXTENSION IS: {all_known_ext}'


# print(show_all_known_extensions(main_directory))
# print(show_unknown_extension('C:\\SORT_FOLDER\\unknown'))
# sort_folder('C:\\Projects\\HW6\\TEMP')
# unpack_arc()

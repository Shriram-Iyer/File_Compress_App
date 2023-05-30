import zipfile
import pathlib


def make_archive(filepaths, dist_dir, filename):
    dist_path = pathlib.Path(dist_dir, f"{filename}.zip")
    with zipfile.ZipFile(dist_path, "w") as archive:
        for filepath in filepaths:
            archive.write(filepath)

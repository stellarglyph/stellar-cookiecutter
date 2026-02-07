#!/usr/bin/env python
import shutil
from pathlib import Path

DATA_PLATFORM_FOLDERS = [
    "pipelines",
    "orchestration",
    "transformation",
    "visualisation",
]


def remove_data_platform_folders():
    """Remove data platform folders if not a data platform project."""
    src_dir = Path("src") / "{{ cookiecutter.project_slug }}"
    for folder in DATA_PLATFORM_FOLDERS:
        folder_path = src_dir / folder
        if folder_path.exists():
            shutil.rmtree(folder_path)


if __name__ == "__main__":
    if "{{ cookiecutter.is_data_platform }}" == "no":
        remove_data_platform_folders()

    print("Your modern Python package project has been created successfully!")

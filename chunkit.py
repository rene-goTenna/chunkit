import os
import shutil
import sys
from pathlib import Path

# --- Configuration ---
MAX_FOLDER_SIZE = 10 * 1024 * 1024 * 1024  # 10 GB in bytes

def get_size(path: Path) -> int:
    """Return size of a file in bytes."""
    return path.stat().st_size

def create_subfolder(base_output: Path, index: int) -> Path:
    """Create a new subfolder like output_01, output_02, etc."""
    subfolder = base_output / f"part_{index:02d}"
    subfolder.mkdir(parents=True, exist_ok=True)
    return subfolder

def split_folder(input_folder: Path, output_base: Path):
    """Split input_folder into subfolders of max 10GB."""
    files = sorted([f for f in input_folder.rglob('*') if f.is_file()])
    if not files:
        print("No files found in the input folder.")
        return

    total_folders = 0
    current_size = 0
    current_folder = create_subfolder(output_base, total_folders + 1)

    for file_path in files:
        file_size = get_size(file_path)
        # If the file itself exceeds the 10 GB limit, warn the user
        if file_size > MAX_FOLDER_SIZE:
            print(f"⚠️ Skipping {file_path.name}: file size exceeds 10GB limit ({file_size/1e9:.2f} GB).")
            continue

        # If adding this file exceeds the limit, start a new subfolder
        if current_size + file_size > MAX_FOLDER_SIZE:
            total_folders += 1
            current_folder = create_subfolder(output_base, total_folders + 1)
            current_size = 0

        # Copy file to the new subfolder (preserving relative structure)
        rel_path = file_path.relative_to(input_folder)
        dest_path = current_folder / rel_path
        dest_path.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(file_path, dest_path)

        current_size += file_size
        print(f"📦 Added {file_path.name} ({file_size/1e6:.2f} MB) → {current_folder.name}")

    print(f"\n✅ Done! Split into {total_folders + 1} folders under {output_base}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python split_folder_by_size.py <path_to_folder>")
        sys.exit(1)

    input_folder = Path(sys.argv[1]).resolve()
    if not input_folder.exists() or not input_folder.is_dir():
        print(f"Error: {input_folder} is not a valid folder.")
        sys.exit(1)

    output_base = input_folder.parent / f"{input_folder.name}_split"
    output_base.mkdir(exist_ok=True)

    split_folder(input_folder, output_base)

if __name__ == "__main__":
    main()
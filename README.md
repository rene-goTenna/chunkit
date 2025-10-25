# ChunkIt

A simple Python tool for macOS that splits a large folder into smaller folders of up to **10 GB each** — perfect for managing backups, uploads, or archive media.

---

## 🧩 Features
- Splits any folder into 10GB (configurable) chunks  
- Keeps entire files intact (no partial splits)  
- Preserves the original folder structure  
- Works out of the box on macOS and Linux  
- Option to copy or move files  

---

## 🚀 Installation

1. Clone this repository:
   ```bash
   git clone ...
   cd chunkit
   ```

2. Make sure Python 3 is installed:
   ```bash
   python3 --version
   ```
   (macOS comes with Python 3 preinstalled on recent versions)

---

## 🧠 Usage

Run the script from Terminal:

```bash
python3 chunkit.py /path/to/your/large_folder
```

This will create a new folder next to your original one, named:
```
large_folder_split/
├── part_01/
├── part_02/
└── part_03/
```

Each part folder will contain up to **10 GB** of files.

---

## ⚙️ Configuration

You can change the max folder size by editing the script:
```python
MAX_FOLDER_SIZE = 10 * 1024 * 1024 * 1024  # 10 GB
```

To **move** files instead of copying them (to save disk space), replace this line:
```python
shutil.copy2(file_path, dest_path)
```
with:
```python
shutil.move(file_path, dest_path)
```

---

## 🧾 License

This project is licensed under the [MIT License](LICENSE).

---

## 💡 Example

```bash
python3 chunkit.py ~/Downloads/BigBackup
```

Output:
```
📦 Added photo1.jpg (4.5 MB) → part_01
📦 Added movie.mp4 (8000.0 MB) → part_01
📦 Added archive.zip (1200.0 MB) → part_02
✅ Done! Split into 2 folders under BigBackup_split
```

---

## 🙌 Contributing

Pull requests and improvements are welcome!  
If you find a bug or want to suggest a feature, feel free to open an issue.

---

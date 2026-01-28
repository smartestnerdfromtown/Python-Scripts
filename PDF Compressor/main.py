import os
from pathlib import Path
import subprocess

PDF_DIR = Path("PDFs")

def file_size_mb(path):
    return round(os.path.getsize(path) / 1024 / 1024, 2)

def compress_pdf(input_path: Path, quality="screen"):
    """
    quality options:
    - screen   (lowest quality, smallest size)
    - ebook
    - printer
    - prepress (highest quality)
    """

    output_path = input_path.with_name(
        f"{input_path.stem}_compressed{input_path.suffix}"
    )
    print(os.getcwd())
    print(output_path)

    command = [
        "gswin64c",
        "-sDEVICE=pdfwrite",
        "-dCompatibilityLevel=1.4",
        f"-dPDFSETTINGS=/{quality}",
        "-dNOPAUSE",
        "-dQUIET",
        "-dBATCH",
        f"-sOutputFile={output_path}",
        input_path
    ]

    subprocess.run(command, check=True)

    return output_path

def main():
    input_path = PDF_DIR / "pdf24_converted.pdf"

    before = file_size_mb(input_path)
    output_path = compress_pdf(input_path, quality="ebook")
    after = file_size_mb(output_path)

    print(f"Before: {before} MB")
    print(f"After:  {after} MB")
    print(f"Saved:  {round(before - after, 2)} MB")

if __name__ == "__main__":
    main()

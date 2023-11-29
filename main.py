import glob
import pikepdf
import argparse
import os


def remove_password_from_pdf(dst, filename, password=None):
    pdf = pikepdf.open(filename, password=password, allow_overwriting_input=True)
    pos = -1
    filenameToSave = os.path.basename(filename)
    for i in range(len(filenameToSave) - 1, 0, -1):
        if filenameToSave[i] == ".":
            pos = i
            break
    if pos != -1:
        filenameToSave = filenameToSave[:pos] + "_unlocked" + filenameToSave[pos:]
    if not os.path.exists(dst):
        os.mkdir(dst)
    pdf.save(os.path.join(dst, filenameToSave))


if __name__ == "__main__":

    parser = argparse.ArgumentParser("pdf_unlocker")
    parser.add_argument("--password", help="password that needed to unlock files.", type=str, default=True)
    parser.add_argument("--src", help="source directory to read", type=str, default=False)
    parser.add_argument("--dst", help="destination directory to save", type=str, default=False)
    args = parser.parse_args()

    src = args.src if args.src is not None else "original"
    dst = args.dst if args.dst is not None else ""

    pdf_files = glob.glob(os.path.join(src, '*.pdf'))

    for file in pdf_files:
        remove_password_from_pdf(dst, filename=file, password=args.password)

import os, io
import pycdlib

try:
    from cStringIO import StringIO as BytesIO
except ImportError:
    from io import BytesIO

file_path = input(r"Enter path to file  >> ")
file_name = file_path.split("\\")[-1].split(".")[0]

iso = pycdlib.PyCdlib()
iso.new()

for folders, _, files in os.walk(file_path):
    for file in files:
        absolute_path = os.path.join(folders, file)
        iso.add_fp(BytesIO(absolute_path), len(absolute_path), f"/{absolute_path}.;1")
    iso.write(f"{file_name}.iso")
    iso.close()


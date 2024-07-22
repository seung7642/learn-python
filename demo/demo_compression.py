import zipfile

with zipfile.ZipFile('../comp.zip', 'w') as comp_file:
    comp_file.write('readme1.txt', compress_type=zipfile.ZIP_DEFLATED)
    comp_file.write('readme2.txt', compress_type=zipfile.ZIP_DEFLATED)

with zipfile.ZipFile('../comp.zip', 'r') as zip_obj:
    zip_obj.extractall('extracted')


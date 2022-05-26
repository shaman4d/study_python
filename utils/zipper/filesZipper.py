import os
import zipfile
import time

zip_file_name_prefix = f'study_'
src_target = f'd:\YandexDisk\study'
dst_target = f'd:\Backup'


def zipFilesInDirectory(path, zipf):
    for root, dirs, files in os.walk(path):
        for file in files:
            zipf.write(os.path.join(root, file))


zipf = zipfile.ZipFile(dst_target + os.sep + zip_file_name_prefix +
                       time.strftime('%Y%m%d_%H%M%S') + '.zip', 'w', zipfile.ZIP_DEFLATED)
zipFilesInDirectory(src_target, zipf)
zipf.close()

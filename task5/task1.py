import argparse
from ftplib import FTP
import gzip
import os


parser = argparse.ArgumentParser()
parser.add_argument('--download',
                    help='define the url of the file',
                    default='ftp.fu-berlin.de/pub/misc/'
                            'movies/database/frozendata/'
                            'ratings.list.gz')
parser.add_argument('--format',
                    help='define the acceptable file format',
                    default='gz')
args = parser.parse_args()
download_url = args.download
download_format = args.format

website_address = download_url[:download_url.find('/'):]
folder_path = download_url[download_url.find('/'):download_url.rfind('/'):]
full_file_name = download_url[download_url.rfind('/') + 1::]
file_name = full_file_name[:full_file_name.rfind('.'):]
file_extension = full_file_name[full_file_name.rfind('.') + 1::]

print('website_address: ' + website_address)
print('folder_path: ' + folder_path)
print('full_file_name: ' + full_file_name)
print('file_name: ' + file_name)
print('file_extension: ' + file_extension)

if not os.path.isfile(full_file_name) \
        and file_extension == download_format:
    with FTP(website_address, timeout=600) as ftp:
        ftp.login()
        ftp.cwd(folder_path)
        ftp.retrbinary("RETR {full_file_name}"
                       .format(full_file_name=full_file_name),
                       open(full_file_name, 'wb').write)

        input_file = gzip.GzipFile(full_file_name, 'rb')
        s = input_file.read()
        input_file.close()

        output_file = open("{file_name}.txt"
                           .format(file_name=full_file_name), 'wb')
        output_file.write(s)
        output_file.close()

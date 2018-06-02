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
args = parser.parse_args()
download_url = args.download

website_address = download_url[:download_url.find('/'):]
folder_path = download_url[download_url.find('/'):download_url.rfind('/'):]
full_file_name = download_url[download_url.rfind('/') + 1::]
file_name = full_file_name[:full_file_name.rfind('.'):]

# the FTP takes a lot of time to respond
# so sometimes the script ends with TimeoutError
if not os.path.isfile(full_file_name):
    with FTP(website_address, timeout=600) as ftp:
        ftp.login()
        ftp.cwd(folder_path)
        ftp.retrbinary("RETR {full_file_name}"
                       .format(full_file_name=full_file_name),
                       open(full_file_name, 'wb').write)

    with gzip.GzipFile(full_file_name, 'rb') as input_file:
        s = input_file.read()

    with open("{file_name}.txt".format(file_name=file_name), 'wb') \
            as output_file:
        output_file.write(s)

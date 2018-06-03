import argparse
from csv import DictWriter
import json
import urllib.request
# pip install xmltodict
import xmltodict
import yaml


def output_csv(file_name, content):
    with open(file_name + '.csv', 'w') as file:
        writer = DictWriter(file, content[0].keys())
        writer.writeheader()
        writer.writerows(content)


def output_json(file_name, content):
    with open(file_name + '.json', 'w') as file:
        json.dump(content, file, indent=4)


def output_yml(file_name, content):
    with open(file_name + '.yml', 'w') as file:
        yaml.dump(content, file, default_flow_style=False)


def output_xml(file_name, content):
    with open(file_name + '.xml', 'w') as file:
        content_with_root = {'root': {'item': content}}
        xml_string = xmltodict.unparse(content_with_root, pretty=True)
        file.write(xml_string)


# NOTE: it is expected that the called url returns an array in json
parser = argparse.ArgumentParser()
parser.add_argument('--download',
                    help='define the url of the file',
                    default='https://api.nexchange.io/en/api/v1/currency/')
parser.add_argument('--format',
                    help='define the acceptable file format',
                    default='json')
args = parser.parse_args()
download_url = args.download
file_format = args.format

content = urllib.request.urlopen(download_url)
data = json.loads(content.read())

if file_format == 'yml':
    output_yml('output', data)
elif file_format == 'json':
    output_json('output', data)
elif file_format == 'xml':
    output_xml('output', data)
elif file_format == 'csv':
    output_csv('output', data)

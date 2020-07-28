#!/usr/bin/env python3

from prometheus_client.parser import text_string_to_metric_families
import requests
import sys

url = sys.argv[1]
r = requests.get(url)

markdown_lines = []

for family in text_string_to_metric_families(r.text):
    markdown_lines.append('- `' + family.name + '` (' + family.type + '): ' + family.documentation)

markdown_lines.sort()

for line in markdown_lines:
    print(line)


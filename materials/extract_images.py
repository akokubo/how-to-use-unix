import sys
import re

if len(sys.argv) < 2:
    print("使い方: python extract_images.py <markdownファイル>")
    sys.exit(1)

filename = sys.argv[1]

pattern = re.compile(r'!\[.*?\]\(.*?/([^/]+)\)')

try:
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()
except FileNotFoundError:
    print(f"ファイルが見つかりません: {filename}")
    sys.exit(1)

filenames = []
for line in lines:
    match = pattern.search(line)
    if match:
        filenames.append(match.group(1))

for name in filenames:
    print(name)


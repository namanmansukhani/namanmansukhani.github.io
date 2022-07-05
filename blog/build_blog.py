#!/bin/python3

import os
import markdown

for file in os.listdir():
    if file.endswith('.md'):
        if file == 'index.md':
            continue
        dst = f"{file.replace('.md', '.html')}"
        os.system(f"lowdown {file} > {dst}")
        print(f"converted {file} to {dst}")

with open('index.md') as md:
    md_text = md.readlines()
    md_text = ''.join(md_text)
    html = markdown.markdown(md_text)

with open('index.html', 'w') as f:
    f.writelines([html])

print('Converted index.md to index.html')

final_cmd = '''../ssg5 . ../blog/ "Naman's Blog" "https://namanmansukhani.github.io/"'''

os.system(final_cmd)

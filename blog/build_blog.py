#!/bin/python3

import os

for file in os.listdir():
    if file.endswith('.md'):
        dst = f"{file.replace('.md', '.html')}"
        os.system(f"lowdown {file} > {dst}")
        print(f"converted {file} to {dst}")

final_cmd = '''../ssg5 . ../blog/ "Naman's Blog" "https://namanmansukhani.github.io/"'''

os.system(final_cmd)

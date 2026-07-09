import re
import os.path

regex = r'\]\(([^)]+)\)'
base_url = "https://github.com/mycelialdesigns/Plaice/blob/main"

repo_root_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
readme_path = os.path.join(repo_root_path, "README.md")

def replace_func(match):
    return "](" + base_url + match.group(1) + ")"


with open(readme_path, 'r') as file:
    text = file.read()
    replaced_text = re.sub(regex, replace_func, text)
    print(replaced_text)

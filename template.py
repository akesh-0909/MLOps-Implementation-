import os

# os.path.join we use this to join paths acc to system because diff systems, have diff-2 syles of paths


dirs = [
    os.path.join('data', 'raw'),
    os.path.join('data', 'proecssed'),
    'notebooks',
    'saved_models',
    "src"

]


for dir_ in dirs:
    # if true it will create if dir not exits else do nothing (if present)
    os.makedirs(dir_, exist_ok=True)
    with open(os.path.join(dir_, ".gitkeep"), 'w') as f:
        pass

files = [
    "dvc.yaml",
    "params.yaml",
    ".gitignore",  # files are not pushed which are mentioned in this
    os.path.join("src", "__init__.py")
    # README.md etc fioles
]

for file_ in files:
    with open(file_, 'w'):
        pass

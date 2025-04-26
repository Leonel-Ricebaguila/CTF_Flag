added_files = [
    ('background.jpg', '.'),
    ('icon.ico', '.'),
    ('icon.png', '.')
]

a = Analysis(
    ['Flag_code.py'],
    datas=added_files,
    ...
)
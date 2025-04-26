# build.spec
# -*- mode: python -*-

block_cipher = None

# List of data files to include (images/icons)
added_files = [
    ('background.jpg', '.'),   # (source, destination_folder_in_bundle)
    ('icon_windows.ico', '.'),     # Windows icon
    ('icon_mac.icns', '.'),    # macOS icon
    ('icon_linux.png', '.')      # Linux/fallback icon
]

a = Analysis(
    ['Flag_code.py'],          # Your main Python script
    pathex=[],                 # Additional search paths
    binaries=[],
    datas=added_files,         # Include your images/icons
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

# Windows/Mac/Linux configuration
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='Flag',           # Output name (no .exe needed)
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,                  # Compress executable (install UPX first)
    runtime_tmpdir=None,       # Fixes temp folder issues
    console=False,             # Set to True to show console
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='icon.ico',       # Windows icon
)

# For macOS .app bundles
app = APP(
    exe,
    name='Flag',
    icon='icon.icns',      # macOS icon
    info_plist={
        'NSHighResolutionCapable': 'True'  # Retina display support
    }
)
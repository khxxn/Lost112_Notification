# -*- mode: python ; coding: utf-8 -*-
import os

block_cipher = None


a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('.env', '.'),
        (os.path.join('assets', 'frame0', '*.png'), os.path.join('assets', 'frame0')),
        (os.path.join('assets', 'frame0', '*.gif'), os.path.join('assets', 'frame0'))  
    ],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='Lost112 Notification',
    icon=os.path.join('assets', 'frame0', 'main_icon.ico'),
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
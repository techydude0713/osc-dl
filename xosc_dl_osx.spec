# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['xosc_dl.py'],
    pathex=[],
    binaries=[],
    datas=[('assets/gui/icons/controllers/*.png', './assets/gui/icons/controllers/'),
                    ('assets/gui/icons/category/*.png', './assets/gui/icons/category/'),
                    ('assets/gui/*.png', './assets/gui/'),
                    ('assets/themes/*.qss', './assets/themes/'),
                    ('assets/gui/icons/*.gif', './assets/gui/icons/'),
                    ('assets/gui/icons/*.png', './assets/gui/icons/'),
                    ('assets/gui/icons/status/*.png', './assets/gui/icons/status')],
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
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='xosc_dl',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='xosc_dl',
)
app = BUNDLE(
    coll,
    name='OSC-DL.app',
    icon='oscicon.ico',
    bundle_identifier="com.OSC.OSCDL",
    info_plist={
        'CFBundleURLTypes' : [
            {
                'CFBundleTypeRole' : 'Viewer',
                'CFBundleURLName' : 'OSC-DL',
                'CFBundleURLSchemes' : ['osc-dl'],
            }
        ]
    }
)

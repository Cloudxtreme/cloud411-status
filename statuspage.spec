# -*- mode: python -*-

block_cipher = None


a = Analysis(['statuspage.py'],
             pathex=['.'],
             binaries=None,
             datas=None,
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [
            (
                'template/index.html',
                'template/index.html',
                'template'
            ),
            (
                'template/style.css',
                'template/style.css',
                'template'
            ),
            (
                'template/milligram.min.css',
                'template/milligram.min.css',
                'template'
            ),
            (
                'template/script.js',
                'template/script.js',
                'template'
            ),
            (
                'template/mustache.min.js',
                'template/mustache.min.js',
                'template'
            ),
            (
                'template/lockr.js',
                'template/lockr.js',
                'template'
            )
          ],
          name='statuspage',
          debug=False,
          strip=False,
          upx=True,
          console=True )

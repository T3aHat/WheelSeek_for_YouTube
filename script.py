import zipfile
with zipfile.ZipFile('wheelseeker.zip', 'w')as zf:
    zf.write('manifest.json')
    zf.write('background.js')
    zf.write('contents.js')
    zf.write('contentsGen.js')
    zf.write('popup.js')
    zf.write('popup.html')
    zf.write('style.css')
    zf.write('popupstyle.css')
    zf.write('icon128.png')

"""Tải 11 ảnh chụp thực tế về máy (tùy chọn) để website hoạt động offline.

Chạy bằng: python download_real_photos.py
Mặc định website dùng URL Wikimedia Commons và tự fallback sang hình minh họa.
"""
from pathlib import Path
from urllib.request import Request, urlopen
import json
import io
import re
from PIL import Image

ROOT=Path(__file__).resolve().parent
META=json.loads((ROOT/'PHOTO_SOURCES.json').read_text(encoding='utf-8'))
CATALOG=ROOT/'catalog.js'
OUT=ROOT/'assets'/'real-photos'
OUT.mkdir(parents=True,exist_ok=True)
js=CATALOG.read_text(encoding='utf-8')
worked=0
for ident,item in META.items():
    target=OUT/f'{ident}.webp'
    print(f'[{ident}] {item["title"]}')
    if not target.exists():
        try:
            req=Request(item['image'],headers={'User-Agent':'Mozilla/5.0 (compatible; ThaoThuCungDemo/1.0)'})
            with urlopen(req,timeout=20) as res:
                raw=res.read(8*1024*1024)
            with Image.open(io.BytesIO(raw)) as img:
                img=img.convert('RGB')
                img.thumbnail((1000,900))
                img.save(target,'WEBP',quality=83,method=5)
        except Exception as e:
            print('   Không tải được:',str(e)[:110]);continue
    # Change only PHOTO metadata image URL to downloaded local path.
    remote=json.dumps(item['image'],ensure_ascii=False)
    local=json.dumps('assets/real-photos/'+ident+'.webp',ensure_ascii=False)
    if remote in js:
        js=js.replace(remote,local,1)
        worked+=1
        print('   Đã cài ảnh offline:',target.name)
    elif local in js:
        worked+=1
        print('   Ảnh offline đã sẵn sàng.')
if worked:
    CATALOG.write_text(js,encoding='utf-8')
print(f'Xong: {worked}/{len(META)} ảnh đã được cài đặt để sử dụng offline.')
print('Nếu thiếu ảnh, website tự sử dụng hình vẽ minh họa cũ.')

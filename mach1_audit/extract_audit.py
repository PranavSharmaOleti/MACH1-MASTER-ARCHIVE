import csv, hashlib, json, mimetypes, os, re, stat, subprocess, sys, zipfile
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path('/home/sankara/Downloads/MACH1_WORKING_FILES')
OUT = Path('/tmp/mach1_audit')
ARCHIVE_NAME = 'MACH1_MASTER_ARCHIVE'

def sha256(path):
    h = hashlib.sha256()
    with path.open('rb') as f:
        for b in iter(lambda: f.read(1024 * 1024), b''):
            h.update(b)
    return h.hexdigest()

def trunc(value, n=60000):
    value = value or ''
    return value[:n] + ('\n[EXTRACTION TRUNCATED]' if len(value) > n else '')

def pdf_extract(path):
    result = {'pages': [], 'error': None}
    try:
        info = subprocess.run(['pdfinfo', str(path)], capture_output=True, text=True, check=True)
        match = re.search(r'^Pages:\s+(\d+)', info.stdout, re.M)
        if not match: raise RuntimeError('pdfinfo did not report page count')
        result['page_count'] = int(match.group(1))
        for i in range(1, result['page_count'] + 1):
            try:
                page = subprocess.run(['pdftotext', '-layout', '-f', str(i), '-l', str(i), str(path), '-'], capture_output=True, text=True, check=True)
                result['pages'].append({'page': i, 'text': trunc(page.stdout)})
            except Exception as e:
                result['pages'].append({'page': i, 'text': '', 'error': str(e)})
    except Exception as e:
        result['error'] = str(e)
    return result

def zip_listing(path):
    try:
        with zipfile.ZipFile(path) as z:
            return {'members': [{'name': x.filename, 'size': x.file_size} for x in z.infolist()[:10000]]}
    except Exception as e:
        return {'error': str(e)}

def text_extract(path):
    try:
        return trunc(path.read_text(encoding='utf-8', errors='replace'))
    except Exception as e:
        return '[UNREADABLE TEXT: %s]' % e

def pptx_extract(path):
    result = {'slides': [], 'error': None}
    try:
        with zipfile.ZipFile(path) as z:
            names = sorted([n for n in z.namelist() if re.match(r'ppt/slides/slide\d+\.xml$', n)], key=lambda n:int(re.search(r'(\d+)', n).group(1)))
            for name in names:
                raw = z.read(name).decode('utf-8', 'replace')
                strings = re.findall(r'<a:t>(.*?)</a:t>', raw, re.S)
                strings = [re.sub(r'<.*?>', '', s).replace('&amp;', '&') for s in strings]
                result['slides'].append({'slide': int(re.search(r'(\d+)', name).group(1)), 'text': '\n'.join(strings)})
    except Exception as e:
        result['error'] = str(e)
    return result

def classify(rel, suffix):
    p = rel.lower()
    if 'superseded' in p or 'round1' in p or 'draft' in p or 'old' in p: return 'Archive / older version'
    if suffix in {'.py', '.pyc'}: return 'Code / automation'
    if suffix == '.csv': return 'Raw or processed tabular data'
    if suffix in {'.dwg'}: return 'CAD / drawing'
    if suffix in {'.png','.jpg','.jpeg','.svg'}: return 'Image / plot / screenshot'
    if suffix in {'.pptx'}: return 'Presentation source'
    if suffix in {'.zip'}: return 'Compressed package / dependency archive'
    if suffix in {'.html','.md','.txt'}: return 'Technical note / working document'
    if suffix == '.pdf': return 'PDF document / report / reference'
    if suffix == '.mp4': return 'Video deliverable'
    return 'Other'

files=[]; extract={}; dirs=[]
for path in sorted(ROOT.rglob('*')):
    if ARCHIVE_NAME in path.parts: continue
    rel=str(path.relative_to(ROOT))
    if path.is_dir():
        dirs.append(rel)
        continue
    if not path.is_file(): continue
    st=path.stat(); suffix=path.suffix.lower()
    rec={'path':rel, 'name':path.name, 'extension':suffix or '[no extension]', 'size_bytes':st.st_size,
         'modified_utc':datetime.fromtimestamp(st.st_mtime, tz=timezone.utc).isoformat(), 'sha256':sha256(path),
         'mime':mimetypes.guess_type(path.name)[0] or 'application/octet-stream', 'classification':classify(rel,suffix)}
    files.append(rec)
    if suffix == '.pdf': extract[rel]=pdf_extract(path)
    elif suffix in {'.py','.md','.html','.txt','.csv','.svg'}: extract[rel]={'text': text_extract(path)}
    elif suffix == '.pptx': extract[rel]=pptx_extract(path)
    elif suffix == '.zip': extract[rel]=zip_listing(path)

dups=defaultdict(list)
for f in files: dups[f['sha256']].append(f['path'])
duplicate_groups=[v for v in dups.values() if len(v)>1]
payload={'root':str(ROOT),'generated_utc':datetime.now(timezone.utc).isoformat(),'files':files,'directories':dirs,'extract':extract,'duplicate_groups':duplicate_groups}
(OUT/'inventory.json').write_text(json.dumps(payload, indent=2), encoding='utf-8')
print(json.dumps({'files':len(files),'directories':len(dirs),'duplicate_groups':len(duplicate_groups)}))

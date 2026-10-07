#!/usr/bin/env python3
"""Duplicatedove: read-only exact duplicate text-line counts, source text hidden."""
import argparse,collections,json,re,sys
from pathlib import Path
MAX=1048576
def analyze(data):
    text=data.decode('utf-8');lines=re.split(r'\r\n|\r|\n',text)
    if not text:lines=[]
    elif text.endswith(('\r','\n')):lines.pop()
    positions=collections.defaultdict(list)
    for idx,line in enumerate(lines,1):positions[line].append(idx)
    duplicates=[{'count':len(p),'line_numbers':p} for p in positions.values() if len(p)>1];duplicates.sort(key=lambda x:x['line_numbers'][0])
    return {'lines':len(lines),'unique_lines':len(positions),'duplicate_groups':duplicates,'repeated_occurrences_beyond_first':sum(x['count']-1 for x in duplicates),'note':'Exact decoded lines, terminators removed, no trimming/casefolding. Text/keys/hashes not emitted; positions/counts may be sensitive.'}
def inspect(path):
    p=Path(path)
    if not p.is_file() or p.stat().st_size>MAX:raise ValueError()
    with p.open('rb') as f:data=f.read(MAX+1)
    if len(data)>MAX:raise ValueError()
    return analyze(data)
def main(argv=None):
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('file',nargs='?');a=p.parse_args(argv)
    try:
        path=a.file
        if not path:print('UTF-8 file (0 exits): ',end='',file=sys.stderr);path=input()
        if not a.file and path=='0':return 0
        print(json.dumps(inspect(path),indent=2))
    except (ValueError,UnicodeError,OSError):print('Cannot read regular UTF-8 file <=1 MiB. Source not echoed.',file=sys.stderr);return 2
    except (EOFError,KeyboardInterrupt):print('\nCancelled.',file=sys.stderr)
    return 0
if __name__=='__main__':raise SystemExit(main())

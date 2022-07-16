#!/usr/bin/env python3

import html
import re
import sys
import urllib.parse
import urllib.request

from typing import List


BOLD_CYAN = '\x1b[1;36m'
BOLD_RED = '\x1b[1;31m'
BOLD_UNDERLINE_RED = '\x1b[1;4;31m'
BOLD_YELLOW = '\x1b[1;33m'
NEGATIVE_GREEN = '\x1b[1;7;32m'
RESET = '\x1b[0m'

OPTIONS = [
    'shell',
    'command',
    'reverse-shell',
    'non-interactive-reverse-shell',
    'bind-shell',
    'non-interactive-bind-shell',
    'file-upload',
    'file-download',
    'file-write',
    'file-read',
    'library-load',
    'suid',
    'sudo',
    'capabilities',
    'limited-suid'
]


def gtfobins(cmd: str, options: List[str]):
    url = f'https://gtfobins.github.io/gtfobins/{cmd}/'
    res = get_url(url)

    print(f'\n{NEGATIVE_GREEN}{cmd}{RESET} ==> {BOLD_YELLOW}{url}{RESET}\n')

    blocks = list(map(lambda x: f'<h2{x}', res.split('<h2')[1:]))
    results = []

    for res in blocks:
        method, title = re.findall(
            r'\s*?<h2 id="(.*?)".*?>(.*?)</h2>', res, re.MULTILINE)[0]
        descriptions = re.findall(
            r'\s*?</h2>\n<p>([\s\S]*?)</p>', res, re.MULTILINE)
        lists = re.findall(r'\s*?<ul.*?>([\s\S]*?)</ul>', res, re.MULTILINE)

        if method in options or not options:
            results += [f'\n{BOLD_UNDERLINE_RED}{title}{RESET}']
            results += map(parse_text, descriptions)
            results += map(parse_lists, lists)

    if results:
        print('\n\n'.join(results))
    else:
        print(f'\n{BOLD_UNDERLINE_RED}Could not load method for `{cmd}`{RESET}')


def print_help():
    options = '\n         --'.join(OPTIONS)
    print(f'\n{BOLD_UNDERLINE_RED}Usage: gtfobins-cli [options] <command>')
    print(f'\n{RESET}Options: {BOLD_RED}--{options}{RESET}')

    res = get_url('https://gtfobins.github.io/')

    examples = re.findall(
        r'\s*?<td><a href=".*?" class="bin-name">(.*?)</a>', res, re.MULTILINE)

    print('\nBinaries:')
    print(f'{BOLD_YELLOW}{f"{RESET}, {BOLD_YELLOW}".join(examples)}{RESET}')


def get_url(url: str) -> str:
    try:
        return html.unescape(urllib.request.urlopen(url).read().decode())
    except:
        print(f'\n{BOLD_UNDERLINE_RED}Could not load page{RESET}')
        print(f'\nSearch on: {BOLD_YELLOW}https://gtfobins.github.io/{RESET}')
        sys.exit(1)


def parse_text(res: str) -> str:
    res = re.sub(r'<a.+?>', BOLD_YELLOW, res)
    res = re.sub(r'<em>', BOLD_RED, res)
    res = re.sub(r'<code.+?>', BOLD_CYAN, res)

    return re.sub(r'</a>|</em>|</code>', RESET, res).strip()


def parse_lists(res: str) -> str:
    items = re.findall(r'\s*?<li>([\s\S]*?)</li>', res, re.MULTILINE)
    res = []

    for item in items:
        descriptions = re.findall(r'\s*?<p>([\s\S]*?)</p>', item, re.MULTILINE)
        codeblocks = re.findall(
            r'\s*?<pre.*?><code>([\s\S]*?)</code></pre>', item, re.MULTILINE)
        res += map(parse_text, descriptions)
        res += map(lambda t: f'{BOLD_CYAN}{t.strip()}{RESET}', codeblocks)

    return '\n\n'.join(res)


def main():
    if len(sys.argv) == 1 or sys.argv[1] in {'-h', '--help'}:
        print_help()
        sys.exit(1)

    options = list(map(lambda s: s.lstrip('--'), sys.argv[1:-1]))
    gtfobins(sys.argv[-1], options)


if __name__ == '__main__':
    main()

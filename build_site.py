"""Builds index.html from src.html + data/src/overrides.js. Run after editing either. Bumps the service worker version."""
import re, time, os
HERE = os.path.dirname(os.path.abspath(__file__))
s = open(os.path.join(HERE, "src.html")).read()
s = s.replace("__DATA__", open(os.path.join(HERE, "data/src/overrides.js")).read())
s = s.replace('const IMG = {front:"__FRONT__", back:"__BACK__"};', 'const IMG = {front:"icons/front.jpg", back:"icons/back.jpg"};')
assert "__FRONT__" not in s and "__DATA__" not in s
head = '''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="color-scheme" content="light dark">
<meta name="theme-color" content="#3d5a38" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#131a15" media="(prefers-color-scheme: dark)">
<meta name="description" content="A guided first step for veterans with no records: your job, your service, your body, your next move.">
<link rel="manifest" href="manifest.webmanifest">
<link rel="icon" href="icons/icon-192.png" type="image/png">
<link rel="apple-touch-icon" href="icons/apple-touch-icon.png">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="default">
<meta name="apple-mobile-web-app-title" content="Where Do I Start">
<style>:root{padding-top:env(safe-area-inset-top,0px)}body{margin:0}img{max-width:100%}[hidden]{display:none!important}</style>
'''
i = s.index("<style>")
out = head + s[:i] + s[i:].replace("</style>", "</style>\n</head>\n<body>", 1) + "\n</body>\n</html>\n"
open(os.path.join(HERE, "index.html"), "w").write(out)
sw = open(os.path.join(HERE, "sw.js")).read()
ver = "wdis-" + time.strftime("%Y%m%d%H%M")
sw = re.sub(r'const VERSION = "[^"]+";', f'const VERSION = "{ver}";', sw)
if "./data/mos.json" not in sw:
    sw = sw.replace('"./icons/back.jpg"]', '"./icons/back.jpg", "./data/mos.json", "./data/profiles.json"]')
open(os.path.join(HERE, "sw.js"), "w").write(sw)
print("built index.html,", len(out), "bytes; service worker", ver)

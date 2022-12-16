#!/bin/python
# coding=utf-8

html_template="""
<!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>
        《群体遗传学原理（中译版）》-目录
        </title>
        <style>
/* From extension vscode.github */
/*---------------------------------------------------------------------------------------------
 *  Copyright (c) Microsoft Corporation. All rights reserved.
 *  Licensed under the MIT License. See License.txt in the project root for license information.
 *--------------------------------------------------------------------------------------------*/

.vscode-dark img[src$=\#gh-light-mode-only],
.vscode-light img[src$=\#gh-dark-mode-only] {
	display: none;
}

</style>
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex/dist/katex.min.css">
<link href="https://cdn.jsdelivr.net/npm/katex-copytex@latest/dist/katex-copytex.min.css" rel="stylesheet" type="text/css">
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/Microsoft/vscode/extensions/markdown-language-features/media/markdown.css">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/Microsoft/vscode/extensions/markdown-language-features/media/highlight.css">
<style>
            body {
                font-family: -apple-system, BlinkMacSystemFont, 'Segoe WPC', 'Segoe UI', system-ui, 'Ubuntu', 'Droid Sans', sans-serif;
                font-size: 14px;
                line-height: 1.6;
            }
        </style>
        <style>
.task-list-item {
    list-style-type: none;
}

.task-list-item-checkbox {
    margin-left: -20px;
    vertical-align: middle;
    pointer-events: none;
}
</style>
</head>        
<body class="vscode-body vscode-light">
        <h1 id="Title">《群体遗传学原理》（Principle of population genetics, 4th）中译本</h1>
        <h2 id="Content">(translated by Warren Z)</h2>
        <h2 id="Content">目录</h2>
<ul>
{{li}}
</ul>
"""

li_template = """
<li><a href="{{link}}" target=_blank>{{title}}</a></li>
"""

# 先生成前言的链接
inner_HTML = li_template.replace("{{link}}","preface.html").replace("{{title}}","前言")

# 然后生成各章节的链接
import os
ls = os.listdir() # 这个语句可以获取当前目录下所有文件的列表
mdfl = []
for f in ls:
    if(("chapter"in f) and (f.endswith('md'))): # 然后只保留文件名包含chapter的markdown文件名
        mdfl.append(f)
# 并依次打开这些文件，读取第一行的文本，这一行文本中有章节标题。
for f in mdfl:
    inf = open(f,'r',encoding="utf-8")
    title = ""
    for line in inf:
        title = line
        break
    inf.close()
    title = title.strip().replace("# ","")
    link  = f.replace(".md",".html")
    inner_HTML += li_template.replace("{{link}}",link).replace("{{title}}",title)
# 然后写入index.html
HTML = html_template.replace("{{li}}",inner_HTML)
outf = open("index.html",'w',encoding="utf-8")
outf.write(HTML)
outf.close()
        





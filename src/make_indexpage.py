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
<!------- Flow analysis:BEGIN -------->
<script>
var _hmt = _hmt || [];
(function() {
  var hm = document.createElement("script");
  hm.src = "https://hm.baidu.com/hm.js?8fd7869a3d296e620f31f7541dec4e7f";
  var s = document.getElementsByTagName("script")[0];
  s.parentNode.insertBefore(hm, s);
})();
</script>
<!------- Flow analysis:END -------->
</head>        
<body class="vscode-body vscode-light">
  <a href="https://github.com/cyclinbox/PrincipleOfPopulationGenomics" class="github-corner" style="z-index: 9999;" aria-label="View source on GitHub"><svg width="80" height="80" viewBox="0 0 250 250" style="fill:#151513; color:#fff; position: absolute; top: 0; border: 0; left: 0; transform: scale(-1, 1);" aria-hidden="true"><path d="M0,0 L115,115 L130,115 L142,142 L250,250 L250,0 Z"></path><path d="M128.3,109.0 C113.8,99.7 119.0,89.6 119.0,89.6 C122.0,82.7 120.5,78.6 120.5,78.6 C119.2,72.0 123.4,76.3 123.4,76.3 C127.3,80.9 125.5,87.3 125.5,87.3 C122.9,97.6 130.6,101.9 134.4,103.2" fill="currentColor" style="transform-origin: 130px 106px;" class="octo-arm"></path><path d="M115.0,115.0 C114.9,115.1 118.7,116.5 119.8,115.4 L133.7,101.6 C136.9,99.2 139.9,98.4 142.2,98.6 C133.8,88.0 127.5,74.4 143.8,58.0 C148.5,53.4 154.0,51.2 159.7,51.0 C160.3,49.4 163.2,43.6 171.4,40.1 C171.4,40.1 176.1,42.5 178.8,56.2 C183.1,58.6 187.2,61.8 190.9,65.4 C194.5,69.0 197.7,73.2 200.1,77.6 C213.8,80.2 216.3,84.9 216.3,84.9 C212.7,93.1 206.9,96.0 205.4,96.6 C205.1,102.4 203.0,107.8 198.3,112.5 C181.9,128.9 168.3,122.5 157.7,114.1 C157.9,116.9 156.7,120.9 152.7,124.9 L141.0,136.5 C139.8,137.7 141.6,141.9 141.8,141.8 Z" fill="currentColor" class="octo-body"></path></svg><style>.github-corner:hover .octo-arm{animation:octocat-wave 560ms ease-in-out}@keyframes octocat-wave{0%,100%{transform:rotate(0)}20%,60%{transform:rotate(-25deg)}40%,80%{transform:rotate(10deg)}}@media (max-width:500px){.github-corner:hover .octo-arm{animation:none}.github-corner .octo-arm{animation:octocat-wave 560ms ease-in-out}}</style></a>
        <h1 id="Title">《群体遗传学原理》（Principle of population genetics, 4th）中译本</h1>
        <h2 id="Content">(translated by cyclinbox)</h2>
        <h2 id="Content">目录</h2>
<ul>
{{li}}
</ul>
"""

li_template = """
<li><a href="{{link}}">{{title}}</a></li>
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
        





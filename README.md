# 《群体遗传学原理》第四版 中译本

> Hartl and Clark. Principle of population genetics, 4th

## 如何阅读

文档已经以GitHub Pages的形式发布。请访问[https://cyclinbox.github.io/PrincipleOfPopulationGenomics/](https://cyclinbox.github.io/PrincipleOfPopulationGenomics/)进行阅读。

要阅读英文原版书（PDF扫描件），请直接访问根目录文件或下载 [Principle of population genetics 4th ed - Hartl and Clark.pdf](https://raw.githubusercontent.com/cyclinbox/PrincipleOfPopulationGenomics/refs/heads/main/Principle%20of%20population%20genetics%204th%20ed%20-%20Hartl%20and%20Clark.pdf) 


## 目录组织

```
.
+---docs
\---src
    \---asset
```

其中，`docs` 是编译完成的html文件存档，可以使用浏览器访问浏览。`src` 为markdown源代码目录以及一些资源文件（如插图）。

## 编译说明

所有章节内容的html文档使用VS Code的[Markdown All in One](https://github.com/yzhang-gh/vscode-markdown/)插件进行编译。

根目录下的`build.sh`是一个自动化处理的脚本，主要用于（1）`index.html`的生成；（2）`docs`目录的更新；（3）备份文件的生成。另一个脚本`deploy.sh`则用于自动化提交更新到Github存储库当中。读者朋友可以不用理会这两个脚本，直接访问[docs目录](https://cyclinbox.github.io/PrincipleOfPopulationGenomics/)即可。


## 其他补充信息

这份中译版由个人翻译，由于译者精力和英语水平所限，翻译内容恐有疏漏，还请大家批评指正。

网上有人提到这本书有中译本了，估计再翻译一遍也不会有太大意义。但是，这本书有极高的学习价值，因此我想通过翻译课本这种方式督促自己学习，同时也用中译本帮助群体遗传学领域的读者们。

全书凡六百余页，内容较多，因此何时能够全部翻译完成并不好说。只是希望自己能够坚持下去，且行且珍惜。

以上。

-----------

2022-11-25 创建项目

2022-12-16 更新README文件并构建GitHub存储库

2022-12-23 添加 `.gitignore` 文件

2022-12-26 优化了部分html代码

2023-04-24 添加`deploy.sh`脚本文件





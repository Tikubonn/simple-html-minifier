
# Simple HTML Minifier 

![](https://img.shields.io/badge/python-v3.9-blue)
![](https://img.shields.io/badge/license-MIT-green)

\| [English](README.md) \| Japanese \|

Simple HTML Minifier は標準ライブラリのみで書かれたシンプルな HTML Minifier です。
この Minifier は不要なコメントとインデントを削除します。
この Minifier は和文の表示がおかしくならないように、
複数行のテキストを minify する際、空白文字ではなく、改行文字を用います。

## Usage

導入後 minify を行うふたつの関数が利用できます。
`minify_html` 関数は任意の HTML 文字列を受け取り minify を行います。

```python
import html_minifier 

html_minifier.minify_html("any html formatted texts.")
```

ファイル入力から minify したい場合には `minify_html_from_file` 関数も利用することができます。

```python
import html_minifier 

with open("example.html", "r") as stream:
  html_minifier.minify_html_from_file(stream)
```

## License 

Simple HTML Minifier は [MIT License](LICENSE) で公開されています。

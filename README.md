
# Simple HTML Minifier 

![](https://img.shields.io/badge/python-v3.9-blue)
![](https://img.shields.io/badge/license-MIT-green)

\| English \| [Japanese](README.ja.md) \|

the simple HTML minifier that made of standard libraries.
this minifier remove indentations and comments.
if this minify multiple line text, this use newline as separator for line.
it's important, because use white-space to separator is make a wrong effect to Japanese typography.

## Usage

after installed, you can use two minifier functions from this library.
`minify_html` try minify inputted text as html.

```python
import html_minifier 

html_minifier.minify_html("any html formatted texts.")
```

if you want to input from file stream, you could use  `minify_html_from_file` function.

```python
import html_minifier 

with open("example.html", "r") as stream:
  html_minifier.minify_html_from_file(stream)
```

## License 

Simple HTML Minifier is released under the [MIT License](LICENSE).

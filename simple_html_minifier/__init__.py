
from io import IOBase, StringIO
from html.parser import HTMLParser

class HTMLMinifier (HTMLParser):

  def __init__ (self):
    super().__init__()
    self.buffer = StringIO()

  def __enter__ (self):
    return self 

  def __exit__ (self, error_type, error_value, backtrace):
    self.buffer.close()

  def get_result (self):
    return self.buffer.getvalue()

  def close (self):
    self.buffer.close()

  def handle_starttag (self, tag: str, attributes: list):
    self.buffer.write("<")
    self.buffer.write(tag)
    for key, value in attributes:
      self.buffer.write(" ")
      self.buffer.write(key)
      self.buffer.write("=\"")
      self.buffer.write(value)
      self.buffer.write("\"")
    self.buffer.write(">")

  def handle_endtag (self, tag: str):
    self.buffer.write("</")
    self.buffer.write(tag)
    self.buffer.write(">")

  def handle_startendtag (self, tag: str):
    self.buffer.write("<")
    self.buffer.write(tag)
    for key, value in attributes:
      self.buffer.write(" ")
      self.buffer.write(key)
      self.buffer.write("=\"")
      self.buffer.write(value)
      self.buffer.write("\"")
    self.buffer.write(">")

  def handle_data (self, data: str):
    minified = "\n".join(filter(lambda stripped: stripped, (line.strip() for line in data.split("\n"))))
    self.buffer.write(minified)

  def handle_entityref (self, name: str):
    self.buffer.write("&")
    self.buffer.write(name)
    self.buffer.write(";")

  def handle_charref (self, name: str):
    self.buffer.write("&#")
    self.buffer.write(name)
    self.buffer.write(";")

  def handle_comment (self, data: str):
    pass

  def handle_decl (self, declaration: str):
    self.buffer.write("<!")
    self.buffer.write(declaration)
    self.buffer.write(">")

def minify_html_from_file (stream: IOBase):

  """
  minify html from file stream.
  """

  with HTMLMinifier() as minifier:
    minifier.feed(stream.read())
    return minifier.get_result()

def minify_html (text: str):

  """
  minify html from string.
  """

  with HTMLMinifier() as minifier:
    minifier.feed(text)
    return minifier.get_result()

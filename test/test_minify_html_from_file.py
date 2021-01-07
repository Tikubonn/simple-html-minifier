
import unittest
from io import StringIO 
from simple_html_minifier import minify_html_from_file 

class TestMinifyHTMLFromFile (unittest.TestCase):

  def test_minify_html_from_file1 (self):
    source = """
    moco
    and
    nanashi
    """
    shouldbe = "moco\nand\nnanashi"
    with StringIO(source) as stream:
      self.assertEqual(minify_html_from_file(stream), shouldbe)

  def test_minify_html_from_file2 (self):
    source = """
    <a href="any pages">
    moco
    and
    nanashi
    </a>
    """
    shouldbe = "<a href=\"any pages\">moco\nand\nnanashi</a>"
    with StringIO(source) as stream:
      self.assertEqual(minify_html_from_file(stream), shouldbe)

  def test_minify_html_from_file3 (self):
    source = """
    <div>
    <a href="any pages">
    moco
    and
    nanashi
    </a>
    <a href="any pages">chibi-chan</a>
    </div>
    """
    shouldbe = "<div><a href=\"any pages\">moco\nand\nnanashi</a><a href=\"any pages\">chibi-chan</a></div>"
    with StringIO(source) as stream:
      self.assertEqual(minify_html_from_file(stream), shouldbe)

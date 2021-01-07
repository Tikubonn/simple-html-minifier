
import unittest
from simple_html_minifier import minify_html 

class TestMinifyHTML (unittest.TestCase):

  def test_minify_html1 (self):
    source = """
    moco
    and
    nanashi
    """
    shouldbe = "moco\nand\nnanashi"
    self.assertEqual(minify_html(source), shouldbe)

  def test_minify_html2 (self):
    source = """
    <a href="any pages">
    moco
    and
    nanashi
    </a>
    """
    shouldbe = "<a href=\"any pages\">moco\nand\nnanashi</a>"
    self.assertEqual(minify_html(source), shouldbe)

  def test_minify_html3 (self):
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
    self.assertEqual(minify_html(source), shouldbe)

import unittest

from textnode import TextNode
from htmlnode import LeafNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold", "https://hello.com")
        node2 = TextNode("This is a text node", "bold", "https://hello.com")
        self.assertEqual(node, node2)
    def test_not_eq(self):
        node = TextNode("This is a text node", "bold", "https://hello.com")
        node2 = TextNode("This is a different text node", "italic", "https://bye.com")
        self.assertIsNot(node, node2)
    def test_no_url(self):
        node = TextNode("This is a text node", "bold")
        self.assertEqual(node.url, "")
    def test_repr(self):
        node = TextNode("This is a text node", "italic", "https://www.boot.dev")
        self.assertEqual(
            "TextNode(This is a text node, italic, https://www.boot.dev)", repr(node)
        )
    def test_text_html(self):
        text_node = TextNode("Text Node", "text", None)
        leaf_node = LeafNode("", "Text Node")
        self.assertEqual(text_node.text_node_to_html_node(), leaf_node)
    def test_text_html_gen(self):
        text_node = TextNode("Text Node", "text", None)
        self.assertEqual(text_node.text_node_to_html_node().to_html(), "Text Node")
    def test_text_bold(self):
        text_node = TextNode("Bold", "bold", None)
        leaf_node = LeafNode("b", "Bold")
        self.assertEqual(text_node.text_node_to_html_node(), leaf_node)
    def test_text_bold_html(self):
        text_node = TextNode("Bold", "bold", None)
        leaf_node = text_node.text_node_to_html_node()
        self.assertEqual(leaf_node.to_html(), "<b>Bold</b>")
    def test_text_italic(self):
        text_node = TextNode("Italicized", "italic", None)
        leaf_node = LeafNode("i", "Italicized")
        self.assertEqual(text_node.text_node_to_html_node(), leaf_node)
    def test_text_italic_html(self):
        text_node = TextNode("Italicized", "italic", None)
        leaf_node = text_node.text_node_to_html_node()
        self.assertEqual(leaf_node.to_html(), "<i>Italicized</i>")
    def test_text_code(self):
        text_node = TextNode("Code Tag", "code", None)
        leaf_node = LeafNode("code", "Code Tag")
        self.assertEqual(text_node.text_node_to_html_node(), leaf_node)
    def test_text_code_html(self):
        text_node = TextNode("Code Tag", "code", None)
        leaf_node = text_node.text_node_to_html_node()
        self.assertEqual(leaf_node.to_html(), "<code>Code Tag</code>")
    def test_text_link(self):
        text_node = TextNode("Link", "link", "https://www.test.com")
        leaf_node = LeafNode("a", "Link", {"href": "https://www.test.com"})
        self.assertEqual(text_node.text_node_to_html_node(), leaf_node)
    def test_text_link_html(self):
        text_node = TextNode("Link", "link", "https://www.test.com")
        leaf_node = text_node.text_node_to_html_node()
        self.assertEqual(leaf_node.to_html(), '<a href="https://www.test.com">Link</a>')
    def test_text_image(self):
        text_node = TextNode("Image", "image", "image_url")
        leaf_node = LeafNode("img", "", {"src": "image_url", "alt": "Image"})
        self.assertEqual(text_node.text_node_to_html_node(), leaf_node)
    def test_text_image_html(self):
        text_node = TextNode("Image", "image", "image_url")
        leaf_node = text_node.text_node_to_html_node()
        self.assertEqual(leaf_node.to_html(), '<img src="image_url" alt="Image"></img>')
    def test_text_wrong_text(self):
        text_node = TextNode("Random", "na", "")
        with self.assertRaises(Exception):
            text_node.text_node_to_html_node()
    def test_text_wrong_text2(self):
        text_node = TextNode("", "", "")
        with self.assertRaises(Exception):
            text_node.text_node_to_html_node()

if __name__ == "__main__":
    unittest.main()
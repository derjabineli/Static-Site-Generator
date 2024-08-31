import unittest

from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("h1", "hello world", None, {"style": "color: black"})
        node2 = HTMLNode("h1", "hello world", None, {"style": "color: black"})
        self.assertEqual(node, node2)
    
    def test_repr(self):
        node = HTMLNode("h1", "hello world", None, {"style": "color: black"})
        repr(node)
        self.assertEqual("HTMLNode(h1, hello world, None, {'style': 'color: black'})", repr(node))

    def test_no_args(self):
        try:
            node = HTMLNode()
        except:
            self.fail("Couldn't successfuly create new HTMLNode when arguments are empty")
    
    def test_leaf_eq(self):
        node = LeafNode("p", "This is a paragraph of text.")
        node2 = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual(node, node2)
    
    def test_leaf_eq2(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        node2 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node, node2)
    
    def test_no_value(self):
        with self.assertRaises(TypeError):
            node = LeafNode("")
    
    def test_to_html(self):
        node = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual(node.to_html(), '<p>This is a paragraph of text.</p>')
    
    def test_to_html2(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

if __name__ == "__main__":
    unittest.main()
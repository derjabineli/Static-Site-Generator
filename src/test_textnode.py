import unittest

from textnode import TextNode


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
        with self.assertRaises(TypeError):
            node = TextNode("This is a text node", "bold")
    def test_repr(self):
        node = TextNode("This is a text node", "italic", "https://www.boot.dev")
        self.assertEqual(
            "TextNode(This is a text node, italic, https://www.boot.dev)", repr(node)
        )
    
        
        

if __name__ == "__main__":
    unittest.main()
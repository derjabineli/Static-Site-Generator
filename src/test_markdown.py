import unittest
from markdown_utils import split_nodes_delimiter, extract_markdown_links, extract_markdown_images
from textnode import TextNode

text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"

class TestMarkdownUtils(unittest.TestCase):
    def test_split_nodes(self):
        node = TextNode("This is text with a `code block` word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "`", text_type_code)
        test_list = [TextNode("This is text with a ", text_type_text), TextNode("code block", text_type_code), TextNode(" word", text_type_text),]
        self.assertEqual(new_nodes, test_list)
    def test_split_nodes(self):
        node = TextNode("This is text with a `code block` word and another `code block` word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "`", text_type_code)
        test_list = [TextNode("This is text with a ", text_type_text), TextNode("code block", text_type_code), TextNode(" word and another ", text_type_text), TextNode("code block", text_type_code), TextNode(" word", text_type_text)]
        self.assertEqual(new_nodes, test_list)
    def test_split_multiple_nodes(self):
        node = TextNode("This is text with a `code block` word", text_type_text)
        node2 = TextNode("This is text with a `code block` word", text_type_text)
        new_nodes = split_nodes_delimiter([node, node2], "`", text_type_code)
        test_list = [TextNode("This is text with a ", text_type_text), TextNode("code block", text_type_code), TextNode(" word", text_type_text), TextNode("This is text with a ", text_type_text), TextNode("code block", text_type_code), TextNode(" word", text_type_text),]
        self.assertEqual(new_nodes, test_list)
    def test_early_delimiter(self):
        node = TextNode("`code block` in the beginning", text_type_text)
        new_nodes = split_nodes_delimiter([node], "`", text_type_code)
        test_list = [TextNode("code block", text_type_code), TextNode(" in the beginning", text_type_text)]
        self.assertEqual(new_nodes, test_list)
    def test_late_delimiter(self):
        node = TextNode("list if we have a late `code block`", text_type_text)
        new_nodes = split_nodes_delimiter([node], "`", text_type_code)
        self.assertEqual(new_nodes, [TextNode("list if we have a late ", text_type_text), TextNode("code block", text_type_code)])
    def test_no_trailing_delimeter(self):
        node = TextNode("No trailing *delimiter", text_type_text)
        with self.assertRaises(Exception):
            split_nodes_delimiter([node], text_type_italic)
    def test_no_trailing_delimeter2(self):
        node = TextNode("No trailing delimiter*", text_type_text)
        with self.assertRaises(Exception):
            split_nodes_delimiter([node], text_type_italic)
    def test_extract_images(self):
        images = extract_markdown_images("This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)")
        self.assertEqual(images, [('rick roll', 'https://i.imgur.com/aKaOqIh.gif'), ('obi wan', 'https://i.imgur.com/fJRm4Vk.jpeg')])
    def test_extract_images_no_closing_parantheses(self):
        images = extract_markdown_images("This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif")
        self.assertEqual(images, [])
    def test_extract_image(self):
        image = extract_markdown_images("This is text with a ![image](https://i.imgur.com/aKaOqIh.gif)")
        self.assertEqual(image, [('image', 'https://i.imgur.com/aKaOqIh.gif')])
    def test_extract_links(self):
        links = extract_markdown_links("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)")
        self.assertEqual(links, [('to boot dev', 'https://www.boot.dev'), ('to youtube', 'https://www.youtube.com/@bootdotdev')])
    def test_extract_link(self):
        link = extract_markdown_links("This is a link to [wikipedia](https://www.wikipedia.com)")
        self.assertEqual(link, [('wikipedia', 'https://www.wikipedia.com')])

if __name__ == "__main__":
    unittest.main()
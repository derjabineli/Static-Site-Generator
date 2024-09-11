import unittest
from src.markdown_to_html import markdown_to_html_node
from src.htmlnode import HTMLNode

class TestMarkdownUtils(unittest.TestCase):
    def test_markdown_to_html(self):
        markdown = """
        # A big heading at the top

        * List Item 1
        * List Item 2
        * List Item 3

        ```
        print(variable)
        ```
        """
        expected_result = HTMLNode("div", None, [HTMLNode("h1", None, [HTMLNode("", "A big heading at the top")], None), HTMLNode("ul", None, [HTMLNode("li", None, [HTMLNode("", "List Item 1", None, None)]), HTMLNode("li", None, [HTMLNode("", "List Item 2", None, None)]), HTMLNode("li", None, [HTMLNode("", "List Item 3", None, None)])], None), HTMLNode("pre", None, [HTMLNode("code", "print(variable)", None, None)], None)], None)
        actual = markdown_to_html_node(markdown)
        
        self.assertEqual(actual, expected_result)
    
    def test_markdown_to_html2(self):
        markdown = """
        # Why Michael Scott Rules
    
        > Do I need to be liked? Absolutely not. I like to be liked.
        > I enjoy being liked. I have to be liked. But it's not like this compulsive need like my need
        > to be praised.
    
        1. He's funny
        2. Great Character development
        """
        expected_result = HTMLNode("div", None, [HTMLNode("h1", None, [HTMLNode("", "Why Michael Scott Rules")], None), HTMLNode("blockquote", None, [HTMLNode("", "Do I need to be liked? Absolutely not. I like to be liked. I enjoy being liked. I have to be liked. But it's not like this compulsive need like my need to be praised.", None)], None), HTMLNode("ol", None, [HTMLNode("li", None, [HTMLNode("", "He's funny", None, None)], None), HTMLNode("li", None, [HTMLNode("", "Great Character development", None, None)])], None)], None)
        actual = markdown_to_html_node(markdown)
        
        self.assertEqual(actual, expected_result)

    def test_markdown_to_html_broken_quote(self):
        markdown = """
        # Why Michael Scott Rules
    
        > Do I need to be liked? Absolutely not. I like to be liked.
        > I enjoy being liked. I have to be liked. But it's not like this compulsive need like my need
        to be praised.
        """
        expected_result = HTMLNode("div", None, [HTMLNode("h1", None, [HTMLNode("", "Why Michael Scott Rules")], None), HTMLNode("p", None, [HTMLNode("", "> Do I need to be liked? Absolutely not. I like to be liked.\n> I enjoy being liked. I have to be liked. But it's not like this compulsive need like my need\nto be praised.", None, None)], None)], None)
        actual = markdown_to_html_node(markdown)
        
        self.assertEqual(actual, expected_result)

if __name__ == "__main__":
    unittest.main()
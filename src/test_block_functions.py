import unittest

from blocks import markdown_to_blocks, block_to_block_type

class TestHTMLNode(unittest.TestCase):
    # MARKDOWN TO BLOCKS TESTS
    def test_markdown_to_blocks(self):
        markdown_content = """# This is a heading

        This is a paragraph of text. It has some **bold** and *italic* words inside of it

        * This is the first list item in a list block
        * This is a list item
        * This is another list item
        """
        blocks = markdown_to_blocks(markdown_content)
        expected_results = ["# This is a heading", "This is a paragraph of text. It has some **bold** and *italic* words inside of it", "* This is the first list item in a list block\n* This is a list item\n* This is another list item"]
        self.assertEqual(blocks, expected_results)
    
    def test_markdown_to_blocks2(self):
        markdown = """# Heading

        Paragraph line 1
        Paragraph line 2

        * List item 1
        * List item 2
        """
        blocks = markdown_to_blocks(markdown)
        expected_results = [
            "# Heading",
            "Paragraph line 1\nParagraph line 2",
            "* List item 1\n* List item 2"
        ]
        self.assertEqual(blocks, expected_results)
    
    def test_markdown_to_blocks3(self):
        markdown = """
        # Main Heading

        ## Subheading 1

        This is a paragraph with *italic* and **bold** text.
        It continues on a second line.

        * List item 1
        * List item 2
        * List item 3

        ## Subheading 2

        1. Ordered list item 1
        2. Ordered list item 2
        """
        blocks = markdown_to_blocks(markdown)
        expected_results = [ 
            "# Main Heading",
            "## Subheading 1",
            "This is a paragraph with *italic* and **bold** text.\nIt continues on a second line.",
            "* List item 1\n* List item 2\n* List item 3",
            "## Subheading 2",
            "1. Ordered list item 1\n2. Ordered list item 2"
        ]
        self.assertEqual(blocks, expected_results)

    def test_markdown_to_blocks_with_indents(self):
        markdown = """
                    # Main Heading

        ## Subheading 1

        This is a paragraph with *italic* and **bold** text.
        It continues on a second line.

                    * List item 1
        * List item 2
        * List item 3

        ## Subheading 2

        1. Ordered list item 1
        2. Ordered list item 2
        """
        blocks = markdown_to_blocks(markdown)
        expected_results = [ 
            "# Main Heading",
            "## Subheading 1",
            "This is a paragraph with *italic* and **bold** text.\nIt continues on a second line.",
            "* List item 1\n* List item 2\n* List item 3",
            "## Subheading 2",
            "1. Ordered list item 1\n2. Ordered list item 2"
        ]
        self.assertEqual(blocks, expected_results)
    
    def test_markdown_to_blocks_with_indents(self):
        markdown = """
        # Main Heading

        """
        blocks = markdown_to_blocks(markdown)
        expected_results = ["# Main Heading"]
        self.assertEqual(blocks, expected_results)

    # BLOCK TO BLOCK TYPES TESTS
    def test_block_to_blocktype_heading(self):
        markdown = "# Main Heading"
        markdown_type = block_to_block_type(markdown)
        self.assertEqual(markdown_type, "heading")

    def test_block_to_blocktype_heading2(self):
        markdown = "#### Main Heading"
        markdown_type = block_to_block_type(markdown)
        self.assertEqual(markdown_type, "heading")
    
    def test_block_to_blocktype_heading3(self):
        markdown = "###### Main Heading"
        markdown_type = block_to_block_type(markdown)
        self.assertEqual(markdown_type, "heading")
    
    def test_block_to_blocktype_incorrect_heading(self):
        markdown = "####### Main Heading"
        markdown_type = block_to_block_type(markdown)
        self.assertEqual(markdown_type, "paragraph")

    def test_block_to_blocktype_incorrect_heading(self):
        markdown = "#Main Heading"
        markdown_type = block_to_block_type(markdown)
        self.assertEqual(markdown_type, "paragraph")
    
    def test_block_to_blocktype_code(self):
        markdown = "``` Code ```"
        markdown_type = block_to_block_type(markdown)
        self.assertEqual(markdown_type, "code")

    def test_block_to_blocktype_code2(self):
        markdown = "```Code\n more Code```"
        markdown_type = block_to_block_type(markdown)
        self.assertEqual(markdown_type, "code")
    
    def test_block_to_blocktype_code3(self):
        markdown = "```Code\n more Code"
        markdown_type = block_to_block_type(markdown)
        self.assertNotEqual(markdown_type, "code")
    
    def test_block_to_blocktype_quote(self):
        markdown = "> Quote"
        markdown_type = block_to_block_type(markdown)
        self.assertEqual(markdown_type, "quote")

    def test_block_to_blocktype_quote2(self):
        markdown = "> Each line\n> starts with\n> the quote symbol >"
        markdown_type = block_to_block_type(markdown)
        self.assertEqual(markdown_type, "quote")

    def test_block_to_blocktype_unordered(self):
        markdown = "* List item 1\n* List item 2\n* List item 3"
        markdown_type = block_to_block_type(markdown)
        self.assertEqual(markdown_type, "unordered_list")

    def test_block_to_blocktype_unordered2(self):
        markdown = "- List item 1\n- List item 2\n- List item 3"
        markdown_type = block_to_block_type(markdown)
        self.assertEqual(markdown_type, "unordered_list")

    def test_block_to_blocktype_unordered_no_space(self):
        markdown = "-List item 1\n- List item 2\n- List item 3"
        markdown_type = block_to_block_type(markdown)
        self.assertNotEqual(markdown_type, "unordered_list")

    def test_block_to_blocktype_ordered(self):
        markdown = "1. List item 1\n2. List item 2\n3. List item 3"
        markdown_type = block_to_block_type(markdown)
        self.assertEqual(markdown_type, "ordered_list")
    
    def test_block_to_blocktype_ordered_no_space(self):
        markdown = "1.List item 1\n2. List item 2\n3.List item 3"
        markdown_type = block_to_block_type(markdown)
        self.assertNotEqual(markdown_type, "ordered_list")
    
    def test_block_to_blocktype_paragraph(self):
        markdown = "This is a regular jo-schmo paragraph"
        markdown_type = block_to_block_type(markdown)
        self.assertEqual(markdown_type, "paragraph")
    
    def test_block_to_blocktype_paragraph2(self):
        markdown = "This is a regular jo-schmo paragraph\nWith added lines\nAll over the place"
        markdown_type = block_to_block_type(markdown)
        self.assertEqual(markdown_type, "paragraph")

if __name__ == "__main__":
    unittest.main()
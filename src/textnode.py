from htmlnode import LeafNode

class TextNode:
    text_type_text = "text"
    text_type_bold = "bold"
    text_type_italic = "italic"
    text_type_code = "code"
    text_type_link = "link"
    text_type_image = "image"

    def __init__(self, text, text_type, url):
        self.text = text
        self.text_type = text_type
        self.url = url
    
    def __eq__(self, node) -> bool:
        if self.text == node.text and self.text_type == node.text_type and self.url == node.url:
            return True
        return False

    def __repr__(self) -> str:
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
    
    def text_node_to_html_node(self):
         match (self.text_type):
             case self.text_type_text:
                 return LeafNode("", self.text)
             case self.text_type_bold:
                 return LeafNode("b", self.text)
             case self.text_type_italic:
                 return LeafNode("i", self.text)
             case self.text_type_code:
                 return LeafNode("code", self.text)
             case self.text_type_link:
                 return LeafNode("a", self.text, {"href": self.url})
             case self.text_type_image:
                return LeafNode("img", "", {"src": self.url, "alt": self.text})
             case _:
                 raise Exception("Text node is not a valid type")

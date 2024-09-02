class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def __eq__(self, node) -> bool:
        if self.tag == node.tag and self.value == node.value and self.children == node.children and self.props == node.props:
            return True
        return False

    def __repr__(self) -> str:
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

    def to_html(self):
        raise NotImplemented()
    
    def props_to_html(self):
        attributes = ""
        if not self.props:
            return attributes
        for key, value in self.props.items():
            attributes = attributes + f' {key}="{value}"'
        return attributes
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None) -> None:
        super().__init__(tag, value, None, props)
    
    def to_html(self):
        if not self.value and self.tag != "img":
            raise ValueError("LeafNode must have a value")
        
        if not self.tag:
            return self.value
    
        props = self.props_to_html()

        if props != "":
            return f"<{self.tag}{props}>{self.value}</{self.tag}>"
        return f"<{self.tag}>{self.value}</{self.tag}>"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if not self.tag:
            raise ValueError("node must have tag")
        if not self.children:
            raise ValueError("node must have children")
        html = f"<{self.tag}>"

        for node in self.children:
            html += node.to_html()
        
        return html + f"</{self.tag}>"
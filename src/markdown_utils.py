from textnode import TextNode

text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
        else:
            text_string = old_node.text
            sections = text_string.split(delimiter)
            if len(sections) % 2 == 0:
                raise Exception("Invalid markdown syntax")
            for i in range (len(sections)):
                current_section = sections[i]
                if current_section == "":
                    continue
                if i % 2 == 0:
                    node = TextNode(current_section, text_type_text)
                else:
                    node = TextNode(current_section, text_type)
                new_nodes.append(node)
    return new_nodes
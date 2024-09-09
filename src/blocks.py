import re

def markdown_to_blocks(markdown):
    formatted_blocks = []
    blocks = markdown.split("\n")
    temp_block = ""
    for block in blocks:
        stripped_block = block.strip()
        if stripped_block != "":
            temp_block += f"{stripped_block}\n"
            continue
        elif not stripped_block and temp_block != "":
            formatted_blocks.append(temp_block.rstrip('\n'))
            temp_block = ""
        
    return formatted_blocks

def block_to_block_type(markdown):
    if is_heading(markdown):
        return "heading"
    elif markdown.startswith("```") and markdown.endswith("```"):
        return "code"
    elif is_block_quote(markdown):
        return "quote"
    elif is_block_uo_list(markdown):
        return "unordered_list"
    elif is_block_o_list(markdown):
        return "ordered_list"
    else:
        return "paragraph"
    
def is_heading(markdown):
    return re.match(r"^#{1,6} ", markdown) is not None

def is_block_quote(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith(">"):
            continue
        return False
    return True

def is_block_uo_list(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("* ") or line.startswith("- "):
            continue
        return False
    return True

def is_block_o_list(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if re.match(r"\d+\. ", line):
            continue
        return False
    return True
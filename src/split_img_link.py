from extract import extract_markdown_images, extract_markdown_links
from textnode import TextNode, TextType

def split_nodes_image(old_nodes):
    node_list = []

    for old in old_nodes:
        image = extract_markdown_images(old.text)

        if old.text_type != TextType.TEXT:
            node_list.append(old)
            continue
        else:
            if len(image) == 0:
                node_list.append(TextNode(old.text, TextType.TEXT))
            
            else:
                original_text = old.text
                for img in image:
                    image_alt = img[0]
                    image_link = img[1]
                    sections = original_text.split(f"![{image_alt}]({image_link})", 1)
                    node_list.append(TextNode(sections[0], TextType.TEXT))
                    node_list.append(TextNode(image_alt, TextType.IMAGE, image_link))
                    original_text = sections[1]
                if original_text.strip():
                    node_list.append(TextNode(original_text, TextType.TEXT))
    return node_list



def split_nodes_link(old_nodes):
    node_list = []

    for old in old_nodes:
        link = extract_markdown_links(old.text)

        if old.text_type != TextType.TEXT:
            node_list.append(old)
            continue
        else:
            if len(link) == 0:
                node_list.append(TextNode(old.text, TextType.TEXT))
            
            else:
                original_text = old.text
                for lin in link:
                    anchor_text = lin[0]
                    link_url = lin[1]
                    sections = original_text.split(f"[{anchor_text}]({link_url})", 1)
                    node_list.append(TextNode(sections[0], TextType.TEXT))
                    node_list.append(TextNode(anchor_text, TextType.LINK, link_url))
                    original_text = sections[1]
                if original_text.strip():
                    node_list.append(TextNode(original_text, TextType.TEXT))
    return node_list
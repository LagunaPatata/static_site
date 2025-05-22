from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    node_list =[]
    

    for old in old_nodes:
        
        if old.text_type != TextType.TEXT:
            node_list.append(old)

        else:
            text = old.text
            start_position = text.find(delimiter)               
            if start_position == -1:
                node_list.append(old)
                continue

            if start_position > 0:
                first_part = text[:start_position]
                node_list.append(TextNode(first_part, text_type.TEXT))
            end_position = text.find(delimiter,start_position+len(delimiter))
            
            if end_position == -1:
                raise Exception("Invalid Markdown syntax")
            second_part = text[start_position+len(delimiter): end_position]
            node_list.append(TextNode(second_part, text_type))

            if end_position + len(delimiter) < len(text):
                rest = text[end_position+len(delimiter):]
                rest_nodes = split_nodes_delimiter([TextNode(rest,TextType.TEXT)], delimiter, text_type)
                node_list.extend(rest_nodes)

    return node_list
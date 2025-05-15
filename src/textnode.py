from enum import Enum
from htmlnode import LeafNode

class TextType(Enum):
	TEXT="text"
	BOLD="bold"
	ITALIC="italic"
	CODE="code"
	LINK="link"
	IMAGE="image"

class TextNode:
	def __init__(self, text, text_type, url=None):
		self.text=text
		self.text_type=text_type
		self.url=url

	def __eq__(self, other):
		return(self.text==other.text and
			self.text_type==other.text_type and
			self.url == other.url)
	def __repr__(self):
		return f"TextNode({self.text}, {self.text_type.value}, {self.url})"


def text_node_to_html_node(text_node):
	if text_node.text_type == TextType.TEXT:
		node_text = LeafNode(None, text_node.text)
		return node_text
	
	if text_node.text_type == TextType.BOLD:
		node_bold = LeafNode("b", text_node.text)
		return node_bold
	
	if text_node.text_type == TextType.ITALIC:
		node_italic = LeafNode("i", text_node.text)
		return node_italic
	
	if text_node.text_type == TextType.CODE:
		node_code = LeafNode("code", text_node.text)
		return node_code

	if text_node.text_type == TextType.LINK:
		node_link = LeafNode("a", text_node.text, {"href":text_node.url})
		return node_link
	
	if text_node.text_type == TextType.IMAGE:
		node_image = LeafNode("img", "", {"src":text_node.url, "alt":text_node.text})
		return node_image
	
	raise Exception(f"{text_node.text_type} is not a valide type")

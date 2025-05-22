from textnode import TextNode, TextType
from split_img_link import split_nodes_image, split_nodes_link
from delimiter import split_nodes_delimiter
print("hello world")

def main():
	new_textnode = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
	print(new_textnode)


def text_to_textnodes(text):
	link = split_nodes_link(text)
	image = split_nodes_image(link)
	bold = split_nodes_delimiter(image, "**", TextType.BOLD)
	italic = split_nodes_delimiter(bold, "_", TextType.ITALIC)
	code = split_nodes_delimiter(italic, "`", TextType.CODE)
	return code

if __name__ == "__main__":
	main()

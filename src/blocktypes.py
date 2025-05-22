from enum import Enum

class BlockType(Enum):
	PARAGRAPH="paragraph"
	HEADING="heading"
	QUOTE="quote"
	CODE="code"
	UNORDERD_LIST="unordered_list"
	ORDERD_LIST="ordered_list"
	
def block_to_block_type(block_of_markdown):
	bom = block_of_markdown.strip()
	if bom[0] == "#" or bom[0] == "##" or bom[0] == "###" or bom[0] == "####" or bom[0] == "#####" or bom[0] == "######":
		return BlockType.HEADING
	if bom[0:3] == "```" and bom[-3:len(bom)] == "```":
		return BlockType.CODE
	if ">" in block_of_markdown:
		for b in block_of_markdown.split("\n"):
			if b:
				if b[0] != ">":
					return BlockType.PARAGRAPH
		return BlockType.QUOTE
	
	if "-" in block_of_markdown:
		for b in block_of_markdown.split("\n"):
			if b:
				if b[0] != "-":
					return BlockType.PARAGRAPH
		return BlockType.UNORDERD_LIST
	if "1." in block_of_markdown:
		num = 1
		for b in block_of_markdown.split("\n"):
			if b:
				if b[0] != f"{num}" and b[1] != f".":
					return BlockType.PARAGRAPH
				else:
					num +=1
		return BlockType.ORDERD_LIST
	else:
		return BlockType.PARAGRAPH

	
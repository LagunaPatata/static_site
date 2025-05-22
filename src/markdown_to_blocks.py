def markdown_to_blocks(markdown):
    list_of_blocks = []
    for m in markdown.split("\n\n"):
        n = m.strip()
        if n:
            list_of_blocks.append(n)
    return list_of_blocks
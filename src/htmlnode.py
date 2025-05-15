class HTMLNode:
    def __init__(self, tag=None, value= None, children=None, props= None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("to_html method not implemented")

    def props_to_html(self):
        if self.props is None:
            return""
        output=""
        for s in self.props:
            output += f' {s}="{self.props[s]}"'
        return output
    
    def __repr__(self):
        return f"HTMLNode {self.tag}, {self.value}, {self.children}, {self.props}"
    

class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("The tag has no value")
        if self.tag is None:
            return str(self.value)
        else:
            return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>' 

    def __repr__(self):
        return f"HTMLNode {self.tag}, {self.value}, {self.props}"
    


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        if self.tag is None:
            raise ValueError("No tag found")
        if self.children is None:
            raise ValueError("Parent Node is missing Child")
        else:
            output=""
            for c in self.children:
                output += c.to_html()
            
        return f"<{self.tag}>{output}</{self.tag}>"

    
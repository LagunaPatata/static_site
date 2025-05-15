import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode
from textnode import TextNode, TextType, text_node_to_html_node

class TestTextNode(unittest.TestCase):
    def test_tag_value(self):
        node = HTMLNode("a", "Piranha")
        self.assertEqual(node.tag, "a")
        self.assertEqual(node.value, "Piranha")

    def test_props(self):
        node = HTMLNode("a", "Piranha", None, {"class": "greetings", "url": "www.hamburg-knights.de"})

        self.assertEqual(node.children, None)
        self.assertEqual(node.props, {"class":"greetings", "url": "www.hamburg-knights.de"})
        self.assertEqual(node.props_to_html(),' class="greetings" url="www.hamburg-knights.de"') 


    def test_leafnode(self):
        node = LeafNode("p", "This is a test")
        self.assertEqual(node.to_html(), "<p>This is a test</p>")
    
    def test_leafnode_url(self):
        node = LeafNode("a", "Click me!",{"href":"https://google.com"})
        self.assertEqual(node.to_html(),'<a href="https://google.com">Click me!</a>')
    
    def test_leafnode_no_value(self):
        node = LeafNode("a")
        with self.assertRaises(ValueError):
            node.to_html()
    
    def test_leafnode_no_tag(self):
        node = LeafNode(None, "Click me!")
        self.assertEqual(node.to_html(), "Click me!")

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
    
    def test_to_html_with_grandchildren_url(self):
        grandchild_node = LeafNode("b", "Click me!",{"href":"https://google.com"})
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            '<div><span><b href="https://google.com">Click me!</b></span></div>',
        )


    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
        node = TextNode("This is a text node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a text node")
    
    def test_italic(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i") 
        self.assertEqual(html_node.value, "This is a text node")

    def test_code(self):
        node = TextNode("This is a text node", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "This is a text node")

    def test_link(self):
        node = TextNode("This is a link", TextType.LINK, "https://google.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This is a link")
        self.assertEqual(html_node.props["href"],"https://google.com")

    def test_img(self):
        node = TextNode("This is an image", TextType.IMAGE, "https://google.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.props["alt"], "This is an image")
        self.assertEqual(html_node.props["src"],"https://google.com")

if __name__ == "__main__":
    unittest.main()
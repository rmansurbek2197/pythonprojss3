import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom

class XmlParser:
    def __init__(self, filename):
        self.filename = filename
        self.root = None

    def parse(self):
        tree = ET.parse(self.filename)
        self.root = tree.getroot()

    def get_root(self):
        return self.root

    def get_elements(self, tag):
        return self.root.findall('.//' + tag)

    def get_element_text(self, element):
        return element.text

    def get_element_attribute(self, element, attribute):
        return element.get(attribute)

    def print_tree(self):
        print(ET.tostring(self.root, encoding='unicode'))

    def pretty_print(self):
        xmlstr = minidom.parseString(ET.tostring(self.root)).toprettyxml(indent="   ")
        print(xmlstr)

class XmlGenerator:
    def __init__(self, root):
        self.root = root

    def add_element(self, tag, text):
        element = ET.SubElement(self.root, tag)
        element.text = text

    def add_attribute(self, element, attribute, value):
        element.set(attribute, value)

    def generate_xml(self):
        return ET.tostring(self.root, encoding='unicode')

def main():
    parser = XmlParser('example.xml')
    parser.parse()
    root = parser.get_root()
    print(parser.get_element_text(root))
    elements = parser.get_elements('tag')
    for element in elements:
        print(parser.get_element_text(element))
        print(parser.get_element_attribute(element, 'attribute'))
    parser.print_tree()
    parser.pretty_print()

    generator = XmlGenerator(ET.Element('root'))
    generator.add_element('tag', 'text')
    generator.add_attribute(generator.root[0], 'attribute', 'value')
    print(generator.generate_xml())

if __name__ == '__main__':
    main()
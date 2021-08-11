class HtmlElement:
    indent_size = 2

    def __init__(self, name='', text=''):
        self.name = name
        self.text = text
        self.elements = []
    
    def __str(self, indent):
        lines = []

        # opening tag with indentation
        i = ' ' * (indent * self.indent_size) # indentation
        lines.append(f'{i}<{self.name}>')

        # sub text
        if self.text:
            i1 = ' ' * ((indent+1) * self.indent_size)
            lines.append(f'{i1}{self.text}')
        
        # sub elements
        for e in self.elements:
            lines.append(e.__str(indent + 1))
        
        # closing tag
        lines.append(f'{i}</{self.name}>')

        # return final val
        return '\n'.join(lines)
    
    def __str__(self):
        return self.__str(0)

    @staticmethod
    def create(name):
        return HtmlBuilder(name)


'''
The builder class which builds a huge HTML element
step by step
'''
class HtmlBuilder:
    def __init__(self, root_name):
        self.root_name = root_name
        self.__root = HtmlElement(name=root_name)

    def add_child(self, name, text):
        child = HtmlElement(name=name, text=text)
        self.__root.elements.append(child)

    def add_child_fluent(self, name, text=''):
        '''
        Fluent interface: method chaining
        '''
        child = HtmlElement(name=name, text=text)
        self.__root.elements.append(child)
        return self

    def __str__(self):
        return str(self.__root)


if __name__ == "__main__":
    htmlbuilder = HtmlElement.create('body')
    htmlbuilder.add_child('p', 'This is a pragraph')
    htmlbuilder.add_child_fluent(
        'p', 'This is a pragraph2'
    ).add_child_fluent('p')
    print(htmlbuilder)

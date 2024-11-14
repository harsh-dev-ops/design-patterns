from abc import ABC, abstractmethod
import enum


class OutputFormat(enum.Enum):
    MARKDOWN = enum.auto()
    HTML = enum.auto()


class Strategy(ABC):
    @abstractmethod
    def start(self, buffer: list): pass

    @abstractmethod
    def end(self, buffer: list): pass

    @abstractmethod
    def add_list_item(self, buffer: list, item: str): pass


class MarkdownStrategy(Strategy):
    def start(self, buffer: list):
        buffer.append("* \n")

    def end(self, buffer: list):
        buffer.append("* \n")

    def add_list_item(self, buffer: list, item: str):
        buffer.append(f"  **{item}\n")


class HtmlStrategy(Strategy):
    def start(self, buffer: list):
        buffer.append("<ul> \n")

    def end(self, buffer: list):
        buffer.append("</ul> \n")

    def add_list_item(self, buffer: list, item: str):
        buffer.append(f"  <li> {item} </li>\n")


class TextProcessor:
    def __init__(self, strategy=HtmlStrategy()):
        self.strategy = strategy
        self.buffer = []

    def set_output_format(self, output_format: OutputFormat):
        if output_format == OutputFormat.HTML:
            self.strategy = HtmlStrategy()
        elif output_format == OutputFormat.MARKDOWN:
            self.strategy = MarkdownStrategy()

    def append_list(self, items: list[str]):
        self.strategy.start(self.buffer)
        for item in items:
            self.strategy.add_list_item(
                self.buffer, item
            )
        self.strategy.end(self.buffer)

    def clear(self):
        self.buffer = []

    def __str__(self):
        return ''.join(self.buffer)


if __name__ == '__main__':
    tp = TextProcessor()
    tp.set_output_format(output_format=OutputFormat.MARKDOWN)

    items = ['foo', 'bar', 'baz']

    tp.append_list(items)

    print(tp)

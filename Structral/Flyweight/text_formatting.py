class FormattedText:
    def __init__(self, text: str) -> None:
        self.text = text
        self.caps = [False] * len(text)

    def capitalize(self, start, end):
        for i in range(start, end):
            self.caps[i] = True

    def __str__(self):
        result = []
        for i in range(len(self.text)):
            c = self.text[i]
            result.append(c.upper() if self.caps[i] else c)

        return ''.join(result)


class BetterFormattedText:
    def __init__(self, text):
        self.text = text
        self.formatting = []

    class TextRange:
        def __init__(
            self,
            start: int,
            end: int,
            capitalize: bool = False,
            italic: bool = False,
            bold: bool = False
        ):

            self.end = end
            self.start = start
            self.capitalize = capitalize
            self.italic = italic
            self.bold = bold

        def covers(self, position):
            return self.start <= position <= self.end

    def get_range(self, start, end):
        range = self.TextRange(start, end)
        self.formatting.append(range)
        return range

    def __str__(self):
        result = []

        for i in range(len(self.text)):
            ch = self.text[i]
            for r in self.formatting:
                if r.covers(i) and r.capitalize:
                    ch = ch.upper()

            result.append(ch)
        return ''.join(result)


if __name__ == '__main__':
    ft = FormattedText('This is a brave new world')
    ft.capitalize(10, 15)
    print(ft)

    bft = BetterFormattedText('This is a brave new world')
    text_range = bft.get_range(16, 19)
    text_range.capitalize = True
    print(bft)

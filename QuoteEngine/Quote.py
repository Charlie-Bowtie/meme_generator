"""Simple class to represent quotes."""

class Quote():
    """A quote.

    A quote consists of the body of text and the author of the quote

    """

    def __init__(self, body, author):
        """Create a new Quote object.

        :param body: Text of the quote
        :param author: Author of the body
        """
        self.body = body
        self.author = author

    def __repr__(self):
        """Return a 'str(self)'."""
        return f'{self.body}-{self.author}'

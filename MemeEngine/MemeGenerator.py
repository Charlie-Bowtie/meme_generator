"""Save generated memes to a directory."""

from PIL import Image, ImageDraw, ImageFont
from random import randint
from textwrap import fill


class MemeEngine():
    """Meme generating class."""

    def __init__(self, output_dir):
        """Create a MemeEngine class object.

        :param output_dir: Path to directory for saving generated memes.

        """
        self.output = output_dir

    def __str__(self) -> str:
        """Return a 'str(self)'."""
        return f"{self.output}"

    def make_meme(self, img_path, text, author, width=500) -> str:
        """Create a new meme.

        Intakes a path to a image, and strings of text for the quote body
        and quote author. The image is resized to a width of 500px while
        maintaing the orginal aspect ratio. The quote and author are then
        added to a random place on the image and the new meme is
        saved to the output_dir of the MemeEngine instance.

        :param img_path: Path to image file.
        :param text: String of text for body of quote.
        :param author: Author of the quote
        :param width: Set at 500px.
        """
        img = Image.open(img_path)
        quote = f"{str(text)}\n-{str(author)}"

        ratio = float(img.size[1])/float(img.size[0])
        height = int(ratio*float(width))
        img = img.resize((width, height), Image.NEAREST)

        fnt_size = int((width * .05))
        fnt = ImageFont.truetype("./MemeEngine/NerkoOne-Regular.ttf", fnt_size)
        d = ImageDraw.Draw(img)
        pos_x = randint(0, int(width*.20))
        pos_y = randint(0, int(height*.75))

        if len(quote) > 30:
            quote = fill(quote, width=30)

        d.multiline_text((pos_x, pos_y), quote, font=fnt, fill='white')

        out_path = f"{self.output}/meme_{str(randint(0,100000))}.jpg"
        img.save(out_path)

        return out_path

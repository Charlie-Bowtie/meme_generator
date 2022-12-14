"""A web based version of the MemeGenerator package.

This Flask based server allows user to generate a randome meme from a directory
of default images/quotes or create a custom meme.
"""

import random
import os
import requests
from flask import Flask, render_template, abort, request
from QuoteEngine import Ingestor
from MemeEngine import MemeEngine

app = Flask(__name__)

meme = MemeEngine('./static')


def setup():
    """Load all resources."""
    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']

    quotes = []
    for file in quote_files:
        quote_list = Ingestor.parse(file)
        for quote in quote_list:
            quotes.append(quote)

    images_path = "./_data/photos/dog/"
    imgs = None
    for root, dirs, files in os.walk(images_path):
        imgs = [os.path.join(root, name) for name in files]

    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """Generate a random meme."""
    img = random.choice(imgs)
    quote = random.choice(quotes)
    path = meme.make_meme(img, quote.body, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """User input for meme information."""
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """Create a user defined meme."""
    image_url = request.form['image_url']
    body = request.form['body']
    author = request.form['author']

    try:
        r = requests.get(image_url)
    except requests.exceptions.ConnectionError:
        print("Please input a valid URL.")
        return render_template('meme_error.html')

    tmp = f'./tmp{random.randint(0, 1000)}.jpg'
    with open(tmp, 'wb') as img:
        img.write(r.content)

    path = meme.make_meme(tmp, body, author)
    os.remove(tmp)

    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()

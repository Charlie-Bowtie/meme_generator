# **meme_generator**
meme_generator is capable of randomly producing memes from an included directory of images/quotes,and it can also create custome memes. The meme_generator package includes a locally ran meme generator and a Flask based web version of the meme_generator.

## **Setup**
Install Required Libraries:

    $ pip install -r requirements.txt

To run the local meme_generator:

    $ python meme.py

Meme.py takes three optional arguments:

    $ python meme.py --path --body --author
    $ python meme.py --path ./_data/photos/custom/BDAY.jpg --body "GOOD TIMES" --author "Charlie Barlie"

The memes will be saved to the ./tmp directory.

To run the web meme_generator server:

    $ python app.py

The memes will be saved to the ./static directory.


## **Module Structure**

The meme_generator depends on two main sub_modules.

### 1. QuoteEngine
This package parses text from a variety of file formats and
returns a list of Quote class objects. 

There are separate Ingestor classes for each type of file format. They all inherit from the
IngestorInterface abstract class. Ingestor.py then imports all the Ingestor classes 
and automatically selects the correct Ingestor for the file type inputed. 

#### Example:
    Ingestor.parse(file_path) -> List[Quote Objects]

### 2. MemeEngine
This package includes the MemeEngine class that takes an output directory(outpit_dir) for generated memes. The MemeEngine class has a 
make_meme method that takes in a path to a image, a body of text and a author. This outputs an image to the MemeEngine instance output_dir and returns the path to the new meme.

#### Example:
    meme = MemeEngine('file_path')
    meme.make_meme(img, quote.body, quote.author) -> 'file_path'

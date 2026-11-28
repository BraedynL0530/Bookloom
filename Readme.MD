# BookLoom 
**A digital library**
+tv

# where books are stored

"/Bookloom/Books/{book.title}" (then can do "book-title/chapter1.cbz")

# where covers are stored

"libary/covers"

## both should go in app data along with database and possibly assets/config/saves
but im unsure as of now whast going to construct %LocalAPPDATA%/Bookloom 
* used extends user to fix the cross platform issue



# TODO: 
* ~~finish cbz importer~~
* ~~work on gui~~ (Wip) NOTE: gotta do layout!!!!!!!!
* begin epub importer
* finsh web importer
* work on browser interface(with pre set ways to view)
* more gui work
* chibi design
* TV functionality
* lan(interchangeable with 2 avoce)
* Steal a repos i saw TTS/narration (+highlight line) feature :3c 



#webviewer feature:
use playwrigt or beutifal soup

what it needs:
* a way to check for every chapter
* a way to tell what images are actual content and not ads
* for cbz(intended use for browser but may add epub in future) have a view preset urls that it supports
* then use a second request while user is loading first chapter to see if a next chapter exist(determines if button is useable)
* redis? to have a llike cache of previous chapters in web.
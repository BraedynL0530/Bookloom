import uuid


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.tags = []
        self.description = "not found"
        self.source = "file" #Qdefualt
        self.id = str(uuid.uuid4())
        self.chapters = None #int
        self.chapter_name = ""
        self.current_chapter = None
        self.last_viewed = None
        self.cover_img_path = None

    def add_tag(self, tag):
        self.tags.append(tag)

    def remove_tag(self, tag):
        self.tags.remove(tag)

    def update_chapter(self, chapter):
        self.current_chapter = chapter

    def update_chapters(self, chapters): #update on network finding new/newly uploaded files?
        self.chapters = chapters

    def update_last_viewed(self, last_viewed): # basically only going to me time.now
        self.last_viewed = last_viewed

    def add_book(self, title, source, author="N/A", tags="", description="",  cover_img_path="N/A"): #source and title are not optional, the rest are
        self.title = title
        self.author = author
        self.id = str(uuid.uuid4())
        self.tags = tags
        self.description = description
        self.source = source
        self.cover_img_path = cover_img_path
        self.current_chapter
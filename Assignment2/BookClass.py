class Book:
    def __init__(self,title,author):
        self.title=title
        self.author=author
        self.reviews =[]
    
    def add_reviwes(self,review):
        self.reviews.append(review)  #append()is used to insert each new review into the reviews list so they can be counted and displayed later.
    
    def count_reviews(self):
        return len(self.reviews)

    def display_reviews(self):
        for r in self.reviews:
            print(r)

b=Book("Python","Guido")
b.add_reviwes("Nice Book")
b.add_reviwes("Very Helpful")
b.add_reviwes("This book used for beginners")
b.display_reviews()
print("Total Reviews:", b.count_reviews())
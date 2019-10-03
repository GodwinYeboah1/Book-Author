from django.db import models

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __repr__(self):
        return "<User object:  name:{} | desc {} ".format(self.name, self.desc)

class Author(models.Model):
    first_name = models.CharField(max_length=255)
    book = models.ForeignKey(Book, related_name="authors", on_delete=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __repr__(self):
        return "<User object:  name:{} | book: {} ".format(self.first_name,self.book)
from django.db import models
from django.contrib.auth.models import User



class AuthorModel(models.Model):
    first_name=models.CharField(max_length=100, verbose_name='First Name')
    last_name=models.CharField(max_length=100, verbose_name='Last Name')
    # books = models.ManyToManyField('BookModel', related_name='authors')



    class Meta:
        verbose_name='Author'
        verbose_name_plural='Authors'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    


class BookModel(models.Model):
    title=models.CharField(max_length=100, verbose_name='Book Title')
    pageCount=models.IntegerField(verbose_name='Page Count')
    longDescription=models.TextField(verbose_name='Long Description', null=True, blank=True)
    shortDescription = models.CharField(max_length=255,verbose_name='Short Decription')
    releasedAt = models.DateField(auto_now_add=True, verbose_name='Released At')
    authors = models.ManyToManyField(AuthorModel, related_name='books')
    bookImage=models.ImageField(upload_to='bookImages', verbose_name='Book Image',null=True,blank=True)
    orImageUrl=models.URLField(verbose_name='Or Image URL',null=True,blank=True)


    class Meta:
        verbose_name='Book'
        verbose_name_plural='Books'

    def __str__(self):
        return f"{self.title}"
    
class ReviewsModel(models.Model):
    book = models.ForeignKey(BookModel, on_delete=models.CASCADE, related_name='reviews')
    reviewer=models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    reviewContent = models.TextField(verbose_name='Review Text')
    rating = models.IntegerField(verbose_name='Rating',null=True,default=1)
    createdAt = models.DateTimeField(auto_now_add=True, verbose_name='Review Created At')


    class Meta:
        verbose_name='Review'
        verbose_name_plural='Reviews'

    def __str__(self):
        return f"{self.book.title} - {self.rating}"


# auto_now_add:
# When auto_now_add=True is set, the date/time field is automatically set to the current date/time only when the object is first created.
# This option is useful for tracking the creation time of an object


# auto_now:
# When auto_now=True is set, the date/time field is automatically updated to the current date/time whenever the model instance is saved.
# This option is useful for tracking the last modification time of an object.

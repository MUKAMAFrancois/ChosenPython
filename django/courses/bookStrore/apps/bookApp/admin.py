from django.contrib import admin
from .models import AuthorModel,BookModel,ReviewsModel

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = ['title','pageCount','releasedAt']
    search_fields = ['title','authors__first_name','authors__last_name']
    list_filter = ['releasedAt','authors__first_name','authors__last_name']


admin.site.register(BookModel,BookAdmin)



class AuthorAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name']
    search_fields = ['first_name','last_name']


admin.site.register(AuthorModel,AuthorAdmin)


class ReviewsAdmin(admin.ModelAdmin):
    list_display = ['book','reviewer','rating']
    search_fields = ['book__title','reviewer__username']
    list_filter = ['rating']


admin.site.register(ReviewsModel,ReviewsAdmin)

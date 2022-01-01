from django.contrib import admin
from django.db.models import fields
from .models import *

# Register your models here.
#admin.site.register(Book)
#admin.site.register(BookInstance)
#admin.site.register(Author)
admin.site.register(Language)
admin.site.register(Genre)

#BOOK INSTANCE
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = (
        'display_book',
        'status',
        'due_back',
        'id',
    )

    list_filter = ('status', 'due_back')

    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        })
    )

#BOOK
class BookInstanceInline(admin.TabularInline):
    model, extra = BookInstance, 0


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BookInstanceInline]

#AUTHOR
class BookInLine(admin.TabularInline): #StackedInline
    model, extra = Book, 0

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]

    inlines = [BookInLine]





admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(BookInstance, BookInstanceAdmin)
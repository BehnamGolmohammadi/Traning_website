from django.contrib import admin
from blog.models import Post, Category
# Register your models here.

@admin.register(Post)
class Post_Admin_Customization(admin.ModelAdmin):
    date_hierarchy= "Created_Date"
    empty_value_display= 'No Information'
    fieldsets = (
        ('Main options', {
            'fields': ("Author", "Image", "Title", "Content")
        }),
        ('Advanced options', {
            'classes': ('wide', 'collapse', 'extrapretty'),
            'fields': ("Category","Status", "Counted_view", "Published_Date", ),
        }),
    )
    list_display= ("Title", "Author" ,"Status", "Counted_view", "Published_Date")
    list_filter= ("Status", "Author", "Published_Date")
    search_fields= ["Title", "Author", "Content"]

admin.site.register(Category)
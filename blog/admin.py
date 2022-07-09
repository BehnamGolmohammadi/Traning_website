from django.contrib import admin
from blog.models import Post
# Register your models here.

@admin.register(Post)
class Post_Admin_Customization(admin.ModelAdmin):
    date_hierarchy= "Created_Date"
    empty_value_display= 'No Information'
    fieldsets = (
        ('Main options', {
            'fields': ("Title", "Content")
        }),
        ('Advanced options', {
            'classes': ('wide', 'collapse', 'extrapretty'),
            'fields': ("Status", "Counted_view", "Published_Date", ),
        }),
    )
    list_display= ("Title", "Content" ,"Status", "Counted_view", "Published_Date")
    list_filter= ("Status", "Published_Date")
    search_fields= ["Title", "Content"]
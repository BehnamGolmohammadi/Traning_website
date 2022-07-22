from django.contrib import admin
from website.models import Contact, Newsletter
# Register your models here.

@admin.register(Contact)
class Contact_Admin_Customization(admin.ModelAdmin):
    date_hierarchy= "Created_Date"
    empty_value_display= 'No Information'
    fieldsets = (
        ('Main options', {
            'fields': (("Name", "Email") ,("Subject", "Message"))
        }),
        )
    list_display= ("Name", "Email" ,"Subject")
    list_filter= ("Subject", "Created_Date")
    search_fields= ["Name", "Email" ,"Subject", "Message"]


admin.site.register(Newsletter)
from django.contrib import admin
from . models import Enquiry,StudentInfo,LoginInfo
# Register your models here.
@admin.register(Enquiry)
class EnquiryAdmin(admin.ModelAdmin):

    list_display = [
        'name',
        'gender',
        'contactno',
        'emailaddress',
        'posteddate'
    ]

    list_filter = [
        'gender',
        'posteddate'
    ]

    search_fields = [
        'name',
        'contactno',
        'emailaddress'
    ]

admin.site.register(StudentInfo)
admin.site.register(LoginInfo)





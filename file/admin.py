from django.contrib import admin
from file.models import Document, File


# Register your models here.

admin.site.register(File)
admin.site.register(Document)

class DocumentAdmin(admin.ModelAdmin):
    list_display = ['name','publishing_date']
    list_display_links = ['name','publishing_date']
    list_filter = ['publishing_date']
    search_fields = ['name','description']

    class Meta:
       model = Document 
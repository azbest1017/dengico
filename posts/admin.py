from django.contrib import admin

from .models import Post, Affiliate_Partner, Reviews, Methot_Withdraw

admin.site.register(Post)
admin.site.register(Affiliate_Partner)
admin.site.register(Reviews)
admin.site.register(Methot_Withdrasdaw)

from ckeditor.widgets import CKEditorWidget

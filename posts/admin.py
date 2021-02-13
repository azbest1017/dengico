from django.contrib import admin

from .models import Post, Affiliate_Partner, Category, Methot_Withdraw

admin.site.register(Post)
admin.site.register(Affiliate_Partner)
admin.site.register(Category)
admin.site.register(Methot_Withdraw)

from ckeditor.widgets import CKEditorWidget

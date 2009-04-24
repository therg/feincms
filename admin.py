from django.contrib import admin

from medialibrary import models


class MediaFileTranslationInline(admin.TabularInline):
    model = models.MediaFileTranslation


admin.site.register(models.Category)
admin.site.register(models.MediaFile,
    date_hierarchy='created',
    inlines=[MediaFileTranslationInline],
    list_display=('__unicode__', 'file', 'created'),
    list_filter=('categories',),
    )


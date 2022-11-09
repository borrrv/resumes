from django.contrib import admin

from .models import Post, Group


class PostAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'group',
                    'city', 'birth_day', 'sex', 'nationality',
                    'experience', 'carrer_objective', 'education',
                    'language', 'employment', 'about_me')
    list_editable = ('group',)
    search_fields = ('name',)
    list_filter = ('pub_date',)
    empty_value_display = '-пусто-'


class GroupAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title')
    list_filter = ('title',)
    search_fields = ('title',)


admin.site.register(Post, PostAdmin)
admin.site.register(Group, GroupAdmin)
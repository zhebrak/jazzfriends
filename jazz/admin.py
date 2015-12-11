# coding: utf-8

from django.contrib import admin

from jazz.models import Concert, Attachment, Feedback, Video


class ConcertAdmin(admin.ModelAdmin):
    list_display = ['title', 'show_time']


class AttachmentAdmin(admin.ModelAdmin):
    list_display = ['group', 'name', 'file_type']
    list_filter = ['file_type', 'group']


class VideoAdmin(admin.ModelAdmin):
    list_display = ['title', 'location', 'embed_link', 'show_date']


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['name', 'contact', 'created_at']


admin.site.register(Concert, ConcertAdmin)
admin.site.register(Attachment, AttachmentAdmin)
admin.site.register(Feedback, FeedbackAdmin)
admin.site.register(Video, VideoAdmin)

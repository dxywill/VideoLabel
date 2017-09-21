from django.contrib import admin

# Register your models here.

from .models import Participant, Video, Annotator, Labels

admin.site.register(Participant)
admin.site.register(Video)
admin.site.register(Annotator)
admin.site.register(Labels)

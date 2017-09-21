from django.shortcuts import render
from django.http import HttpResponse
from .models import Participant, Video, Annotator, Labels
from django.contrib.sessions.models import Session


def index(request):
    if request.method == 'POST':
        engage_level = int(request.POST.get('engageOptions'))
        video_id = int(request.POST.get('video_id'))

        # create label
        annotator = Annotator.objects.latest('id')
        current_video = Video.objects.get(pk=video_id)
        new_label = Labels(video_id=current_video, annotator=annotator, engage_level=engage_level)
        new_label.save()

        next_video_id = video_id + 1
        if next_video_id <= Video.objects.latest('id').id:
            next_video = Video.objects.get(pk=next_video_id)
            return render(request, 'engage/index.html', {'video_name': next_video.video_name, 'video_id': next_video.id})
        else:
           return HttpResponse("<h1>Finally done! Go Play</h1>")
    else:
        if Labels.objects.all().count() == 0:
            next_video_id = 1
        else:
            latest_label = Labels.objects.latest('id')
            next_video_id = latest_label.video_id.id + 1
        video_to_display = Video.objects.get(pk=next_video_id).video_name

        return render(request, 'engage/index.html', {'video_name': video_to_display, 'video_id': next_video_id})
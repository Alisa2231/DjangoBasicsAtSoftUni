from django.http import HttpResponse
from django.shortcuts import render

from notes.models import Note


def notes_view(request):
    # output = ['My notes:']
    # all_notes = Note.objects.all()
    #
    # for note in all_notes:
    #     output.append('<li>' + note.title + '</li>')

    # return HttpResponse('\n'.join(output))


    all_notes = Note.objects.all()
    context = {'notes': all_notes}

    return render(request, 'notes/index.html', context)

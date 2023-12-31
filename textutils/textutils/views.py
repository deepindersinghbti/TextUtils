from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def analyze(request):
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    if removepunc == 'on':
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed += char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed
    if fullcaps == 'on':
        analyzed = ""
        for char in djtext:
            analyzed += char.upper()
            # if char == '\n':
            #     analyzed += '\n'
        params = {'purpose': 'Change entire text to uppercase', 'analyzed_text': analyzed}
        djtext = analyzed

    if newlineremover == 'on':
        analyzed = ""
        for char in djtext:
            if char != '\n' and char != '\r':
                analyzed += char
        params = {'purpose': 'Remove new lines from text', 'analyzed_text': analyzed}
        djtext = analyzed

    if extraspaceremover == 'on':
        analyzed = ""
        for index, char in enumerate(djtext):
            if djtext[index] == ' ' and djtext[index + 1] == ' ':
                pass
            else:
                analyzed += char
        params = {'purpose': 'Remove extra spaces from text', 'analyzed_text': analyzed}
        djtext = analyzed

    if removepunc!='on' and fullcaps!='on' and newlineremover!='on' and extraspaceremover!='on':
        return HttpResponse("Error! Please select at least one function.")
    return render(request, 'analyze.html', params)

    # else:
    #     return HttpResponse("Error!")

# def capfirst(request):
#     return HttpResponse("Capitalizes first char")

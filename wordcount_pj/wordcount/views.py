from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def count(request):
    return render(request, 'count.html')

def result(request):
    text = request.GET['fulltext']
    words = text.split() 
    words_count = {}
    length = len(words)
    for word in words:
        if word in words_count:
            words_count[word] = words_count[word] + 1
        else:
            words_count[word] = 1
    return render(request, 'result.html',{'full':text, 'words':words, 'words_count':words_count.items(), 'length':length})

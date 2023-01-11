from django.shortcuts import render

# Create your views here.

#boostap and django
#https://ngangasn.com/how-to-use-bootstrap-5-with-django-the-right-way/

from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .forms import InsertYoutubeLink

from .process_url import video_id, transcriptYoutube
    
def index(request):
    # if this is a POST request we need to process the form data
    
    if request.method == 'POST':
        text1=''
        # create a form instance and populate it with data from the request:
        form = InsertYoutubeLink(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
     
            login_data = request.POST.dict()
            youtube_URL = login_data.get("youtube_URL")
           # y='https://www.youtube.com/watch?v=l9updbL58xY'

            result=video_id(youtube_URL)
            #print(result)
            if (result==''):
                test1='the input is wrong'
            else:
                text1=transcriptYoutube(result)
            #print(text1)

            #return HttpResponseRedirect('')

    # if a GET (or any other method) we'll create a blank form
    else:
        text1=''
        form = InsertYoutubeLink()

    return render(request, 'index.html', {'form': form , 'text1':text1})



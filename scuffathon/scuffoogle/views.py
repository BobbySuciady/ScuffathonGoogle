from django.shortcuts import render
from .forms import SearchForm
import requests
import openai


def search_view(request):
    if request.method == 'POST':
        query = request.POST.get('query')
        newquery = "insult someone who does not know" + query
        if query:
            # Send user input to the ChatGPT API
            openai.api_key = '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'
            response = openai.Completion.create(
                engine='text-davinci-003',
                prompt=newquery,
                max_tokens=1024,
                n=1,
                stop=None,
                temperature=0.7,
            )
            chat_response = response.choices[0].text
        else:
            chat_response = None
    else:
        chat_response = None

    return render(request, 'search.html', {'chat_response': chat_response})




# Create your views here.

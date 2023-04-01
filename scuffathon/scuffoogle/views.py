from django.shortcuts import render
import openai


def search_view(request):
    if request.method == 'POST':
        query = request.POST.get('query')
        newquery = "harsh insults for someone who does not know" + query + " and write a 100 word essay on why someone who does not know" + query + " is dumb"
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
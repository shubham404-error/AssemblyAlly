from django.shortcuts import render

from util import generator, gemini
import PIL.Image

# from chatbot.models import ImageModel


# def your_view(request):
#     response_images = ImageModel.objects.all()  # Retrieve all images
#     context = {'response_images': response_images}
#     return render(request, 'index.html', context)

def report(request):
    chain, docsearch = generator.ready()

    if request.method == 'POST':
        response_text, response_images = process_input(chain, docsearch, "Generate a complete report of the document, give step by step pointers for each topic with what tools are important and what cautions to take")
        context = {'response_text': response_text, 'response_images':response_images}
    else:
        response_text = ''  # Empty initial response

        context = {'response_text': response_text}
    return render(request, 'index.html', context)


def process_image(request):
    chain, docsearch = generator.ready()
    if request.method == 'POST':
        # Handle image input
        uploaded_image = request.FILES['image']
        img = PIL.Image.open(uploaded_image)
        desc = gemini.give_desc(img)
        response_text, response_images = process_input(chain, docsearch, desc)

        context = {'response_text': response_text, 'response_images':response_images}
    else:
        response_text = ''  # Empty initial response

        context = {'response_text': response_text}
    return render(request, 'index.html', context)


def process_text(request):
    chain, docsearch = generator.ready()

    if request.method == 'POST':
        # Handle text input
        user_text = request.POST.get('text')
        response_text, response_images = process_input(chain, docsearch, user_text)
        context = {'response_text': response_text, 'response_images':response_images}
    else:
        response_text = ''  # Empty initial response

        context = {'response_text': response_text}
    return render(request, 'index.html', context)


def process_input(chain, docsearch, query):
    # Implement your text processing logic here
    return generator.give_output(chain, docsearch, query)


def index(request):
    # Render your desired content for the root page
    return render(request, 'index.html')  # Assuming an index.html template

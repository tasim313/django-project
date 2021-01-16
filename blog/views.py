from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("<h1>..........This is a blog project..........</h1>"
                        "<h2>Hello Everyone welcome to Django project </h2>"
                        "<p>Other collaborative online encyclopedias were attempted before Wikipedia, but none were as successful.[13] Wikipedia began as a complementary project for Nupedia, a free online English-language encyclopedia project whose articles were written by experts and reviewed under a formal process</p>")


def about(requuest):
    return HttpResponse("<h3>Wikipedia is an online free-content encyclopedia project"
                        " helping to create a world in which everyone can freely "
                        "share in the sum of all knowledge. "
                        "It is supported by the Wikimedia Foundation and based on a model "
                        "of freely editable content. The name Wikipedia is a blending of the words wiki"
                        " (a technology for creating collaborative websites, "
                        "from the Hawaiian word wiki, meaning quick ) and encyclopedia. Wikipedia's articles "
                        "provide links designed to guide the user to related pages with additional information.</h3>")

def contact(request):
    return HttpResponse("<h6>This page is not ready ! Try to visit later</h6>")
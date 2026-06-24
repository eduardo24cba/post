from django.shortcuts import render

def post_list(request):
    return render(request, "entradas_blog/post_list.html", {})
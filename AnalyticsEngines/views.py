from django.shortcuts import render

# Create your views here.

#def frontpage_index(request):
#    return render(request, 'frontpage/index.html',{})

#def post_list(request):
#    return render(request, 'blog/post_list.html',{})

def post_list(request):
    return render(request, 'blog/post_list.html',{})

from django.http.response import JsonResponse
from django.shortcuts import render
from .models import M, Messages
# Create your views here.
def link(n):
    a = ''
    import random as r
    char = ['q', 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'l', 'k', 'j', 'h', 'g', 'f', 'd', 's', 'a', 'z', 'x', 'c', 'v', 'b', 'n', 'm', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'L', 'K', 'J', 'H', 'G', 'F', 'D', 'S', 'A', 'Z', 'X', 'C', 'V', 'B', 'N', 'M']
    for _ in range(0, n):
        b = r.randint(0, len(char) - 1)
        a += char[b]
    return a



def Index(request):   
    context = {}
    if 'message' in request.session:
        m = request.session['message']
        context['m'] = m

    return render(request, 'message/index.html', context)
    pass

def clear(request):
    if 'message' in request.session:
        m = request.session['message']
        id = m['id']
        Messages.objects.get(id = id).delete()
        del request.session['message']
    return JsonResponse(
        {
            'status': 200
        }
    )
def create(request):
    link1 = link(50)
    link2 = link(50)
    m = Messages.objects.create(
        link1 = link1,
        link2 = link2
    )
    request.session['message'] = {
            'link1' : f'sn/{link1}',
            'link2' : f'vr/{link2}',
            'id': m.id
        }
    return JsonResponse(
        {
            'link1' : f'sn/{link1}',
            'link2' : f'vr/{link2}'
        }
    )

def sendMessage(request, link):
    context = {}
    if request.method == 'POST':
        if Messages.objects.filter(link1 = link).exists():
            me = Messages.objects.get(link1 = link)
            s = request.POST['m']
            m = M.objects.create(message = s)
            me.messages.add(m)
            me.save()
    if Messages.objects.filter(link1 = link).exists():
        context['status'] = True
    return render(request, 'message/send.html', context)
    pass
def view(request, link):
    context = {}
    if Messages.objects.filter(link2 = link).exists():
        m = Messages.objects.get(link2 = link)
        context['messages'] = m.messages.all().order_by('-timestamp')
        context['status'] = True
    return render(request, 'message/view.html', context)
    pass


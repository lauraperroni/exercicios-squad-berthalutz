from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Post
from blog.forms import ComentarioForm
# from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import redirect


# View da página inicial 
def index_html(request):
    posts = Post.objects.all() #o valor de posts é uma lista de objetos
    return render(request, 'post_preview.html', {'posts1': posts}) #você pega o valor da chave no HTML 


def resenha_do_livro(request):
    sucesso = False
    posts = Post.objects.get(pk=2) #aqui tbm é uma lista de objetos, que traz só 1 item
    print("request", request)
    form = ComentarioForm()
    # print({'posts': posts})
    print("sucesso", sucesso)
    context = {
        'posts': posts,
        'form': form,
        "sucesso": sucesso
    }
    print(context)
    return render(request, 'post1.html', context)

# @api_view(['POST'])
def fazer_comentario(request):
    if request.method =='POST':
        form = ComentarioForm(request.POST)
        print("form", form)
        if form.is_valid():
            form.save()
            sucesso = True
            print("posts", posts)

            dados = {
                'form': form,
                'posts': posts,
                "sucesso": sucesso
            }
            # return render(request, 'post1.html', {'dados': dados })
            # return redirect("/crepusculo", {'dados': dados })
            sucesso = True
            return redirect("/crepusculo")
        print(form.is_valid())
    else: 
        form = ComentarioForm()
    return render(request, 'post1.html', {'form': form})


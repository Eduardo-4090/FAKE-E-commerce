from django.shortcuts import render ,  redirect ,get_object_or_404
from .models import Produtos , Category , Cart , CartItem
from django.contrib.auth.decorators import login_required
from django.contrib import messages



def home (request):
    categorias = Category.objects.all()
    produtos = Produtos.objects.all()

    contexto = {
        'produtos':produtos,
        'categorias':categorias
    }
    return render(request,'home.html', contexto )

def filtro (request , slug_categoria):
    categoria_objeto = get_object_or_404(Category , slug = slug_categoria)
    produtos_filtro = Produtos.objects.filter(category = categoria_objeto)

    categorias = Category.objects.all()
    contexto = {
        'produtos':produtos_filtro,
        'categorias': categorias
    }
    return render(request , 'home.html', contexto)

def detalhe_produto(request , produto_slug):
    slug_url = get_object_or_404(Produtos, slug=produto_slug)
    return render(request,'produto.html',{'slug_url':slug_url})

@login_required
def add_carrinho(request):
    if request.method == 'POST':
        produto_id = request.POST.get('produto_id')
        produto_slug = request.POST.get('produto_slug')
        
        try:
            quantidade = int(request.POST.get('quantidade', 1))
        except ValueError:
            messages.error(request, 'Erro: A quantidade informada é inválida.')
            return redirect('detalhe_produto', produto_slug=produto_slug)
        
        if quantidade <= 0:
            messages.error(request, 'Erro: A quantidade deve ser um número positivo.')
            return redirect('detalhe_produto', produto_slug=produto_slug)

        produto = get_object_or_404(Produtos, id=produto_id)

        cart, created = Cart.objects.get_or_create(user=request.user)
        
        cart_item_exists = CartItem.objects.filter(cart=cart, produtos=produto)

        if cart_item_exists.exists():
            cart_item = cart_item_exists.first()
            cart_item.quantidade += quantidade
            cart_item.save()
        else:
            CartItem.objects.create(
                cart=cart,
                produtos=produto,
                quantidade=quantidade
            )
        return redirect('detalhe_produto', produto_slug=produto_slug)
    else:
        messages.error(request, 'Método de requisição inválido.')
        return redirect('home')
@login_required
def excluir_item(request, item):
    if request.method == 'POST':
        item_obejto = get_object_or_404(CartItem , produtos = item , cart__user=request.user)
        
        if item_obejto.quantidade > 1:
            item_obejto.quantidade -=1
            item_obejto.save()
            messages.success(request , 'Item Excluido com succeso')
            return redirect('carrinho')
        else:
            item_obejto.delete()
            return redirect('carrinho')

    else:
        messages.error(request , 'Erro , tente novamente')
        return redirect('carrinho')
     

@login_required 
def carrinho(request):

    cart , existe = Cart.objects.get_or_create(user=request.user)
    cart_items = CartItem.objects.filter(cart=cart).select_related('produtos')

    contexto={
        'cart_items':cart_items
    }

    return render(request,'carrinho.html',contexto)
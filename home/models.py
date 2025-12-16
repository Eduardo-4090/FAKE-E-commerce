from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    nome = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.nome

class Produtos(models.Model):
    category = models.ForeignKey( Category , on_delete=models.CASCADE)
    nome = models.CharField(max_length=200)
    descrition = models.TextField(blank=True)
    valor = models.DecimalField(max_digits=10 , decimal_places=2)
    capa = models.ImageField(upload_to='produto/capa/')
    slug = models.SlugField( unique=True)

    def __str__(self):
        return self.nome

class Galeria(models.Model):
    produto = models.ForeignKey(Produtos, on_delete=models.CASCADE)
    imagem_opcional = models.ImageField(upload_to='produto/galeria/')

    def __str__(self):
        return self.produto.nome

class Cart(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)

    def __str__(self):
        return f"Carrinho de {self.user.username}"
    
class CartItem(models.Model):
    cart = models.ForeignKey(Cart , on_delete= models.CASCADE)
    produtos = models.ForeignKey(Produtos , on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField(default=1)

    def subtotal(self):
        return self.quantidade * self.produtos.valor
    
    def __str__(self):
        return f"{self.quantidade}x de {self.produtos.nome} no carrinho {self.cart.id}"
    



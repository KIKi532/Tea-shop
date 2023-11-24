from .cart import Cart


def cart(request):
    """Процесор контекста кошика"""
    return {'cart': Cart(request)}

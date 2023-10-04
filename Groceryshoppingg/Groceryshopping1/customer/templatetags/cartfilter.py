from django import template

register = template.Library()


@register.filter(name='is_in_cart')
def is_in_cart(product1, cart):
    keys = cart.keys()
    for id in keys:
        if int_or_0(id)==product1.id:
            return True

    return False;

def int_or_0(value):
    try:
        return int(value)
    except:
        return 0

@register.filter(name='cart_qquantity')
def cart_qquantity(product1, cart):
    keys = cart.keys()
    for id in keys:
        if int_or_0(id)==product1.id:
            return cart.get(id)

    return 0;

def int_or_0(value):
    try:
        return int(value)
    except:
        return 0



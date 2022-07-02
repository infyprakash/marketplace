from django import template

register = template.Library()

@register.simple_tag(name="render_partner")
def render_partner(product):
    code = product.stockrecords.filter(product__id=product.id)[0].partner.code
    return code

@register.simple_tag(name="render_partner_name")
def render_partner_name(product):
    name = product.stockrecords.filter(product__id=product.id)[0].partner.name
    return name
    

from oscar.apps.shipping import repository
from . import methods

class Repository(repository.Repository):
    
    def get_available_shipping_methods(self, basket, user=None, shipping_addr=None, request=None, **kwargs):
        method = (methods.FixedPrice(100,0),)
        # if shipping_addr and shipping_addr.country.code == 'NP':
            # Express is only available in the UK
            # methods = (methods.Standard(), methods.Express())
        return method

# from oscar.apps.shipping import methods
# from oscar.core import prices

# class Standard(methods.FixedPrice):
#     code = 'standard'
#     name = 'Standard shipping'
#     charge_excl_tax = ('5.00')
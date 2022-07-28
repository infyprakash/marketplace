from oscar.apps.basket.forms import AddToBasketForm as AddToBasketFormCore
from django import forms

from oscar.core.loading import get_model
from oscar.forms import widgets
from django.utils.translation import gettext_lazy as _

Line = get_model('basket', 'line')
Basket = get_model('basket', 'basket')
Option = get_model('catalogue', 'option')
Product = get_model('catalogue', 'product')

class AddToBasketForm(AddToBasketFormCore):
    pass


class SimpleAddToBasketMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for av in self.product.attribute_values.all():

            self.fields[av.attribute.name] = forms.ChoiceField(
                choices=self.get_choices(av.value),
                required=False,
                # widget=forms.RadioSelect,
                # help_text=av.attribute.name
                )
        # print(self.fields,'-------------------------')
        if 'quantity' in self.fields:
            self.fields['quantity'].initial = 1
            self.fields['quantity'].widget = forms.HiddenInput()

    def get_choices(self,av):
        p = []
        q = []
        for option in av:
            print(option)
            # print(type(option))
            p.append(option.option)
            q.append(option.option)
        return(list(zip(p,q)))
        # op1 = av.value_as_text.split(',')
        # op2 = av.value_as_text.split(',')
        # option = list(zip(op1,op2))
        # return option



class SimpleAddToBasketForm(SimpleAddToBasketMixin, AddToBasketForm):
    pass


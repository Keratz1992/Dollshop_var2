from django import forms

from dollshop1.models import Commentary, Cart


class CommentaryForm(forms.ModelForm):

    class Meta:
        model = Commentary
        fields = ['text']
        widgets = {'text': forms.Textarea(attrs={
            'name': 'comment',
            'id': 'review_comment',
        })}


class CartQuantityForm(forms.Form):
    quantity = forms.IntegerField(min_value=1, max_value=20)

    # class Meta:
    #     model = Cart
    #     fields = ['quantity']


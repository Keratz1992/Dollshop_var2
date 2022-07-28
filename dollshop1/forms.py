from django import forms

from dollshop1.models import Commentary


class CommentaryForm(forms.ModelForm):

    class Meta:
        model = Commentary
        fields = ['text']
        widgets = {'text': forms.Textarea(attrs={
            'name': 'comment',
            'id': 'review_comment',
        })}

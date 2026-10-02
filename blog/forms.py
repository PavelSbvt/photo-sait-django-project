from django import forms

class CommentForm(forms.Form):
    author = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Ваше имя'
    }))
    text = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Ваш комментарий',
        'rows': 3
    }))

    # class CommentForm(forms.ModelForm):
    #     author = forms.CharField(
    #         label='Автор',  # Название поля для пользователя
    #         max_length=100,
    #         widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Ваше имя'})
    #     )
    #     text = forms.CharField(
    #         label='Текст',  # Название поля для пользователя
    #         widget=forms.Textarea(attrs={'class': 'form-control','rows': 3, 'placeholder': 'Ваш комментарий'})
    #     )
    #
    # class Meta:
    #     model = Comment
    #     fields = ['author', 'text']

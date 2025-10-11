from django import forms

from accounts.models import Tadbir


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    # def clean(self):
    #     username = self.cleaned_data.get('username')
    #     password = self.cleaned_data.get('password')


class TadbirForm(forms.ModelForm):
    class Meta:
        model = Tadbir
        fields = ['h_qism', 'aloqa_t', 'nomi', 'fayl', 'asosiy_q']
        widgets = {
            'h_qism': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Hududiy qism'}),
            'aloqa_t': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Aloqa turi'}),
            'nomi': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tadbir nomi'}),
            'fayl': forms.ClearableFileInput(attrs={'class': 'form-control','name': 'fayl'}),
            'asosiy_q': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Asosiy ma’lumot'}),
        }


class EditTadbirForm(forms.ModelForm):
    class Meta:
        model = Tadbir
        fields = ['h_qism', 'aloqa_t', 'nomi', 'asosiy_q','izoh']
        widgets = {
            'h_qism': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Hududiy qism'}),
            'aloqa_t': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Aloqa turi'}),
            'nomi': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tadbir nomi'}),
            'asosiy_q': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Asosiy ma’lumot'}),
            'izoh': forms.Textarea(attrs={'class': 'form-control', 'placeholder': ' izoh....'}),
        }

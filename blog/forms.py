from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit
from .models import Article, Comment

class ArticleForm(forms.ModelForm):
	class Meta:
		model = Article
		fields = ['image', 'title', 'body']
        
		widgets = {
            'image': forms.ClearableFileInput(),
        }

	def __init__(self, *args, **kwargs):
		super(ArticleForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_method = 'post'
		self.helper.form_enctype = 'multipart/form-data'
		self.helper.layout = Layout(
            'image',
            'title',
            'body',
            'upload',
            ButtonHolder(
                Submit('submit', 'Save', css_class='btn btn-primary')
            )
        )

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')
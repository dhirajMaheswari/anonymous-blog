

from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
	'''
	our PostForm class is an instance of ModelForm, as this allows us to create or update model (our data model) instances

	'''
	class Meta:
		model = Post # this model will be used to create the form, by taking fields defined below.
		fields = ('title', 'text',)



class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)
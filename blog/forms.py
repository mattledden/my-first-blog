from django import forms

from .models import Post, Comment, CV

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)

class CVForm(forms.ModelForm):

    class Meta:
        model = CV
        fields = ('name', 'location', 'age', 'contact', 'profile', 'experience', 'qualifications', 'hobbies', 'references',)
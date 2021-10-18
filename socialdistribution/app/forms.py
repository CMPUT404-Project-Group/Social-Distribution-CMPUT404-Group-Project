from django import forms
from django.contrib.auth.forms import UserCreationForm
from api.models import Comment, Post, User
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
class RegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.label_suffix = ''
        # https://stackoverflow.com/a/46283680 - CC BY-SA 3.0
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

    github = forms.CharField(max_length=30, required=False)
    email = forms.EmailField(max_length=255, required=True)
    username = forms.CharField(max_length=30, required=True)

    def save(self, commit=True):
            # user = super().save(commit=False)
            # user.set_password(self.cleaned_data["password1"])
            if commit:
                user = get_user_model().objects.create_user(email=self.cleaned_data["email"], username=self.cleaned_data["username"], github=self.cleaned_data["github"], password=self.cleaned_data["password1"], type="author")
            return user
    class Meta:
        model = User
        fields = ('username', 'email', 'github', 'password1', 'password2')

class PostCreationForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ('title', 'text_content', 'image_content', 'categories', 'visibility')
    
    def __init__(self, *args, **kwargs):
        self.user = None
        self.image = None

        if "user" in kwargs:
            self.user = kwargs.pop("user")
        if "data" in kwargs and 'image_content' in 'data':
            self.image = kwargs['data']['image_content']
        super(PostCreationForm, self).__init__(*args, **kwargs)
    
    #TODO: Unlisted always false
    def save(self, commit=True):
        assert self.user, "User is not defined"
        post = Post.objects.create_post(
            author=self.user,
            categories=self.cleaned_data['categories'],
            image_content=self.image,
            text_content=self.cleaned_data["text_content"],
            title=self.cleaned_data["title"],
            visibility=self.cleaned_data["visibility"],
            unlisted=False
        )
        return post

class CommentCreationForm(forms.ModelForm):

    class Meta:
        model = Comment
        exclude = ('type', 'author', 'content_type', 'published', 'post_id', 'id')
    
    def __init__(self, *args, **kwargs):
        self.user = None
        self.post = None

        if "user" in kwargs:
            self.user = kwargs.pop("user")
        
        if "post" in kwargs:
            self.post = kwargs.pop("post")
    
    def save(self, commit=True):
        #Currently throws assertion error is user or post are not defined as I am unsure when you would comment on something
        #that is not a post

        assert self.user, "User is not defined"
        assert self.post, "Post is not defined"

        comment = Comment.objects.create(
            author=self.user,
            comment=self.cleaned_data['comment'],
            post_id=self.post_id
        )

        return comment
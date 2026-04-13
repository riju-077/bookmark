from django.forms import ModelForm
from links.models import Bookmark

class BookmarkForm(ModelForm):
    class Meta:
        model = Bookmark
        fields = ["title", "url", "tag", "importance_level"]
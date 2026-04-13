from django.db import models
from django.contrib.auth.models import User


class Bookmark(models.Model):
    IMPORTANCE_LEVEL = {
    "H": "High",
    "M": "Medium",
    "L": "Low",
}
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookmarks')
    title = models.CharField(max_length=200)
    url = models.URLField()
    tag = models.CharField(max_length=100, blank=True)
    importance_level = models.CharField(max_length=1, choices=IMPORTANCE_LEVEL)
    created_at = models.DateTimeField(auto_now_add=True)

    
    def __str__(self):
          return f"{self.title} ({self.user.username})"

    class Meta:
        ordering = ['-created_at']


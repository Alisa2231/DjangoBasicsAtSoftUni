from django.db import models

class Note(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField()
    category = models.ForeignKey('categories.Category', on_delete=models.SET_NULL, null=True, blank=True, related_name='notes')

    def __str__(self):
        return self.title

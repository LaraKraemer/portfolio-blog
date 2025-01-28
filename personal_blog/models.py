from django.conf import settings
from django.db import models
from django.utils import timezone
from django.utils.text import slugify

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    slug = models.SlugField(unique=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def save(self, *args, **kwargs):
        if not self.slug:  
            # Generate the slug based on the title
            base_slug = slugify(self.title)
            slug = base_slug

            # Check for uniqueness and append a number if needed
            counter = 1
            while Post.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1

            self.slug = slug
        
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


from django.db import models

class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    introduction = models.CharField(max_length=255, null=True, default="")
    content = models.TextField()
    date_published = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to='blog_images', default="")
    
    def __str__(self):
        return self.title

class BlogPostImage(models.Model):
    blog_post = models.ForeignKey(BlogPost, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='blog_images')
    caption = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"Image for {self.blog_post.title}"

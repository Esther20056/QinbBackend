# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework import status
# from .models import BlogPost
# from .Serializer import BlogPostSerializer

# @api_view(["GET"])
# def getALLBlogPosts(request):
#     all_blog_posts = BlogPost.objects.all()
#     serializer = BlogPostSerializer(all_blog_posts, many=True)
#     return Response(serializer.data)
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.template.defaultfilters import linebreaksbr
from .models import BlogPost
from rest_framework import status
from .Serializer import BlogPostSerializer

@api_view(["GET"])
def getALLBlogPosts(request):
    all_blog_posts = BlogPost.objects.all()
    serializer = BlogPostSerializer(all_blog_posts, many=True)
    
    # Convert newlines to <br> tags in the content field
    for post in serializer.data:
        post['content'] = linebreaksbr(post['content'])
    
    return Response(serializer.data)



@api_view(['GET'])
def getBlogPost(request, pk):
    blog_post = BlogPost.objects.filter(pk=pk).first()
    if blog_post is None:
        return Response({"detail": "Blog post not found."}, status=status.HTTP_404_NOT_FOUND)
    serializer = BlogPostSerializer(blog_post)
    return Response(serializer.data)

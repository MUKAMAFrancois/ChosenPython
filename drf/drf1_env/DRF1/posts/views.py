import json
from django.shortcuts import render,get_object_or_404
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from .serializers import PostSerializer
from .models import Post
import uuid
# Create your views here.


# posts=[{
#     "id":1,
#     "title":"Post 1",
#     "content":"This is the first post"
# },
# {
#     "id":2,
#     "title":"Post 2",
#     "content":"This is the second post"
# },
# {
#     "id":3,
#     "title":"Post 3",
#     "content":"This is the third post"
# }

# ]

# @api_view(http_method_names=["GET","POST"])
# def homepage(request:Request):

#     if request.method == 'POST':
#         # data = json.loads(request.body.decode('utf-8'))
#         data=request.data #no manual decoding needed, request.data does it
#         res={
#             "msg":"successfully posted!",
#             "data":data
#         }
#         return Response(data=res,status=201)

#     response={
#         "message":"Welcome to the homepage"
#     }
#     return Response(data=response,status=200,headers={"Content-Type":"application/json"})



@api_view(http_method_names=["get"])
def list_posts(request:Request):
    posts=Post.objects.all()
    serializer = PostSerializer(instance=posts,many=True)
    return Response(data=serializer.data,status=200)

@api_view(http_method_names=["POST"])
def create_a_post(request:Request):
    if request.method=="POST":
        data=request.data
        serializer=PostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            res={
                "msg":"Post created successfully",
                "data":serializer.data
            }
            return Response(data=res,status=201)
        return Response(data=serializer.errors,status=400)

@api_view(http_method_names=["GET"])    
def single_post(request,post_id:uuid.UUID):
    post=get_object_or_404(Post,pk=post_id)
    serializer=PostSerializer(instance=post)
    if post:
        return Response(data=serializer.data,status=200)
    return Response(data={"message":"Post not found"},status=404)


@api_view(http_method_names=["PATCH"])
def update_post(request,post_id:uuid.UUID):
    post=get_object_or_404(Post,pk=post_id)
    serializer=PostSerializer(instance=post)
    if request.method=="PATCH":
        data=request.data
        serializer=PostSerializer(instance=post,data=data,partial=True)
        if serializer.is_valid():
            serializer.save()
            res={
                "msg":"Post updated successfully",
                "data":serializer.data
            }
            return Response(data=res,status=200)
        return Response(data=serializer.errors,status=400)
    return Response(data={"message":"Post not found"},status=404)

@api_view(http_method_names=["DELETE"])
def delete_post(request,post_id:uuid.UUID):
    post=get_object_or_404(Post,pk=post_id)
    if post:
        post.delete()
        return Response(data={"message":"Post deleted successfully"},status=200)
    return Response(data={"message":"Post not found"},status=404)




# @api_view(http_method_names=["GET"])
# def single_post(request:Request,post_id:uuid.UUID):
#     post =get_object_or_404(Post,pk=post_id)
#     serializer=PostSerializer(post)
#     if post:
#         return Response(data=serializer.data,status=200)
#     return Response(data={"message":"Post not found"},status=404)




# ##################


# class Post_ListCreate(APIView):
#     def get(self,request:Request):
#         posts=Post.objects.all()
#         serializer=PostSerializer(posts,many=True)
#         return Response(data=serializer.data,status=200)
    

#     def post(self, request: Request):
#         serializer = PostSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=201)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

# class Post_RetrieveUpdateDestroy(APIView):
#     def get(self,request:Request,pk:uuid.UUID):
#         try:
#             post=Post.objects.get(pk=pk)
#         except Post.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND,data={"message":"Post not found"})
#         serializer=PostSerializer(post)
#         return Response(data=serializer.data,status=200)
    
#     def patch(self, request:Request, pk:uuid.UUID):
#         try:
#             post = Post.objects.get(pk=pk)
#         except Post.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)

#         serializer = PostSerializer(post, data=request.data, partial=True) # partial=True allows for partial updates, not all fields are required
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self,request:Request,pk:uuid.UUID):
#         try:
#             post=Post.objects.get(pk=pk)
#         except Post.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND, data={"message":"Post not found"})
#         post.delete()
#         return Response(data={"message":"Post deleted successfully"},status=200)
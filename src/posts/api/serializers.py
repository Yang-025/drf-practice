from rest_framework.serializers import (
    HyperlinkedIdentityField,
    ModelSerializer,
    SerializerMethodField,
)

from comments.api.serializers import CommentSerializer
from comments.models import Comment

from posts.models import Post


class PostCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = [
            # 'id',
            'title',
            # 'slug',
            'content',
            'publish',
        ]

post_detail_url = HyperlinkedIdentityField(
        view_name='posts-api:detail',
        lookup_field='slug'
    )


class PostDetailSerializer(ModelSerializer):
    url = post_detail_url
    comments = SerializerMethodField()

    class Meta:
        model = Post
        fields = [
            'url',
            'id',
            'title',
            'slug',
            'content',
            'publish',
            'comments',
        ]

    def get_comments(self, obj):
        # content_type = obj.get_content_type
        # object_id = obj.id
        c_qs = Comment.objects.filter_by_instance(obj)
        comments = CommentSerializer(c_qs, many=True).data
        return comments

class PostListSerializer(ModelSerializer):
    # view_name 來自於blog/urls.py 的 namespace='posts-api'
    # 再加上 posts/urls.py 的 name='detail'
    # url = HyperlinkedIdentityField(
    #     view_name='posts-api:detail',
    #     lookup_field='slug'
    # )
    # delete_url = HyperlinkedIdentityField(
    #     view_name='posts-api:delete',
    #     lookup_field='slug'
    # )
    url = post_detail_url
    user = SerializerMethodField()
    image = SerializerMethodField()
    html = SerializerMethodField()

    class Meta:
        model = Post
        fields = [
            'url',
            'user',
            'title',
            'content',
            'publish',
            'image',
            'html',
            # 'delete_url',
        ]

    def get_html(self, obj):
        return obj.get_markdown()

    def get_user(self, obj):
        return str(obj.user.username)

    def get_image(self, obj):
        try:
            image = obj.image.url
        except:
            image = None
        return image



""" [test]not valid
data = {
    "title": "Teahh buddy",
    "content": "New content",
    "publish": "2016-2-12",
}

new_item = PostSerializer(data=data)
if new_item.is_valid():
    new_item.save()
else:
    print(new_item.errors)

"""


""" [test]valid
from posts.models import Post
from posts.api.serializers import PostDetailSerializer

data = {
    "title": "Teahh buddy",
    "content": "New content",
    "publish": "2016-2-12",
    "slug":"yeah-buddy",
}

obj = Post.objects.get(id=3)
new_item = PostDetailSerializer(obj, data=data)
if new_item.is_valid():
    new_item.save()
else:
    print(new_item.errors)

"""

from rest_framework.serializers import ModelSerializer, HyperlinkedIdentityField

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

    class Meta:
        model = Post
        fields = [
            'url',
            'id',
            'title',
            'slug',
            'content',
            'publish',
        ]


class PostListSerializer(ModelSerializer):
    url = post_detail_url
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

    class Meta:
        model = Post
        fields = [
            'url',
            'user',
            'title',
            'content',
            'publish',
            # 'delete_url',
        ]




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

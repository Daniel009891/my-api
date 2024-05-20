from rest_framework import serializers
from posts.models import Post
from likes.models import Like
from downvotes.models import DownVote
from saved.models import Saved


class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    like_id = serializers.SerializerMethodField()
    likes_count = serializers.ReadOnlyField()
    comments_count = serializers.ReadOnlyField()
    downvote_id = serializers.SerializerMethodField()
    downvotes_count = serializers.ReadOnlyField()
    saved_id = serializers.SerializerMethodField()
    saved_count = serializers.ReadOnlyField()

    def validate_image(self, value):
        if value.size > 2 * 1024 * 1024:
            raise serializers.ValidationError(
                'Image size larger than 2MB!'
            )
        if value.image.width > 4096:
            raise serializers.ValidationError(
                'Image width larger than 4096px!'
             )
        if value.image.height > 4096:
            raise serializers.ValidationError(
                'Image height larger than 4096px!'
             )
        return value

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_like_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            like = Like.objects.filter(
                owner=user, post=obj
            ).first()
            return like.id if like else None
        return None

    def get_downvote_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            downvote = DownVote.objects.filter(
                owner=user, post=obj
            ).first()
            return downvote.id if downvote else None
        return None

    def get_saved_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            saved = Saved.objects.filter(
                owner=user, post=obj
            ).first()
            return saved.id if saved else None
        return None

    class Meta:
        model = Post
        fields = [
            'id', 'owner', 'is_owner', 'profile_id',
            'profile_image', 'created_at', 'updated_at',
            'title', 'content', 'image', 'image_filter', 'like_id',
            'likes_count', 'comments_count', 'downvote_id', 'downvotes_count',
            'saved_id', 'saved_count',
        ]

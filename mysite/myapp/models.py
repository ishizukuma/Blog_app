from accounts.models import CustomUser
from django.db import models

class Myapp(models.Model):
    """日記モデル"""

    user = models.ForeignKey(CustomUser, verbose_name='ユーザー', on_delete=models.PROTECT)
    title = models.CharField(verbose_name='タイトル', max_length=40)
    content = models.TextField(verbose_name='本文', blank=True, null=True)
    photo1 = models.ImageField(verbose_name='写真1', blank=True, null=True)
    photo2 = models.ImageField(verbose_name='写真2', blank=True, null=True)
    photo3 = models.ImageField(verbose_name='写真3', blank=True, null=True)
    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)

    class Meta:
        verbose_name_plural = 'Myapp'

    def __str__(self):
        return self.title
    


class Chat(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    message = models.CharField(max_length=255)
    response = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    @classmethod
    def create(cls, **kwargs):
        # データベース内の Chat インスタンス数を確認
        chats = Chat.objects.all()
        if chats.count() >= 3:
            # 古いものから削除
            oldest_chat = chats.order_by('created_at').first()
            oldest_chat.delete()

        # インスタンスを作成
        chat = cls(**kwargs)
        chat.save()
        return chat

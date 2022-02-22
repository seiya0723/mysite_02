from django.db import models

class Topic(models.Model):

    #models.Modelを継承した時点でここに主キーである、idフィールドが作られている。だからあえてidフィールドを書く必要はない。

    #文字列型で、2000文字まで許容し、入力必須(Null禁止、空文字列禁止)
    comment     = models.CharField(verbose_name="コメント",max_length=2000)

    #TODO:後に投稿日時、投稿者の名前、画像、などの入力を受け付けるフィールドを追加する。

    #モデルオブジェクト単体をprint()文あるいはテンプレートでモデルオブジェクトを表示させた時、何を返すかを指定している。この場合はcommentを出す。
    #これがないとTopic Objects (1) などと表示される
    def __str__(self):
        return self.comment

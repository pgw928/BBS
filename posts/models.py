from django.db import models

class Post(models.Model) :
    author = models.CharField("작성자", max_length=20)
    title = models.CharField("글제목", max_length=50,default="")
    contents = models.TextField("글내용",max_length=1000)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.contents


class Comment(models.Model) :
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.CharField("댓글 작성자",max_length=20)
    contents = models.TextField("댓글 내용", max_length=1000)

    def __str__(self):
        return self.contents

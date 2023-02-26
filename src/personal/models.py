from django.db import models

# Priority = [
#     ("L", "low"),
#     ("M", "medium"),
#     ("H", "high"),
# ]


# class Question(models.Model):
#     title = models.CharField(max_length=60)
#     question = models.TextField(max_length=600)
#     priority = models.CharField(max_length=1, choices=Priority, default="medium")

#     def __str__(self):
#         return self.title

#     class Meta:
#         verbose_name = "The questions"
#         verbose_name_plural = "People question"

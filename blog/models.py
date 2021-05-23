from django.db import models

# Create your models here.
class Blog(models.Model): #models의 Model 클래스 상속. 상속받으면 모델 클래스의 메소드 사용가능
    title = models.CharField(max_length=200)
    writer = models.CharField(max_length=100)
    pub_date = models.DateTimeField()
    body = models.TextField()

    def __str__(self):  
	    return self.title

    def summary(self):
    	return self.body[:100]  
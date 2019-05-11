from django.db import models

# Create your models here.
#question 모델 클래스
#설문 제목,설문 생성일
class Question(models.Model):
    name = models.CharField(max_length = 200)
    #DateField는 날짜 데이터를 저장할 수 있는 저장공간
    #DatetimeField는 날짜 + 시간 데이터를 저장 할 수 있는 공간
    pub_date = models.DateField()
    
    def __str__(self):
        return self.name
#choice 모델 클레스
#답변 항목 내용,투표 수 ,어떤 question과 연결 되있는지?(외래키)
class Choice(models.Model):
    name =models.CharField(max_length = 50)
    #IntegerField: 정수값 데이터를 저장 할 수 있는 공간
    #default: 모든 field 클래스에 존재하는 매개변수로,객체 생성시 기본값설정을 할수있음
    votes= models.IntegerField(default=0)
    #Question 모델클래스와 1:n관계를 가지는 설정.
    #Choice 객체가 연결한 Question객체가 삭제가 되면,자신도 삭제되도록 설정
    #ex)글 삭제하면 그 글에 작성된 댓글이 같이 삭제됨
    q = models.ForeignKey(Question,on_delete=models.CASCADE)
    
    #self.q.name: 현재 choice객체가 연결한 Question 객체의 이름 불러옴
    def __str__(self):
        return self.q.name + '/' + self.name
'''
models.Foreignkey:다른 모델클래스의 객체와 해당 모델 클래스의 객체가 연결관계를 가지는 저장 공간
Foreignkey(연결할 모델,on_delete= 연결객체 삭제시 ,삭제 방식)
현재 chioce 모델 클래스의 q변수는 연결한 QUestion객체를 의미함
>choice 객체.q.name: 연결된 모델클래스의 객체가 삭제될떄 연결한 객체들을 어떻게 처리할지
지정하는 변수
models.CASCADE:연결된 모델클래스의 객체가 삭제될떄 같이 삭제
models.PROTECT:연결된 모델클래스가 삭제되지 않도록 막아줌
models.SET_NULL:연결된 객체가 삭제되면 아무것도 연결하지 않은 상태 유지
models.SET(연결할객체):연결된 객체가 삭제되면 매개변수로 넣은 객체와 연결
models.SET_DEFAULT: 연결된 객체가 삭제되면 기본값 객체와 연결
'''

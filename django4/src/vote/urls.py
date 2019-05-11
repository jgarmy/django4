'''
Created on 2019. 4. 21.

@author: 405-5
'''
'''
어플 별도의 url conf를 만들수있음
단, app name 와 urlpatterns 변수 정의해야함 (이름이 틀리면 url conf가 설정되지않음)
app_name: 이파일에 정의한 url들의 그룹이름(문자열)
urlpatterns: path함수를 이용해 뷰함수를 등록하는 변수 (리스트)
만들어진 urls.py를 프로잭트의 urls.py에 알려줘야함
'''
from django.urls import path
from vote.views import *
app_name='vote'
# 기본 도메인 주소 : 127.0.0.1:8000/vote/
#127.0.0.1:8000/vote/요청이 들어오면 index함수 호출

urlpatterns=[
    path('',index),
    #127.0.0.1:8000/vote/숫자값 요청이 들어오면 detail함수 호출
    #숫자값은 q_id 매개변수에 값으로 사용됨
    path('<int:q_id>/',detail),
    #127.0.0.1:8000/vote/vote/ -> vote함수 호출
    path('vote/',vote),
    #127.0.0.1:8000/vote/result/숫자값 -> result함수 호출
    path('result/<int:q_id>/',result),
    #파이썬코드나 html에서 vote:qr 별칭으로 url을 찾을 수 있음
    path('qr/', qregiste, name='qr'),
    path('cr/', cregiste, name='cr'),
    path('<int:q_id>/qchange/', qupdate, name='qu'),
    path('<int:q_id>/qdelete/', qdelete, name='qd'),
    path('<int:c_id>/cdelete/', cdelete, name='cd'),
    path('<int:c_id>/cchange/', cupdate, name='cu')
    ]
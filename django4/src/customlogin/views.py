from django.shortcuts import render
from customlogin.forms import SigninForm,SignupForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login, logout
from django.http.response import HttpResponseRedirect
from django.urls.base import reverse
#User.objects.create_user(username, email, password)
#회원가입
def signup(request):
    #GET 방식 요청
    if request.method == "GET":
        #회원가입폼 객체 생성 및 HTML파일 전달
        form = SignupForm()
        return render(request, 'cl/signup.html',{'form':form})
    #POST 방식 요청
    if request.method == "POST":    
        #사용자 입력기반 회원가입폼 객체 생성 - 에러 발생시 사용할 객체
        form = SignupForm(request.POST)
        #사용자 입력이 유효한지 확인(아이디중복체크,패스워드나 이메일 형식)
        #폼객체.is_valid(): 입력양식의 형태를 사용자가 잘 작성했는지 확인하는함수
        #True를 반환한 경우 : 사용자 입력이 유효한 값인 것을 확인. 폼객체.cleaned_data[] 변수를 사용하 사용자 입력을 추출할 수 있음
        #False를 반환한 경우 : 사용자가 올바른 입력을 할 수 있도록 HTML코드를 전달
        if form.is_valid():
            #입력한 패스워드가 일치하는지 확인
            if form.cleaned_data['password']==form.cleaned_data['password_check']:
                print(form.cleaned_data)
                #회원 생성
                '''
                a폼객체.save()는 사용자 입력을 바탕으로 연동된 모델클래스 객체를 데이터베이스에 저장함
                user 모델클래스에 password란은 원본 비밀번호를 저장하는 것이 아닌 암호화된
                a비밀번호를 저장해야되기 떄문에, save()함수를 사용할 수 없음.
                user 모델클래스에 잇는 회원생성 함수를 사용해 새로운 회원을 데이터베이스에 만들수 있음
                user.objects.create_user(아이디,비밀번호,이메일): 매개변수에 들어온 입력을 바탕으로 새로운 회원을 생성하는 함수
                '''
                #데이터베이스에 새로운 회원이 생성 및 news_user변수에 user객체가 저장됨
                new_user = User.objects.create_user(username=form.cleaned_data['username'],
                                                     email=form.cleaned_data['email'],
                                                    password=form.cleaned_data['password'])
                print('회원가입 완료:',new_user)
                new_user.first_name = form.cleaned_data['first_name']
                new_user.last_name = form.cleaned_data['last_name']
                #변경사항를 데이터베이스에 반영
                new_user.save()
                #다른 페이지나 HTML파일 전송
                return render(request,'cl/signupcom.html',{'name': new_user.username})
            else:
                return render(request,'cl/signup.html',{'form':form,'error':'비밀번호가 다릅니다.'}) #입력한 비밀번호가 틀린경우의 처리
        else:
            return render(request,'cl/signup.html',{'form':form,
                          'error':'형식에 맞지않는 입력을 했습니다.'}) #사용자가 입력이 올바르지 않은경우의 처림    
#로그인
def signin(request):
    #GET 방식 요청
    if request.method == "GET":
        #SigninForm 객체 생성 및 HTML파일 전달
        form = SigninForm()
        return render(request, 'cl/signin.html',{'form':form})
    #POST 방식 요청
    elif request.method == "POST":
        #사용자 입력에서 id와 password부분을 추출
        id = request.POST.get('username')
        pw = request.POST.get('password')
        #유저 객체 추출(authenticate 함수 사용)
        #authenticate(username,password): 비밀번호는 암호화 된 상태로
        #username과 비밀번호가 일치하는 user 객체 한객를 추츨하는 함수
        #만약 username이나 비밀번호가 틀린경우, None값을 반환함
        u = authenticate(username = id,password = pw)
        #유저가 데이터베이스에 있는지 확인
        if u:    
            #로그인처리
            #login(클라이언트, user객체) : 해당 요청을 한 클라이언트가 Usr객체
            #정보로 로그인됨. 로그인 된 클라이언트는 request.user 변수를 사용해
            #로그인된 회원의 정보(firsr_name, username)를 가져올 수 있음
            #ex)로그인된 클라이언트의 이름정보를 추출 : request.user.first_name
            #비로그인상태의 클라이언트는 request.user에 None값이 저장되어 있음
            login(request,u)
            return HttpResponseRedirect('/vote/')
        #유저가 존재하지않은경우
        else:
            #로그인페이지를 에러코드와 함깨 전달
            form = SigninForm()
            return render(request,'cl/signin.html',{'form':form,
                                                    'error':'아이디나 비밀번호가 맞지않습니다'})
#로그아웃
def signout(request):
    #logout(클라이언트정보): 해당클라이언트의 user정보를 지워주는 함수
    #request.user 에 None값으로 변경됨
    #만약 비로그인 상태의 클라이언트가 접근하더라도 에러가 발생하지 않음
    logout(request)
    #reverse('그룹이름:별칭',args=(추가변수의 값,))
    #그룹이름과 별칭이 일치하는 url주소를 문자열형태로 반환해주는 함수
    #만약 추가매개변수가 있는 뷰함수인 경우, args 매개변수를 통해
    #매개변수에 넘겨줄 값을 저장할 수 있음(튜플)
    #ex)detail뷰함슈 reverse('',args=(q_id,)
    return HttpResponseRedirect(reverse('cl:signin'))
    



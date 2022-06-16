# urbanplay_clone_back

본 프로젝트는 어반플레이(urbanplay) 웹사이트를 클론 코딩해보는 스터디 프로젝트입니다. 레포지토리는 총 두 개로 아래와 같이 구성되어 있습니다.

* [urbanplay_clone_back](https://github.com/theGreatEnds/urbanplay_clone_back)
* [urbanplay_clone_front](https://github.com/theGreatEnds/urbanplay_clone_front)

urbanplay_clone_back 레포지토리는 Django RESTFramework 로 구축되었습니다. 
처음에는 서버 가동에 필요한 모듈을 설치, DB 설정, 관리자 계정 생성이 필요합니다.

    pip install -r requirements.txt
    python manage.py makemigrations
    python manage.py migrate
    python manage.py createsuperuser
    
그런 다음에 마지막으로 서버를 실행하면 됩니다.

    python manage.py runserver


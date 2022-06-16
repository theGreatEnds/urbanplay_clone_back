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

urbanplay_clone_back 안에 urbanplay_clone_front가 submodule로 포함되어 있는 형태입니다. 그러므로 frontend 코드도 build 해줄 필요가 있는데, 이 때 사용하는 명령어는 아래와 같습니다.

    cd urbanplay_clone_front
    npm run build
    
urbanplay_clone_front 레포지토리 안에서 build를 실행해주게 되면 webpack --config webpack.config.js 명령이 자동으로 실행됩니다.

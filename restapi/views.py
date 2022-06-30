from django.http import JsonResponse
from django.views.generic import View


class PressView(View):
    def get(self, request):
        return JsonResponse(self.get_data(), json_dumps_params={'ensure_ascii': True})

    def get_data(self):
        return {
            "counts": 30,
            "lists":
            [
                {
                    "url": "https://www.urbanplay.co.kr/press/?q=YToxOntzOjEyOiJrZXl3b3JkX3R5cGUiO3M6MzoiYWxsIjt9&bmode=view&idx=11153629&t=board",
                    "title": "\"높은 임대수익률? 입지 보다 중요한 건 이것\"",
                    "date": "2022-04-11",
                    "writer": "땅집고",
                },
                {
                    "url": "https://www.urbanplay.co.kr/press/?q=YToxOntzOjEyOiJrZXl3b3JkX3R5cGUiO3M6MzoiYWxsIjt9&bmode=view&idx=11062371&t=board",
                    "title": "컴퍼니합, 어반플레이와 전략적 제휴 체결",
                    "date": "2022-03-29",
                    "writer": "이데일리",
                },
                {
                    "url": "https://www.urbanplay.co.kr/press/?q=YToxOntzOjEyOiJrZXl3b3JkX3R5cGUiO3M6MzoiYWxsIjt9&bmode=view&idx=11109858&t=board",
                    "title": "동네에서 놀자고 판 벌리는 스타트업: 어반플레이",
                    "date": "2022-03-23",
                    "writer": "서울프라퍼티인사이트",
                },
                {
                    "url": "https://www.urbanplay.co.kr/press/?q=YToxOntzOjEyOiJrZXl3b3JkX3R5cGUiO3M6MzoiYWxsIjt9&bmode=view&idx=10579126&t=board",
                    "title": "부동산 수익증권 거래소 '소유', 어반플레이와 전략적 제휴",
                    "date": "2022-02-23",
                    "writer": "뉴시스",
                },
                {
                    "url": "https://www.urbanplay.co.kr/press/?q=YToxOntzOjEyOiJrZXl3b3JkX3R5cGUiO3M6MzoiYWxsIjt9&bmode=view&idx=9558239&t=board",
                    "title": "도시에 로컬 OS를 입히는 로컬 크리에이터 집단, 어반플레이",
                    "date": "2022-01-17",
                    "writer": "CHIEFEXECUTIVE",
                },
                {
                    "url": "https://www.urbanplay.co.kr/press/?q=YToxOntzOjEyOiJrZXl3b3JkX3R5cGUiO3M6MzoiYWxsIjt9&bmode=view&idx=9435336&t=board",
                    "title": "어반플레이가 연남동에서 명성을 얻기까지",
                    "date": "2022-01-12",
                    "writer": "BUYBRAND",
                },
                {
                    "url": "https://www.urbanplay.co.kr/press/?q=YToxOntzOjEyOiJrZXl3b3JkX3R5cGUiO3M6MzoiYWxsIjt9&bmode=view&idx=8908882&t=board",
                    "title": "침체된 조선업 고장 영도에 핫플레이스를…피아크P.ARK(2)",
                    "date": "2021-11-19",
                    "writer": "디자인프레스",
                },
                {
                    "url": "https://www.urbanplay.co.kr/press/?q=YToxOntzOjEyOiJrZXl3b3JkX3R5cGUiO3M6MzoiYWxsIjt9&bmode=view&idx=8892049&t=board",
                    "title": "침체된 조선업 고장 영도에 핫플레이스를…피아크P.ARK(1)",
                    "date": "2021-11-19",
                    "writer": "디자인프레스",
                },
                {
                    "url": "https://www.urbanplay.co.kr/press/?q=YToxOntzOjEyOiJrZXl3b3JkX3R5cGUiO3M6MzoiYWxsIjt9&bmode=view&idx=8790897&t=board",
                    "title": "동네에 콘텐츠를 담겠다고하니…\"네가 왜 나서냐\" 소리도 들었죠",
                    "date": "2021-11-05",
                    "writer": "매일경제",
                },
                {
                    "url": "https://www.urbanplay.co.kr/press/?q=YToxOntzOjEyOiJrZXl3b3JkX3R5cGUiO3M6MzoiYWxsIjt9&bmode=view&idx=8790870&t=board",
                    "title": "콘텐츠 플랫폼 어반플레이, 85억 규모 프리B 투자 유치",
                    "date": "2021-11-05",
                    "writer": "머니투데이",
                },
                {
                    "url": "https://www.urbanplay.co.kr/press/?q=YToxOntzOjEyOiJrZXl3b3JkX3R5cGUiO3M6MzoiYWxsIjt9&bmode=view&idx=8745407&t=board",
                    "title": "온오프라인 도시문화 콘텐츠 플랫폼 '어반플레이', 85억 원 규모 시리즈 B 투자 유치",
                    "date": "2021-11-04",
                    "writer": "Platum",
                },
                {
                    "url": "https://www.urbanplay.co.kr/press/?q=YToxOntzOjEyOiJrZXl3b3JkX3R5cGUiO3M6MzoiYWxsIjt9&bmode=view&idx=8809944&t=board",
                    "title": "[폴인인사이트] 부산 영도에 '3000평 카페'가 들어선 배경은",
                    "date": "2021-11-04",
                    "writer": "중앙일보",
                },
                {
                    "url": "https://www.urbanplay.co.kr/press/?q=YToxOntzOjEyOiJrZXl3b3JkX3R5cGUiO3M6MzoiYWxsIjt9&bmode=view&idx=9096676&t=board",
                    "title": "정초이웍스, 레드닷 디자인 어워드 디자인 2개 부문 본상",
                    "date": "2021-10-14",
                    "writer": "굿모닝경제",
                },
                {
                    "url": "https://www.urbanplay.co.kr/press/?q=YToxOntzOjEyOiJrZXl3b3JkX3R5cGUiO3M6MzoiYWxsIjt9&bmode=view&idx=8714378&t=board",
                    "title": "백화점 \"당분간 새점포 없다\" 리뉴얼 大戰",
                    "date": "2021-09-30",
                    "writer": "서울경제",
                },
                {
                    "url": "https://www.urbanplay.co.kr/press/?q=YToxOntzOjEyOiJrZXl3b3JkX3R5cGUiO3M6MzoiYWxsIjt9&bmode=view&idx=8714356&t=board",
                    "title": "창립 이래 첫 CM송에 93년생 랩퍼…. 달라지는 롯데",
                    "date": "2021-09-24",
                    "writer": "조선비즈",
                },
                {
                    "url": "https://www.urbanplay.co.kr/press/?q=YToxOntzOjEyOiJrZXl3b3JkX3R5cGUiO3M6MzoiYWxsIjt9&bmode=view&idx=7984309&t=board",
                    "title": "순천시, 역세권 창업활성화 협약 어반플레이·브루웍스",
                    "date": "2021-09-13",
                    "writer": "전남일보",
                },
                {
                    "url": "https://www.urbanplay.co.kr/press/?q=YToxOntzOjEyOiJrZXl3b3JkX3R5cGUiO3M6MzoiYWxsIjt9&bmode=view&idx=8714312&t=board",
                    "title": "SBA 'SEOUL MADE' 매거진, 홍주석 어반플레이 대표와 라이브 북토크 개최",
                    "date": "2021-09-13",
                    "writer": "매일경제",
                },
                {
                    "url": "https://www.urbanplay.co.kr/press/?q=YToxOntzOjEyOiJrZXl3b3JkX3R5cGUiO3M6MzoiYWxsIjt9&bmode=view&idx=9096713&t=board",
                    "title": "연남방앗간, 서울역점 오픈 기념 '챕터원 : 부산' 팝업 실시",
                    "date": "2021-08-27",
                    "writer": "매일경제",
                },
                {
                    "url": "https://www.urbanplay.co.kr/press/?q=YToxOntzOjEyOiJrZXl3b3JkX3R5cGUiO3M6MzoiYWxsIjt9&bmode=view&idx=7569093&t=board",
                    "title": "문화 싣고 영도에 상륙한 가장 '부산'스러운 배 '피아크'",
                    "date": "2021-08-11",
                    "writer": "부산일보",
                },
                {
                    "url": "https://www.urbanplay.co.kr/press/?q=YToxOntzOjEyOiJrZXl3b3JkX3R5cGUiO3M6MzoiYWxsIjt9&bmode=view&idx=7401388&t=board",
                    "title": "\"좋은 콘텐츠가 있는 곳에 사람이 모여요\"",
                    "date": "2021-07-26",
                    "writer": "이로운넷",
                },
                {
                    "url": "https://www.urbanplay.co.kr/press/?q=YToxOntzOjEyOiJrZXl3b3JkX3R5cGUiO3M6MzoiYWxsIjt9&bmode=view&idx=7463442&t=board",
                    "title": "지역·청년 그리고 상생... '2021 로컬게더링 문경' 성황리 마쳐",
                    "date": "2021-06-22",
                    "writer": "프레시안",
                },
                {
                    "url": "https://www.urbanplay.co.kr/press/?q=YToxOntzOjEyOiJrZXl3b3JkX3R5cGUiO3M6MzoiYWxsIjt9&bmode=view&idx=7463447&t=board",
                    "title": "현대건설, 업계 최초 입주민 대상 제주도 여행 테마 서비스 개발",
                    "date": "2021-06-16",
                    "writer": "이투데이",
                },
                {
                    "url": "https://www.urbanplay.co.kr/press/?q=YToxOntzOjEyOiJrZXl3b3JkX3R5cGUiO3M6MzoiYWxsIjt9&bmode=view&idx=7463446&t=board",
                    "title": "[문경소식] '소상공인 새바람 체인지업 사업' 신청ㆍ접수 외",
                    "date": "2021-06-16",
                    "writer": "쿠키뉴스",
                },
                {
                    "url": "https://www.urbanplay.co.kr/press/?q=YToxOntzOjEyOiJrZXl3b3JkX3R5cGUiO3M6MzoiYWxsIjt9&bmode=view&idx=7463445&t=board",
                    "title": "입주민에 제주여행 테마서비스..현대건설, 어반플레이-프립과 제휴",
                    "date": "2021-06-16",
                    "writer": "한국정경신문",
                },
                {
                    "url": "https://www.urbanplay.co.kr/press/?q=YToxOntzOjEyOiJrZXl3b3JkX3R5cGUiO3M6MzoiYWxsIjt9&bmode=view&idx=7463444&t=board",
                    "title": "21일 로컬게더링 2021 문경 개최…지역·청년 상생 모색",
                    "date": "2021-06-16",
                    "writer": "아시아투데이",
                },
                {
                    "url": "https://www.urbanplay.co.kr/press/?q=YToxOntzOjEyOiJrZXl3b3JkX3R5cGUiO3M6MzoiYWxsIjt9&bmode=view&idx=7463443&t=board",
                    "title": "지역과 청년이 함께 꿈꾸는 상생 하모니",
                    "date": "2021-06-16",
                    "writer": "스카이데일리",
                },
                {
                    "url": "https://www.urbanplay.co.kr/press/?q=YToxOntzOjEyOiJrZXl3b3JkX3R5cGUiO3M6MzoiYWxsIjt9&bmode=view&idx=7463448&t=board",
                    "title": "화면에서 만난 제주 구석구석, 원도심부터 어촌마을까지",
                    "date": "2021-06-13",
                    "writer": "이로운넷",
                },
                {
                    "url": "https://www.urbanplay.co.kr/press/?q=YToxOntzOjEyOiJrZXl3b3JkX3R5cGUiO3M6MzoiYWxsIjt9&bmode=view&idx=7463449&t=board",
                    "title": "광안리 타월, 이천쌀 캔… 디자인, 地方으로 가다",
                    "date": "2021-06-07",
                    "writer": "조선일보",
                },
                {
                    "url": "https://www.urbanplay.co.kr/press/?q=YToxOntzOjEyOiJrZXl3b3JkX3R5cGUiO3M6MzoiYWxsIjt9&bmode=view&idx=7463450&t=board",
                    "title": "지속가능한 로컬 비즈니스를 모색하는 로컬게더링 2021 제주 컨퍼런스 개최 예정",
                    "date": "2021-05-05",
                    "writer": "한국경제",
                },
                {
                    "url": "https://www.urbanplay.co.kr/press/?q=YToxOntzOjEyOiJrZXl3b3JkX3R5cGUiO3M6MzoiYWxsIjt9&bmode=view&idx=7463451&t=board",
                    "title": "동네가게 사장님들! 하이퍼로컬과 친해지세요",
                    "date": "2021-04-12",
                    "writer": "중소기업뉴스",
                },
            ]
        }

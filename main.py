from fastapi import FastAPI, Query

app = FastAPI()

# 가상의 수업 데이터
courses = [
    {
        "id": "CS201",
        "과목명": "데이타베이스 구조",
        "담당교수": "홍길동",
        "구분" : "전공필수",
        "학점": 3,
        "학과" : "전산학과",
        "요일" : ["월","수"],
        "시간" : "10:00 ~ 12:00"
    },
    {
        "id": "CS202",
        "과목명": "이산구조",
        "담당교수": "김갑돌",
        "구분" : "전공필수",
        "학점": 3,
        "학과" : "전산학과",
        "요일" : ["화","목"],
        "시간" : "10:00 ~ 12:00"
    },
    {
        "id": "CS101",
        "과목명": "프로그래밍의 이해",
        "담당교수": "김철수",
        "구분" : "전공선택",
        "학점": 3,
        "학과" : "전산학과",
        "요일" : ["월","수"],
        "시간" : "14:00 ~ 16:00"
    },
    {
        "id": "CS301",
        "과목명": "프로그래밍 언어",
        "담당교수": "이영희",
        "구분" : "전공선택",
        "학점": 3,
        "학과" : "전산학과",
        "요일" : ["월","수"],
        "시간" : "14:00 ~ 16:00"
    }
]

@app.get("/courses")
async def get_courses(
    id: int = Query(default=None),
    과목명: str = Query(default=None),
    담당교수: str = Query(default=None),
    학점: int = Query(default=None, gt=0),
    최소학점: int = Query(default=None, gt=0),
    학과: str = Query(default=None),
    구분: str = Query(default=None)
):
    filtered_courses = courses

    if id is not None:
        # id 필터링
        filtered_courses = [course for course in filtered_courses if course["id"] == id]

    if 과목명 is not None:
        # 이름 포함 필터링
        filtered_courses = [course for course in filtered_courses if 과목명.lower() in course["과목명"].lower()]

    if 담당교수 is not None:
        # 교수명 포함 필터링
        filtered_courses = [course for course in filtered_courses if 담당교수.lower() in course["담당교수"].lower()]
        
    if 구분 is not None:
        # 구분 포함 필터링
        filtered_courses = [course for course in filtered_courses if 구분.lower() in course["구분"].lower()]
        
    if 학과 is not None:
        # 학과 포함 필터링
        filtered_courses = [course for course in filtered_courses if 학과.lower() in course["학과"].lower()]

    if 학점 is not None:
        # 학점 필터링
        filtered_courses = [course for course in filtered_courses if course["학점"] >= credits]

    if 최소학점 is not None:
        # 최소 학점 필터링
        filtered_courses = [course for course in filtered_courses if course["최소학점"] >= min_credits]

    return filtered_courses

from fastapi import FastAPI, Query, Body
from typing import List, Optional

app = FastAPI()

#벌크 테스트
strawberry_data = [
  {
    "food_name": "빈츠 딸기 프로마쥬",
    "food_type": "과자",
    "food_brand": "롯데제과",
    "food_keywords": [
      "딸기",
      "초콜릿",
      "쿠키",
      "2024년",
      "핑크",
      "봄",
      "빈츠"
    ],
    "food_price": 4500,
    "release_date": "2024-02-10",
    "review_rating": 4.3
  },
  {
    "food_name": "몽쉘 딸기 생크림 케이크",
    "food_type": "과자",
    "food_brand": "롯데제과",
    "food_keywords": [
      "딸기",
      "초콜릿",
      "케이크",
      "2024년",
      "딸기잼",
      "봄",
      "몽쉘"
    ],
    "food_price": 6500,
    "release_date": "2024-02-12",
    "review_rating": 4.5
  },
  {
    "food_name": "딸기라떼 카스타드",
    "food_type": "과자",
    "food_brand": "롯데제과",
    "food_keywords": [
      "딸기",
      "딸기라떼",
      "케이크",
      "2024년",
      "카스타드",
      "봄"
    ],
    "food_price": 5500,
    "release_date": "2024-02-11",
    "review_rating": 4.4
  },
  {
    "food_name": "딸기라떼 명가 찰떡파이",
    "food_type": "과자",
    "food_brand": "롯데제과",
    "food_keywords": [
      "딸기",
      "찰떡",
      "찰떡파이",
      "딸기라떼",
      "2024년",
      "핑크",
      "봄"
    ],
    "food_price": 7650,
    "release_date": "2024-02-06",
    "review_rating": 4.3
  },
  {
    "food_name": "팔도 봄 에디션 딸기 비빔면",
    "food_type": "라면",
    "food_brand": "팔도",
    "food_keywords": [
      "딸기",
      "비빔면",
      "딸기맛",
      "2024년",
      "상큼",
      "봄"
    ],
    "food_price": 5500,
    "release_date": "2024-02-05",
    "review_rating": 4.2
  },
  {
    "food_name": "딸기 블라썸 붕어싸만코",
    "food_type": "빙과",
    "food_brand": "빙그레",
    "food_keywords": [
      "딸기",
      "벚꽃",
      "붕어싸만코",
      "2024년",
      "아이스크림",
      "봄",
      "핑크",
      "편의점신상"
    ],
    "food_price": 2200,
    "release_date": "2024-03-02",
    "review_rating": 4.7
  },
  {
    "food_name": "딸기 글레이즈드 도넛",
    "food_type": "베이커리",
    "food_brand": "크리스피크림",
    "food_keywords": [
      "딸기",
      "도넛",
      "2024년",
      "핑크",
      "봄"
    ],
    "food_price": 2500,
    "release_date": "2024-03-15",
    "review_rating": 4.9
  },
  {
    "food_name": "상큼한 딸기크림을 토핑한 스트로베리 피그 도넛",
    "food_type": "베이커리",
    "food_brand": "크리스피크림",
    "food_keywords": [
      "딸기",
      "초콜릿",
      "딸기크림",
      "도넛",
      "동물모양",
      "2024년",
      "핑크",
      "봄"
    ],
    "food_price": 3900,
    "release_date": "2024-03-13",
    "review_rating": 4.1
  },
  {
    "food_name": "생딸기 마스카포네 도넛",
    "food_type": "베이커리",
    "food_brand": "노티드",
    "food_keywords": [
      "딸기",
      "생딸기",
      "도넛",
      "2024년",
      "크림치즈",
      "봄",
      "마스카포네"
    ],
    "food_price": 5200,
    "release_date": "2024-03-21",
    "review_rating": 4.6
  },
  {
    "food_name": "스트로베리 자스민티",
    "food_type": "음료",
    "food_brand": "노티드",
    "food_keywords": [
      "딸기",
      "자스민",
      "차",
      "2024년",
      "핑크",
      "봄",
      "허브티",
      "아이스티",
      "논카페인"
    ],
    "food_price": 6800,
    "release_date": "2024-03-06",
    "review_rating": 4.3
  }
]

@app.get("/limited_edition_strawberry_food_search")
async def searchLimitedEditionStrawberryFood(
    food_name: Optional[str] = Query(
        None,
    ),
    food_type: Optional[str] = Query(
        None,
        description="과자, 라면, 빙과, 베이커리, 음료 중 하나를 선택하세요"
    ),
    food_brand: Optional[str] = Query(
        None,
    ),
    food_keywords: List[str] = Query(
        ...,
        description="한글로 띄어쓰기 없이 제품키워드를 입력하세요"
    )
):
    # 데이터에서 검색 조건에 맞는 항목 필터링
    filtered_data = []
    for item in strawberry_data:
        if (food_name is None or food_name == item["food_name"]) \
                and (food_type is None or food_type == item["food_type"]) \
                and (food_brand is None or food_brand == item["food_brand"]) \
                and all(keyword in item["food_keywords"] for keyword in food_keywords):
            filtered_data.append(item)
    return filtered_data

# 무형문화제 데이터
intangible_cultural_heritage_data = [    {
        "name": "판소리",
        "main_category": "전통공연",
        "subcategory": "음악",
        "designated_date": "1964.12.28",
        "location": "기타",
        "introduction": "판소리는 한 명의 소리꾼이 고수(북치는 사람)의 장단에 맞추어 창(소리), 말(아니리), 몸짓(너름새)을 섞어가며 긴 이야기를 엮어가는 것을 말한다."
    },
    {
        "name": "양주별산대놀이",
        "main_category": "전통공연",
        "subcategory": "연희",
        "designated_date": "1964.12.07",
        "location": "경기도 양주시",
        "introduction": "양주별산대놀이는 경기도 양주군 주내면 유양리 지역에서 전승되는 산대놀이 계통의 탈놀이다."
    },
    {
        "name": "자수장",
        "main_category": "전통기술",
        "subcategory": "공예",
        "designated_date": "1984.10.15",
        "location": "부산광역시 금정구",
        "introduction": "자수(刺繡)는 여러 색깔의 실을 바늘에 꿰어 바탕천에 무늬를 수놓아 나타내는 조형활동이다."
    },
    {
        "name": "주철장",
        "main_category": "전통기술",
        "subcategory": "공예",
        "designated_date": "2001.03.12",
        "location": "충청북도 진천군",
        "introduction": "주철장이란 인류가 오랫동안 사용하였던 쇠를 녹여서 각종 기물을 만드는 장인을 말한다."
    },
    {
        "name": "사직대제",
        "main_category": "의례의식",
        "subcategory": "그 밖의 의식의례",
        "designated_date": "2000.10.19",
        "location": "서울특별시 종로구",
        "introduction": "사직대제는 땅과 곡식의 신에게 드리는 국가적인 제사로, 사(社)는 땅의 신, 직(稷)은 곡식의 신을 의미한다. 예로부터 나라를 세우면 먼저 조상에게 제사를 지내고 이와 함께 땅과 곡식의 신에게 백성이 편안하게 살 수 있도록 풍요를 기원하는 사직제를 올렸다."
    },
    {
        "name": "강강술래",
        "main_category": "전통공연",
        "subcategory": "음악",
        "designated_date": "1966.02.15",
        "location": "전라남도 진도군",
        "introduction": "강강술래는 노래와 춤이 하나로 어우러진 부녀자들의 집단놀이이다."
    },
    {
        "name": "강릉단오제",
        "main_category": "전통놀이",
        "subcategory": "축제",
        "designated_date": "1967.01.16",
        "location": "강원도 강릉시",
        "introduction": "강릉단오제는 우리나라에서 가장 역사가 깊은 축제로, 마을을 지켜주는 대관령 산신을 제사하고, 마을의 평안과 농사의 번영, 집안의 태평을 기원한다."
    },
    {
        "name": "한산모시짜기",
        "main_category": "전통기술",
        "subcategory": "공예",
        "designated_date": "1967.01.16",
        "location": "충청남도 서천군",
        "introduction": "한산모시는 우리나라의 미를 상징하는 여름 전통옷감으로 역사적 가치가 높아 제작기술을 보호하고자 국가무형유산으로 지정했다."
    },
    {
        "name": "북청사자놀음",
        "main_category": "전통공연",
        "subcategory": "연희",
        "designated_date": "1967.03.31",
        "location": "서울특별시",
        "introduction": "북청사자놀음은 대사의 묘미나 풍자적인 측면보다는 사자춤의 묘기와 흥겨움이 중심이 되어 다른 사자춤사위보다 교묘하고 힘찬 동작이 특징이다."
    },
    {
        "name": "줄타기",
        "main_category": "전통공연",
        "subcategory": "연희",
        "designated_date": "1976.06.16",
        "location": "경기도 과천시",
        "introduction": "줄타기는 공중에 맨 줄 위에서 재미있는 이야기와 발림을 섞어가며 여러 가지 재주를 보여주는 놀이이다."
    },
    {
        "name": "종묘제례",
        "main_category": "의례의식",
        "subcategory": "그 밖의 의식의례",
        "designated_date": "1975.05.09",
        "location": "서울특별시 종로구",
        "introduction": "종묘제례란 조선시대 역대 왕과 왕비의 신위를 모셔 놓은 사당(종묘)에서 지내는 제사를 말한다."
    },
    {
        "name": "제주민요",
        "main_category": "전통공연",
        "subcategory": "음악",
        "designated_date": "1989.12.01",
        "location": "제주특별자치도 서귀포시",
        "introduction": "제주민요는 일하면서 부르는 노동요가 많고 부녀자들이 부르는 민요가 흔하다는 점에서 주목된다. 노랫말도 특이한 제주도 사투리를 많이 사용하고 있으며, 경기지역 민요보다 구슬프다."
    },
    {
        "name": "영산줄다리기",
        "main_category": "전통놀이",
        "subcategory": "놀이",
        "designated_date": "1969.02.11",
        "location": "경상남도 창녕군",
        "introduction": "영산줄다리기는 경상남도 창녕군 영산면에서 전승되는 민속놀이로 현재는 3·1문화제 행사의 하나로 줄다리기를 하고 있다."
    },
    {
        "name": "연등회",
        "main_category": "전통놀이",
        "subcategory": "축제",
        "designated_date": "2012.04.06",
        "location": "서울특별시 종로구",
        "introduction": "연등회는 관불의식, 연등행렬, 회향의 형식으로 진행되며 연등행렬 때 동원되는 등(燈)이 다양하고 다채롭다."
    },
    {
        "name": "번와장",
        "main_category": "전통기술",
        "subcategory": "건축",
        "designated_date": "2008.10.21",
        "location": "기타",
        "introduction": "번와장'이란 지붕의 기와를 잇는 장인을 말한다."
    }
]

@app.get("/intangible_cultural_heritage")
async def filterIntangibleCulturalHeritage(
    name: Optional[str] = Query(
        None,
        description="문화재명을 한글로 적어주세요 (ex. 판소리, 양주별산대놀이, 주철장)"
    ),
    main_category: str = Query(
        ...,
        description="대분류를 한글로 적어주세요 (ex. 전통공연, 전통기술, 의례의식)"
    ),
    subcategory: Optional[str] = Query(
        None,
        description="소분류를 한글로 적어주세요 (ex. 음악, 공예, 그 밖의 의식의례)"
    ),
    designated_date: Optional[str] = Query(
        None,
        description="지정일을 1964.12.28 형식으로 적어주세요"
    ),
    location: Optional[str] = Query(
        None,
        description="소재지를 한글로 적어주세요 (ex. 기타, 경기도 양주시, 부산광역시 금정구, 충청북도 진천군)"
    )
):
    # 데이터에서 검색 조건에 맞는 항목 필터링
    filtered_data = []
    for item in intangible_cultural_heritage_data:
        if (name is None or name == item["name"]) \
                and main_category == item["main_category"] \
                and (subcategory is None or subcategory == item["subcategory"]) \
                and (designated_date is None or designated_date == item["designated_date"]) \
                and (location is None or location == item["location"]):
            filtered_data.append(item)
    return filtered_data

cooking_receipe_data = [  {
    "creator": "뇨리사",
    "food_classification": [
      "음료"
    ],
    "cook_name": "셀러리 주스",
    "ingredients": [
      "셀러리",
      "물",
      "바나나",
      "사과",
      "레몬"
    ],
    "time": 5,
    "receipe": "1. 셀러리는 깨끗하게 씻어서 잎은 떼어내고 줄기만  갈기 좋은 크기로 자릅니다. 2. 사과는 껍질을 벗긴 후 역시 갈리 좋은 크기로 잘라둡니다. 3. 믹서 용기에 물을 붓고 잘라둔 셀러리와 사과를 넣어요. 그 위에 바나나도 뚝뚝 잘라 넣습니다. 4. 레몬은 껍질은 벗기고 씨를 발라낸 후 과육만 넣어요. 5. 재료들이 곱게 갈릴 때까지 믹서를 돌린 후 컵에 담아요. ",
    "views": 12902
  },
  {
    "creator": "히트주부",
    "food_classification": [
      "죽"
    ],
    "cook_name": "버섯 굴죽",
    "ingredients": [
      "쌀",
      "굴",
      "버섯",
      "물",
      "참기름",
      "국간장",
      "소금",
      "후추"
    ],
    "time": 30,
    "receipe": "1. 굴은 굵은 소금을 뿌려서 껍질을 골라내고 살살 씻어서 건져둡니다. 2. 냄비에 참기름과 쌀, 물 한큰술을 넣고 기름이 잘 섞이도록 살살 볶아요. 찹쌀을 섞거나 쌀알을 다져서 넣으면 더 촉촉한 느낌이 납니다. 3. 물 5컵을 넣고 쌀알이 완전히 떠오를때까지 끓여요. 4. 물기를 뺀 굴과 다진 버섯을 냄비에 넣고 물 1컵을 추가해서 살짝 더 끓여요. 5. 국간장으로는 색만 내고 소금, 후추로 간해요.   ",
    "views": 14319
  },
  {
    "creator": "프로쿠커",
    "food_classification": [
      "매일반찬"
    ],
    "cook_name": "두부 조림",
    "ingredients": [
      "두부",
      "대파",
      "실고추",
      "들기름"
    ],
    "time": 15,
    "receipe": "1. 두부를 3 ×4.5 ×0.8㎝ 정도로 잘라서 소금을 뿌려 물기를 잠시 뺀 후 면보나 키친타올로 닦아서 준비해요.  2. 두부 물기가 빠질 동안 양념 재료를 섞고 실고추와 채썬 대파를 1~2㎝ 길이로 잘라둡니다.  3. 팬에 기름을 두른 후 두부를 넣고 한쪽이 완전히 노릇노릇하게 될때까지 중간불에 두었다 뒤집어요. 빨리 뒤집지말고 한쪽면이 단단해질때까지 기다려야 부서지지않아요.  4. 두부에 양념장을 조금씩 올리고 약불~중불에서 천천히 조려요.  5. 수분이 반정도 줄어들면 실고추와 채썬 파를 올려요. 처음부터 넣으면 색이 이쁘지않아요. 6. 센불로 잠깐 올려서 남은 수분을 날려줍니다",
    "views": 24031
  },
  {
    "creator": "금손곰손",
    "food_classification": [
      "매일반찬"
    ],
    "cook_name": "고기전",
    "ingredients": [
      "쇠고기 다짐육",
      "양파",
      "당근",
      "밀가루",
      "달걀",
      "식용유",
      "마늘",
      "국간장",
      "참기름"
    ],
    "time": 35,
    "receipe": "1. 채소는 다져서 준비해요. 2. 식용유를 제외한 채소, 고기, 양념, 달걀, 밀가루를 모두 섞어요.  3. 팬에 기름을 두르고 데운 후 재료를 한수저씩 떠서 팬에 놓아요. 중간에 한번 뒤집어주세요. 4. 고기가 주재료라 약한 불에서 천천히 익혀야 타지않고 보기좋아요.",
    "views": 13714
  },
  {
    "creator": "라이프쿠커",
    "food_classification": [
      "저장음식",
      "매일반찬"
    ],
    "cook_name": "두릅장아찌",
    "ingredients": [
      "두릅",
      "물",
      "국간장",
      "식초",
      "설탕",
      "소주",
      "청양고추"
    ],
    "time": 10,
    "receipe": "1. 두릅의 딱딱한 끝부분을 잘라내고 겉껍질을 떼어낸 후 씻어요. 2. 소금을 약간 넣은 끓는 물에 두릅의 줄기부터 넣어 30초 정도 먼저 데쳐요. 3. 두릅을 모두 넣고 줄기를 먼저 넣은 시간부터 총 3분 정도 데쳐줍니다.4. 건져서 찬물에 빨리 헹궈야 숨이 죽지 않고 아삭해요. 5. 두릅의 물기를 빼고 꼭 짜두세요. 6. 소스를 끓여서 한 김 식혀둡니다. 7. 용기에 두릅을 담고 소스를 넣어 3일간 숙성시킨 후 먹어요. 용기가 넓으면 소스가 더 필요하니 유념하세요.",
    "views": 4908
  },
  {
    "creator": "마카롱언니",
    "food_classification": [
      "가족",
      "초대요리",
      "매일반찬"
    ],
    "cook_name": "치킨 너겟",
    "ingredients": [
      "닭 안심살",
      "마요네즈",
      "시리얼",
      "마늘",
      "소금",
      "후추",
      "생각가루"
    ],
    "time": 50,
    "receipe":"1. 고기는 물에 한번 씻어서 물기를 빼두세요. 안심은 기름이 거의 없어 냄새가 나지않아 우유에 담가두지 않아도 괜찮아요.  2. 안심을 2등분 합니다. 이때 힘줄이 보이면 잘라내 줍니다. 힘줄을 제거하면 더 부드럽게 먹을 수 있어요. 3. 한입 크기로 자른 고기에 소금, 후추, 생강가루로 밑간을 합니다. 4. 마요네즈에 다진 마늘을 섞은 후 고기에 버무립니다.  5. 시리얼을 지퍼백에 넣고 방망이나 병으로 성글게 밀어요. 조금 크게 부숴야 바삭하게 씹히는 느낌이 좋아요. 6. 마요네즈에 버무린 고기에다 부순 시리얼을  골고루  묻혀요.  7. 오븐팬에 고기끼리 닿지않게 놓아요. 8. 200℃로 예열한 오븐에서 20분간 구워요. 중간에 한번 뒤집어주어야 앞뒤로 바삭하게 구워져요.",
    "views":54336
  },
  {"creator": "빨간모자",
    "food_classification": [
      "국",
      "가족"
    ],
    "cook_name": "버섯 들깨탕",
    "ingredients": [
      "느타리버섯",
      "말린 표고버섯",
      "대파",
      "멸치다시마",
      "국간장",
      "들깨가루",
      "쌀가루",
      "소금",
      "멸치",
      "다시마"
    ],
    "time": 30,
    "receipe": "1. 물 5~6컵에 멸치를 넣어 육수를 만든 후 다시마를 넣어요. 2. 5분 후 불을 끄고 다시마는 건져내고 육수 4컵을 준비해요. 3. 말린 표고버섯은 물에 불려서 썰고 느타리버섯은 가늘게 찢어요. 표고버섯은 말린 후 물에 불리는게 향과 맛이 더 좋지만 말린게 없으면 생표고를 사용해도 됩니다. 4. 육수 4컵에 국간장을 넣어 간을 미리 맞추고 버섯을 넣어요. 혹시, 싱거우면 소금을 넣어주세요.  5. 들깨가루와 쌀가루를 국물에 섞어요. 채를 사용하면 뭉치지않게 잘 풀어집니다. 쌀가루를 넣으면 영양면에서도 보완이 되고 식사대용으로 먹을 수 있습니다. 쌀가루를 넣은 후에는 타지않게 바닥을 저어주는게 좋아요. 6. 한소큼 끓으면 어슷하게 썬 대파를 넣어줍니다.",
    "views": 73456
  },
  {
    "creator": "지갑텅명",
    "food_classification": [
      "가족",
      "초대요리",
      "매일반찬"
    ],
    "cook_name": "새우 춘권",
    "ingredients": [
      "춘권피",
      "달걀",
      "식용유",
      "새우살",
      "양파",
      "당근",
      "풋고추",
      "녹말가루",
      "소금",
      "후추"
    ],
    "time": 120,
    "receipe": "1. 춘권피는 냉동실에서 꺼내 살짝 녹여두고 달걀은 잘 풀어둡니다. 2. 춘권피 가장자리에 붓이나 손으로 달걀물을 바른 후 중간에 속재료를 넣고 한쪽 모서리로 덮어요. 3. 잘 말아준 뒤 잠시 잘 붙도록 둡니다. 5. 170~180℃로 데운 기름에 춘권을 튀긴 후 키친타월에 밭쳐 기름을 빼요. 6. 초간장이나 스위트칠리소스, 해선장 등을 곁들이면 잘 어울려요.",
    "views": 36434
  },
  {
    "creator": "사랑맘",
    "food_classification": [
      "찌개",
      "가족"
    ],
    "cook_name": "참치 김치찌개",
    "ingredients": [
      "참치캔",
      "김치",
      "고추장",
      "참기름",
      "참치액",
      "두부"
    ],
    "time": 18,
    "receipe": "1. 김치를 먹기좋게 자르고 고추장과 기름을 넣어서 중간불에서 잘 어우러지게 볶아요. 2. 참치캔의 기름은 버리고 참치만 건져둬요. 올리브유에 담긴 참치는 그 기름으로 볶으세요. 3. 김치에 고추장과 기름이 잘 섞였으면 물을 붓고 끓여요. 4. 김치가 완전히 익으면 참치를 넣고 맛이 어우러지게 5분 정도만 더 끓여요. 5. 혹, 싱거우면 김칫국물 (참치액이나 조미료) 등으로 간을 맞춰주세요.",
    "views": 3923
  },
  {
    "creator": "유지누나",
    "food_classification": [
      "국",
      "미역"
    ],
    "cook_name": "들깨 미역국",
    "ingredients": [
      "미역",
      "들기름",
      "물",
      "국간장",
      "들깨가루",
      "마늘"
    ],
    "time": 10,
    "receipe": "1. 불린 미역은 먹기 좋게 잘라요.  2. 냄비에 미역과 들기름, 국간장, 마늘을 넣고 중간불에서 양념이 섞이도록 잠시 볶아요.  3. 뜨물(물)을 넣고 10분 정도 미역이 부드러워질때까지 끓여요. 뜨물을 넣으면 육수를 따로 내지않아도 맛있어요. 4. 소금으로 간을 맞춰요.  5. 거피한 들깨가루를 체에 걸러 국물에 풀어주세요. 걸쭉한게 좋으면 들깨가루를 더 넣어도 됩니다.  ",
    "views": 342284
  },
  {
    "creator": "빵덕후",
    "food_classification": [
      "간식"
    ],
    "cook_name": "전 남친 토스트",
    "ingredients": [
      "식삥",
      "크림치즈",
      "블루베리잼"
    ],
    "time": 2,
    "receipe": "1. 먼저 식빵을 토스터나 프라이팬에 노릇노릇하게 구워줍니다. 2. 구워진 식빵에 크림치즈를 골고루 펴발라줍니다. 3. 크림치즈에 위에 블루베리잼을 바릅니다. 4. 전자렌지에 넣어 10초간 돌려 완성합니다.",
    "views": 645453
  },
  {
    "creator": "카랑카랑",
    "food_classification": [
      "간식"
    ],
    "cook_name": "소떡소떡",
    "ingredients": [
      "떡볶이떡",
      "비엔나 소시지",
      "꼬치",
      "식용유",
      "허니머스터드",
      "케첩",
      "고추장",
      "물엿",
      "맛술",
      "핫소스"
    ],
    "time": 20,
    "receipe": "1. 단단한 떡볶이 떡은 끓는 물에 데쳐서 부드럽게 만들어요. 소시지도 데쳐서 기름기를 빼는게 좋아요. 2. 떡과 소시지를 체에 밭쳐 물기를 말려요.  3. 나무 꼬치에 소시지와 떡을 차례로 끼워요. 4. 기름을 넉넉하게 넣은 팬에서 튀기듯이 앞뒤를 구워요. 떡을 튀기면 튀어올라 화상을 입을 수 있으니 굽는게 안전합니다.  5. 소스를 팬에서 졸이거나 전자레인지에 1분 정도 돌려서 걸쭉하게 만들어요.6. 취향에 따라 소스와 허니머스터드 소스를 발라서 먹어요.",
    "views": 132221
  },
  {
    "creator": "두시의쿠킹",
    "food_classification": [
      "간식"
    ],
    "cook_name": "감말랭이",
    "ingredients": [
      "감"
    ],
    "time": 300,
    "receipe": "1. 감의 껍질을 벗긴 후 반으로 갈라요. 2. 꼭지를 떼어주고 씨도 보이는대로 빼줍니다. 3. 말리기 좋은 크기로 잘라줍니다. 4. 감을 건조기에 고루 깔아주세요.감끼리 겹쳐지지않게 놓아야 더 빨리 마릅니다. 5. 온도는 70℃로 맞춰놓고 시간은 10~20시간 사이로 감의 양에 따라 조절해요. 8. 감이 다 마르면 건조기를 끈 다음 감말랭이가 식으면 그릇이나 지퍼백에 담아 냉동실에 보관해요.",
    "views": 6654
  },
  {
    "creator": "이선주요리교실",
    "food_classification": [
      "기타",
      "소스"
    ],
    "cook_name": "발사믹 양파조림",
    "ingredients": [
      "양파",
      "포도씨오일",
      "발사믹비니거",
      "소금",
      "후추"
    ],
    "time": 40,
    "receipe": "1. 양파를 최대한 가늘게 썰어줍니다. 두께가 비슷해야 익는 속도가 같아지니 채칼을 사용하면 편해요. 2. 포도씨유를 두르고 약불에서 한동안 볶아 부드럽게 숨을 죽여요. 3. 양파가 부드럽게 볶아졌으면 발사믹비니거를 넣고 더 볶아줍니다.(총 40분 정도 소요됨) 4. 소금, 후추로 간해요. 5. 불을 끈 후 덜어내지말고 그대로 두고 뜸을 더 들인 후 용기에 담는게 좋아요.",
    "views": 248543
  },
  {
    "creator": "하사랑",
    "food_classification": [
      "저장음식"
    ],
    "cook_name": "동치미",
    "ingredients": [
      "총각무",
      "쪽파",
      "마늘",
      "생강",
      "지고추"
    ],
    "time": 100,
    "receipe": "1. 김장때 나오는 작은 달랑무를 소금에 굴려서 쪽파와 함께 하룻 동안 통에 담아둡니다. 달랑무가 없으면  큰무 하나를 토막낸 후 쪽파와 함께 소금을 그냥 고루 발라두세요. 2. 하루가 지난 후  생수에 소금으로 간을 짭짤하게 맞춰둡니다. 3. 지고추와 편으로 썬 마늘과 생강,  파프리카나 배, 감 등을 배보자기에 담아 모두 넣어요. 4. 실온에 하루정도 두었다가 김치냉장고에 넣어요.  5. 일주일 후부터 먹을 수 있습니다.",
    "views": 63454
  }
]

@app.get("/cooking_receipe")
async def filterCookingReceipe(
    creator: Optional[str] = Query(
        None,
        description="창작자를 한글로 적어주세요(ex. 꿀키, 양순맘)"
    ),
    food_classification: str = Query(
        ...,
        description="음식 분류를 한글로 적어주세요(ex. 밥, 죽, 면, 매일반찬, 저장음식, 소스, 양념장, 가족, 초대요리, 국, 찌개, 전골, 간식, 음료, 기타)"
    ),
    cook_name: Optional[str] = Query(
        None,
        description="요리명을 한글로 적어주세요(ex. 당근라페, 계란버섯전, 전 남친 토스트)"
    ),
    ingredients: Optional[str] = Query(
        None,
        description="재료를 한글로 적어주세요(ex. 당근, 버섯, 홀그레인머스타드, 시금치, 간장, 설탕)"
    ),
    time: Optional[int] = Query(
        None,
        ge=0,
        description="소요시간(단위: 분)은 0이상의 정수로 적어주세요."
    )
):
    # 데이터에서 검색 조건에 맞는 항목 필터링
    filtered_data = []
    for item in cooking_receipe_data:
        if (creator is None or creator == item["creator"]) \
                and food_classification in item["food_classification"] \
                and (cook_name is None or cook_name == item["cook_name"]) \
                and (ingredients is None or all(ingredient in item["ingredients"] for ingredient in ingredients.split(','))) \
                and (time is None or time == item["time"]):
            filtered_data.append(item)
    return filtered_data



#나이키 테스트
nikes = [    {
        "intent": "추천",
        "product_type": "신발",
        "category": "런닝",
        "gender": None,
        "color": None,
        "product_name": None,
        "answer": "나이키 러닝화 추천'에 대해 찾아볼게요!\n\n1. 인피니티 런 4\n나이키 리액트 폼보다 13% 더 높은 에너지 반환력을 갖춘 새로운 나이키 리액트X 폼으로 제작되어 상쾌하고 탄력 있는 발걸음이 유지되며, 지지력 있는 쿠셔닝을 적용해 러닝 시 안정적인 자세를 유지할 수 있도록 도와줍니다.\n\n2. 페가수스 40\n나이키 페가수스 40은 기존의 페가수스 모델을 업그레이드한 제품으로, 더욱 편안하고 안정적인 러닝을 할 수 있도록 설계되었습니다. 리액트 폼을 적용하여 부드럽고 탄력 있는 쿠셔닝을 제공하며, 발 중앙 부분에 아치를 지지해 주는 디자인이 적용되어 안정적인 러닝을 할 수 있도록 도와줍니다.\n\n3. 인빈서블 3\n줌X 폼을 적용하여 부드럽고 탄력 있는 쿠셔닝을 제공하며, 발 중앙 부분에 아치를 지지해 주는 디자인이 적용되어 안정적인 러닝을 할 수 있도록 도와줍니다.",
        "card": ["인피니티 런 4","페가수스 40"],
        "bubble": ["인빈서블3 알려줘", "페가수스 40 알려줘", "인피니티 런 4 알려줘"]
    },
             {
        "intent": "정보",
        "product_type": "신발",
        "category": "런닝",
        "gender": None,
        "color": None,
        "product_name": "인피니티런4",
        "answer": "나이키 인피니티 런 4'에 대해 알려드릴게요.\n\n나이키 인피니티 런 4는 지지력 있는 쿠셔닝을 적용한 제품입니다. 나이키 리액트 폼보다 13% 더 높은 에너지 반환력을 갖춘 새로운 나이키 리액트X 폼으로 제작되어 더욱 상쾌하고 탄력 있는 발걸음을 유지할 수 있습니다. 플라이니트와 리액트X 폼이 어우러진 부드러운 갑피의 지지력과 통기성으로 자신감 있는 러닝을 만들어줘요.",
        "card": ["인피니티 런 4"],
        "bubble": ["인피니티 런 4 사이즈 알려줘", "인피니티 런 4 특징 알려줘", "인피니티 런 4 소재 알려줘"]
    },
             {
        "intent": "정보",
        "product_type": "신발",
        "category": "런닝",
        "gender": "남성",
        "color": "오렌지",
        "product_name": "알파플라이2",
        "answer": "'나이키 알파플라이 2 남성 로드 레이싱화 사이즈'에 대해 찾아볼게요!\n\n나이키 알파플라이 2 남성 로드 레이싱화는 사이즈 250 ~ 310까지 있습니다.\n정확한 정보는 [제품 상세 페이지](https://www.nike.com/kr/t/%EC%95%8C%ED%8C%8C%ED%94%8C%EB%9D%BC%EC%9D%B4-2-%EB%82%A8%EC%84%B1-%EB%A1%9C%EB%93%9C-%EB%A0%88%EC%9D%B4%EC%8B%B1%ED%99%94-tL7CEVL8/DN3555-600)에서 확인해 주세요",
        "card": ["나이키 알파플라이 2 남성 로드 레이싱화"],
        "bubble": ["나이키 알파플라이 2 남성 로드 레이싱화 색상 알려줘", "나이키 알파플라이 2 남성 로드 레이싱화 소재 알려줘", "나이키 알파플라이 2 남성 로드 레이싱화 특징 알려줘"]
    }
            ]

@app.get("/nike_test")
async def search_nikes(
    intent: str,
    product_type: Optional[str] = None,
    category: Optional[str] = None,
    gender: Optional[str] = None,
    color: Optional[str] = None,
    product_name: Optional[str] = None,
):
    # 필터링된 결과를 저장할 리스트
    filtered_nikes = []
    
    for nike in nikes:
        # 각 필터에 대한 조건 확인
        if (
            (intent is None or nike['intent'] == intent) and
            (product_type is None or nike['product_type'] == product_type) and
            (category is None or nike['category'] == category) and
            (gender is None or nike['gender'] == gender) and
            (color is None or nike['color'] == color) and
            (product_name is None or nike['product_name'] == product_name)
        ):

            filtered_nikes.append(nike)

    
    return filtered_nikes


#240305 테스트
rag_data = [{
        "category": "Security Monitoring",
        "context": "[['Security Monitoring Managed 서비스가 무엇인가요?', 'Security Monitoring Managed 서비스는 네이버 서비스를 외부의 공격으로부터 안전하게 보호하고 있  는 보안전문 인력이 네이버 클라우드 플랫폼 고객의 서비스를 24시간 365일 보호하는 보안관제 서비스예요.\nSecurity Monitoring Basic 서비스에서 보다 강화  된 모니터링을 원하는 고객에게 유료로 제공되는 서비스로 탐지/차단 서비스 및 분석 서비스를 추가로 제공해요.'], ['Security Monitoring Managed 서비스에   서 주간/월간 보고서를 제공하나요?', 'Security Monitoring Managed는 보다 강화된 모니터링을 원하는 고객에게 유료로 제공되는 서비스로 탐지/차단 서비스   별 주간/월간 보고서를 제공하고 있어요.'], ['WAF를 통해 차단된 것 같은데 예외 처리하려면 어떻게 해야하나요?', 'Security Monitoring에서 WAF를 통해 차   단되었을 때 예외 처리하려면,  아래 두 항목을 포함하여 [고객지원 > 문의하기]로 접수해 주세요.\n\n1. 예외 처리가 필요한 탐지 이벤트\n2. 예외 처리가 필  요한 Request URL\n3. 예외 처리가 필요한 Source IP\n\n자세한 내용은 아래 버튼을 눌러 확인해 주세요.'], ['모의 침투 테스트란 무엇인가요?', '모의 침투   테스트란, 네이버 클라우드 플랫폼 상에 구성한 고객의 서비스 및 리소스에 대한 보안 수준을 평가하기 위해 실제 공격과 유사한 행위를 수행하는 것을 의미해  요.\n\n다만, 고객은 네이버 클라우드 플랫폼의 인프라 또는 네이버 클라우드 플랫폼 서비스 자체에 대한 보안 평가를 수행할 수 없어요.\n\n모의 침투 테스트  와 관련하여 상세한 정책과 사전 신청을 원하시는 경우, 아래 링크의 모의 침투 테스트 지원 정책 및 신청서를 참고해 주세요.'], ['모의 침투 테스트를 하기   위한 네이버 클라우드 플랫폼의 지원 정책은 무엇인가요?', '네이버 클라우드 플랫폼은 고객의 보안인증 및 감사를 위한 혹은 자체 계획에 따른 모의 침투 테   스트 진행을 지원하고 있어요.\n\n다만, 테스트 전 반드시 당사에 사전 신청을 해 주셔야 해요. 상세한 내용 및 사전 신청서의 양식은 아래 버튼을 눌러 확인   해 주세요.'], ['IPS V2 보안 이벤트 발생 시 어떻게 인지할 수 있나요?', 'Managed 서비스 이용 시 Security Monitoring IPS 이벤트가 발생하는 경우 Notification Setting에 설정된 정보로 이벤트 정보를 안내하고 있어요.\n상세 정보는 Console에서 확인하실 수 있어요.\n\nClassic 플랫폼 이용 시 [네이버 클라우드   플랫폼 > Console > Security Monitoring > Notification Setting > IPS(V1)]에서 안내받고자 하는 담당자를 설정할 수 있어요.\n\nVPC 플랫폼 이용 시 [네이  버 클라우드 플랫폼 > Console > Security Monitoring > Notification Setting > IPS(V2)]에서 안내받고자 하는 담당자를 설정할 수 있어요.\n\n자세한 내용은   아래 버튼을 눌러 확인해 주세요.'], ['Anti-DDoS 보안 이벤트 발생 시 어떻게 인지할 수 있나요?', 'Security Monitoring Anti-DDoS 이벤트 발생 시 Managed 고객에게는 Notification Setting에 설정된 정보로 이벤트 정보를 안내하고 있어요.\n\n자세한 내용은 아래 버튼을 눌러 확인해 주세요.'], ['WAF 보안 이벤   트 발생 시 어떻게 인지할 수 있나요?', 'Security Monitoring WAF 이벤트 발생 시 Managed 고객에게는 Notification Setting에 설정된 정보로 이벤트 정보를   안내하고 있어요.\n\n자세한 내용은 아래 버튼을 눌러 확인해 주세요.'], ['IDS 보안 이벤트 발생 시 어떻게 인지할 수 있나요?', 'Security Monitoring IDS    이벤트 발생 시 Managed 고객에게는 Notification Setting에 설정된 정보로 이벤트 정보를 간략하게 안내하고 있어요.\n\n자세한 내용은 아래 버튼을 눌러 확   인해 주세요.'], ['기본으로 제공되는 무료 보안 서비스는 무엇인가요?', 'Classic 플랫폼에서는 IDS, Anti-Virus(Window에 한해) 서비스를 무료로 제공하며,\nVPC 플랫폼에서는 IDS 서비스를 무료로 제공해요. (Anti-Virus는 무료로 제공하지 않아요.)\n\n무료 보안 서비스에 대한 더 자세한 내용은 아래 버튼을 눌러   확인해 주세요.'], ['IPS V2 서비스를 사용 시 주의사항은 무엇인가요?', 'IPS(V2) 서비스 사용 시 주의사항에 대해 알려 드릴게요.'], ['Security Monitoring의 IPS V2는 무엇인가요?', 'Security Monitoring의 IPS(V2)는 VPC 플랫폼에서 제공하며 Host 기반의 인바운드/아웃바운드 트래픽을 모니터링하여 의심스러운   활동을 탐지하고 차단해요.\n\nIPS는 24시간 365일 모니터링하고 공격에 대해 실시간 차단함으로써 안전하게 서비스가 운영될 수 있도록 지원해요.\n\nIPS(V2)에서 제공하는 서비스에 대한 자세한 내용은 아래 버튼을 눌러 확인해 주세요.'], ['Anti-Virus 서비스를 사용 시 주의사항은 무엇인가요?', 'Anti-Virus 서비  스를 사용 시 주의사항에 대해 알려드릴게요.'], ['Anti-Virus 보안 이벤트 발생 시 어떻게 인지할 수 있나요?', 'Security Monitoring Anti-Virus 이벤트 발   생 시 Managed 고객에게는 Notification Setting에 설정된 정보로 이벤트 정보를 안내하고 있어요. 상세 정보는 Console에서 확인해 주세요.\n\n※ Security Monitoring에는 Basic과 Managed 서비스가 있으며,\nBasic 서비스를 사용하시는 경우 보안 이벤트가 발생했을 때 정보를 받아볼 이메일을 별도로 설정할 수 없으  며, 로그인 ID로 정보를 보내드려요.\nManaged 서비스를 사용하시는 경우 Notification Setting 메뉴에서 정보를 받아볼 이메일을 설정할 수 있으며, 별도 설   정을 하지 않으신 경우에는 로그인 ID로 정보를 보내드려요.\n\n자세한 내용은 아래 버튼을 눌러 확인해 주세요.'], ['WAF 모니터링 대상은 어떻게 되나요?',   '\u200bWAF는 HTTP/HTTPS 표준 프로토콜을 사용하는 웹 서비스에 대해서만 모니터링할 수 있어요.\nLoad Balancer 설정된 서비스 모니터링을 위해서 Load Balancer Protocol 을 반드시 HTTP/HTTPS로 설정하셔야 해요. (TCP, SSL로 설정 시 WAF 서비스를 제공받을 수 없습니다.)'], ['OS 커널을 업데이트 할 경우 Security Monitoring에 영향이 있나요?', '고객이 임의로 OS 커널을 업데이트할 경우, Security Monitoring 서비스가 정상적으로 제공되지 않을 수 있어요.\n커널 업  데이트가 필요한 경우 호환 커널 리스트를 참고해 주세요.'], ['Security Monitoring의 IPS가 뭐야?', 'IPS(Intrusion Prevention System)란 고객의 서비스로   인입되는 공격을 탐지/차단하는 보안 솔루션으로, 24시간*365일 모니터링하여 고객의 서비스가 안전하게 운영될 수 있도록 지원하고 있어요.'], ['Security Monitoring의 보고서는 언제 발송돼?', '침입행위가 탐지될 경우 이를 분석하여 고객의 서비스에 위협이 된다고 판단되면 보고서를 발송해요.'], ['Security Monitoring에서 탐지된 공격정보는 어디서 확인해?', 'Security Monitoring에서 탐지된 공격정보는 [콘솔 > Security Monitoring > Dashboard] 에서 확인할 수 있  어요.'], ['Security Monitoring에서 침해사고 기술 지원이 뭐야?', '침해사고 기술 지원은 고객 서비스에 침해사고가 발생하면 대응 전문가가 침해사고에 대   한 분석을 수행하고, 원인을 파악해 차후 동일한 피해가 발생하지 않도록 지원하는 서비스예요.'], ['Security Monitoring에서 Anti-Virus 패턴 업데이트 주기   알려줘', '백신 패턴은 매일 새벽 1시에 업데이트 되며, 실시간 모니터링에 즉시 반영돼요.'], ['Security Monitoring의 Anti-Virus가 뭐야?', 'Anti-Virus는   고객이 운영 중인 서버에 악성코드를 실시간으로 탐지하고 격리/삭제 조치함으로써 고객의 서비스가 안정적으로 운영될 수 있도록 지원해요.\n플랫폼 환경에   따라 Anti-Virus(V1), Anti-Virus(V2)로 구분되며, Classic 환경에서 제공하는 서비스는 Anti-Virus(V1), VPC 환경에서 제공하는 서비스는 Anti-Virus(V2)라고   해요.\n\n더 자세한 내용은 아래 버튼을 눌러 확인해 주세요.'], ['Security Monitoring의 WAF가 뭐야?', 'WAF(Web Application Firewall)는 Web 기반(HTTP/HTTPS) 트래픽을 모니터링하여 공격 트래픽을 탐지 및 차단하는 보안 솔루션이에요.\n\nWAF에서 제공하는 서비스에 대한 자세한 내용은 아래 버튼을 눌러 확인   해 주세요.']]"
                }
           ]

@app.get("/rag_test")
async def get_rag_test(
    category: Optional[str] = Query(None, description="Location of the rental car")
) -> List[dict]:
    filtered_rag = rag_data

    if category:
        filtered_rag = [rag for rag in filtered_rag if rag["category"] == category]
    return filtered_rag


rag_data2 = [{
        "category": "Security Monitoring",
        "context": "Security Monitoring에는 Basic 서비스와 Managed 서비스가 있으며, 서비스 구분에 따라 제공하는 기능 및 이용 요금이 상이합니다. Security Monitoring Managed가 플랫폼별로 제공하는 보안 서비스는 다음과 같습니다. 사용자 환경이 VPC인지 Classic인지에 따라 동일한 서비스여도 일부 기능에 차이가 있을 수 있습니다. 이용 중인 플랫폼을 먼저 확인한 후 상세 설명을 참고해 주십시오.  참고  •	Security Monitoring 개념의 원활한 이해를 위해 다음 용어에 유의해 주십시오.  o	V1: Classic 환경을 일컫는 약어  o	V2: VPC 환경을 일컫는 약어  •	Security Monitoring 개념 학습 전 보안 서비스별 주의 사항도 사전에 반드시 숙지해야 합니다. 보안 서비스별 주의 사항은 Security Monitoring 사용 준비를 참조해 주십시오.  VPC  VPC 환경에서 Security Monitoring Managed가 제공하는 IDS, Anti-Virus, Anti-DDoS, WAF, IPS 기능을 설명합니다.  IDS(V2)  사용자의 서비스로 인입되는 공격을 실시간 탐지합니다. 24시간 365일 모니터링함으로써 사용자의 서비스가 안전하게 운영될 수 있도록 지원합니다. 제공하는 기능은 다음과 같습니다.  •	보안 사고 의심 이벤트 발생 시 탐지 및 분석 보고서 전달  •	최신 공격 위협에 대해서 지속적인 탐지 정책 설정 및 패턴 업데이트 적용  •	사용자 요청 시 탐지 예외 처리 제공  •	주간, 월간 보고서 제공  Anti-Virus(V2)  악성코드를 탐지하고 방어합니다. 사용자가 운영 중인 서버에 악성코드를 실시간으로 탐지하고 격리 및 삭제 조치함으로써 사용자의 서비스가 안정적으로 운영될 수 있도록 지원합니다. 제공하는 기능은 다음과 같습니다.  •	바이러스, 스파이웨어의 격리 및 삭제  •	악성코드 의심 이벤트 발생 시 분석 보고서 제공  •	Windows/Linux용 서버 백신 제공  •	특정 파일 및 폴더에 대한 예외 처리 제공  •	최신 탐지 패턴 자동 업데이트  •	네이버 클라우드 플랫폼 콘솔에서 탐지 정보 확인 및 대시보드 제공  •	주간, 월간 보고서 제공  참고  Anti-Virus 백신 패턴은 매일 새벽 1시에 업데이트되며, 실시간 모니터링에 즉시 반영됩니다.  Anti-DDoS(V2)  사용자의 서비스로 인입되는 DDoS 공격을 24시간 365일 모니터링하여 탐지 및 차단함으로써 사용자의 서비스가 안정적으로 운영될 수 있도록 지원합니다. Full Packet Analysis 방식으로 빠르고 정확한 공격 탐지가 가능합니다. 제공하는 기능은 다음과 같습니다.  •	다단계 필터를 통한 다양한 유형의 DDoS 공격으로부터 보호  •	사용자별 특화된 보호 대상(Zone)을 생성하여 별도 정책으로 공격을 감지  •	사용자 특화 공격에 대한 분석 및 차단 룰 생성, 등록을 지원  •	정상적인 대량 트래픽을 유발하는 Source IP(NAT IP) 별도 관리 및 오탐 방지  •	학습을 통한 사용자 맞춤형 임계치 설정 제공  •	주간, 월간 보고서 제공  WAF(V2)  웹 공격을 전문적으로 탐지하고 방어합니다. HTTP, HTTPS의 웹 기반 트래픽을 모니터링하여 사용자의 웹 서비스로 공격이 인입될 경우 WAF 전용 솔루션을 통해 탐지하고 방어함으로써 즉각적인 대응이 가능하도록 지원합니다. VPC 환경에서 WAF는 Reverse Proxy 방식으로 사용자별 별도의 WAF 플랫폼을 제공하며, 안정적인 서비스를 위해 기본적으로 이중화 구조를 갖추고 있습니다. WAF VM과 사용자 서비스 Load Balancer 간의 통신은 HTTP 80 port 공인 통신을 사용합니다.  위 내용을 토대로 VPC 환경에서의 WAF 서비스 구성을 도식화하면 다음과 같습니다.    WAF는 기본적으로 탐지 모드와 차단 모드로 운영됩니다. 약 1개월 동안 탐지 모드로 운영한 다음 탐지 이벤트를 분석하여 차단 정책과 차단 모드 변경 일정을 사용자에게 제안하는 방식입니다. 이러한 방식으로 인해 탐지 모드로 운영되는 동안 네이버 클라우드 플랫폼 콘솔에서는 확인되는 로그는 없으며, 차단 모드로 변경된 후 차단된 로그만 제공하게 됩니다.  WAF에서 제공하는 기능은 다음과 같습니다.  •	접근 권한 취약점 탐지 및 차단  •	암호화 오류 탐지 및 차단  •	보안 설정 오류 탐지 및 차단  •	어플리케이션 취약점 탐지 및 차단  •	SSRF, XSS, CSRF, Injection 탐지 및 차단  •	Cookie 변조 및 도용 방지 등 다양한 웹 공격 탐지 및 차단  •	고객사 환경에 적합한 차단 정책 설정 및 관리  •	IP 및 URL 예외 기능 제공  •	주기적인 보안 정책 업데이트 제공  •	네이버 클라우드 플랫폼 콘솔에서 차단 정보 확인 및 대시보드 제공  •	주간, 월간 보고서 제공  IPS(V2)  호스트 기반의 Inbound, Outbound 트래픽을 24시간 365일 모니터링하여 의심스러운 활동을 탐지하고 차단하여 사용자의 서비스를 안전하게 운영될 수 있도록 지원합니다. IPS는 기본적으로 탐지 모드와 차단 모드로 운영됩니다. 약 1개월 동안 탐지 모드로 운영한 다음 탐지 이벤트를 분석하여 차단 정책과 차단 모드 변경 일정을 사용자에게 제안하는 방식입니다. 이러한 방식으로 인해 탐지 모드로 운영되는 동안 네이버 클라우드 플랫폼 콘솔에서는 확인되는 로그는 없으며, 차단 모드로 변경된 후 차단된 로그만 제공하게 됩니다.  IPS에서 제공하는 기능은 다음과 같습니다.  •	운영체제별, 애플리케이션별, 서버 용도별 맞춤형 탐지 및 차단 정책 기능 제공  •	가상 패치(virtual patching) 제공을 통해 취약한 버전의 애플리케이션이 패치될 때까지 시스템을 보호하여 제로데이 공격으로부터 VM 보호  •	IPS 탐지 및 차단 정책의 주기적인 업데이트  •	호스트의 애플리케이션에 대해 주기적인 스캔 및 탐지 정책 적용을 통해 취약점으로부터 VM 보호  •	네이버 클라우드 플랫폼 콘솔에서 차단 정보 확인 및 대시보드 제공  •	주간, 월간 보고서 제공  Classic  Classic 환경에서 Security Monitoring Managed가 제공하는 IDS, Anti-Virus, Anti-DDoS, WAF, IPS 기능을 설명합니다.  IDS(V1)  VPC 환경의 IDS 지원 내용과 동일합니다. 이 페이지의 VPC > IDS(V2)를 참조해 주십시오.  Anti-Virus(V1)  VPC 환경의 Anti-Virus 지원 내용과 동일합니다. 이 페이지의 VPC > Anti-Virus(V2)를 참조해 주십시오.  Anti-DDoS(V1)  VPC 환경의 Anti-DDoS 지원 내용과 동일합니다. 이 페이지의 VPC > Anti-DDoS(V2)를 참조해 주십시오.  WAF(V1)  웹 공격을 전문적으로 탐지하고 방어합니다. HTTP, HTTPS의 웹 기반 트래픽을 모니터링하여 사용자의 웹 서비스로 공격이 인입될 경우 WAF 전용 솔루션을 통해 탐지하고 방어함으로써 즉각적인 대응이 가능하도록 지원합니다. WAF는 기본적으로 탐지 모드와 차단 모드로 운영됩니다. 약 1개월 동안 탐지 모드로 운영한 다음 탐지 이벤트를 분석하여 차단 정책과 차단 모드 변경 일정을 사용자에게 제안하는 방식입니다. 이러한 방식으로 인해 탐지 모드로 운영되는 동안 네이버 클라우드 플랫폼 콘솔에서는 확인되는 로그는 없으며, 차단 모드로 변경된 후 차단된 로그만 제공하게 됩니다.  WAF에서 제공하는 기능은 다음과 같습니다.  •	접근 권한 취약점 탐지 및 차단  •	암호화 오류 탐지 및 차단  •	보안 설정 오류 탐지 및 차단  •	어플리케이션 취약점 탐지 및 차단  •	SSRF, XSS, CSRF, Injection 탐지 및 차단  •	Cookie 변조 및 도용 방지 등 다양한 웹 공격 탐지 및 차단  •	고객사 환경에 적합한 차단 정책 설정 및 관리  •	IP 및 URL 예외 기능 제공  •	주기적인 보안 정책 업데이트 제공  •	네이버 클라우드 플랫폼 콘솔에서 차단 정보 확인 및 대시보드 제공  •	주간, 월간 보고서 제공  IPS(V1)  네트워크 기반의 Inbound, Outbound 트래픽을 24시간 365일 모니터링하여 의심스러운 활동을 탐지하고 차단하여 사용자의 서비스를 안전하게 운영될 수 있도록 지원합니다. IPS는 기본적으로 탐지 모드와 차단 모드로 운영됩니다. 약 1개월 동안 탐지 모드로 운영한 다음 탐지 이벤트를 분석하여 차단 정책과 차단 모드 변경 일정을 사용자에게 제안하는 방식입니다. 이러한 방식으로 인해 탐지 모드로 운영되는 동안 네이버 클라우드 플랫폼 콘솔에서는 확인되는 로그는 없으며, 차단 모드로 변경된 후 차단된 로그만 제공하게 됩니다.  IPS에서 제공하는 기능은 다음과 같습니다.  •	실시간 트래픽 분석을 통해서 악의적인 유해 트래픽 탐지 차단  •	사용자별 차단 정책 제공  o	시그니처 기반 방어  o	Application 방어  o	프로토콜 기반 방어  o	도메인 차단  o	유해 사이트/URL 기반 차단  •	패턴 기반의 차단 예외 처리 제공  •	IP 차단 예외 처리 제공  •	IPS 탐지 및 차단 정책의 주기적인 업데이트  •	네이버 클라우드 플랫폼 콘솔에서 차단 정보 확인 및 대시보드 제공  •	주간, 월간 보고서 제공"
                }
           ]

@app.get("/rag_test2")
async def get_rag_test(
    category: Optional[str] = Query(None, description="Location of the rental car")
) -> List[dict]:
    filtered_rag = rag_data2

    if category:
        filtered_rag = [rag for rag in filtered_rag if rag["category"] == category]
    return filtered_rag


#240226 테스트
new_books = [    {
        "title": "위대한 개츠비",
        "year": 1925,
        "country_code": 1,
        "author": "프란시스 스콧 피츠제럴드",
        "publisher": "차이크",
        "rating": 8.9,
        "price": 15000,
        "genre_code": 1,
        "reviews": ["로맨틱한 분위기가 가득한 명작", "최고의 소설 중 하나"]
    },
    {
        "title": "1984",
        "year": 1949,
        "country_code": 1,
        "author": "조지 오웰",
        "publisher": "한국출판사",
        "rating": 9.2,
        "price": 12000,
        "genre_code": 1,
        "reviews": ["거장의 예언, 끝없는 경고", "현실적인 비전"]
    },
    {
        "title": "미움받을 용기",
        "year": 2013,
        "country_code": 81,
        "author": "기히로 시모노",
        "publisher": "북하우스",
        "rating": 8.5,
        "price": 18000,
        "genre_code": 1,
        "reviews": ["자신을 다시 발견하는 여정", "위로와 용기를 주는 책"]
    },
    {
        "title": "반지의 제왕",
        "year": 1954,
        "country_code": 1,
        "author": "J.R.R. 톨킨",
        "publisher": "팬텀",
        "rating": 9.8,
        "price": 25000,
        "genre_code": 1,
        "reviews": ["환상의 세계로 초대하는 대작", "마법같은 모험"]
    },
    {
        "title": "죽은 시인의 사회",
        "year": 1989,
        "country_code": 1,
        "author": "피터 위어",
        "publisher": "대한출판사",
        "rating": 9.0,
        "price": 16000,
        "genre_code": 1,
        "reviews": ["자유와 열정을 논하는 명작", "파워풀한 메시지"]
    },
    {
        "title": "동물농장",
        "year": 1945,
        "country_code": 1,
        "author": "조지 오웰",
        "publisher": "로지",
        "rating": 8.7,
        "price": 11000,
        "genre_code": 1,
        "reviews": ["유쾌하면서도 경쾌한 이야기", "사회 비판의 걸작"]
    },
    {
        "title": "토지",
        "year": 1935,
        "country_code": 82,
        "author": "박경리",
        "publisher": "현대문학",
        "rating": 9.5,
        "price": 20000,
        "genre_code": 1,
        "reviews": ["한국 문학의 걸작", "희망과 우정의 이야기"]
    },
    {
        "title": "데미안",
        "year": 1919,
        "country_code": 1,
        "author": "헤르만 헤세",
        "publisher": "서양문고",
        "rating": 8.8,
        "price": 17000,
        "genre_code": 1,
        "reviews": ["내면의 탐색과 성장", "청춘의 명작"]
    },
    {
        "title": "사랑의 불시착",
        "year": 2016,
        "country_code": 82,
        "author": "박지은",
        "publisher": "샘터",
        "rating": 9.3,
        "price": 22000,
        "genre_code": 1,
        "reviews": ["감동과 재미를 모두 잡은 대작", "눈을 뗄 수 없는 몰입도"]
    },
    {
        "title": "빨간 머리 앤",
        "year": 1908,
        "country_code": 1,
        "author": "루시 모드 몽고메리",
        "publisher": "문학동네",
        "rating": 8.6,
        "price": 13000,
        "genre_code": 1,
        "reviews": ["꿈과 용기의 이야기", "사랑스러운 캐릭터들"]
    },
        {
        "title": "꽃을 보듯 너를 본다",
        "year": 1992,
        "country_code": 82,
        "author": "나태주",
        "publisher": "문학동네",
        "rating": 9.2,
        "price": 16000,
        "genre_code": 2,
        "reviews": ["감성을 자극하는 시집", "시를 통해 세상을 본다"]
    },
    {
        "title": "어떻게 말해줘야 할까",
        "year": 2018,
        "country_code": 82,
        "author": "윤정비",
        "publisher": "시인정글",
        "rating": 9.0,
        "price": 18000,
        "genre_code": 2,
        "reviews": ["마음을 담은 시의 향연", "어떤 말로 표현할까 고민되는 감정을 담은 시"]
    },
    {
        "title": "우리 집에 가는 길",
        "year": 2005,
        "country_code": 82,
        "author": "하태완",
        "publisher": "샘터",
        "rating": 8.8,
        "price": 15000,
        "genre_code": 2,
        "reviews": ["일상의 아름다움을 느낄 수 있는 시집", "마음이 따뜻해지는 시"]
    },
    {
        "title": "내 마음의 숲",
        "year": 2010,
        "country_code": 82,
        "author": "정호승",
        "publisher": "행복한 어린이",
        "rating": 8.5,
        "price": 14000,
        "genre_code": 2,
        "reviews": ["힐링되는 시집", "자연과 함께하는 시"]
    },
    {
        "title": "봄이 오나요",
        "year": 2015,
        "country_code": 82,
        "author": "이해인",
        "publisher": "봄봄",
        "rating": 9.5,
        "price": 20000,
        "genre_code": 2,
        "reviews": ["봄의 따뜻함을 느낄 수 있는 시집", "꽃 향기처럼 달콤한 시"]
    },
    {
        "title": "오늘의 기분",
        "year": 2008,
        "country_code": 82,
        "author": "이상철",
        "publisher": "무드",
        "rating": 8.9,
        "price": 17000,
        "genre_code": 2,
        "reviews": ["하루를 마무리하는 시집", "감성을 자극하는 달콤한 시"]
    },
    {
        "title": "너의 뒤에 서서",
        "year": 2019,
        "country_code": 82,
        "author": "손히",
        "publisher": "서현",
        "rating": 9.2,
        "price": 19000,
        "genre_code": 2,
        "reviews": ["사랑을 담은 시집", "눈물과 웃음을 함께하는 시"]
    },
    {
        "title": "한 뼘의 자유",
        "year": 2002,
        "country_code": 82,
        "author": "홍현희",
        "publisher": "오늘의 책",
        "rating": 8.7,
        "price": 18000,
        "genre_code": 2,
        "reviews": ["자유로움을 노래하는 시집", "희망의 메시지를 전하는 시"]
    },
    {
        "title": "여름날",
        "year": 2017,
        "country_code": 82,
        "author": "박희진",
        "publisher": "희망",
        "rating": 9.0,
        "price": 16000,
        "genre_code": 2,
        "reviews": ["여름의 시원함을 담은 시집", "더운 여름을 시원하게 해주는 시"]
    },
    {
        "title": "소리없는 아우성",
        "year": 2007,
        "country_code": 82,
        "author": "정재승",
        "publisher": "소나무",
        "rating": 8.8,
        "price": 15000,
        "genre_code": 2,
        "reviews": ["감동과 울림을 주는 시집", "작은 소리에서 큰 울림을 느끼는 시"]
    },
    {
        "title": "김정은의 불편한 진실",
        "year": 2020,
        "country_code": 82,
        "author": "이선희",
        "publisher": "한국출판사",
        "rating": 8.7,
        "price": 18000,
        "genre_code": 3,
        "reviews": ["북한에 대한 새로운 시각을 제시하는 책", "김정은의 인간적인 면을 다룬 책"]
    },
    {
        "title": "여행의 이유",
        "year": 2015,
        "country_code": 82,
        "author": "김영하",
        "publisher": "북한산",
        "rating": 9.1,
        "price": 20000,
        "genre_code": 3,
        "reviews": ["여행의 진정한 의미를 찾아가는 여정", "인생을 바꿀 수 있는 책"]
    },
    {
        "title": "삶과 죽음에 대하여",
        "year": 2018,
        "country_code": 82,
        "author": "조용필",
        "publisher": "다산북스",
        "rating": 8.8,
        "price": 17000,
        "genre_code": 3,
        "reviews": ["인생의 가치에 대해 다시 생각하게 만드는 책", "삶과 죽음에 대한 깊은 인사이트를 제공하는 책"]
    },
    {
        "title": "우리들의 무지개",
        "year": 2019,
        "country_code": 82,
        "author": "이영철",
        "publisher": "모아씨엔씨",
        "rating": 8.9,
        "price": 19000,
        "genre_code": 3,
        "reviews": ["다양성과 포용에 대한 메시지를 전하는 책", "우리 사회의 미래를 엿보는 책"]
    },
    {
        "title": "나의 하루",
        "year": 2017,
        "country_code": 82,
        "author": "서울시립",
        "publisher": "세계문학",
        "rating": 8.6,
        "price": 16000,
        "genre_code": 3,
        "reviews": ["일상의 아름다움을 발견하는 책", "작은 것들에 감사하는 마음을 심는 책"]
    },
    {
        "title": "무모한 도전",
        "year": 2016,
        "country_code": 82,
        "author": "김영민",
        "publisher": "노란별",
        "rating": 8.5,
        "price": 15000,
        "genre_code": 3,
        "reviews": ["포기하지 않는 열정을 보여주는 책", "성공과 실패 사이의 비밀을 말해주는 책"]
    },
    {
        "title": "한 걸음 더",
        "year": 2021,
        "country_code": 82,
        "author": "강호동",
        "publisher": "성안당",
        "rating": 8.4,
        "price": 14000,
        "genre_code": 4,
        "reviews": ["자기계발의 길을 찾아가는 책", "한 발 더 나아가는 비결을 알려주는 책"]
    },
        {
        "title": "부의 시나리오",
        "year": 2018,
        "country_code": 1,
        "author": "이제니",
        "publisher": "성인당",
        "rating": 8.9,
        "price": 18000,
        "genre_code": 4,
        "reviews": ["부자가 되기 위한 실전 가이드", "재무 교육의 바이블"]
    },
    {
        "title": "죽음에 관하여",
        "year": 1999,
        "country_code": 1,
        "author": "베르테르스만",
        "publisher": "문학동네",
        "rating": 9.2,
        "price": 20000,
        "genre_code": 4,
        "reviews": ["인생의 가치를 깊이 생각하게 하는 책", "생의 진정한 의미를 찾아가는 여정"]
    },
    {
        "title": "코스모스",
        "year": 1980,
        "country_code": 1,
        "author": "칼 세이건",
        "publisher": "사이언스북스",
        "rating": 8.8,
        "price": 17000,
        "genre_code": 3,
        "reviews": ["우주에 대한 감탄을 자아내는 책", "과학을 통해 세계를 이해하는 철학적인 접근"]
    },
    {
        "title": "인생의 가치",
        "year": 2015,
        "country_code": 1,
        "author": "팀 클라인",
        "publisher": "빅픽처스프레스",
        "rating": 9.0,
        "price": 19000,
        "genre_code": 4,
        "reviews": ["인생의 방향을 재정립하는 책", "진정한 행복의 길을 찾아가는 지침서"]
    },
    {
        "title": "내가 좋아하는 것만 남기고, 나머지는 모두 정리하라",
        "year": 2019,
        "country_code": 1,
        "author": "미노스",
        "publisher": "현대경제사",
        "rating": 8.7,
        "price": 16000,
        "genre_code": 4,
        "reviews": ["간소화된 삶을 위한 지혜", "불필요한 것을 버리고 진정한 가치를 찾아가는 여정"]
    },
    {
        "title": "성공하는 사람들의 7가지 습관",
        "year": 2010,
        "country_code": 1,
        "author": "스티븐 R. 코비",
        "publisher": "시네21",
        "rating": 8.5,
        "price": 15000,
        "genre_code": 4,
        "reviews": ["성공의 비결을 알려주는 베스트셀러", "변화와 성장을 이끌어내는 실용적인 가이드북"]
    },
    {
        "title": "행복의 운",
        "year": 2005,
        "country_code": 1,
        "author": "조슈아 워튼",
        "publisher": "한국경제사",
        "rating": 8.4,
        "price": 14000,
        "genre_code": 4,
        "reviews": ["인생의 목표를 달성하는 법을 알려주는 책", "내면의 우주적인 행복을 발견하는 여정"]
    }
]

@app.get("/books/search")
async def search_books(
    genre_code: Optional[int] = None,
    country_code: Optional[int] = None,
    author: Optional[str] = None,
    publisher: Optional[str] = None,
    rating: Optional[float] = None,
    min_price: Optional[int] = None,
    max_price: Optional[int] = None,
    title: Optional[str] = None,
    keyword: Optional[str] = None
):
    # 필터링된 결과를 저장할 리스트
    filtered_books = []
    
    for book in new_books:
        # 각 필터에 대한 조건 확인
        if (
            (genre_code is None or book['genre_code'] == genre_code) and
            (country_code is None or book['country_code'] == country_code) and
            (author is None or author.lower() in book['author'].lower()) and
            (publisher is None or publisher.lower() in book['publisher'].lower()) and
            (rating is None or book['rating'] >= rating) and
            (min_price is None or book["price"] >= min_price) and
            (max_price is None or book["price"] <= max_price) and
            (title is None or (title.lower() in book['title'].lower()))
        ):
            # keyword가 None이 아닌 경우에만 검색
            if keyword is not None:
                # 키워드 검색 결과 저장
                keyword_results = [keyword.lower() in ' '.join(book['reviews']).lower() for keyword in keyword.split(',')]
                # 모든 키워드가 만족하는지 확인
                if all(keyword_results):
                    filtered_books.append(book)
            else:
                filtered_books.append(book)
            
            # 호출 개수 제한
            if len(filtered_books) >= 10:
                break
    
    return filtered_books


new_movies = [
    {
        "title": "기생충",
        "year": 2019,
        "country_code": 82,
        "director": "봉준호",
        "actors": ["송강호", "이선균"],
        "rating": 8.6,
        "audience_count": 10000000,
        "genre_code": 6,
        "reviews": ["현실을 반영한 작품", "봉준호 감독의 뛰어난 연출"]
    },
    {
        "title": "올드보이",
        "year": 2003,
        "country_code": 82,
        "director": "박찬욱",
        "actors": ["최민식", "유지태"],
        "rating": 8.4,
        "audience_count": 5000000,
        "genre_code": 2,
        "reviews": ["긴박한 스토리", "완벽한 연출과 연기"]
    },
    {
        "title": "마더",
        "year": 2009,
        "country_code": 82,
        "director": "봉준호",
        "actors": ["김혜자", "원빈"],
        "rating": 8.1,
        "audience_count": 3000000,
        "genre_code": 5,
        "reviews": ["감정을 자극하는 작품", "봉준호 감독의 역작"]
    },
    {
        "title": "괴물",
        "year": 2006,
        "country_code": 82,
        "director": "봉준호",
        "actors": ["송강호", "박해일"],
        "rating": 7.8,
        "audience_count": 4000000,
        "genre_code": 5,
        "reviews": ["모든 것이 완벽한 영화", "최고의 엔딩"]
    },
    {
        "title": "택시운전사",
        "year": 2017,
        "country_code": 82,
        "director": "장훈",
        "actors": ["송강호", "토마스 크레취만"],
        "rating": 8.0,
        "audience_count": 7000000,
        "genre_code": 5,
        "reviews": ["감동적인 이야기", "우리의 역사를 되새기게 하는 작품"]
    },
    {
        "title": "범죄와의 전쟁: 나쁜놈들 전성시대",
        "year": 2012,
        "country_code": 82,
        "director": "윤종빈",
        "actors": ["최민식", "하정우"],
        "rating": 7.9,
        "audience_count": 6000000,
        "genre_code": 2,
        "reviews": ["긴장감 넘치는 스토리", "연기력이 돋보이는 작품"]
    },
    {
        "title": "아가씨",
        "year": 2016,
        "country_code": 82,
        "director": "박찬욱",
        "actors": ["김민희", "김태리"],
        "rating": 8.3,
        "audience_count": 4500000,
        "genre_code": 6,
        "reviews": ["비정한 세계를 그린 작품", "박찬욱 감독의 아름다운 영상"]
    },
    {
        "title": "좋은 놈, 나쁜 놈, 이상한 놈",
        "year": 2008,
        "country_code": 82,
        "director": "김지운",
        "actors": ["이선균", "이정재"],
        "rating": 7.5,
        "audience_count": 5500000,
        "genre_code": 1,
        "reviews": ["한국 영화의 역사를 다시 쓴 작품", "유쾌한 액션과 긴장감 있는 스토리"]
    },
    {
        "title": "타짜",
        "year": 2006,
        "country_code": 82,
        "director": "최동훈",
        "actors": ["최승현", "박신양"],
        "rating": 7.6,
        "audience_count": 6500000,
        "genre_code": 2,
        "reviews": ["도박 소재의 재미있는 영화", "역동적인 연출과 스토리"]
    },
        {
        "title": "해운대",
        "year": 2009,
        "country_code": 82,
        "director": "윤제균",
        "actors": ["하정우", "강동원"],
        "rating": 7.8,
        "audience_count": 4200000,
        "genre_code": 5,
        "reviews": ["스릴 넘치는 해변 액션", "감동적인 우정 이야기"]
    },
    {
        "title": "내부자들",
        "year": 2015,
        "country_code": 82,
        "director": "우민호",
        "actors": ["이병헌", "조승우"],
        "rating": 8.2,
        "audience_count": 4800000,
        "genre_code": 2,
        "reviews": ["긴박한 범죄 스릴러", "뛰어난 연기력"]
    },
    {
        "title": "광복절 특사",
        "year": 2010,
        "country_code": 82,
        "director": "신재영",
        "actors": ["송강호", "류승룡"],
        "rating": 7.6,
        "audience_count": 3700000,
        "genre_code": 5,
        "reviews": ["극적인 역사 드라마", "훈훈한 가족 이야기"]
    },
    {
        "title": "밀정",
        "year": 2016,
        "country_code": 82,
        "director": "김지운",
        "actors": ["송강호", "공유"],
        "rating": 7.9,
        "audience_count": 5300000,
        "genre_code": 2,
        "reviews": ["일제 강점기의 은밀한 스파이 이야기", "긴장감 넘치는 전개"]
    },
    {
        "title": "아수라",
        "year": 2016,
        "country_code": 82,
        "director": "김성수",
        "actors": ["정우성", "황정민"],
        "rating": 8.0,
        "audience_count": 5900000,
        "genre_code": 2,
        "reviews": ["폭력과 복수의 소재를 다룬 작품", "긴박한 액션과 연기"]
    },
    {
        "title": "백두산",
        "year": 2019,
        "country_code": 82,
        "director": "이해준",
        "actors": ["이병헌", "하정우"],
        "rating": 7.7,
        "audience_count": 4600000,
        "genre_code": 5,
        "reviews": ["북한을 배경으로 한 인간 드라마", "감동적인 결말"]
    },
    {
        "title": "신과함께: 죄와 벌",
        "year": 2017,
        "country_code": 82,
        "director": "김용화",
        "actors": ["하정우", "차태현"],
        "rating": 8.1,
        "audience_count": 7100000,
        "genre_code": 5,
        "reviews": ["죽음을 다룬 판타지 영화", "인생과 죽음에 대한 깊은 사유"]
    },
    {
        "title": "베테랑",
        "year": 2015,
        "country_code": 82,
        "director": "류승완",
        "actors": ["황정민", "유아인"],
        "rating": 8.3,
        "audience_count": 6400000,
        "genre_code": 2,
        "reviews": ["타격감 넘치는 액션 스릴러", "사회 비판적 메시지"]
    },
    {
        "title": "아저씨",
        "year": 2010,
        "country_code": 82,
        "director": "이정범",
        "actors": ["원빈", "김새론"],
        "rating": 7.9,
        "audience_count": 5000000,
        "genre_code": 2,
        "reviews": ["한국판 복수 액션물", "긴장감 넘치는 전개"]
    },
    {
        "title": "광해, 왕이 된 남자",
        "year": 2012,
        "country_code": 82,
        "director": "이준익",
        "actors": ["이병헌", "한효주"],
        "rating": 7.7,
        "audience_count": 8000000,
        "genre_code": 1,
        "reviews": ["사극의 재미를 만끽할 수 있는 작품", "화려한 영상미"]
    },
    {
        "title": "어벤져스: 엔드게임",
        "year": 2019,
        "country_code": 1,
        "director": "안소니 루소, 조 루소",
        "actors": ["로버트 다우니 주니어", "크리스 에반스"],
        "rating": 8.4,
        "audience_count": 12000000,
        "genre_code": 4,
        "reviews": ["마블의 히어로들의 대미 장면", "감동적인 결말"]
    },
    {
        "title": "인셉션",
        "year": 2010,
        "country_code": 1,
        "director": "크리스토퍼 놀란",
        "actors": ["레오나르도 디카프리오", "조셉 고든 레빗"],
        "rating": 8.8,
        "audience_count": 8500000,
        "genre_code": 4,
        "reviews": ["꿈 속의 꿈을 그린 사이킷 액션", "뛰어난 시나리오와 비주얼"]
    },
    {
        "title": "다크 나이트",
        "year": 2008,
        "country_code": 1,
        "director": "크리스토퍼 놀란",
        "actors": ["크리스찬 베일", "히스 레저"],
        "rating": 9.0,
        "audience_count": 9000000,
        "genre_code": 4,
        "reviews": ["조커의 뛰어난 연기", "어둠 속의 영웅"]
    },
    {
        "title": "포레스트 검프",
        "year": 1994,
        "country_code": 1,
        "director": "로버트 저메키스",
        "actors": ["톰 행크스", "로빈 라이트"],
        "rating": 8.8,
        "audience_count": 7000000,
        "genre_code": 5,
        "reviews": ["감동적인 우정 이야기", "삶의 의미를 다시 생각하게 함"]
    },
    {
        "title": "인터스텔라",
        "year": 2014,
        "country_code": 1,
        "director": "크리스토퍼 놀란",
        "actors": ["매튜 맥커너히", "앤 해서웨이"],
        "rating": 8.6,
        "audience_count": 6500000,
        "genre_code": 4,
        "reviews": ["우주 여행을 다룬 SF 스토리", "시간 여행의 개념"]
    },
    {
        "title": "레옹",
        "year": 1994,
        "country_code": 1,
        "director": "뤽 베송",
        "actors": ["장 르노", "나탈리 포트만"],
        "rating": 8.5,
        "audience_count": 6000000,
        "genre_code": 2,
        "reviews": ["소년과 킬러의 독특한 우정", "액션과 감동의 조화"]
    },
    {
        "title": "인사이드 아웃",
        "year": 2015,
        "country_code": 1,
        "director": "피트 닥터, 론니 델 카르멘",
        "actors": ["에이미 포엘러", "필리스 스미스"],
        "rating": 8.2,
        "audience_count": 7500000,
        "genre_code": 5,
        "reviews": ["감정의 세계를 그린 애니메이션", "어른들도 공감하는 메시지"]
    },
    {
        "title": "셔터 아일랜드",
        "year": 2010,
        "country_code": 1,
        "director": "마틴 스콜세지",
        "actors": ["레오나르도 디카프리오", "마크 러팔로"],
        "rating": 8.1,
        "audience_count": 6000000,
        "genre_code": 4,
        "reviews": ["환상적인 섬 모험", "의미 있는 결말"]
    },
    {
        "title": "쇼생크 탈출",
        "year": 1994,
        "country_code": 1,
        "director": "프랭크 다라본트",
        "actors": ["팀 로빈스", "모건 프리먼"],
        "rating": 9.3,
        "audience_count": 8000000,
        "genre_code": 2,
        "reviews": ["감옥에서의 탈출 이야기", "삶과 자유에 대한 깊은 이야기"]
    },
    {
        "title": "캐스트 어웨이",
        "year": 2000,
        "country_code": 1,
        "director": "로버트 저메키스",
        "actors": ["톰 행크스", "헬렌 헌트"],
        "rating": 7.8,
        "audience_count": 5500000,
        "genre_code": 5,
        "reviews": ["무인도에서의 생존기", "우정과 결단의 이야기"]
    },
    {
        "title": "레디 플레이어 원",
        "year": 2018,
        "country_code": 1,
        "director": "스티븐 스필버그",
        "actors": ["테이크 액시트", "올리비아 쿡"],
        "rating": 7.5,
        "audience_count": 6000000,
        "genre_code": 4,
        "reviews": ["가상 현실을 다룬 SF 모험", "팝컬처의 풍부한 참조"]
    },
    {
        "title": "캐치 미 이프 유 캔",
        "year": 2002,
        "country_code": 1,
        "director": "스티븐 스필버그",
        "actors": ["레오나르도 디카프리오", "톰 행크스"],
        "rating": 8.1,
        "audience_count": 7000000,
        "genre_code": 1,
        "reviews": ["슬픈 장면과 따뜻한 감동", "캐치볼 게임을 통한 성장 이야기"]
    },
    {
        "title": "그래비티",
        "year": 2013,
        "country_code": 1,
        "director": "알폰소 쿠아론",
        "actors": ["샌드라 블록", "조지 클루니"],
        "rating": 7.7,
        "audience_count": 5500000,
        "genre_code": 4,
        "reviews": ["우주 공간에서의 사람의 생존을 그린 SF 스릴러", "진짜감 있는 비주얼"]
    },
    {
        "title": "터미네이터 2:오리지널",
        "year": 1991,
        "country_code": 1,
        "director": "제임스 카메론",
        "actors": ["아놀드 슈워제네거", "린다 해밀턴"],
        "rating": 8.5,
        "audience_count": 8000000,
        "genre_code": 2,
        "reviews": ["로봇의 액션 시퀀스", "과거와 미래의 충돌"]
    },
    {
        "title": "인디아나 존스: 마법의 석호",
        "year": 1984,
        "country_code": 1,
        "director": "스티븐 스필버그",
        "actors": ["해리슨 포드", "캐럴라인 무클로드"],
        "rating": 8.4,
        "audience_count": 7500000,
        "genre_code": 2,
        "reviews": ["모험과 액션의 대표적인 시리즈", "고전적인 어드벤처"]
    },
    {
        "title": "피어스트 킹덤",
        "year": 1993,
        "country_code": 1,
        "director": "스티븐 스필버그",
        "actors": ["사무엘 L. 잭슨", "리암 니슨"],
        "rating": 7.6,
        "audience_count": 6000000,
        "genre_code": 4,
        "reviews": ["공룡의 세계를 그린 전투 액션", "흥미진진한 모험"]
    },
    {
        "title": "레인 맨",
        "year": 1988,
        "country_code": 1,
        "director": "배리 레빈슨",
        "actors": ["더스틴 호프먼", "톰 크루즈"],
        "rating": 8.0,
        "audience_count": 7000000,
        "genre_code": 5,
        "reviews": ["조수를 따라가는 두 남자의 이야기", "정신병의 이해와 용기"]
    },
    {
        "title": "크루엘라",
        "year": 2021,
        "country_code": 1,
        "director": "크레이그 질레스피",
        "actors": ["엠마 스톤", "엠마 톰슨"],
        "rating": 7.4,
        "audience_count": 6500000,
        "genre_code": 6,
        "reviews": ["디즈니 악당의 미래를 보여주는 영화", "패션과 반항의 여정"]
    },
    {
        "title": "아메리칸 뷰티",
        "year": 1999,
        "country_code": 1,
        "director": "샘 멘데스",
        "actors": ["케빈 스페이시", "안네트 베닝"],
        "rating": 8.3,
        "audience_count": 6000000,
        "genre_code": 1,
        "reviews": ["중년의 위기와 욕망을 그린 블랙 코미디", "인간 심리의 다층적인 이해"]
    },
    {
        "title": "로건",
        "year": 2017,
        "country_code": 1,
        "director": "제임스 맨골드",
        "actors": ["휴 잭맨", "패트릭 스튜어트"],
        "rating": 8.1,
        "audience_count": 7000000,
        "genre_code": 2,
        "reviews": ["월버린의 마지막 이야기", "액션과 감동의 조화"]
    },
    {
        "title": "아마데우스",
        "year": 1984,
        "country_code": 1,
        "director": "밀로스 포르만",
        "actors": ["톰 훌스", "페이 브러스넌"],
        "rating": 8.3,
        "audience_count": 5500000,
        "genre_code": 6,
        "reviews": ["모차르트의 삶과 음악을 그린 작품", "명작 클래식"]
    },
    {
        "title": "라이프 이즈 비욘드",
        "year": 1999,
        "country_code": 1,
        "director": "프랭크 다라본트",
        "actors": ["짐 캐리", "에드 해리스"],
        "rating": 8.8,
        "audience_count": 7000000,
        "genre_code": 5,
        "reviews": ["현실과 환상이 교차하는 판타지 영화", "생각할 거리를 주는 작품"]
    },
    {
        "title": "테오와 마법의 성",
        "year": 2006,
        "country_code": 1,
        "director": "미켈란젤로 코르비니",
        "actors": ["리처드 해리스", "사이러스 벤"],
        "rating": 7.9,
        "audience_count": 6500000,
        "genre_code": 6,
        "reviews": ["어린이를 위한 판타지 모험", "마법과 용의 세계"]
    },
    {
        "title": "아마데우스: 최후의 소원",
        "year": 1988,
        "country_code": 1,
        "director": "밀로스 포르만",
        "actors": ["톰 훌스", "페이 브러스넌"],
        "rating": 8.0,
        "audience_count": 7000000,
        "genre_code": 6,
        "reviews": ["모차르트의 삶과 음악을 그린 작품", "감동적인 이야기"]
    },
    {
        "title": "레옹: 감독판",
        "year": 1996,
        "country_code": 1,
        "director": "뤽 베송",
        "actors": ["장 르노", "나탈리 포트만"],
        "rating": 8.7,
        "audience_count": 7500000,
        "genre_code": 2,
        "reviews": ["감독의 감정적인 집착", "더욱 깊어진 캐릭터 탐구"]
    },
    {
        "title": "이터널 선샤인",
        "year": 2004,
        "country_code": 1,
        "director": "미셸 공드리",
        "actors": ["진 캐리", "케이트 윈슬렛"],
        "rating": 8.3,
        "audience_count": 6000000,
        "genre_code": 5,
        "reviews": ["기억과 사랑의 이야기", "시간과 공간을 초월한 결말"]
    },
    {
        "title": "시간을 달리는 소녀",
        "year": 2006,
        "country_code": 81,
        "director": "시마무라 마모루",
        "actors": ["타카하시 미술", "카미시라이시 모네"],
        "rating": 8.4,
        "audience_count": 6500000,
        "genre_code": 6,
        "reviews": ["타임 트래블을 다룬 판타지 이야기", "감동과 여운의 메시지"]
    },
    {
        "title": "아포칼립토",
        "year": 1999,
        "country_code": 1,
        "director": "린다스 파르머",
        "actors": ["조지 클루니", "니콜 키드먼"],
        "rating": 7.8,
        "audience_count": 6000000,
        "genre_code": 4,
        "reviews": ["최후의 날을 그린 인류의 생존 이야기", "파괴와 희망의 대립"]
    }
]


@app.get("/movies/search")
async def search_movies(
    genre_code: Optional[int] = None,
    country_code: Optional[int] = None,
    director: Optional[str] = None,
    actor: Optional[str] = None,
    rating: Optional[float] = None,
    min_audience_count: Optional[int] = None,
    max_audience_count: Optional[int] = None,
    title: Optional[str] = None,
    keyword: Optional[str] = None
):
    # 필터링된 결과를 저장할 리스트
    filtered_movies = []
    
    for movie in new_movies:
        # 각 필터에 대한 조건 확인
        if (
            (genre_code is None or movie['genre_code'] == genre_code) and
            (country_code is None or movie['country_code'] == country_code) and
            (director is None or director.lower() in movie['director'].lower()) and
            (actor is None or actor.lower() in [actor.lower() for actor in movie['actors']]) and
            (rating is None or movie['rating'] >= rating) and
            (min_audience_count is None or movie["audience_count"] >= min_audience_count) and
            (max_audience_count is None or movie["audience_count"] <= max_audience_count) and
            (title is None or (title.lower() in movie['title'].lower()))
        ):
            # keyword가 None이 아닌 경우에만 검색
            if keyword is not None:
                # 키워드 검색 결과 저장
                keyword_results = [keyword.lower() in ' '.join(movie['reviews']).lower() for keyword in keyword.split(',')]
                # 모든 키워드가 만족하는지 확인
                if all(keyword_results):
                    filtered_movies.append(movie)
            else:
                filtered_movies.append(movie)
            
            # 호출 개수 제한
            if len(filtered_movies) >= 10:
                break
    
    return filtered_movies
##1004 test

# 가상의 데이터
data = [{"month": 10, "day": 23, "destination": "제주도", "class": "F", "price": 200000},
       {"month": 11, "day": 23, "destination": "제주도", "class": "F", "price": 200000},
        {"month": 12, "day": 23, "destination": "제주도", "class": "F", "price": 200000},
         {"month": 10, "day": 22, "destination": "제주도", "class": "F", "price": 200000}
          ,{"month": 11, "day": 22, "destination": "제주도", "class": "F", "price": 200000}
            ,{"month": 12, "day": 22, "destination": "제주도", "class": "F", "price": 200000}
            ,{"month": 9, "day": 22, "destination": "제주도", "class": "F", "price": 200000}
            ,{"month": 9, "day": 22, "destination": "제주도", "class": "E", "price": 100000}
            ,{"month": 9, "day": 21, "destination": "제주도", "class": "F", "price": 200000}]

# 필터링을 위한 엔드포인트 설정
@app.get("/filter_data")
async def filter_data(
    month: int = Query(None, description="Month (e.g., 10)"),
    day: int = Query(None, description="Day (e.g., 23)"),
    destination: str = Query(None, description="Destination"),
    class_type: str = Query(None, description="Class Type (e.g., F)")
):
    filtered_data = data

    # 월(month)에 대한 필터링
    if month is not None:
        filtered_data = [item for item in filtered_data if item["month"] == month]

    # 일(day)에 대한 필터링
    if day is not None:
        filtered_data = [item for item in filtered_data if item["day"] == day]

    # 목적지(destination)에 대한 필터링
    if destination is not None:
        filtered_data = [item for item in filtered_data if destination in item["destination"]]

    # 클래스(class)에 대한 필터링
    if class_type is not None:
        filtered_data = [item for item in filtered_data if item["class"] == class_type]

    return filtered_data

### 0823 test

@app.get("/0823test")
async def connect_test(
    query: str = Query(..., description="쿼리"),
    period: Optional[str] = Query(None, description="기간"),
    name: Optional[str] = Query(None, description="작성자 이름"),
    role: Optional[str] = Query(None, description="null을 사용"),
    space: Optional[str] = Query(None, description="null을 사용")
):
    result = '{source : "OSS", '
    
    if query is not None:
        result = result + 'query : "' + str(query) + '"'
    if period is not None:
        result = result + ', period : "' + str(period) + '"'
    else:
        result = result + ', period : "none"'
    if name is not None:
        result = result + ', name : "' + str(name) + '"'
    else:
        result = result + ', name : "none"'
    if role is not None:
        result = result + ', role : "' + str(role) + '"'
    else:
        result = result + ', role : "none"'
    if space is not None:
        result = result + ', space : "' + str(space) + '"}'
    else:
        result = result + ', space : "none"}'
    

    return result


### 0809 Update

swimming_cap_data = [
    ["르망고", "LGNSC61002144", "실리콘", True, False, 18000],
    ["스피도", "8-7098415349", "실리콘", False, True, 12000],
    ["후그", "SUC236", "코팅", True, False, 14000],
    ["스피도", "SE12050(K)", "메쉬", False, True, 8000],
    ["가나스윔", "PLAN SPAN CAP", "스판", False, False, 2500]
]

@app.get("/swimming_cap")
async def filter_swimming_cap(
    brand: Optional[str] = Query(None, description="브랜드 이름을 한글로 적어주세요 (ex. 르망고, 후그 등)"),
    name: Optional[str] = Query(None, description="상품명은 영어, 숫자를 이용해 적어주세요 (ex. LGNSC61002144, 8-7098415349 등)"),
    material: str = Query(..., description="재질을 한글로 적어주세요 (ex. 실리콘, 매쉬, 스판 등)"),
    patterTF: Optional[bool] = Query(None, description="패턴 여부를 알기 위해 패턴 있길 원하시면 True, 그렇지 않으시면 False를 적어주세요"),
    longHairTF: Optional[bool] = Query(None, description="긴머리용 여부를 알기 위해 긴머리용을 원하시면 True, 그렇지 않으시면 False를 적어주세요"),
    min_price: Optional[int] = Query(None, description="최소 가격(단위: 원)은 정수로 적어주세요"),
    max_price: Optional[int] = Query(None, description="최대 가격(단위: 원)은 정수로 적어주세요")
):
    filtered_data = []

    for item in swimming_cap_data:
        if (
            (brand is None or item[0] == brand) and
            (name is None or item[1] == name) and
            item[2] == material and
            (patterTF is None or item[3] == patterTF) and
            (longHairTF is None or item[4] == longHairTF) and
            (min_price is None or item[5] >= min_price) and
            (max_price is None or item[5] <= max_price)
        ):
            filtered_data.append({
                "brand": item[0],
                "name": item[1],
                "material": item[2],
                "patterTF": item[3],
                "longHairTF": item[4],
                "price": item[5]
            })

    return filtered_data


dog_step_data = [
    ["아르르", 1000022487, "슬라이드", 40, 72, 35, 39920],
    ["퍼핑", 1000002518, "슬라이드", 40, 60, 39, 109000],
    ["퍼핑", 1000017614, "스텝", 45, 95, 43, 159000],
    ["펫테일", 1000018770, "스텝", 38, 50, 28, 46900],
    ["스몰스터프", 1000003491, "스텝", 49, 58, 35, 211000]
]

@app.get("/dog_step")
async def filter_dog_step(
    brand: Optional[str] = Query(None, description="브랜드는 한글로 적어주세요 (ex. 아르르, 퍼핑)"),
    name: Optional[str] = Query(None, description="상품코드는 11자리 정수로 적어주세요 (ex. 1000022487)"),
    category: str = Query(..., description="찾으시는 강아지 계단의 카테고리를 한글로 적어주세요 (ex. 슬라이드, 스텝)"),
    width: Optional[float] = Query(None, description="가로 길이(단위: cm)는 실수로 적어주세요"),
    depth: Optional[float] = Query(None, description="세로 길이(단위: cm)는 실수로 적어주세요"),
    min_height: Optional[float] = Query(None, description="최소 높이(단위: cm)는 실수로 적어주세요"),
    max_height: Optional[float] = Query(None, description="최대 높이(단위: cm)는 실수로 적어주세요"),
    min_price: Optional[int] = Query(None, description="최소 가격(단위: 원)은 정수로 적어주세요"),
    max_price: Optional[int] = Query(None, description="최대 가격(단위: 원)은 정수로 적어주세요")
):
    filtered_data = []

    for item in dog_step_data:
        if (
            (brand is None or item[0] == brand) and
            (name is None or item[1] == name) and
            item[2] == category and
            (width is None or item[3] == width) and
            (depth is None or item[4] == depth) and
            (min_height is None or item[5] >= min_height) and
            (max_height is None or item[5] <= max_height) and
            (min_price is None or item[6] >= min_price) and
            (max_price is None or item[6] <= max_price)
        ):
            filtered_data.append({
                "brand": item[0],
                "name": item[1],
                "category": item[2],
                "width": item[3],
                "depth": item[4],
                "height": item[5],
                "price": item[6]
            })

    return filtered_data
    
kids_cloth_data = [
    ["뉴발란스 키즈", "NK9YC2403U", "반팔티", "면", 3, [90, 110, 130, 150], 35800],
    ["폴햄키즈", "PKD2UI3850", "반바지", "시어서커", 1, [100, 150], 28000],
    ["베베드피노", "BP22OS130", "잠옷세트", "면", 2, [95, 105, 120], 31500],
    ["소이빈", "SB3331DA", "나시", "면", 1, [120, 130, 140], 15000],
    ["지오다노 주니어", "273501", "긴팔티", "면", 3, [100, 110], 19250]
]

@app.get("/kids_cloth")
async def filter_kids_cloth(
    brand: Optional[str] = Query(None, description="브랜드를 한글로 적어주세요 (ex. 뉴발란스 키즈, 폴햄키즈)"),
    name: Optional[str] = Query(None, description="상품명을 영어대문자, 숫자를 이용해 적어주세요 (ex. NK9YC2403U, 273501)"),
    sort: str = Query(..., description="찾으시는 아동복 종류를 한글로 적어주세요 (ex. 티셔츠, 바지, 가디건)"),
    min_stretch: Optional[int] = Query(None, description="최소 신축성을 1~3 사이의 정수로 적어주세요", ge=1, le=3),
    max_stretch: Optional[int] = Query(None, description="최대 신축성을 1~3 사이의 정수로 적어주세요", ge=1, le=3),
    size: Optional[int] = Query(None, description="사이즈는 정수로 적어주세요 (ex. 90, 95, 100)"),
    min_price: Optional[int] = Query(None, description="최소 가격(단위: 원)은 정수로 적어주세요"),
    max_price: Optional[int] = Query(None, description="최대 가격(단위: 원)은 정수로 적어주세요")
):
    filtered_data = []

    for item in kids_cloth_data:
        stretch_mapping = {1: "낮음", 2: "보통", 3: "높음"}
        
        if (
            (brand is None or item[0] == brand) and
            (name is None or item[1] == name) and
            item[2] == sort and
            (min_stretch is None or item[4] >= min_stretch) and
            (max_stretch is None or item[4] <= max_stretch) and
            (size is None or size in item[5]) and
            (min_price is None or item[6] >= min_price) and
            (max_price is None or item[6] <= max_price)
        ):
            filtered_data.append({
                "brand": item[0],
                "name": item[1],
                "sort": item[2],
                "stretch": stretch_mapping[item[4]],
                "size": item[5],
                "price": item[6]
            })

    return filtered_data

vacation_package_data = [
    ["하나투어", True, False, ["세부 산토 니뇨 성당", "얍 샌디에고 조상의 집", "카와산 폭포"], False, 210000],
    ["여행이지", False, False, ["후말론 나비 보호구역", "SM 시사이드 시티", "라푸라푸 기념비"], False, 180000],
    ["곰블리투어", False, True, ["마젤란의 십자가", "카와산 폭포"], True, 155000],
    ["호핑에빠지다", True, True, ["세부 도교 사원", "마젤란의 십자가", "라푸라푸 기념비"], True, 200000],
    ["올웨이즈투어", False, True, ["톱스 전망대", "후말론 나비 보호구역"], True, 130000]
]

@app.get("/vacation_package")
async def filter_vacation_package(
    companyName: Optional[str] = Query(None, description="여행사 이름을 한글로 적어주세요 (ex. 하나투어, 여행이지)"),
    hoppingTF: bool = Query(..., description="호핑 투어 여부를 알기 위해 호핑 투어가 포함되길 원하시면 True, 그렇지 않으시면 False를 적어주세요"),
    localGuideTF: bool = Query(..., description="현지인 가이드 여부를 알기 위해 현지인 가이드가 포함되길 원하시면 True, 그렇지 않으시면 False를 적어주세요"),
    course: Optional[str] = Query(None, description="여행 코스를 한글로 적어주세요 (ex. 세부 산토 니뇨 성당, 후말론 나비 보호구역)"),
    freeMealTF: bool = Query(..., description="자유식사 가능여부를 알기 위해 자유식사가 포함되길 원하시면 True, 그렇지 않으시면 False를 적어주세요"),
    min_price: Optional[int] = Query(None, description="최소 가격(단위: 원)은 정수로 적어주세요"),
    max_price: Optional[int] = Query(None, description="최대 가격(단위: 원)은 정수로 적어주세요")
):
    filtered_data = []

    for item in vacation_package_data:
        if (
            (companyName is None or item[0] == companyName) and
            item[1] == hoppingTF and
            item[2] == localGuideTF and
            (course is None or course in item[3]) and
            item[4] == freeMealTF and
            (min_price is None or item[5] >= min_price) and
            (max_price is None or item[5] <= max_price)
        ):
            filtered_data.append({
                "companyName": item[0],
                "hoppingTF": item[1],
                "localGuideTF": item[2],
                "course": item[3],
                "freeMealTF": item[4],
                "price": item[5]
            })

    return filtered_data

adopted_oversea_data = [
    ["미국", "단감이", "진도믹스", 4, "Evlyn", "Lizzle", "2020.09.30"],
    ["캐나다", "난나", "믹스", 3, "Chloe", "Thomas", "2022.04.06"],
    ["독일", "선미", "믹스", 1, "Aaron", "Nicholas", "2023.07.05"],
    ["미국", "홍시", "푸들", 9, "Duncan", "Martin", "2022.12.16"],
    ["캐나다", "제이비", "포메라니안", 10, "Sharon", "Emily", "2020.02.15"]
]

@app.get("/adopted_oversea")
async def filter_adopted_oversea(
    country: str = Query(..., description="나라 이름을 한글로 적어주세요 (ex. 미국, 캐나다)"),
    cName: Optional[str] = Query(None, description="입양전 이름을 한글로 적어주세요 (ex. 단감이, 난나, 제이비)"),
    breed: Optional[str] = Query(None, description="품종을 한글로 적어주세요 (ex. 진도믹스, 믹스, 푸들, 포메라니안)"),
    min_age: Optional[int] = Query(None, description="최소 나이(단위: 살)는 정수로 적어주세요"),
    max_age: Optional[int] = Query(None, description="최대 나이(단위: 살)는 정수로 적어주세요"),
    aName: Optional[str] = Query(None, description="입양후 이름은 첫글자를 대문자인 영어로 적어주세요 (ex. Evlyn, Chloe)"),
    adoptedPerson: Optional[str] = Query(None, description="입양자 이름을 첫글자를 대문자인 영어로 적어주세요 (ex. Lizzle, Thomas)"),
    adoptDate: Optional[str] = Query(None, description="입양날짜는 2020.09.30의 양식으로 적어주세요")
):
    filtered_data = []

    for item in adopted_oversea_data:
        if (
            item[0] == country and
            (cName is None or item[1] == cName) and
            (breed is None or item[2] == breed) and
            (min_age is None or item[3] >= min_age) and
            (max_age is None or item[3] <= max_age) and
            (aName is None or item[4] == aName) and
            (adoptedPerson is None or item[5] == adoptedPerson) and
            (adoptDate is None or item[6] == adoptDate)
        ):
            filtered_data.append({
                "country": item[0],
                "cName": item[1],
                "breed": item[2],
                "age": item[3],
                "aName": item[4],
                "adoptedPerson": item[5],
                "adoptDate": item[6]
            })

    return filtered_data

secondhand_book_data = [
    ["부키", "나는 왜 네가 힘들까 셀프 테라피북", "크리스텔 프티콜랭", "에세이", "2020-05-15", "2023-07-26", 12500, 7600],
    ["문학동네", "H마트에서 울다", "미셸 자우너", "에세이", "2022-02-28", "2023-07-01", 16000, 10100],
    ["창비", "초정리 편지", "배유안", "소설", "2006-08-03", "2015-12-15", 10800, 1000],
    ["인플루엔셜", "미움받을 용기", "기시미 이치로", "심리", "2014-11-17", "2019-05-07", 16900, 8500],
    ["아이씨디", "오즈의 마법사", "프랭크 모건", "어린이", "2022-01-08", "2023-04-16", 2900, 100]
]

@app.get("/secondhand_book")
async def filter_secondhand_book(
    publisher: Optional[str] = Query(None, description="출판사는 한글로 적어주세요 (ex. 부키, 인플루엔셜)"),
    bookName: Optional[str] = Query(None, description="책 제목은 한글과 영어를 사용해 적어주세요 (ex. H마트에서 울다, 나는 왜 네가 힘들까 셀프 테라피북)"),
    bookAuthor: Optional[str] = Query(None, description="지은이는 한글을 사용해 적어주세요 (ex. 크리스텔 프티콜랭, 미셸 자우너)"),
    category: str = Query(..., description="검색하시는 책의 분야를 한글을 사용해 적어주세요 (ex. 소설, 에세이, 금융, 자격증)"),
    publishDate: Optional[str] = Query(None, description="출판날짜는 2020-05-15의 양식으로 적어주세요"),
    receivDate: Optional[str] = Query(None, description="입고날짜는 2020-05-15의 양식으로 적어주세요"),
    originPrice: Optional[int] = Query(None, description="중고책의 원래 가격은 정수로 적어주세요"),
    min_price: Optional[int] = Query(None, description="최소 판매가(단위: 원)는 정수로 적어주세요"),
    max_price: Optional[int] = Query(None, description="최대 판매가(단위: 원)는 정수로 적어주세요")
):
    filtered_data = []

    for item in secondhand_book_data:
        if (
            (publisher is None or item[0] == publisher) and
            (bookName is None or item[1] == bookName) and
            (bookAuthor is None or item[2] == bookAuthor) and
            item[3] == category and
            (publishDate is None or item[4] == publishDate) and
            (receivDate is None or item[5] == receivDate) and
            (originPrice is None or item[6] == originPrice) and
            (min_price is None or item[7] >= min_price) and
            (max_price is None or item[7] <= max_price)
        ):
            filtered_data.append({
                "publisher": item[0],
                "bookName": item[1],
                "bookAuthor": item[2],
                "category": item[3],
                "publishDate": item[4],
                "receivDate": item[5],
                "originPrice": item[6],
                "price": item[7]
            })

    return filtered_data

resume_data = [
    ["이영지", "010-0000-0001", 25, ["정보처리기사", "리눅스마스터"], "개발", 3.2],
    ["전안형", "010-0000-0002", 31, ["정보보안기사", "리눅스마스터"], "기획", 3.8],
    ["김성남", "010-0000-0003", 29, ["컴퓨터활용능력1급", "토스7"], "인사", 4.1],
    ["안영열", "010-0000-0004", 24, ["컴퓨터활용능력2급"], "마케팅", 4.5],
    ["오은지", "010-0000-0005", 32, ["1종운전면허", "한국사능력시험1급"], "영업", 4.3]
]

@app.get("/resume")
async def filter_job_resume(
    name: Optional[str] = Query(None, description="이름으로 성이름을 한글로 적어주세요 (ex. 이영지, 전안형)"),
    phone: Optional[str] = Query(None, description="전화번호는 010-0000-0001의 양식으로 적어주세요"),
    min_age: Optional[int] = Query(None, description="최소 나이는 정수로 적어주세요"),
    certificate: str = Query(..., description="자격증은 한글과 영어를 사용해 적어주세요 (ex. 정보처리기사, SQLD, 정보보안기사, 리눅스마스터)"),
    field: Optional[str] = Query(None, description="지원분야는 한글로 적어주세요 (ex. 마케팅, 인사, 개발, 기획)"),
    min_grade: Optional[float] = Query(None, description="최소 학점은 실수로 적어주세요", ge=0, le=5),
    max_grade: Optional[float] = Query(None, description="최대 학점은 실수로 적어주세요", ge=0, le=5)
):
    filtered_data = []

    for item in resume_data:
        if (
            (name is None or item[0] == name) and
            (phone is None or item[1] == phone) and
            (min_age is None or item[2] >= min_age) and
            certificate in item[3] and
            (field is None or item[4] == field) and
            (min_grade is None or item[5] >= min_grade) and
            (max_grade is None or item[5] <= max_grade)
        ):
            filtered_data.append({
                "name": item[0],
                "phone": item[1],
                "age": item[2],
                "certificate": item[3],
                "field": item[4],
                "grade": item[5]
            })

    return filtered_data

stock_data = [
    ["삼성전자", 71700, ["전기", "전자"], 0.53, 8.66, 8100.2],
    ["네이버", 211500, ["서비스업"], 0.47, 42.66, 4005.3],
    ["카카오", 50600, ["서비스업"], 0.25, 15.747, 3000.02],
    ["현대차", 197800, ["운수장비"], 0.328, 7.47, 30350],
    ["SK하이닉스", 124000, ["전기", "전자"], 0.51, 1.25, 2500.5]
]

@app.get("/k_stock")
async def filter_korea_stock(
    stockName: Optional[str] = Query(None, description="주식명은 한글과 영어를 사용해 적어주세요 (ex. 삼성전자, SK하이닉스)"),
    min_price: Optional[int] = Query(None, description="최소 가격(단위: 원)은 정수로 적어주세요"),
    max_price: Optional[int] = Query(None, description="최대 가격(단위: 원)은 정수로 적어주세요"),
    category: str = Query(..., description="카테고리는 숫자, 영어, 한글을 이용해 적어주세요 (ex. 2차전지, 자동차, AI, 철강, 조선)"),
    foreigner: Optional[float] = Query(None, description="외국인 보유비중(단위: %)은 실수로 적어주세요"),
    min_per: Optional[float] = Query(None, description="최소 주가수익비율(PER(단위: %))은 실수로 적어주세요"),
    min_eps: Optional[float] = Query(None, description="최소 주당순이익(EPS(단위: %))은 실수로 적어주세요")
):
    filtered_data = []

    for item in stock_data:
        if (
            (stockName is None or item[0] == stockName) and
            (min_price is None or item[1] >= min_price) and
            (max_price is None or item[1] <= max_price) and
            category in item[2] and
            (foreigner is None or item[3] >= foreigner) and
            (min_per is None or item[4] >= min_per) and
            (min_eps is None or item[5] >= min_eps)
        ):
            filtered_data.append({
                "stockName": item[0],
                "price": item[1],
                "category": item[2],
                "foreigner": item[3],
                "per": item[4],
                "eps": item[5]
            })

    return filtered_data

baby_food_data = [
    ["헬로베이비", "중기", ["버섯", "소고기"], 110.5, 79, 4500],
    ["마미냠냠", "중기", ["당근", "닭고기"], 120, 81, 4300],
    ["헬로베이비", "후기1", ["시금치", "닭고기"], 150, 110, 4800],
    ["담다", "후기1", ["단호박", "돼지고기"], 158, 119, 4900],
    ["아가밀", "후기2", ["버섯", "단호박", "닭고기"], 190, 205, 5100]
]

@app.get("/baby_food")
async def filter_baby_food(
    brand: Optional[str] = Query(None, description="브랜드 이름을 띄어쓰기 없이 한글로 적어주세요 (ex. 헬로베이비, 마미냠냠)"),
    period: str = Query(..., description="이유식 시기를 한글과 숫자를 이용해 적어주세요 (ex. 중기, 후기1, 후기2)"),
    ingredient: Optional[str] = Query(None, description="식재료를 한글로 적어주세요 (ex. 소고기, 버섯)"),
    min_calorie: Optional[float] = Query(None, description="최소 칼로리(단위: kcal)를 실수로 적어주세요"),
    min_weight: Optional[float] = Query(None, description="최소 무게(단위: g)를 실수로 적어주세요"),
    max_weight: Optional[float] = Query(None, description="최대 무게(단위: g)를 실수로 적어주세요"),
    min_price: Optional[int] = Query(None, description="최소 가격(단위: 원)을 정수로 적어주세요"),
    max_price: Optional[int] = Query(None, description="최대 가격(단위: 원)을 정수로 적어주세요")
):
    filtered_data = []

    for item in baby_food_data:
        if (
            (brand is None or item[0] == brand) and
            (item[1] == period) and
            (ingredient is None or ingredient in item[2]) and
            (min_calorie is None or item[3] >= min_calorie) and
            (min_weight is None or item[4] >= min_weight) and
            (max_weight is None or item[4] <= max_weight) and
            (min_price is None or item[5] >= min_price) and
            (max_price is None or item[5] <= max_price)
        ):
            filtered_data.append({
                "brand": item[0],
                "period": item[1],
                "ingredient": item[2],
                "calorie": item[3],
                "weight": item[4],
                "price": item[5]
            })

    return filtered_data

cultural_center_data = [
    ["필라테스", "초급", "어린이", ["화요일", "목요일"], "안지영", "010-0000-0001", 35000, ["폼롤러", "요가매트"]],
    ["스마트폰 기초", "초급", "노인", ["월요일", "수요일"], "김파란", "010-0000-0002", 25000, ["스마트폰"]],
    ["기타", "초급", "성인", ["수요일"], "강연희", "010-0000-0003", 41000, ["클래식기타", "피크"]],
    ["요가", "중급", "성인", ["월요일", "금요일"], "동아란", "010-0000-0004", 32000, ["요가링"]],
    ["우쿠렐레", "고급", "성인", ["화요일", "목요일"], "김단아", "010-0000-0005", 41000, ["우쿠렐레", "악보대"]]
]

@app.get("/cultural_center")
async def filter_cultural_center(
    className: Optional[str] = Query(None, description="수업명은 한글로 적어주세요 (ex. 필라테스, 스마트폰 기초)"),
    level: Optional[str] = Query(None, description="난이도는 초급, 중급, 고급 중 하나를 적어주세요"),
    target: str = Query(..., description="수업대상은 영유아, 어린이, 성인, 노인 중 하나를 적어주세요"),
    day: Optional[str] = Query(None, description="요일은 월요일, 화요일, 수요일의 양식으로 적어주세요"),
    teacherName: Optional[str] = Query(None, description="강사명은 성이름을 한글로 적어주세요 (ex. 홍길동)"),
    supply: Optional[str] = Query(None, description="준비물은 한글로 적어주세요 (ex. 스마트폰, 폼룰러)"),
    min_price: Optional[int] = Query(None, description="최소 가격(단위: 원)을 정수로 적어주세요"),
    max_price: Optional[int] = Query(None, description="최대 가격(단위: 원)을 정수로 적어주세요")
):
    filtered_data = []

    for item in cultural_center_data:
        if (
            (className is None or item[0] == className) and
            (level is None or item[1] == level) and
            (item[2] == target) and
            (day is None or day in item[3]) and
            (teacherName is None or item[4] == teacherName) and
            (supply is None or supply in item[7]) and
            (min_price is None or item[6] >= min_price) and
            (max_price is None or item[6] <= max_price)
        ):
            filtered_data.append({
                "className": item[0],
                "level": item[1],
                "target": item[2],
                "day": item[3],
                "teacherName": item[4],
                "phone": item[5],
                "supply": item[7],
                "price": item[6]
            })

    return filtered_data

kindergarten_center_data = [
    ["파란 유치원", "경기도 성남시 수정구 위례동로 55", "031-0000-0001", "공립", True, 358000],
    ["아름 유치원", "경기도 성남시 수정구 복정안골로 35", "031-0000-0002", "공립", False, 290000],
    ["플로린 유치원", "경기도 성남시 중원구 광명로 184번길", "031-0000-0003", "사립", True, 890000],
    ["제이앤던 유치원", "경기도 성남시 분당구 장미로 88", "031-0000-0004", "사립", True, 990000],
    ["성아 유치원", "경기도 성남시 분당구 서판교로 74", "031-0000-0005", "사립", False, 750000]
]

@app.get("/kindergarten_center")
async def filter_kindergarten_center(
    centerName: Optional[str] = Query(None, description="유치원 이름은 한글로 적어주세요 (ex. 파란 유치원, 플로린 유치원)"),
    category: str = Query(..., description="공립과 사립 중 하나를 적어주세요"),
    engClassTF: Optional[bool] = Query(None, description="영어수업 여부를 알기 위해 영어수업을 하는 경우 True, 그렇지 않은 경우 False를 적어주세요"),
    min_price: Optional[int] = Query(None, description="최소 원비(단위: 원)는 정수로 적어주세요"),
    max_price: Optional[int] = Query(None, description="최대 원비(단위: 원)는 정수로 적어주세요"),
    ctprvNm: Optional[str] = Query(None, description="시도명은 한글로 적어주세요(ex. 서울특별시, 인천광역시, 강원도, 경기도, 경상남도 등)"),
    sgngNm: Optional[str] = Query(None, description="시군구명은 한글로 적어주세요(ex. 전주시, 강릉시, 포항시, 양평군 등)"),
    emdNm: Optional[str] = Query(None, description="읍면동명은 한글로 적어주세요(ex. 전주시, 강릉시, 포항시, 양평군 등)"),
    phone: Optional[str] = Query(None, description="전화번호는 031-0000-0001의 양식으로 적어주세요")
):
    filtered_data = []

    for item in kindergarten_center_data:
        if (
            (centerName is None or item[0] == centerName) and
            (item[2] == category) and
            (engClassTF is None or item[4] == engClassTF) and
            (min_price is None or item[5] >= min_price) and
            (max_price is None or item[5] <= max_price) and
            (ctprvNm is None or ctprvNm in item[1]) and
            (sgngNm is None or sgngNm in item[1]) and
            (emdNm is None or emdNm in item[1]) and
            (phone is None or item[2] == phone)
        ):
            filtered_data.append({
                "centerName": item[0],
                "category": item[3],
                "phone": item[2],
                "address": item[1],
                "engClassTF": item[4],
                "price": item[5]
            })

    return filtered_data

middle_school_teacher_data = [
    ["동영선", 1, 3, "사회", "dys@naver.com", 10],
    ["강하늘", 3, 5, "국어", "khn@naver.com", 5],
    ["김미연", 2, 4, "수학", "kmy@naver.com", 4],
    ["황선영", 2, 2, "국어", "hsy@naver.com", 11],
    ["홍지영", 3, 1, "영어", "hjy@naver.com", 4]
]

@app.get("/middle_teacher")
async def filter_middle_school_teacher(
    teacherName: Optional[str] = Query(None, description="교사명은 한글로 적어주세요 (ex. 동영선)"),
    min_grade: Optional[int] = Query(None, description="최소 학년(단위: 학년)은 1~3 사이의 정수로 적어주세요", ge=1, le=3),
    max_grade: Optional[int] = Query(None, description="최대 학년(단위: 학년)은 1~3 사이의 정수로 적어주세요", ge=1, le=3),
    class_: Optional[int] = Query(None, description="반(단위: 반)은 정수로 적어주세요"),
    subject: str = Query(..., description="과목은 한글로 적어주세요 (ex. 영어, 사회, 국어)"),
    email: Optional[str] = Query(None, description="이메일은 dys@naver.com의 양식으로 적어주세요"),
    min_year: Optional[int] = Query(None, description="최소 연차(단위: 년)는 0 이상의 정수로 적어주세요", ge=0),
    max_year: Optional[int] = Query(None, description="최대 연차(단위: 년)는 0 이상의 정수로 적어주세요", ge=0)
):
    filtered_data = []

    for item in middle_school_teacher_data:
        if (
            (teacherName is None or item[0] == teacherName) and
            (min_grade is None or item[1] >= min_grade) and
            (max_grade is None or item[1] <= max_grade) and
            (class_ is None or item[2] == class_) and
            (item[3] == subject) and
            (email is None or item[4] == email) and
            (min_year is None or item[5] >= min_year) and
            (max_year is None or item[5] <= max_year)
        ):
            filtered_data.append({
                "teacherName": item[0],
                "grade": item[1],
                "class": item[2],
                "subject": item[3],
                "email": item[4],
                "year": item[5]
            })

    return filtered_data

supermarket_data = [
    ["롯데마트 덕소점", "10:00", "23:00", "둘째주 넷째주 수요일", True, "031-579-7700"],
    ["이마트 가든파이브점", "10:00", "22:30", "둘째주 넷째주 일요일", False, "02-411-1234"],
    ["이마트 강릉점", "10:00", "23:00", "둘째주 넷째주 수요일", True, "033-649-1234"],
    ["홈플러스 동래점", "10:00", "24:00", "둘째주 넷째주 일요일", True, "051-559-8000"],
    ["롯데마트 군산점", "10:00", "23:00", "둘째주 넷째주 일요일", True, "063-441-2500"]
]

@app.get("/supermarket")
async def filter_supermarket(
    name: Optional[str] = Query(None, description="지점명은 한글로 적어주세요 (ex. 롯데마트 덕소점 등)"),
    opening_time: Optional[str] = Query(None, description="오픈 시간은 10:00의 양식으로 적어주세요"),
    closed_time: str = Query(..., description="마감 시간은 20:00의 양식으로 적어주세요"),
    closed_days: Optional[str] = Query(None, description="휴무일은 다음의 양식으로 적어주세요 (ex. 둘째주 넷째주 수요일, 둘째주 넷째주 일요일 등)"),
    free_parking: Optional[bool] = Query(None, description="무료주차여부를 알기 위해 무료 주차가 가능한 대형마트를 원하시면 True, 그렇지 않으시면 False를 적어주세요")
):
    filtered_data = []

    for item in supermarket_data:
        if (
            (name is None or item[0] == name) and
            (opening_time is None or item[1] == opening_time) and
            (item[2] == closed_time) and
            (closed_days is None or item[3] == closed_days) and
            (free_parking is None or item[4] == free_parking)
        ):
            filtered_data.append({
                "name": item[0],
                "opening_time": item[1],
                "closed_time": item[2],
                "closed_days": item[3],
                "free_parking": item[4],
                "telephone_number": item[5]
            })

    return filtered_data

apple_service_center_data = [
    ["위니아에이드 교대역센터", "김석준", "디스플레이", "2023-04-02", "10:00", False, 40000],
    ["투바 압구정", "김하랑", "배터리", "2023-06-08", "15:20", True, 124000],
    ["투바 청주", "이희정", "배터리", "2023-06-08", "16:30", False, 51000],
    ["KT 고양점", "박서준", "기타 손상", "2023-07-22", "12:00", False, 370000],
    ["ANTZ 춘천", "이수민", "배터리", "2023-06-25", "18:00", True, 80000]
]

@app.get("/AppleServiceCenter")
async def filter_apple_service_center(
    center_name: Optional[str] = Query(None, description="업체명을 한글과 영어를 사용해 적어주세요 (ex. 위니아에이드 교대역센터, ANTZ 춘천)"),
    name: Optional[str] = Query(None, description="예약자명으로 성이름을 한글로 적어주세요 (ex. 김석준)"),
    content: Optional[str] = Query(None, description="수리 내용을 한글로 적어주세요 (ex. 디스플레이, 배터리 등)"),
    reservation_date: str = Query(..., description="예약일을 2023-06-08의 양식으로 적어주세요"),
    reservation_time: Optional[str] = Query(None, description="예약시간을 10:00의 양식으로 적어주세요"),
    the_day_repair: Optional[bool] = Query(None, description="당일수리가능여부를 알기 위해 당일수리 가능을 원하시면 True, 그렇지 않으시면 False를 적어주세요"),
    min_price: Optional[int] = Query(None, description="최소 수리비용(단위: 원)은 정수로 적어주세요"),
    max_price: Optional[int] = Query(None, description="최대 수리비용(단위: 원)은 정수로 적어주세요")
):
    filtered_data = []

    for item in apple_service_center_data:
        if (
            (center_name is None or item[0] == center_name) and
            (name is None or item[1] == name) and
            (content is None or item[2] == content) and
            (item[3] == reservation_date) and
            (reservation_time is None or item[4] == reservation_time) and
            (the_day_repair is None or item[5] == the_day_repair) and
            (min_price is None or item[6] >= min_price) and
            (max_price is None or item[6] <= max_price)
        ):
            filtered_data.append({
                "center_name": item[0],
                "name": item[1],
                "content": item[2],
                "reservation_date": item[3],
                "reservation_time": item[4],
                "the_day_repair": item[5],
                "expense": item[6]
            })

    return filtered_data

tumbler_data = [
    ["스타벅스 DT 텀블러", 13900, 591, False, True, ["보온", "보냉"]],
    ["카르닉 텀블러", 9900, 600, True, False, ["보냉"]],
    ["록키마운틴 텀블러", 6000, 900, True, True, ["보냉"]],
    ["락앤락 퓨어 텀블러", 11000, 470, False, False, ["보온", "보냉"]],
    ["락앤락 클립 텀블러", 15700, 540, True, True, ["보온", "보냉"]],
]

@app.get("/tumbler_search")
async def filter_tumbler_search(
    name: Optional[str] = Query(None, description="상품명을 한글로 적어주세요 (ex. 스타벅스 텀블러, 락앤락 클립 텀블러)"),
    max_price: Optional[int] = Query(None, description="최대 가격(단위: 원)은 0이상의 정수로 적어주세요"),
    min_price: Optional[int] = Query(None, description="최소 가격(단위: 원)은 0이상의 정수로 적어주세요"),
    min_capacity: Optional[float] = Query(None, description="최소용량(단위: mL)은 0이상의 실수로 적어주세요"),
    vacuum_cap: bool = Query(..., description="진공뚜껑 여부를 알기 위해 진공뚜껑을 포함하고 싶으시면 True, 그렇지 않으시면 False를 적어주세요"),
    straw: bool = Query(..., description="빨대포함여부를 알기 위해 빨대를 포함하고 싶으시면 True, 그렇지 않으시면 False를 적어주세요"),
    function: Optional[str] = Query(None, description="기능으로 보냉, 보온을 하나 이상 적어주세요")
):
    filtered_data = []

    for item in tumbler_data:
        if (
            (name is None or item[0] == name) and
            (max_price is None or item[1] <= max_price) and
            (min_price is None or item[1] >= min_price) and
            (min_capacity is None or item[2] >= min_capacity) and
            (item[3] == vacuum_cap) and
            (item[4] == straw) and
            (function is None or function in item[5])
        ):
            filtered_data.append({
                "name": item[0],
                "price": item[1],
                "capacity": item[2],
                "vacuum_cap": item[3],
                "straw": item[4],
                "function": item[5]
            })

    return filtered_data

scale_data = [
    ["앳플리 티엑스", 41900, 180, True, ["체중", "체지방", "기초대사량", "근육량", "골밀도량", "내장지방", "일일필요열량", "체수분", "BMI지수"], 4.8],
    ["카스 디지털", 26800, 180, False, ["체중"], 4.8],
    ["샤오미 미스케일", 18000, 150, True, ["체중", "BMI지수"], 4.7],
    ["휴비딕 디지털", 8800, 180, False, ["체중"], 4.7],
    ["인바디 다이얼 더블유", 200000, 150, True, ["체중", "체지방", "기초대사량", "근육량", "골밀도량", "내장지방", "일일필요열량", "BMI지수"], 4.9],
]

@app.get("/scale_search")
async def filter_scale_search(
    name: Optional[str] = Query(None, description="상품명은 한글로 적어주세요 (ex. 인바디 다이얼 더블유, 앳플리 티엑스)"),
    max_price: Optional[int] = Query(None, description="최대 가격(단위: 원)은 0이상의 정수로 적어주세요"),
    min_price: Optional[int] = Query(None, description="최소 가격(단위: 원)은 0이상의 정수로 적어주세요"),
    min_measuring_range: Optional[float] = Query(None, description="최소 측정 범위는 0이상의 실수로 적어주세요"),
    smart_scale: bool = Query(..., description="스마트체중계 여부를 알기 위해 스마트체중계를 원하시면 True, 그렇지 않으시면 False를 적어주세요"),
    function: Optional[str] = Query(None, description="원하시는 기능을 한글로 적어주세요 (ex. 체중, 체지방,근육량 등)"),
    min_rating: Optional[float] = Query(None, description="최소 평점을 0~5 사이의 실수로 적어주세요")
):
    filtered_data = []

    for item in scale_data:
        if (
            (name is None or item[0] == name) and
            (max_price is None or item[1] <= max_price) and
            (min_price is None or item[1] >= min_price) and
            (min_measuring_range is None or item[2] >= min_measuring_range) and
            (item[3] == smart_scale) and
            (function is None or function in item[4]) and
            (min_rating is None or item[5] >= min_rating)
        ):
            filtered_data.append({
                "name": item[0],
                "price": item[1],
                "measuring_range": item[2],
                "smart_scale": item[3],
                "function": item[4],
                "rating": item[5]
            })

    return filtered_data

running_shoes_data = [
    ["언더아머", 52000, 0.8, "합성섬유", 4.8],
    ["나이키", 89000, 3, "인조가죽", 4.7],
    ["호카", 189000, 2, "합성섬유", 4.9],
    ["나이키", 108000, 1.5, "합성섬유", 4.9],
    ["아디다스", 39000, 2, "메시", 4.6],
]

@app.get("/RunningShoes")
async def filter_running_shoes(
    brand: str = Query(..., description="브랜드를 한글로 적어주세요 (ex. 언더아머, 나이키)"),
    max_price: Optional[int] = Query(None, description="최대 가격(단위: 원)은 0이상의 정수로 적어주세요"),
    min_price: Optional[int] = Query(None, description="최소 가격(단위: 원)은 0이상의 정수로 적어주세요"),
    min_heel_height: Optional[float] = Query(None, description="최소 굽높이는 0~5 사이의 실수로 적어주세요"),
    max_heel_height: Optional[float] = Query(None, description="최대 굽높이는 0~5 사이의 실수로 적어주세요"),
    material: Optional[str] = Query(None, description="소재를 한글로 적어주세요 (ex. 합성섬유, 인조가죽, 메시)"),
    min_rating: Optional[float] = Query(None, description="최소 평점을 0~5 사이의 실수로 적어주세요")
):
    filtered_data = []

    for item in running_shoes_data:
        if (
            (item[0] == brand) and
            (max_price is None or item[1] <= max_price) and
            (min_price is None or item[1] >= min_price) and
            (min_heel_height is None or item[2] >= min_heel_height) and
            (max_heel_height is None or item[2] <= max_heel_height) and
            (material is None or item[3] == material) and
            (min_rating is None or item[4] >= min_rating)
        ):
            filtered_data.append({
                "brand": item[0],
                "price": item[1],
                "heel_height": item[2],
                "material": item[3],
                "rating": item[4]
            })

    return filtered_data

tent_data = [
    ["모비딕", 78000, 4.2, "5-6인용", True, 2],
    ["네이처하이크", 150000, 20, "3-4인용", True, 1],
    ["카즈미 코트", 120000, 2.8, "1인용", True, 2],
    ["아이두젠 오페라3", 44900, 2.2, "3-4인용", False, 2],
    ["코베아 와우코트", 47000, 1.5, "1인용", False, 1],
]

@app.get("/TentSearch")
async def filter_tent_search(
    name: str = Query(..., description="상품명을 한글로 적어주세요 (ex. 모비딕)"),
    max_price: Optional[int] = Query(None, description="최대 가격(단위: 원)은 0이상의 정수로 적어주세요"),
    min_price: Optional[int] = Query(None, description="최소 가격(단위: 원)은 0이상의 정수로 적어주세요"),
    min_weight: Optional[float] = Query(None, description="최소 무게(단위: kg)은 0이상의 실수로 적어주세요"),
    usage_num: Optional[str] = Query(None, description="원하시는 텐트 인용수를 적어주세요 (ex. 5-6인용, 3-4인용 등)"),
    waterproof: bool = Query(..., description="방수여부를 알기 위해 방수가 포함되길 원하시면 True, 그렇지 않으시면 False를 적어주세요"),
    doors_num: Optional[int] = Query(None, description="출입문 개수(단위: 개)는 0이상의 정수로 적어주세요"),
):
    filtered_data = []

    for item in tent_data:
        if (
            (item[0] == name) and
            (max_price is None or item[1] <= max_price) and
            (min_price is None or item[1] >= min_price) and
            (min_weight is None or item[2] >= min_weight) and
            (usage_num is None or item[3] == usage_num) and
            (item[4] == waterproof) and
            (doors_num is None or item[5] >= doors_num)
        ):
            filtered_data.append({
                "name": item[0],
                "price": item[1],
                "weight": item[2],
                "usage_num": item[3],
                "waterproof": item[4],
                "doors_num": item[5]
            })

    return filtered_data

electric_fan_data = [
    ["케어메디 선풍기", 88300, 8, True, True],
    ["듀플렉스 선풍기", 37000, 3, False, True],
    ["한일 캠핑선풍기", 149000, 2, False, False],
    ["윈드피아 선풍기", 48900, 4, True, True],
    ["신일전자 선풍기", 130000, 12, True, True],
]

@app.get("/ElectricFanSearch")
async def filter_electric_fan_search(
    name: str = Query(..., description="상품명"),
    max_price: Optional[int] = Query(None, description="최대 가격(단위: 원)은 0이상의 정수로 적어주세요"),
    min_price: Optional[int] = Query(None, description="최소 가격(단위: 원)은 0이상의 정수로 적어주세요"),
    min_wind_speed: Optional[int] = Query(None, description="최소 바람세기(단위: 단)를 0이상의 정수로 적어주세요"),
    remote_control: bool = Query(..., description="리모컨여부를 알기 위해 리모컨이 포함되길 원하시면 True, 그렇지 않으시면 False를 적어주세요"),
    timer: bool = Query(..., description="타이머 여부를 알기 위해 타이머가 포함되길 원하시면 True, 그렇지 않으시면 False를 적어주세요"),
):
    filtered_data = []

    for item in electric_fan_data:
        if (
            (item[0] == name) and
            (max_price is None or item[1] <= max_price) and
            (min_price is None or item[1] >= min_price) and
            (min_wind_speed is None or item[2] >= min_wind_speed) and
            (item[3] == remote_control) and
            (item[4] == timer)
        ):
            filtered_data.append({
                "name": item[0],
                "price": item[1],
                "wind_speed": item[2],
                "remote_control": item[3],
                "timer": item[4],
            })

    return filtered_data

mattress_data = [
    ["퀵슬립", 363900, 29, "메모리폼", "Q"],
    ["에이스침대", 380000, 23, "스프링", "SS"],
    ["휴도", 79900, 21, "스프링", "S"],
    ["슬로우베드", 699900, 23, "메모리폼", "SS"],
    ["지누스", 400000, 23, "메모리폼", "Q"],
]

@app.get("/Mattress")
async def filter_mattress(
    brand: Optional[str] = Query(None, description="브랜드명은 한글로 적어주세요 (ex. 퀵슬립, 에이스침대)"),
    max_price: Optional[int] = Query(None, description="최대 가격(단위: 원)은 0이상의 정수로 적어주세요"),
    min_price: Optional[int] = Query(None, description="최소 가격(단위: 원)은 0이상의 정수로 적어주세요"),
    min_thickness: Optional[int] = Query(None, description="최소 두께(단위: cm)는 0이상의 정수로 적어주세요"),
    type: Optional[str] = Query(None, description="타입을 한글로 적어주세요 (ex. 메모리폼, 스프링)"),
    size: str = Query(..., description="사이즈를 영어 대문자로 적어주세요 (ex. Q, SS, S)"),
):
    filtered_data = []

    for item in mattress_data:
        if (
            (brand is None or item[0] == brand) and
            (max_price is None or item[1] <= max_price) and
            (min_price is None or item[1] >= min_price) and
            (min_thickness is None or item[2] >= min_thickness) and
            (type is None or item[3] == type) and
            (item[4] == size)
        ):
            filtered_data.append({
                "brand": item[0],
                "price": item[1],
                "thickness": item[2],
                "type": item[3],
                "size": item[4],
            })

    return filtered_data

rice_data = [
    ["이쌀이다", "현미", 5, 12000, 4.8, "보통"],
    ["신동진", "백미", 20, 50800, 4.8, "상"],
    ["신동진", "현미", 10, 35300, 4.7, "보통"],
    ["쌀창고", "현미", 10, 41800, 4.9, "상"],
    ["대왕님표", "백미", 10, 41800, 4.9, "상"],
]

@app.get("/RiceSearch")
async def filter_rice(
    brand: str = Query(..., description="브랜드명을 한글로 적어주세요 (ex. 이쌀이다, 신동진)"),
    type: Optional[str] = Query(None, description="종류를 한글로 적어주세요 (ex. 현미, 백미)"),
    max_weight: Optional[float] = Query(None, description="최대무게(단위: g)는 0이상의 실수로 적어주세요"),
    min_weight: Optional[float] = Query(None, description="최소무게(단위: g)는 0이상의 실수로 적어주세요"),
    max_price: Optional[int] = Query(None, description="최대 가격(단위: 원)은 0이상의 정수로 적어주세요"),
    min_rating: Optional[float] = Query(None, description="최소평점을 0~5 사이의 실수로 적어주세요"),
    grade: Optional[str] = Query(None, description="등급으로 상, 보통 중 하나를 적어주세요"),
):
    filtered_data = []

    for item in rice_data:
        if (
            item[0] == brand and
            (type is None or item[1] == type) and
            (max_weight is None or item[2] <= max_weight) and
            (min_weight is None or item[2] >= min_weight) and
            (max_price is None or item[3] <= max_price) and
            (min_rating is None or (0 <= item[4] <= 5 and item[4] >= min_rating)) and
            (grade is None or item[5] == grade)
        ):
            filtered_data.append({
                "brand": item[0],
                "type": item[1],
                "weight": item[2],
                "price": item[3],
                "rating": item[4],
                "grade": item[5],
            })

    return filtered_data

birthday_event_data = [
    ["송추가마골", "이미진", "2023.08.05", "18:00", "생일 미역국", "010-1111-1111", 5],
    ["정식당", "최희진", "2023.06.20", "12:00", "생일 레터링과 초", "010-1111-2222", 6],
    ["미가정숯불갈비", "김동혁", "2023.10.23", "19:00", "생일 미역국", "010-1111-3333", 4],
    ["우텐더", "이나정", "2023.08.10", "14:00", "생일 케이크", "010-1111-0000", 12],
    ["더호", "박하정", "2023.10.04", "17:30", "생일 케이크", "010-0000-0000", 4],
]

@app.get("/BirthdayEvent")
async def filter_birthday_event(
    restaurant_name: str = Query(..., description="식당명은 한글로 적어주세요 (ex. 송추가마골, 정식당, 우텐더)"),
    name: Optional[str] = Query(None, description="예약자명은 성이름을 한글로 적어주세요 (ex. 홍길동)"),
    reservation_date: Optional[str] = Query(None, description="예약일자는 2023.08.05의 양식으로 적어주세요"),
    reservation_time: Optional[str] = Query(None, description="예약시간은 18:00의 양식으로 적어주세요"),
    contents: Optional[str] = Query(None, description="이벤트 내용을 한글로 적어주세요 (ex. 생일 케이크, 생일 미역국 등)"),
    min_present_num: Optional[int] = Query(None, description="최소 참석 인원(단위: 명)은 0이상의 정수로 적어주세요"),
    max_present_num: Optional[int] = Query(None, description="최대 참석 인원(단위: 명)은 0이상의 정수로 적어주세요"),
):
    filtered_data = []

    for item in birthday_event_data:
        if (
            item[0] == restaurant_name and
            (name is None or item[1] == name) and
            (reservation_date is None or item[2] == reservation_date) and
            (reservation_time is None or item[3] == reservation_time) and
            (contents is None or item[4] == contents) and
            (min_present_num is None or item[6] >= min_present_num) and
            (max_present_num is None or item[6] <= max_present_num)
        ):
            filtered_data.append({
                "restaurant_name": item[0],
                "name": item[1],
                "reservation_date": item[2],
                "reservation_time": item[3],
                "contents": item[4],
                "phone_num": item[5],
                "present_num": item[6],
            })

    return filtered_data

dog_anthelmintic_data = [
    ["넥스가드스펙트라", "먹는 약", 5, True, ["심장사상충","회충","개구충","벼룩","고양이벼룩","개참진드기","살인진드기","개선충","개귀진드기","개모낭충"]],
    ["하트가드플러스", "먹는 약", 4, False, ["심장사상충","회충","개구충"]],
    ["브리벡토", "먹는 약", 12, True, ["벼룩","고양이벼룩","개참진드기","살인진드기","개선충","개귀진드기","개모낭충"]],
    ["에드보킷", "바르는 약", 4, True, ["심장사상충","회충","개구충","벼룩","고양이벼룩","이","개선충","개귀진드기","개모낭충"]],
    ["레볼루션", "바르는 약", 4, True, ["심장사상충","회충","벼룩","고양이벼룩","이","개선충","개귀진드기"]]
]

@app.get("/DogAnthelmintic")
async def filter_dog_anthelmintic(
    name: Optional[str] = Query(None, description="상품명은 한글로 적어주세요 (ex. 넥스가드스펙트라, 브리벡토)"),
    type: str = Query(..., description="종류로 먹는 약, 바르는 약 중 하나를 적어주세요"),
    min_duration: Optional[int] = Query(None, description="최소 지속기간(단위: 주)은 0이상의 정수로 적어주세요"),
    side_effects_risk: Optional[bool] = Query(None, description="부작용위험성 여부를 알기 위해 부작용 위험이 포함된 약을 원하시면 True, 그렇지 않으시면 False를 적어주세요"),
    anthelmintics_range: Optional[str] = Query(None, description="구충범위를 한글로 적어주세요 (ex. 심장사상충, 개구충, 개선충 등)"),
):
    filtered_data = []

    for item in dog_anthelmintic_data:
        if (
            (name is None or item[0] == name) and
            item[1] == type and
            (min_duration is None or item[2] >= min_duration) and
            (side_effects_risk is None or item[3] == side_effects_risk) and
            (anthelmintics_range is None or anthelmintics_range in item[4])
        ):
            filtered_data.append({
                "name": item[0],
                "type": item[1],
                "duration": item[2],
                "side_effects_risk": item[3],
                "anthelmintics_range": item[4],
            })

    return filtered_data

gemstone_beads_data = [
    ["가넷", "플레인볼", 6, 30000, 85],
    ["라리마", "론델", 4, 31000, 140],
    ["라피스라줄리", "드롭", 15, 40000, 25],
    ["로즈쿼츠", "큐브", 7, 21000, 40],
    ["오닉스", "컷팅볼", 7, 23000, 35]
]

@app.get("/gemstone_beads")
async def filter_gemstone_beads(
    name: str = Query(..., description="원석이름은 한글로 적어주세요 (ex. 가넷, 라리마, 라피스라줄리)"),
    category: Optional[str] = Query(None, description="컷팅종류는 한글로 적어주세요 (ex. 플레인볼, 컷팅볼, 큐브,드롭, 론델 등)"),
    min_size: Optional[float] = Query(None, description="최소크기(단위: mm)는 0이상의 실수로 적어주세요"),
    max_size: Optional[float] = Query(None, description="최대크기(단위: mm)는 0이상의 실수로 적어주세요"),
    min_price: Optional[int] = Query(None, description="최소가격(단위: 원)은 0이상의 정수로 적어주세요"),
    max_price: Optional[int] = Query(None, description="최대가격(단위: 원)은 0이상의 정수로 적어주세요"),
    min_amount: Optional[int] = Query(None, description="최소수량(단위: 개)은 0이상의 정수로 적어주세요"),
    max_amount: Optional[int] = Query(None, description="최대수량(단위: 개)은 0이상의 정수로 적어주세요"),
):
    filtered_data = []

    for item in gemstone_beads_data:
        if (
            item[0] == name and
            (category is None or item[1] == category) and
            (min_size is None or item[2] >= min_size) and
            (max_size is None or item[2] <= max_size) and
            (min_price is None or item[3] >= min_price) and
            (max_price is None or item[3] <= max_price) and
            (min_amount is None or item[4] >= min_amount) and
            (max_amount is None or item[4] <= max_amount)
        ):
            filtered_data.append({
                "name": item[0],
                "category": item[1],
                "size": item[2],
                "price": item[3],
                "amount": item[4]
            })

    return filtered_data

keyring_accessories_data = [
    ["디링", "고리", "아연합금", 250, 1],
    ["군번줄", "고리", "아연합금", 500, 1],
    ["투톤젤리", "구슬", "아크릴", 2000, 78],
    ["파스텔펄", "구슬", "유리", 2500, 10],
    ["입체토끼", "참", "아크릴", 1200, 1]
]

@app.get("/keyring_accessories")
async def filter_keyring_accessories(
    name: str = Query(..., description="상품명은 한글로 적어주세요 (ex. 군번줄, 디링, 파스텔펄)"),
    category: str = Query(..., description="상품종류는 한글로 적어주세요 (ex. 구슬, 고리, 재료 등)"),
    material: Optional[str] = Query(None, description="재질은 한글로 적어주세요 (ex. 아연합금, 아크릴)"),
    min_price: Optional[int] = Query(None, description="최소가격(단위: 원)은 0이상의 정수로 적어주세요"),
    max_price: Optional[int] = Query(None, description="최대가격(단위: 원)은 0이상의 정수로 적어주세요"),
    min_amount: Optional[int] = Query(None, description="최소수량(단위: 개)은 0이상의 정수로 적어주세요"),
    max_amount: Optional[int] = Query(None, description="최대수량(단위: 개)은 0이상의 정수로 적어주세요"),
):
    filtered_data = []

    for item in keyring_accessories_data:
        if (
            item[0] == name and
            item[1] == category and
            (material is None or item[2] == material) and
            (min_price is None or item[3] >= min_price) and
            (max_price is None or item[3] <= max_price) and
            (min_amount is None or item[4] >= min_amount) and
            (max_amount is None or item[4] <= max_amount)
        ):
            filtered_data.append({
                "name": item[0],
                "category": item[1],
                "material": item[2],
                "price": item[3],
                "amount": item[4]
            })

    return filtered_data

handmade_accessories_data = [
    ["노방 곱창밴드", "조앤블루", "헤어악세사리", "천", 9900, True],
    ["해바라기 원석 귀걸이", "디에스타", "귀걸이", "원석", 29900, True],
    ["해파리 투명 귀걸이", "함초롱", "귀걸이", "아크릴", 19900, True],
    ["실버 담수진주 목걸이", "르블랑", "목걸이", "담수진주", 39900, False],
    ["써지컬 에리얼 목걸이", "바다바다", "목걸이", "서지컬스틸", 29900, True]
]

@app.get("/handmade_accessories")
async def filter_handmade_accessories(
    name: str = Query(..., description="상품명은 한글로 적어주세요 (ex. 노방 곱창밴드, 써지컬 에리얼 목걸이 등)"),
    a_name: Optional[str] = Query(None, description="작가명은 한글로 적어주세요 (ex. 조앤블루, 함초롱, 바다바다 등)"),
    category: str = Query(..., description="악세사리종류를 한글로 적어주세요 (ex. 귀걸이, 반지, 팔찌 등)"),
    material: Optional[str] = Query(None, description="재질을 한글로 적어주세요 (ex. 천, 원석, 아크릴 등)"),
    min_price: Optional[int] = Query(None, description="최소가격(단위: 원)은 0이상의 정수로 적어주세요"),
    max_price: Optional[int] = Query(None, description="최대가격(단위: 원)은 0이상의 정수로 적어주세요"),
    available: Optional[bool] = Query(None, description="판매여부를 알기 위해 판매하는 상품을 원하시면 True, 그렇지 않으시면 False를 적어주세요"),
):
    filtered_data = []

    for item in handmade_accessories_data:
        if (
            item[0] == name and
            (a_name is None or item[1] == a_name) and
            item[2] == category and
            (material is None or item[3] == material) and
            (min_price is None or item[4] >= min_price) and
            (max_price is None or item[4] <= max_price) and
            (available is None or item[5] == available)
        ):
            filtered_data.append({
                "name": item[0],
                "a_name": item[1],
                "category": item[2],
                "material": item[3],
                "price": item[4],
                "available": item[5]
            })

    return filtered_data

cpu_water_cooler_data = [
    ["DEEPCOOL", "LT720", 5, 140, "블랙", 176100, "2022.11"],
    ["DEEPCOOL", "LT520", 5, 120, "화이트", 158900, "2022.11"],
    ["NZXT", "KRAKEN ELITE 360 RGB", 6, 120, "화이트", 447100, "2023.04"],
    ["NZXT", "NZXT KRAKEN ELITE 240 RGB", 6, 120, "블랙", 365000, "2023.03"],
    ["VALKYRIE", "GL360 ARGB", 5, 140, "화이트", 170100, "2023.06"]
]

@app.get("/cpu_water_cooler")
async def filter_cpu_water_cooler(
    brand: str = Query(..., description="제조사는 영어 대문자로 적어주세요 (ex. DEEPCOOL, NZXT 등)"),
    name: Optional[str] = Query(None, description="제품명은 영어 대문자와 숫자를 사용해 적어주세요 (ex. LT720, KRAKEN ELITE 360 RGB 등)"),
    warranty: Optional[int] = Query(None, description="보증기간은 0이상의 정수로 적어주세요 (ex. 3, 5 등)"),
    size: Optional[float] = Query(None, description="팬크기(단위: mm)는 실수로 적어주세요 (ex. 140, 120.5 등)"),
    color: Optional[str] = Query(None, description="색상은 한글로 적어주세요 (ex. 화이트, 블랙 등)"),
    min_price: Optional[int] = Query(None, description="최소가격(단위: 원)은 0이상의 정수로 적어주세요"),
    max_price: Optional[int] = Query(None, description="최대가격(단위: 원)은 0이상의 정수로 적어주세요"),
    date: Optional[str] = Query(None, description="등록년월은 2023.03의 양식으로 적어주세요"),
):
    filtered_data = []

    for item in cpu_water_cooler_data:
        if (
            item[0] == brand and
            (name is None or item[1] == name) and
            (warranty is None or item[2] == warranty) and
            (size is None or item[3] == size) and
            (color is None or item[4] == color) and
            (min_price is None or item[5] >= min_price) and
            (max_price is None or item[5] <= max_price) and
            (date is None or item[6] == date)
        ):
            filtered_data.append({
                "brand": item[0],
                "name": item[1],
                "warranty": item[2],
                "size": item[3],
                "color": item[4],
                "price": item[5],
                "date": item[6]
            })

    return filtered_data

baby_tactile_books_data = [
    ["졸리베이비 블레이매트 헝겊책", 0, True, 39500, "서로 다른 촉감과 소리로 동물 놀이를 할 수 있어요"],
    ["내 친구 코야 오감발달", 3, True, 27500, "코끼리 모양의 헝겊책으로 삑삑이와 방울이 들어있어요"],
    ["아기 촉감 초점책 세트", 6, False, 30500, "방수 원단으로 세탁이 편리해요"],
    ["플레이 퍼니 공룡", 12, False, 19500, "공룡을 좋아하는 아동에게 딱"],
    ["꿈꾸는 달팽이", 3, True, 19200, "달팽이 인형 모양으로 휴대도 세탁도 편리해요"]
]

@app.get("/baby_tactile_books")
async def filter_baby_tactile_books(
    name: Optional[str] = Query(None, description="상품명은 한글로 적어주세요 (ex. 졸리베이비 블레이매트 헝겊책, 아기 촉감 초점책 세트)"),
    age: int = Query(..., description="최소연령(단위: 개월)은 0이상의 정수로 적어주세요 단, 신생아는 0개월로 적어주세요"),
    kc: Optional[bool] = Query(None, description="KC인증여부를 알기 위해 KC인증된 유아 촉감책을 원하시면 True, 그렇지 않으시면 False를 적어주세요"),
    min_price: Optional[int] = Query(None, description="최소가격(단위: 원)은 0이상의 정수로 적어주세요"),
    max_price: Optional[int] = Query(None, description="최대가격(단위: 원)은 0이상의 정수로 적어주세요"),
):
    filtered_data = []

    for item in baby_tactile_books_data:
        if (
            (name is None or item[0] == name) and
            item[1] == age and
            (kc is None or item[2] == kc) and
            (min_price is None or item[3] >= min_price) and
            (max_price is None or item[3] <= max_price)
        ):
            filtered_data.append({
                "name": item[0],
                "age": item[1],
                "kc": item[2],
                "price": item[3],
                "desc": item[4]
            })

    return filtered_data

fabric_data = [
    ["플라워", "스텔라민트 기모", "면", 20, 8900, "110X90"],
    ["일러스트", "베이킹 레시피", "면", 30, 8200, "110X90"],
    ["플라워", "하바나 다마스크", "린넨", 40, 14900, "140X90"],
    ["기하학", "비비드 체크", "옥스포드면", 60, 32900, "140X90"],
    ["무지", "마시멜로우", "옥스포드면", 40, 28900, "1410X90"]
]

@app.get("/fabric")
async def filter_fabric(
    print_c: str = Query(..., description="프린트종류는 한글로 적어주세요 (ex. 플라워, 패치, 기하학, 일러스트, 무지 등)"),
    name: Optional[str] = Query(None, description="상품명은 한글로 적어주세요 (ex. 스텔라민트 기모, 베이킹 레시피)"),
    material: Optional[str] = Query(None, description="소재는 한글로 적어주세요 (ex. 면, 린넨 등)"),
    thickness: Optional[int] = Query(None, description="두께감(단위: 수)는 정수로 적어주세요 (ex. 11, 12, 13 등)"),
    min_price: Optional[int] = Query(None, description="최소가격(단위: 원)은 0이상의 정수로 적어주세요"),
    max_price: Optional[int] = Query(None, description="최대가격(단위: 원)은 0이상의 정수로 적어주세요"),
    size: Optional[str] = Query(None, description="크기(단위: cm)는 1410X90(가로X세로)의 양식으로 적어주세요"),
):
    filtered_data = []

    for item in fabric_data:
        if (
            item[0] == print_c and
            (name is None or item[1] == name) and
            (material is None or item[2] == material) and
            (thickness is None or item[3] == thickness) and
            (min_price is None or item[4] >= min_price) and
            (max_price is None or item[4] <= max_price) and
            (size is None or item[5] == size)
        ):
            filtered_data.append({
                "print_c": item[0],
                "name": item[1],
                "material": item[2],
                "thickness": item[3],
                "price": item[4],
                "size": item[5]
            })

    return filtered_data

fabric_diy_kit_data = [
    ["키티버니 스크런치 키트", "스크런치", 1, 8000, ["고무줄", "원단 2종", "설명서"]],
    ["밀러블랙 북커버 키트", "북커버", 2, 23000, ["원단 3종", "설명서"]],
    ["그레이키티 앞치마 키트", "앞치마", 4, 38000, ["원단 2종", "설명서", "조임끈"]],
    ["포니 헝겊책 키트", "헝겊책", 5, 32000, ["솜", "원단 8종", "버튼 4종", "설명서"]],
    ["옐로우 컵받침 키트", "컵받침", 2, 10000, ["원단 4종", "설명서"]]
]

@app.get("/fabric_diy_kit")
async def filter_fabric_diy_kit(
    name: Optional[str] = Query(None, description="상품명은 한글로 적어주세요 (ex. 키티버니 스크런치 키트, 밀러블랙 북커버 키트 등)"),
    category: str = Query(..., description="종류는 한글로 적어주세요 (ex. 파우치, 앞지마 등)"),
    min_difficulty: Optional[int] = Query(None, description="최소난이도는 1~5 사이의 정수로 적어주세요", ge=1, le=5),
    max_difficulty: Optional[int] = Query(None, description="최대난이도는 1~5 사이의 정수로 적어주세요", ge=1, le=5),
    min_price: Optional[int] = Query(None, description="최소가격(단위: 원)은 0이상의 정수로 적어주세요", ge=0),
    max_price: Optional[int] = Query(None, description="최대가격(단위: 원)은 0이상의 정수로 적어주세요", ge=0),
    components: Optional[int] = Query(None, description="구성품은 한글과 숫자를 사용해 적어주세요 (ex. 조임끈, 설명서, 원단 3종 등)", ge=0)
):
    filtered_data = []

    for item in fabric_diy_kit_data:
        if (
            item[1] == category and
            (name is None or item[0] == name) and
            (min_difficulty is None or item[2] >= min_difficulty) and
            (max_difficulty is None or item[2] <= max_difficulty) and
            (min_price is None or item[3] >= min_price) and
            (max_price is None or item[3] <= max_price) and
            (components is None or len(item[4]) == components)
        ):
            filtered_data.append({
                "name": item[0],
                "category": item[1],
                "difficulty": item[2],
                "price": item[3],
                "components": item[4]
            })

    return filtered_data

woodwork_diy_kit_data = [
    ["고무나무 둥근손잡이케리어 만들기", "수납함", 2, 16000, "공구함이나 소품 보관함으로 사용하기 좋은 케리어"],
    ["미니 사다리 선반 만들기", "선반", 2, 38000, "초등학생도 할 수 있는 사다리 선반 만들기 키트"],
    ["스메그 수납장 만들기", "수납장", 4, 88000, "경첩이 있는 원목 수납장 만들기"],
    ["호두나무 벽선반 키트", "선반", 3, 52000, "레트로한 분위기의 벽선반 만들기"],
    ["천연 도마 만들기", "도마", 1, 30000, "도마 가공과 관리법을 배울 수 있는 키트"]
]

@app.get("/woodwork_diy_kit")
async def filter_woodwork_diy_kit(
    name: Optional[str] = Query(None, description="상품명은 한글로 적어주세요 (ex. 고무나무 둥근손잡이케리어 만들기, 미니 사다리 선반 만들기)"),
    category: str = Query(..., description="종류는 한글로 적어주세요 (ex. 수납장, 선반 등)"),
    min_difficulty: Optional[int] = Query(None, description="최소난이도는 1~5 사이의 정수로 적어주세요", ge=1, le=5),
    max_difficulty: Optional[int] = Query(None, description="최대난이도는 1~5 사이의 정수로 적어주세요", ge=1, le=5),
    min_price: Optional[int] = Query(None, description="최소가격(단위: 원)은 0이상의 정수로 적어주세요", ge=0),
    max_price: Optional[int] = Query(None, description="최대가격(단위: 원)은 0이상의 정수로 적어주세요", ge=0)
):
    filtered_data = []

    for item in woodwork_diy_kit_data:
        if (
            item[1] == category and
            (name is None or item[0] == name) and
            (min_difficulty is None or item[2] >= min_difficulty) and
            (max_difficulty is None or item[2] <= max_difficulty) and
            (min_price is None or item[3] >= min_price) and
            (max_price is None or item[3] <= max_price)
        ):
            filtered_data.append({
                "name": item[0],
                "category": item[1],
                "difficulty": item[2],
                "price": item[3],
                "desc": item[4]
            })

    return filtered_data

desiccant_data = [
    ["리플러스 습기제거제 대용량", "용기형", "염화칼슘", 18900, "저렴해서 좋아요"],
    ["살림백서 옷걸이 습기제거제", "걸이형", "염화칼슘", 13900, "제습 효과가 좋네요"],
    ["에코후레쉬 반영구 제습제", "봉지형", "제올라이트", 9900, "재사용이 되는 상품 좋네요"],
    ["지누지누 식품용 제습제", "봉지형", "실리카겔", 9750, "장마철에는 필수"],
    ["부케가르니 서랍형 습기제거제", "봉지형", "염화칼슘", 11900, "향기도 좋네요"]
]

@app.get("/desiccant")
async def filter_desiccant(
    name: Optional[str] = Query(None, description="상품명은 한글로 적어주세요 (ex. 리플러스 습기제거제 대용량, 살림백서 옷걸이 습기제거제 등)"),
    category: str = Query(..., description="형태는 한글로 적어주세요 (ex. 용기형, 걸이형, 봉지형)"),
    component: Optional[str] = Query(None, description="주성분을 한글로 적어주세요 (ex. 염화칼슘, 제올라이트 등)"),
    min_price: Optional[int] = Query(None, description="최소가격(단위: 원)은 0이상의 정수로 적어주세요", ge=0),
    max_price: Optional[int] = Query(None, description="최대가격(단위: 원)은 0이상의 정수로 적어주세요", ge=0)
):
    filtered_data = []

    for item in desiccant_data:
        if (
            item[1] == category and
            (name is None or item[0] == name) and
            (component is None or item[2] == component) and
            (min_price is None or item[3] >= min_price) and
            (max_price is None or item[3] <= max_price)
        ):
            filtered_data.append({
                "name": item[0],
                "category": item[1],
                "component": item[2],
                "price": item[3],
                "review": item[4]
            })

    return filtered_data

honey_data = [
    ["스틱허니 세트", "벌꿀", 28000, True, "간편하게 휴대할 수 있는 스틱형 벌꿀"],
    ["천연 화분 허니자", "화분", 428000, True, "천연 비타민인 꽃가루, 예쁜 병에 담겨 선물용으로도 좋아요"],
    ["달콤촉촉 립허니", "화장품", 18000, True, "꿀이 가득 들어간 립글로스"],
    ["레몬 단꿀비누", "비누", 68000, False, "수제 비누로 1년 이내에 사용을 권장합니다"],
    ["보틀허니 세트", "벌꿀", 82000, True, "큰 용량의 보틀 허니, 선물로 좋아요"]
]

@app.get("/honey")
async def filter_honey(
    name: Optional[str] = Query(None, description="상품명은 한글로 적어주세요 (ex. 스틱허니 세트, 천연 화분 허니자)"),
    category: str = Query(..., description="상품종류는 한글로 적어주세요 (ex. 벌꿀, 화분, 비누, 화장품 등)"),
    min_price: Optional[int] = Query(None, description="최소가격(단위: 원)은 0이상의 정수로 적어주세요", ge=0),
    max_price: Optional[int] = Query(None, description="최대가격(단위: 원)은 0이상의 정수로 적어주세요", ge=0),
    gift_wrapping: Optional[bool] = Query(None, description="선물포장가능여부를 알기 위해 선물포장이 가능한 상품을 원하시면 True, 그렇지 않으시면 False를 적어주세요")
):
    filtered_data = []

    for item in honey_data:
        if (
            item[1] == category and
            (name is None or item[0] == name) and
            (min_price is None or item[2] >= min_price) and
            (max_price is None or item[2] <= max_price) and
            (gift_wrapping is None or item[3] == gift_wrapping)
        ):
            filtered_data.append({
                "name": item[0],
                "category": item[1],
                "price": item[2],
                "gift_wrapping": item[3],
                "desc": item[4]
            })

    return filtered_data

laundry_detergent_data = [
    ["르주르 찬물 세제", "가루", ["통돌이"], 10000, 18000, "세정력이 뛰어나고 찬물에도 잘 녹는 가루 세제"],
    ["노마인드 캡슐 포우디향", "캡슐", ["통돌이", "드럼"], 420, 15600, "상쾌한 향으로 섬유유연제가 없어도 부드러운 세제"],
    ["카포트 고농축 브라이트닝", "캡슐", ["드럼"], 1000, 28000, "흰 빨래를 더욱 하얗게"],
    ["다우니 살귤파워", "액체", ["통돌이", "드럼"], 4000, 17500, "꿉꿉한 냄새 없이 살균하자"],
    ["홈토피아 베이비 세제", "액체", ["통돌이", "드럼"], 2700, 38000, "천연유래물로 더욱 안심"]
]

@app.get("/laundry_detergent")
async def filter_laundry_detergent(
    name: Optional[str] = Query(None, description="상품명은 한글로 적어주세요 (ex. 르주르 찬물 세제, 노마인드 캡슐 포우디향)"),
    formula: str = Query(..., description="제형은 한글로 적어주세요 (ex. 액체, 가루, 캡슐 등)"),
    washing_machine: Optional[str] = Query(None, description="세탁기유형을 한글로 적어주세요 (ex. 통돌이, 드럼)"),
    min_amount: Optional[float] = Query(None, description="최소용량(단위: mL)을 0이상의 실수로 적어주세요", ge=0),
    max_amount: Optional[float] = Query(None, description="최대용량(단위: mL)을 0이상의 실수로 적어주세요", ge=0),
    min_price: Optional[int] = Query(None, description="최소가격(단위: 원)은 0이상의 정수로 적어주세요", ge=0),
    max_price: Optional[int] = Query(None, description="최대가격(단위: 원)은 0이상의 정수로 적어주세요", ge=0)
):
    filtered_data = []

    for item in laundry_detergent_data:
        if (
            item[1] == formula and
            (name is None or item[0] == name) and
            (washing_machine is None or washing_machine in item[2]) and
            (min_amount is None or item[3] >= min_amount) and
            (max_amount is None or item[3] <= max_amount) and
            (min_price is None or item[4] >= min_price) and
            (max_price is None or item[4] <= max_price)
        ):
            filtered_data.append({
                "name": item[0],
                "formula": item[1],
                "washing_machine": item[2],
                "amount": item[3],
                "price": item[4],
                "desc": item[5]
            })

    return filtered_data

pierce_data = [
    ["로탈라 골드볼", "귓볼", "14K", "침형", 14900, "볼"],
    ["모던 데일리 샤이닝", "귓볼", "실버", "침형", 8900, "스터드"],
    ["심플 원터치", "이너컨츠", "실버", "원터치형", 10900, "링"],
    ["레이어드 피어싱", "아웃컨츠", "써지컬스틸", "파이프형", 11900, "볼드"],
    ["프리스카제이 스틱", "귓바퀴", "14K", "후크형", 14900, "드롭"]
]

@app.get("/pierce")
async def filter_pierce(
    name: Optional[str] = Query(None, description="상품명을 한글로 적어주세요 (ex. 로탈라 골드볼, 프리스카제이 스틱)"),
    wearing: Optional[str] = Query(None, description="착용위치을 한글로 적어주세요 (ex. 귓볼, 이너컨츠)"),
    material: str = Query(..., description="소재를 한글, 영어, 숫자를 사용해 적어주세요 (ex. 14K, 실버, 써지컬스틸)"),
    shape: Optional[str] = Query(None, description="침형태를 한글로 적어주세요 (ex. 침형, 원터치형)"),
    min_price: Optional[int] = Query(None, description="최소가격(단위: 원)은 0이상의 정수로 적어주세요", ge=0),
    max_price: Optional[int] = Query(None, description="최대가격(단위: 원)은 0이상의 정수로 적어주세요", ge=0)
):
    filtered_data = []

    for item in pierce_data:
        if (
            item[2] == material and
            (name is None or item[0] == name) and
            (wearing is None or item[1] == wearing) and
            (shape is None or item[3] == shape) and
            (min_price is None or item[4] >= min_price) and
            (max_price is None or item[4] <= max_price)
        ):
            filtered_data.append({
                "name": item[0],
                "wearing": item[1],
                "material": item[2],
                "shape": item[3],
                "price": item[4],
                "design": item[5]
            })

    return filtered_data

imported_wallpaper_data = [
    ["안드레아", ["앤틱", "빈티지", "플로럴"], "그린", 186000, 52],
    ["리넨라인", ["모던", "빈티지", "스트라이프"], "아이보리", 126000, 53],
    ["페이퍼아트", ["네추럴", "모던", "기하학"], "옐로우", 386000, 91],
    ["콘도라", ["앤틱", "빈티지", "모던"], "화이트", 486000, 371],
    ["리보코", ["앤틱", "빈티지", "플로럴", "아티스틱"], "블랙", 546000, 265]
]

@app.get("/imported_wallpaper")
async def filter_imported_wallpaper(
    name: Optional[str] = Query(None, description="상품명을 한글로 적어주세요 (ex. 안드레아, 리넨라인 등)"),
    category: Optional[List[str]] = Query(None, description="디자인종류를 한글로 적어주세요 (ex. 빈티지, 모던)"),
    color: str = Query(..., description="색상을 한글로 적어주세요 (ex. 그린, 화이트)"),
    min_price: Optional[int] = Query(None, description="최소가격(단위: 원)은 0이상의 정수로 적어주세요", ge=0),
    max_price: Optional[int] = Query(None, description="최대가격(단위: 원)은 0이상의 정수로 적어주세요", ge=0)
):
    filtered_data = []

    for item in imported_wallpaper_data:
        if (
            item[2] == color and
            (name is None or item[0] == name) and
            (category is None or all(cat in item[1] for cat in category)) and
            (min_price is None or item[3] >= min_price) and
            (max_price is None or item[3] <= max_price)
        ):
            filtered_data.append({
                "name": item[0],
                "category": item[1],
                "color": item[2],
                "price": item[3],
                "size": item[4]
            })

    return filtered_data


cutting_board_data = [
    ["에피큐리언", "원목", "직사각형", "S", False, 50000],
    ["도블레", "실리콘", "원형", "M", False, 48000],
    ["모도리", "월넛", "직사각형", "L", True, 120000],
    ["조셉조셉", "스테인리스스틸", "사각형", "M", True, 13000],
    ["실리트", "월넛", "피자보드형", "S", False, 99000]
]

@app.get("/cuttingboard")
async def filter_cuttingboard(
    brand: str = Query(..., description="브랜드(예:에피큐리언,도블레,모도리등)"),
    material: Optional[str] = Query(None, description="재질(예:원목,실리콘,월넛,스테인리스스틸등)"),
    shape: Optional[str] = Query(None, description="형태(예:직사각형,원형,피자보드형등)"),
    size: Optional[str] = Query(None, description="크기(예:S,M,L등)"),
    price: Optional[int] = Query(None, description="가격(단위: 원)은 0이상의 정수로 적어주세요", ge=0)
):
    filtered_data = []

    for item in cutting_board_data:
        if (
            item[0] == brand and
            (material is None or material in item[1]) and
            (shape is None or shape == item[2]) and
            (size is None or size == item[3]) and
            (price is None or item[5] <= price)
        ):
            filtered_data.append({
                "brand": item[0],
                "material": item[1],
                "shape": item[2],
                "size": item[3],
                "sterilization": item[4],
                "price": item[5]
            })

    return filtered_data

food_tray_data = [
    ["시샘", "스테인리스스틸", "다이어트용", "S", True, False],
    ["네스틱", "세라믹", "가정용", "M", True, False],
    ["도노도노", "유리", "전자레인지용", "S", False, True],
    ["아이사랑", "유리", "유아용", "S", True, True],
    ["모윰", "플라스틱", "성인용", "L", True, False]
]

@app.get("/foodtray")
async def filter_foodtray(
    brand: str = Query(..., description="브랜드(예:시샘,네스틱,도노도노,아이사랑등)"),
    material: Optional[str] = Query(None, description="재질(예:스테인리스스틸,세라믹,유리,플라스틱등)"),
    use: Optional[str] = Query(None, description="용도(예:다이어트,가정용,전자레인지,성인등)"),
    size: Optional[str] = Query(None, description="크기(예:S,M,L등)"),
    freeshipping: Optional[bool] = Query(None, description="무료배송유무")
):
    filtered_data = []

    for item in food_tray_data:
        if (
            item[0] == brand and
            (material is None or material == item[1]) and
            (use is None or use == item[2]) and
            (size is None or size == item[3]) and
            (freeshipping is None or freeshipping == item[4])
        ):
            filtered_data.append({
                "brand": item[0],
                "material": item[1],
                "use": item[2],
                "size": item[3],
                "sterilization": item[5]
            })

    return filtered_data

apron_data = [
    ["리넨", "노란색", 130, "꽃무늬", True, "카페"],
    ["면", "초록색", 100, "레이스", True, "미용실"],
    ["폴리에스테르", "흰색", 120, "민무늬", False, "여름"],
    ["비닐", "투명", 150, "민무늬", True, "미술"],
    ["광목", "감색", 140, "레터링", False, "카페"]
]

@app.get("/apron")
async def filter_apron(
    material: str = Query(..., description="재질(예:리넨,면,폴리에스테르,비닐,광목등)"),
    color: Optional[str] = Query(None, description="색상(예:노란색,하늘색,흰색,회색등)"),
    length: Optional[int] = Query(None, description="길이(예:100,130,150cm등)"),
    pattern: Optional[str] = Query(None, description="패턴(예:꽃무늬,레이스,민무늬,레터링등)"),
    use: Optional[str] = Query(None, description="용도(예:카페,여름,미용실 등)")
):
    filtered_data = []

    for item in apron_data:
        if (
            item[0] == material and
            (color is None or color == item[1]) and
            (length is None or length == item[2]) and
            (pattern is None or pattern == item[3]) and
            (use is None or use == item[5])
        ):
            filtered_data.append({
                "material": item[0],
                "color": item[1],
                "length": item[2],
                "pattern": item[3],
                "waterproof": item[4],
                "use": item[5]
            })

    return filtered_data

stroller_data = [
    [2, 4, "오이스터", 3, 3, False],
    [3, 7, "부가부", 4, 2, False],
    [4, 8, "실버크로스", 3, 2, True],
    [4, 7, "스토케", 4, 3, True],
    [5, 10, "스토케", 3, 5, False]
]

@app.get("/stroller")
async def filter_stroller(
    age: int = Query(..., description="사용연령(예:3,4,5살등)"),
    weight: Optional[int] = Query(None, description="하중(예 4,5,6kg등)"),
    brand: Optional[str] = Query(None, description="브랜드 (예:오이스터,부가부,실버크로스,스토케등)"),
    safe: Optional[int] = Query(None, description="안전성 (최소1~최대5)"),
    folding: Optional[bool] = Query(None, description="접이식 유무")
):
    filtered_data = []

    for item in stroller_data:
        if (
            item[0] == age and
            (weight is None or weight == item[1]) and
            (brand is None or brand == item[2]) and
            (safe is None or safe == item[3]) and
            (folding is None or folding == item[5])
        ):
            filtered_data.append({
                "age": item[0],
                "weight": item[1],
                "brand": item[2],
                "safe": item[3],
                "convenience": item[4],
                "folding": item[5]
            })

    return filtered_data

clipon_data = [
    ["윙블링", "14k", "골드", "링", False, "원터치형"],
    ["로이드", "14k", "핑크", "이어커프", True, "침형"],
    ["볼라레", "은", "실버", "체인", False, "파이프형"],
    ["미니골드", "진주", "골드", "드롭", True, "관통형"],
    ["수스다", "14k", "골드", "링", True, "후크형"]
]

@app.get("/clipon")
async def filter_clipon(
    brand: str = Query(..., description="브랜드(예:윙블링,로이드등)"),
    material: Optional[str] = Query(None, description="재질(예:14K,은, 진주등)"),
    color: Optional[str] = Query(None, description="색깔(예:골드,실버,핑크등)"),
    style: Optional[str] = Query(None, description="스타일(예:링,이어커프,드롭등)"),
    pinshape: Optional[str] = Query(None, description="침형태(예:관통형,침형,파이프형 등)")
):
    filtered_data = []

    for item in clipon_data:
        if (
            item[0] == brand and
            (material is None or material.lower() == item[1]) and
            (color is None or color.lower() == item[2]) and
            (style is None or style.lower() == item[3]) and
            (pinshape is None or pinshape.lower() == item[5])
        ):
            filtered_data.append({
                "brand": item[0],
                "material": item[1],
                "color": item[2],
                "style": item[3],
                "freeshipping": item[4],
                "pinshape": item[5]
            })

    return filtered_data

necklace_data = [
    ["스와로브스키", "십자가", "14k", "골드", False, False],
    ["판도라", "탄생석", "은", "실버", False, True],
    ["비비안웨스트우드", "펜던트", "써지컬스틸", "실버", False, True],
    ["스톤헨지", "장식없음", "14k", "골드", True, False],
    ["로이드", "코인", "가죽", "브라운", False, True]
]

@app.get("/necklace")
async def filter_necklace(
    brand: str = Query(..., description="브랜드(예:스와로브스키,비비안웨스트우드,판도라등)"),
    decorate: Optional[str] = Query(None, description="주요장식(예:하트,탄생석,십자가등)"),
    material: Optional[str] = Query(None, description="주요소재(예:가죽,레이스,14k등)"),
    color: Optional[str] = Query(None, description="색깔(골드,실버,브라운 등)"),
    freeshipping: Optional[bool] = Query(None, description="무료배송여부")
):
    filtered_data = []

    for item in necklace_data:
        if (
            item[0] == brand and
            (decorate is None or decorate.lower() == item[1]) and
            (material is None or material.lower() == item[2]) and
            (color is None or color.lower() == item[3]) and
            (freeshipping is None or freeshipping == item[5])
        ):
            filtered_data.append({
                "brand": item[0],
                "decorate": item[1],
                "material": item[2],
                "color": item[3],
                "discount": item[4],
                "freeshipping": item[5]
            })

    return filtered_data

juice_data = [
    ["돈시몬", "오렌지", "페트병", 200, False, False],
    ["델몬트", "감귤", "종이팩", 350, True, False],
    ["미닛메이드", "사과", "유리병", 500, True, True],
    ["썬키스트", "배", "파우치", 350, False, True],
    ["델몬트", "오렌지", "유리병", 500, False, False]
]

@app.get("/juice")
async def filter_juice(
    brand: str = Query(..., description="브랜드(예:돈시몬,델몬트,미닛메이드,썬키스트등)"),
    taste: Optional[str] = Query(None, description="맛(예:오렌지,감귤,사과,배등)"),
    type: Optional[str] = Query(None, description="용기타입(예:페트병,종이팩,유리병,파우치)"),
    capacity: Optional[int] = Query(None, description="용량(예:200,350,500ml 등)"),
    organic: Optional[bool] = Query(None, description="유기농여부")
):
    filtered_data = []

    for item in juice_data:
        if (
            item[0] == brand and
            (taste is None or taste.lower() == item[1]) and
            (type is None or type.lower() == item[2]) and
            (capacity is None or capacity == item[3]) and
            (organic is None or organic == item[5])
        ):
            filtered_data.append({
                "brand": item[0],
                "taste": item[1],
                "type": item[2],
                "capacity": item[3],
                "freeshipping": item[4],
                "organic": item[5]
            })

    return filtered_data

scratchpad_data = [
    ["모닝글로리", "스프링노트", "모눈", 2000, False, True],
    ["옥스포드", "제본노트", "라인", 3000, False, True],
    ["미래문화사", "스프링노트", "도트", 2500, True, False],
    ["인디고", "스프링노트", "무지", 3000, False, False],
    ["모닝글로리", "제보노트", "도트", 2000, False, True]
]

@app.get("/scratchpad")
async def filter_scratchpad(
    brand: str = Query(..., description="브랜드(예:모닝글로리, 옥스포드,미래문화사,인디고 등)"),
    kind: Optional[str] = Query(None, description="종류(예:스프링노트,제본노트 등)"),
    paper: Optional[str] = Query(None, description="내지(예:모눈,라인,도트,무지 등)"),
    price: Optional[int] = Query(None, description="가격(예: 2000원, 3000원, ~원)"),
    freeshipping: Optional[bool] = Query(None, description="무료배송여부")
):
    filtered_data = []

    for item in scratchpad_data:
        if (
            item[0] == brand and
            (kind is None or kind.lower() == item[1]) and
            (paper is None or paper.lower() == item[2]) and
            (price is None or price == item[3]) and
            (freeshipping is None or freeshipping == item[5])
        ):
            filtered_data.append({
                "brand": item[0],
                "kind": item[1],
                "paper": item[2],
                "price": item[3],
                "freeexchange": item[4],
                "freeshipping": item[5]
            })

    return filtered_data

thanknote_data = [
    ["인디고", "가죽", "A5", False, True, False],
    ["리훈", "하드커버", "A6", False, False, False],
    ["아이코닉", "인조가죽", "B6", True, True, True],
    ["바이풀디자인", "PVC", "A5", False, False, True],
    ["핑크풋", "종이", "A6", True, True, True]
]

@app.get("/thanknote")
async def filter_thanknote(
    brand: str = Query(..., description="브랜드(예:인디고, 리훈, 아이코닉,바이풀디자인 핑크풋 등)"),
    cover: Optional[str] = Query(None, description="커버재질(예:가죽, 하드커버,인조가죽,PVC,종이등)"),
    size: Optional[str] = Query(None, description="사이즈(예:A5,A6,B6등)"),
    freeshipping: Optional[bool] = Query(None, description="무료배송여부"),
    freeexchange: Optional[bool] = Query(None, description="무료교환반품여부")
):
    filtered_data = []

    for item in thanknote_data:
        if (
            item[0] == brand and
            (cover is None or cover.lower() == item[1]) and
            (size is None or size.lower() == item[2]) and
            (freeshipping is None or freeshipping == item[3]) and
            (freeexchange is None or freeexchange == item[5])
        ):
            filtered_data.append({
                "brand": item[0],
                "cover": item[1],
                "size": item[2],
                "freeshipping": item[3],
                "hotdeal": item[4],
                "freeexchange": item[5]
            })

    return filtered_data

clock_data = [
    ["플라이토", "양면", "원목", 1, False, False],
    ["레벤데코", "디지털", "메탈", 3, False, True],
    ["무아스", "양면", "합성목재", 2, True, False],
    ["카파", "LED", "메탈", 3, True, True],
    ["플라이토", "디지털", "ABS", 2, True, False]
]

@app.get("/clock")
async def filter_clock(
    brand: str = Query(..., description="브랜드(예:플라이토,레벤데코,무아스 등)"),
    kind: Optional[str] = Query(None, description="종류(예:양면,디지털,추 등)"),
    material: Optional[str] = Query(None, description="재질(예:원목,메탈,합성목재,ABS등)"),
    weight: Optional[int] = Query(None, description="무게(예 1kg, 2kg)"),
    nonoise: Optional[bool] = Query(None, description="무소음여부")
):
    filtered_data = []

    for item in clock_data:
        if (
            item[0] == brand and
            (kind is None or kind.lower() == item[1]) and
            (material is None or material.lower() == item[2]) and
            (weight is None or weight == item[3]) and
            (nonoise is None or nonoise == item[5])
        ):
            filtered_data.append({
                "brand": item[0],
                "kind": item[1],
                "material": item[2],
                "weight": item[3],
                "quickshipping": item[4],
                "nonoise": item[5]
            })

    return filtered_data

keyboard_data = [
    ["에이투", "기계식", "청축", False, False, True],
    ["로지텍", "멤브레인", "광축", True, True, True],
    ["앱코", "팬터그래프", "갈축", False, True, True],
    ["삼성전자", "멤브레인", "백축", False, False, True],
    ["한성컴퓨터", "무접점", "은축", False, True, True]
]

@app.get("/keyboard")
async def filter_keyboard(
    brand: str = Query(..., description="브랜드(예:에이투, 로지텍,앱코, 삼성전자 등)"),
    key: Optional[str] = Query(None, description="키방식(예:기계식,멤브레인,팬터그래프, 무접점)"),
    contact: Optional[str] = Query(None, description="접점방식(예:청축,광축,갈축 등)"),
    bluetooth: Optional[bool] = Query(None, description="블루투스여부"),
    freeexchange: Optional[bool] = Query(None, description="무료교환반품여부")
):
    filtered_data = []

    for item in keyboard_data:
        if (
            item[0] == brand and
            (key is None or key.lower() == item[1]) and
            (contact is None or contact.lower() == item[2]) and
            (bluetooth is None or bluetooth == item[3]) and
            (freeexchange is None or freeexchange == item[5])
        ):
            filtered_data.append({
                "brand": item[0],
                "key": item[1],
                "contact": item[2],
                "bluetooth": item[3],
                "freeshipping": item[4],
                "freeexchange": item[5]
            })

    return filtered_data

selfprotection_data = [
    ["스프레이", "샤네끄", "S", 10800, True, True],
    ["전기충격기", "세이버", "M", 35000, True, True],
    ["너클", "유나이티드", "S", 18000, False, False],
    ["가스총", "델파", "M", 40000, True, True],
    ["호신봉", "뉴엔", "L", 38000, False, False]
]

@app.get("/selfprotection")
async def filter_selfprotection(
    kind: str = Query(..., description="종류(예:스프레이,전기충격기,가스총 등)"),
    brand: Optional[str] = Query(None, description="브랜드(예:샤네끄,블랙코브라,세이버 등)"),
    size: Optional[str] = Query(None, description="사이즈(예: S,M,L)"),
    price: Optional[int] = Query(None, description="가격 (예: 10000원, 20000원 등)"),
    freeshipping: Optional[bool] = Query(None, description="무료배송여부")
):
    filtered_data = []

    for item in selfprotection_data:
        if (
            item[0] == kind and
            (brand is None or brand.lower() == item[1]) and
            (size is None or size.lower() == item[2]) and
            (price is None or price == item[3]) and
            (freeshipping is None or freeshipping == item[5])
        ):
            filtered_data.append({
                "kind": item[0],
                "brand": item[1],
                "size": item[2],
                "price": item[3],
                "freeexchange": item[4],
                "freeshipping": item[5]
            })

    return filtered_data

mouse_data = [
    ["에이투", "블루투스", "버티컬", "블랙", False],
    ["로지텍", "usb", "사무용", "실버", True],
    ["삼성전자", "블루투스", "인체공학", "화이트", False],
    ["마이크로소프트", "usb", "노트북용", "블랙", True],
    ["앱코", "블루투스", "게이밍", "실버", False]
]

@app.get("/mouse")
async def filter_mouse(
    brand: str = Query(..., description="브랜드(예:에이투,로지텍,삼성전자 등)"),
    transmission: Optional[str] = Query(None, description="전송방식(예:블루투스, usb 등)"),
    use: Optional[str] = Query(None, description="용도(예:버티컬, 사무용, 노트북용등)"),
    color: Optional[str] = Query(None, description="색상(예:블랙,실버,화이트 등)"),
    freeshipping: Optional[bool] = Query(None, description="무료배송여부")
):
    filtered_data = []

    for item in mouse_data:
        if (
            item[0] == brand and
            (transmission is None or transmission.lower() == item[1]) and
            (use is None or use.lower() == item[2]) and
            (color is None or color.lower() == item[3]) and
            (freeshipping is None or freeshipping == item[4])
        ):
            filtered_data.append({
                "brand": item[0],
                "transmission": item[1],
                "use": item[2],
                "color": item[3],
                "freeexchange": item[4]
            })

    return filtered_data

emerald_data = [
    ["에티오피아", 0.3, "녹색", False, False],
    ["멕시코", 0.2, "연두색", False, False],
    ["에티오피아", 0.7, "초록색", True, True],
    ["호주", 0.5, "연두색", False, True],
    ["미국", 0.6, "초록색", True, False]
]

@app.get("/emerald")
async def filter_emerald(
    origin: str = Query(..., description="원산지(예:에티오피아, 멕시코,호주 등)"),
    weight: Optional[float] = Query(None, description="크기: (예:0.3,0.5.0.7)"),
    color: Optional[str] = Query(None, description="색깔: (예:진한 초록색, 초록색, 연두색등)"),
    guarantee: Optional[bool] = Query(None, description="보증서여부"),
    freeshipping: Optional[bool] = Query(None, description="무료배송여부")
):
    filtered_data = []

    for item in emerald_data:
        if (
            item[0] == origin and
            (weight is None or weight == item[1]) and
            (color is None or color.lower() == item[2]) and
            (guarantee is None or guarantee == item[3]) and
            (freeshipping is None or freeshipping == item[4])
        ):
            filtered_data.append({
                "origin": item[0],
                "weight": item[1],
                "color": item[2],
                "guarantee": item[3],
                "freeexchange": item[4]
            })

    return filtered_data

earphone_data = [
    ["삼성전자", "3.5mm", "오픈형", 45000, False, True],
    ["AKG", "USB Type-c", "귀걸이형", 88000, True, True],
    ["소니", "라이트닝단자", "커널형", 63000, True, False],
    ["젠하이저", "마그네틱단자", "오픈형", 51000, False, True],
    ["아즈라", "라이트닝단자", "귀걸이형", 74000, False, True]
]

@app.get("/earphone")
async def filter_earphone(
    brand: str = Query(..., description="브랜드(예:삼성전자,AKG,소니,젠하이저,Shure,아즈라등)"),
    socket: Optional[str] = Query(None, description="단자(예:3.5mm, USB Type-c, 라이트닝단자, 마그네틱단자등)"),
    shape: Optional[str] = Query(None, description="형태(예: 오픈형, 귀걸이형, 커널형 등)"),
    price: Optional[int] = Query(None, description="가격 (예: 50000원, 60000원 등)"),
    freeshipping: Optional[bool] = Query(None, description="무료배송여부")
):
    filtered_data = []

    for item in earphone_data:
        if (
            item[0] == brand and
            (socket is None or socket.lower() == item[1].lower()) and
            (shape is None or shape.lower() == item[2].lower()) and
            (price is None or price == item[3]) and
            (freeshipping is None or freeshipping == item[4])
        ):
            filtered_data.append({
                "brand": item[0],
                "socket": item[1],
                "shape": item[2],
                "price": item[3],
                "freeshipping": item[4],
                "card": item[5]
            })

    return filtered_data

nonoise_earphone_data = [
    ["QCY", "넥밴드", "블루투스5.0", "블랙", False, False],
    ["갤럭시", "넥밴드", "블루투스4.2", "화이트", False, True],
    ["JBL", "귀걸이형", "블루투스3.0", "그레이", True, False],
    ["브리츠", "반커널형", "블루투스5.0", "레드", True, True],
    ["소니", "귀걸이형", "블루투스5.0", "화이트", True, False]
]

@app.get("/nonoise")
async def filter_nonoise(
    brand: str = Query(..., description="브랜드 (예: QCY,갤럭시, JBL, 브리츠, 소니 등)"),
    shape: Optional[str] = Query(None, description="형태 (예: 넥밴드, 귀걸이형,커널형, 반커널형 등)"),
    bluetooth: Optional[str] = Query(None, description="블루투스버전 (예: 블루투스5.0, 블루투스4.2,블루투스 3.0등)"),
    color: Optional[str] = Query(None, description="색깔 (예: 블랙,화이트,레드,그레이 등)"),
    freeshipping: Optional[bool] = Query(None, description="무료배송여부")
):
    filtered_data = []

    for item in nonoise_earphone_data:
        if (
            item[0] == brand and
            (shape is None or shape.lower() == item[1].lower()) and
            (bluetooth is None or bluetooth.lower() == item[2].lower()) and
            (color is None or color.lower() == item[3].lower()) and
            (freeshipping is None or freeshipping == item[4])
        ):
            filtered_data.append({
                "brand": item[0],
                "shape": item[1],
                "bluetooth": item[2],
                "color": item[3],
                "freeshipping": item[4],
                "card": item[5]
            })

    return filtered_data

drainingboard_data = [
    ["한샘", "1단", "수저통포함", "스테인리스스틸", False, True],
    ["밧드야", "1단", "컵걸이포함", "플라스틱", False, True],
    ["로긴", "2단", "받침대포함", "스테인리스스틸", True, True],
    ["아이넥스", "2단", "수저통포함", "스테인리스스틸", True, False],
    ["이케아", "3단이상", "받침대포함", "플라스틱", True, True]
]

@app.get("/drainingboard")
async def filter_drainingboard(
    brand: str = Query(..., description="브랜드 (예: 한샘, 밧드야, 로긴, 아이넥스, 제이비제이, 이케아 등)"),
    level: Optional[str] = Query(None, description="단수 (예: 1단, 2단, 3단이상등)"),
    feature: Optional[str] = Query(None, description="특징 (예: 수저통포함, 컵걸이포함, 받침대포함 등)"),
    material: Optional[str] = Query(None, description="재질 (예: 스테인리스스틸, 플라스틱 등)"),
    freeshipping: Optional[bool] = Query(None, description="무료배송여부")
):
    filtered_data = []

    for item in drainingboard_data:
        if (
            item[0] == brand and
            (level is None or level.lower() == item[1].lower()) and
            (feature is None or feature.lower() in item[2].lower()) and
            (material is None or material.lower() in item[3].lower()) and
            (freeshipping is None or freeshipping == item[4])
        ):
            filtered_data.append({
                "brand": item[0],
                "level": item[1],
                "feature": item[2],
                "material": item[3],
                "freeshipping": item[4],
                "card": item[5]
            })

    return filtered_data

doll_data = [
    ["젤리켓", "곰", "연노랑색", "면", True, True],
    ["이케아", "토끼", "연하늘색", "폴리에스테르", False, False],
    ["태기스", "코끼리", "연분홍색", "마", True, False],
    ["블랑가또", "병아리", "연노랑색", "면", False, True],
    ["베베라온", "공룡", "연초록색", "면", True, False]
]

@app.get("/doll")
async def filter_doll(
    brand: str = Query(..., description="브랜드 (예: 젤리캣, 이케아, 태기스, 블랑가또, 미피, 베베라온 등)"),
    shape: Optional[str] = Query(None, description="모양 (예: 곰, 토끼, 병아리, 상어, 코끼리, 공룡 등)"),
    color: Optional[str] = Query(None, description="색깔 (예: 연노랑색, 연하늘색, 연분홍색 등)"),
    material: Optional[str] = Query(None, description="재질 (예: 폴리에스테르, 면, 마 등)"),
    freeshipping: Optional[bool] = Query(None, description="무료배송여부")
):
    filtered_data = []

    for item in doll_data:
        if (
            item[0] == brand and
            (shape is None or shape.lower() == item[1].lower()) and
            (color is None or color.lower() in item[2].lower()) and
            (material is None or material.lower() in item[3].lower()) and
            (freeshipping is None or freeshipping == item[4])
        ):
            filtered_data.append({
                "brand": item[0],
                "shape": item[1],
                "color": item[2],
                "material": item[3],
                "freeshipping": item[4],
                "card": item[5]
            })

    return filtered_data

speaker_data = [
    ["브리츠", "게이밍스피커", 0.5, "그레이", False, True],
    ["마샬", "컴퓨터스피커", 5, "화이트", True, True],
    ["캔스톤", "노트북스피커", 15, "블랙", False, False],
    ["제네바", "컴퓨터스피커", 35, "화이트", True, True],
    ["오디오엔진", "게이밍스피커", 16, "그레이", False, False]
]

@app.get("/speaker")
async def filter_speaker(
    brand: str = Query(..., description="브랜드 (예: 브리츠, 마샬, 캔스톤, 제네바, 오디오엔진 등)"),
    use: Optional[str] = Query(None, description="용도 (예: 게이밍스피커, 컴퓨터스피커, 노트북스피커 등)"),
    output: Optional[str] = Query(None, description="정격출력 (0.5W, 5W, 16W 등)"),
    color: Optional[str] = Query(None, description="색상 (그레이, 브라운, 블랙, 화이트 등)"),
    freeshipping: Optional[bool] = Query(None, description="무료배송여부")
):
    filtered_data = []

    for item in speaker_data:
        if (
            item[0] == brand and
            (use is None or use.lower() == item[1].lower()) and
            (output is None or output == item[2]) and
            (color is None or color.lower() in item[3].lower()) and
            (freeshipping is None or freeshipping == item[4])
        ):
            filtered_data.append({
                "brand": item[0],
                "use": item[1],
                "output": item[2],
                "color": item[3],
                "freeshipping": item[4],
                "card": item[5]
            })

    return filtered_data

watercolor_pencil_data = [
    ["파버카스텔", 1, True, True, False, False],
    ["알파", 3, True, False, False, True],
    ["프리즈마칼라", 5, True, True, True, True],
    ["스테들러", 4, False, True, True, False],
    ["문화연필", 3, True, True, True, True]
]

@app.get("/watercolorpencil")
async def filter_watercolorpencil(
    brand: str = Query(..., description="브랜드 (예: 파버카스텔, 알파, 프리즈마칼라, 스테들러, 문화연필)"),
    color: Optional[int] = Query(None, description="발색력 (최소 1에서 최대 5까지)"),
    set: Optional[bool] = Query(None, description="세트여부"),
    single: Optional[bool] = Query(None, description="단품판매여부"),
    freeshipping: Optional[bool] = Query(None, description="무료배송여부")
):
    filtered_data = []

    for item in watercolor_pencil_data:
        if (
            item[0] == brand and
            (color is None or color == item[1]) and
            (set is None or set == item[2]) and
            (single is None or single == item[3]) and
            (freeshipping is None or freeshipping == item[4])
        ):
            filtered_data.append({
                "brand": item[0],
                "color": item[1],
                "set": item[2],
                "single": item[3],
                "freeshipping": item[4],
                "card": item[5]
            })

    return filtered_data

jam_data = [
    ["복음자리", "딸기", "수제", 100, False, False],
    ["오뚜기", "블루베리", "저당", 200, True, True],
    ["샹달프", "망고", "무설탕", 200, False, True],
    ["본마망", "땅콩", "일회용", 50, True, True],
    ["스머커즈", "복숭아", "스테비아", 400, False, True]
]

@app.get("/jam")
async def filter_jam(
    brand: str = Query(..., description="브랜드 (예: 복음자리, 오뚜기, 샹달프, 본마망, 스머커즈 등)"),
    tasta: Optional[str] = Query(None, description="맛 (예: 딸기, 블루베리, 망고, 땅콩, 복숭아 등)"),
    characteristic: Optional[str] = Query(None, description="특징 (예: 수제, 저당, 무설탕, 스테비아, 일회용 등)"),
    weight: Optional[int] = Query(None, description="중량 (예: 100, 200, 500, 1000 등)"),
    freeshipping: Optional[bool] = Query(None, description="무료배송여부")
):
    filtered_data = []

    for item in jam_data:
        if (
            item[0] == brand and
            (tasta is None or tasta == item[1]) and
            (characteristic is None or characteristic == item[2]) and
            (weight is None or weight == item[3]) and
            (freeshipping is None or freeshipping == item[4])
        ):
            filtered_data.append({
                "brand": item[0],
                "tasta": item[1],
                "characteristic": item[2],
                "weight": item[3],
                "freeshipping": item[4],
                "card": item[5]
            })

    return filtered_data

bodycare_data = [
    ["바이오더마 아토덤 울트라 크림", "바이오더마", "건성 및 극건성 피부", "바디크림", "프랑스"],
    ["피지오겔 레드 수딩 AI 바디로션", "피지오겔", "모든 피부", "바디로션", "태국"],
    ["에스트라 아토베리어365 바디로션", "에스트라", "모든 피부", "바디로션", "대한민국"],
    ["유리아쥬 EAU 실키바디로션", "유리아쥬", "모든 피부", "바디로션", "프랑스"],
    ["바이오더마 아토덤 PP밤", "바이오더마", "건성피부", "바디밤", "프랑스"]
]

@app.get("/Bodycare/")
async def filter_bodycare(
    name: str = Query(..., description="상품이름"),
    brand: Optional[str] = Query(None, description="브랜드"),
    capacity: Optional[int] = Query(None, description="용량 (예시: 10, 20)"),
    skintype: Optional[str] = Query(None, description="권장피부타입 (예시: 모든 피부, 건성 및 극건성 피부, 건성피부)"),
    type: Optional[str] = Query(None, description="제형 (예시: 바디크림, 바디로션, 바디밤)")
):
    filtered_data = []

    for item in bodycare_data:
        if (
            item[0] == name and
            (brand is None or brand == item[1]) and
            (capacity is None or capacity == item[2]) and
            (skintype is None or skintype == item[3]) and
            (type is None or type == item[4])
        ):
            filtered_data.append({
                "name": item[0],
                "brand": item[1],
                "skintype": item[2],
                "type": item[3],
                "manufacturing_country": item[4]
            })

    return filtered_data

lipmakeup_data = [
    ["웨이크메이크 워터 블러링 픽싱 틴트", "웨이크메이크", "립틴트", 3.5, "대한민국"],
    ["롬앤 쥬시 래스팅 틴트", "롬앤", "립틴트", 5.5, "대한민국"],
    ["MAC 맥 파우더 키스 립스틱", "맥", "립스틱", 3, "이탈리아"],
    ["헤라 루즈 홀릭", "헤라", "립스틱", 3, "대한민국"],
    ["MAC 러브 미 리퀴드 립컬러", "맥", "립글로스", 3.1, "벨기에"]
]

@app.get("/Lipmakeup/")
async def filter_lipmakeup(
    name: str = Query(None, description="상품이름"),
    brand: Optional[str] = Query(..., description="브랜드"),
    capacity: Optional[float] = Query(None, description="용량 (예시: 5.0, 5.5)"),
    manufacturer: Optional[str] = Query(None, description="제조사"),
    type: Optional[str] = Query(None, description="제품타입 (예시: 립틴트, 립스틱, 립글로즈)")
):
    filtered_data = []

    for item in lipmakeup_data:
        if (
            (name is None or item[0] == name) and
            brand == item[1] and
            (capacity is None or capacity == item[2]) and
            (manufacturer is None or manufacturer == item[3]) and
            (type is None or type == item[4])
        ):
            filtered_data.append({
                "name": item[0],
                "brand": item[1],
                "type": item[2],
                "capacity": item[3],
                "manufacturing_country": item[4]
            })

    return filtered_data

cleanser_data = [
    ["바이오더마 센시비오 H2O", "바이오더마", "클렌징워터", "민감 피부 및 모든 피부", "프랑스"],
    ["셀퓨전씨 약산성 패리어 클렌징 워터", "셀퓨전씨", "클렌징워터", "모든 피부", "대한민국"],
    ["아벤느 미셀라 클렌징 워터", "아벤느", "클렌징워터", "모든 피부", "프랑스"],
    ["에스트라 테라크네365 클리어 딥 클렌징 폼", "에스트라", "클렌징폼", "모든 피부", "대한민국"],
    ["셀퓨전씨 포스트 알파 pH밸런싱 젤 클렌저", "셀퓨전씨", "클렌징젤", "모든 피부", "대한민국"]
]

@app.get("/Cleanser/")
async def filter_cleanser(
    name: str = Query(..., description="상품이름"),
    brand: Optional[str] = Query(None, description="브랜드"),
    type: Optional[str] = Query(None, description="제품타입 (예시: 클렌징워터, 클렌징티슈, 클렌징폼)"),
    skintype: Optional[str] = Query(None, description="권장피부타입 (예시: 모든피부, 민감피부)"),
    capacity: Optional[int] = Query(None, description="용량 (예시: 850, 900)")
):
    filtered_data = []

    for item in cleanser_data:
        if (
            item[0] == name and
            (brand is None or brand == item[1]) and
            (type is None or type == item[2]) and
            (skintype is None or skintype == item[3]) and
            (capacity is None or capacity == item[4])
        ):
            filtered_data.append({
                "name": item[0],
                "brand": item[1],
                "type": item[2],
                "skintype": item[3],
                "manufacturing_country": item[4]
            })

    return filtered_data

maskpack_data = [
    ["피지오겔 레드수딩 AI 릴리프 마스크", "피지오겔", 1, "모든 피부", "대한민국"],
    ["셀퓨전씨 포스트 알파 퍼스트 쿨링 마스크", "셀퓨전씨", 5, "모든 피부", "대한민국"],
    ["리쥬란 힐러 스킨 프로텍션 마스크", "리쥬란", 5, "모든 피부", "대한민국"],
    ["닥터디퍼런트 더마 릴렉싱 마스크", "닥터디퍼런트", 5, "모든 피부", "대한민국"],
    ["퓨전씨 포스트 알파 시카 쿨링 마스크", "셀퓨전씨", 1, "모든 피부", "대한민국"]
]

@app.get("/Maskpack/")
async def filter_maskpack(
    name: str = Query(..., description="상품이름"),
    brand: str = Query(..., description="브랜드"),
    num_sheet: Optional[int] = Query(None, description="매수 (예시: 5, 10)"),
    manufacturer: Optional[str] = Query(None, description="제조사"),
    skintype: Optional[str] = Query(None, description="권장피부타입 (예시: 모든피부, 민감피부)")
):
    filtered_data = []

    for item in maskpack_data:
        if (
            item[0] == name and
            item[1] == brand and
            (num_sheet is None or num_sheet == item[2]) and
            (manufacturer is None or manufacturer == item[3]) and
            (skintype is None or skintype == item[4])
        ):
            filtered_data.append({
                "name": item[0],
                "brand": item[1],
                "num_sheet": item[2],
                "skintype": item[3],
                "manufacturing_country": item[4]
            })

    return filtered_data

sneakers_data = [
    ["나이키 디파이올데이", "나이키", 240, 300, 55000],
    ["올드스쿨", "반스", 220, 310, 55000],
    ["슬립스트림 Lth", "푸마", 220, 290, 45000],
    ["웨이브렛 오리지날 라이트", "휠라", 220, 280, 65000],
    ["포럼 로우", "아디다스", 225, 300, 129000]
]

@app.get("/Sneakers/")
async def filter_sneakers(
    name: str = Query(..., description="상품이름"),
    brand: Optional[str] = Query(None, description="브랜드"),
    min_size: Optional[int] = Query(None, description="최소사이즈 (예시: 230, 240)"),
    max_size: Optional[int] = Query(None, description="최대사이즈 (예시: 250, 260)"),
    freeshipping: Optional[bool] = Query(None, description="무료배송여부")
):
    filtered_data = []

    for item in sneakers_data:
        if (
            item[0] == name and
            (brand is None or brand == item[1]) and
            (min_size is None or min_size <= item[2]) and
            (max_size is None or max_size >= item[3]) and
            (freeshipping is None or freeshipping == True)
        ):
            filtered_data.append({
                "name": item[0],
                "brand": item[1],
                "min_size": item[2],
                "max_size": item[3],
                "price": item[4]
            })

    return filtered_data

leotard_data = [
    ["유미코 레오타드 다리아", "Yumiko", "끈", True, True],
    ["지댄스 레오타드 스트랩", "Zidans", "끈", False, True],
    ["인터메조 레오타드", "Intermezzo", "나시", False, True],
    ["웨어무어 레오타드 카르비올레", "Wear Moi", "나시", False, True],
    ["유미코 레오타드 마리케", "Yumiko", "나시", False, True]
]

@app.get("/Leotard/")
async def filter_leotard(
    name: str = Query(..., description="상품이름"),
    brand: Optional[str] = Query(None, description="브랜드"),
    type: Optional[str] = Query(None, description="유형 (예시: 끈, 나시)"),
    manufacturing_country: Optional[str] = Query(None, description="제조국가 (예시: 대한민국, 이탈리아)"),
    price: Optional[int] = Query(None, description="판매가")
):
    filtered_data = []

    for item in leotard_data:
        if (
            item[0] == name and
            (brand is None or brand == item[1]) and
            (type is None or type == item[2]) and
            (manufacturing_country is None or manufacturing_country == item[3]) and
            (price is None or price == item[4])
        ):
            filtered_data.append({
                "name": item[0],
                "brand": item[1],
                "type": item[2],
                "sale": item[3],
                "freeshipping": item[4]
            })

    return filtered_data

coffeebean_data = [
    ["과테말라 와이칸 스페셜티", "싱글오리진", "과테말라", "Specialty", True],
    ["코스타리카 따라주", "싱글오리진", "코스타리카", "SHB", True],
    ["에티오피아 예가체프 G1 하루 수케 워시드", "싱글오리진", "에티오피아", "Specialty", False],
    ["디카페인 브라질", "디카페인", "브라질", "Specialty", True],
    ["디카페인 콜롬비아", "디카페인", "콜롬비아", "Excelso", False]
]

@app.get("/Coffeebean/")
async def filter_coffeebean(
    name: str = Query(..., description="상품이름"),
    type: Optional[str] = Query(None, description="유형 (예시: 싱글오리진, 디카페인)"),
    origin_country: Optional[str] = Query(None, description="원산지"),
    manufacturing_country: Optional[str] = Query(None, description="생산지"),
    grade: Optional[str] = Query(None, description="원두등급 (예시: MICRO LOT, SHB)")
):
    filtered_data = []

    for item in coffeebean_data:
        if (
            item[0] == name and
            (type is None or type == item[1]) and
            (origin_country is None or origin_country == item[2]) and
            (grade is None or grade == item[3])
        ):
            filtered_data.append({
                "name": item[0],
                "type": item[1],
                "origin_country": item[2],
                "grade": item[3],
                "freeshipping": item[4]
            })

    return filtered_data

airfryer_data = [
    ["디디오랩 더블히팅 올스텐 에어프라이어 14L", "오븐형", 14, 1700, True],
    ["보만 저소음 글래스팝 유리 에어프라이어 4L AF41EG1I", "바스켓형", 4, 1000, True],
    ["콕스타 올스텐 에어프라이어23L 오븐형 대용량", "오븐형", 23, 1550, True],
    ["아이닉 AO-16L", "오븐형", 16, 1800, False],
    ["재원전자 FM1800", "오븐형", 18, 1350, False]
]

@app.get("/Airfryer/")
async def filter_airfryer(
    brand: Optional[str] = Query(None, description="브랜드"),
    type: Optional[str] = Query(None, description="상품유형 (예시: 분리형, 일체형, 오븐형, 바스켓형)"),
    capacity: int = Query(..., description="용량L"),
    handle: Optional[bool] = Query(None, description="손잡이유무"),
    powerconsumption: Optional[int] = Query(None, description="소비전력W")
):
    filtered_data = []

    for item in airfryer_data:
        if (
            (brand is None or brand == item[0]) and
            (type is None or type == item[1]) and
            capacity == item[2] and
            (handle is None or handle == item[3]) and
            (powerconsumption is None or powerconsumption == item[4])
        ):
            filtered_data.append({
                "brand": item[0],
                "type": item[1],
                "capacity": item[2],
                "powerconsumption": item[3],
                "freeexchange": item[4]
            })

    return filtered_data

hairdryer_data = [
    ["JMW", 366, "멀티형", 1650, "고정식"],
    ["유닉스", 426.9, "멀티형", 1650, "고정식"],
    ["버디라이프", 370, "전문가용", 1700, "고정식"],
    ["필립스", 722, "휴대용", 2200, "접이식"],
    ["비달사순", 540, "전문가용", 2000, "접이식"]
]

@app.get("/Hairdryer/")
async def filter_hairdryer(
    brand: Optional[str] = Query(None, description="브랜드"),
    weight: Optional[float] = Query(None, description="무게g"),
    purpose: str = Query(..., description="용도 (예시: 멀티형, 전문가용, 휴대용)"),
    powerconsumption: Optional[int] = Query(None, description="소비전력W"),
    fancontrol: Optional[str] = Query(None, description="풍량조절 (예시: 6단, 4단, 3단)")
):
    filtered_data = []

    for item in hairdryer_data:
        if (
            (brand is None or brand == item[0]) and
            (weight is None or weight == item[1]) and
            purpose == item[2] and
            (powerconsumption is None or powerconsumption == item[3]) and
            (fancontrol is None or fancontrol == item[4])
        ):
            filtered_data.append({
                "brand": item[0],
                "weight": item[1],
                "purpose": item[2],
                "powerconsumption": item[3],
                "handle": item[4]
            })

    return filtered_data

hairiron_data = [
    ["JMW", "봉고데기", 120, 200, "TRUE"],
    ["차홍", "봉고데기", 150, 190, "FALSE"],
    ["오아", "볼륨고데기", 100, 230, "TRUE"],
    ["언일전자", "멀티고데기", 100, 200, "FALSE"],
    ["휴브론", "볼륨고데기", 150, 230, "TRUE"]
]

@app.get("/Hairiron/")
async def filter_hairiron(
    brand: str = Query(..., description="브랜드"),
    type: Optional[str] = Query(None, description="상품유형"),
    operation: Optional[str] = Query(None, description="작동방식"),
    min_temp: Optional[int] = Query(None, description="최저온도"),
    max_temp: Optional[int] = Query(None, description="최고온도")
):
    filtered_data = []

    for item in hairiron_data:
        if (
            brand == item[0] and
            (type is None or type == item[1]) and
            (operation is None or operation == item[2]) and
            (min_temp is None or min_temp == item[3]) and
            (max_temp is None or max_temp == item[4])
        ):
            filtered_data.append({
                "brand": item[0],
                "type": item[1],
                "min_temp": item[2],
                "max_temp": item[3],
                "freeshipping": item[4]
            })

    return filtered_data

tabletpc_data = [
    ["삼성전자", 11, "64GB", "8GB", 2.9],
    ["삼성전자", 10.5, "64GB", "4GB", 2.0],
    ["레노버", 10.6, "128GB", "6GB", 2.4],
    ["Apple", 10.9, "64GB", "8GB", 3.2],
    ["Apple", 10.2, "64GB", "3GB", 2.67]
]

@app.get("/TabletPC/")
async def filter_tablet_pc(
    brand: str = Query(..., description="브랜드"),
    screensize: float = Query(..., description="화면크기(인치)"),
    memory: Optional[str] = Query(None, description="내장메모리"),
    RAM: Optional[str] = Query(None, description="램용량"),
    OS: Optional[str] = Query(None, description="출시OS")
):
    filtered_data = []

    for item in tabletpc_data:
        if (
            brand == item[0] and
            screensize == item[1] and
            (memory is None or memory == item[2]) and
            (RAM is None or RAM == item[3]) and
            (OS is None or OS == item[4])
        ):
            filtered_data.append({
                "brand": item[0],
                "screensize": item[1],
                "memory": item[2],
                "RAM": item[3],
                "CPUrate": item[4]
            })

    return filtered_data

monitor_data = [
    ["삼성전자", 49, "커브드", 240, "OLED패널"],
    ["포유디지탈", 32, "평면", 60, "VA패널"],
    ["삼성전자", 24, "커브드", 75, "IPS패널"],
    ["LG전자", 32, "평면", 60, "IPS패널"],
    ["LG전자", 27, "커브드", 75, "IPS패널"]
]

@app.get("/Monitor/")
async def filter_monitor(
    brand: str = Query(..., description="브랜드"),
    screensize: int = Query(..., description="화면크기(인치)"),
    curved: str = Query(..., description="곡면형(예시: 커브드, 평면)"),
    freeshipping: Optional[bool] = Query(None, description="무료배송여부"),
    max_scanrate: Optional[int] = Query(None, description="최대주사율Hz")
):
    filtered_data = []

    for item in monitor_data:
        if (
            brand == item[0] and
            screensize == item[1] and
            curved == item[2] and
            (freeshipping is None or freeshipping == item[3]) and
            (max_scanrate is None or max_scanrate == item[4])
        ):
            filtered_data.append({
                "brand": item[0],
                "screensize": item[1],
                "curved": item[2],
                "max_scanrate": item[3],
                "panel": item[4]
            })

    return filtered_data

microwave_data = [
    ["쿠첸", 23, 900, 1700, "상하"],
    ["SK매직", 28, 900, 2500, "좌우"],
    ["삼성전자", 23, 700, 1100, "좌우"],
    ["LG전자", 23, 1000, 1570, "좌우"],
    ["삼성전자", 23, 700, 2150, "좌우"]
]

@app.get("/Microwaveoven/")
async def filter_microwaveoven(
    brand: str = Query(..., description="브랜드"),
    capacity: Optional[int] = Query(None, description="용량(L)"),
    output: Optional[int] = Query(None, description="출력W"),
    powerconsuption: Optional[int] = Query(None, description="소비전력W"),
    freeshipping: Optional[bool] = Query(None, description="무료배송여부")
):
    filtered_data = []

    for item in microwave_data:
        if (
            brand == item[0] and
            (capacity is None or capacity == item[1]) and
            (output is None or output == item[2]) and
            (powerconsuption is None or powerconsuption == item[3]) and
            (freeshipping is None or freeshipping == item[4])
        ):
            filtered_data.append({
                "brand": item[0],
                "capacity": item[1],
                "output": item[2],
                "powerconsumption": item[3],
                "doortype": item[4]
            })

    return filtered_data

coffeemachine_data = [
    ["유라", "에스프레소머신", "전자동", 1.9, 15],
    ["오르테", "에스프레소머신", "반자동", 1, 20],
    ["일리", "캡슐/POD머신", "반자동", 1, 19],
    ["필립스", "에스프레소머신", "전자동", 1.8, 19],
    ["네스프레소", "캡슐/POD머신", "반자동", 1, 19]
]

@app.get("/Coffeemachine/")
async def filter_coffeemachine(
    brand: str = Query(..., description="브랜드"),
    type: str = Query(..., description="상품유형(예시: 에스프레소머신, 캡슐/POD머신)"),
    purpose: Optional[str] = Query(None, description="용도(예시: 가정용, 업소용)"),
    operation: Optional[str] = Query(None, description="조작방식(예시: 전자동, 반자동, 수동식, 전동식)"),
    watercapacity: Optional[float] = Query(None, description="물탱크용량L")
):
    filtered_data = []

    for item in coffeemachine_data:
        if (
            brand == item[0] and
            type == item[1] and
            (purpose is None or purpose == item[2]) and
            (operation is None or operation == item[3]) and
            (watercapacity is None or watercapacity == item[4])
        ):
            filtered_data.append({
                "brand": item[0],
                "type": item[1],
                "operation": item[2],
                "watercapacity": item[3],
                "pump": item[4]
            })

    return filtered_data

fake_data = [
    ["고점도", "하트", "연결부속", "케이스", 10000, 1],
    ["중점도", "축구공", "은색참", "리본", 5500, 3],
    ["고점도", "인어꼬리", "태슬", "포장재", 0, 2],
    ["하이그로시", "액자", "팬던트", "기타", 1000, 1],
    ["주얼", "별", "금색참", "케이스", 300, 2]
]

@app.get("/Resinartdelivery")
async def filter_resinartdelivery(
    resin: str = Query(..., description="레진"),
    mold: str = Query(None, description="몰드"),
    accessory: str = Query(None, description="악세사리"),
    wrapping: str = Query(None, description="포장재료"),
    numberoftimesleft: int = Query(None, description="잔여 회차")
):
    filtered_data = []
    
    for item in fake_data:
        if (
            (not resin or item[0] == resin) and
            (not mold or item[1] == mold) and
            (not accessory or item[2] == accessory) and
            (not wrapping or item[3] == wrapping) and
            (numberoftimesleft is None or item[5] >= numberoftimesleft)
        ):
            filtered_data.append({
                "resin": item[0],
                "mold": item[1],
                "accessory": item[2],
                "wrapping": item[3],
                "point": item[4],
                "remains": item[5]
            })
    
    return filtered_data

fake_beach_data = [
    ["인천시", "옹진군", "수기해수욕장", "M", False, False],
    ["인천시", "강화군", "민머루해수욕장", "S", True, False],
    ["부산시", "기장군", "일광해수욕장", "L", True, False],
    ["부산시", "기장군", "임랑해수욕장", "M", False, True],
    ["인천시", "옹진군", "서포리해수욕장", "S", True, True]
]

@app.get("/Beach")
async def filter_beach(
    city: str = Query(..., description="시"),
    county: str = Query(None, description="군"),
    name: str = Query(None, description="이름"),
    area: str = Query(None, description="넓이"),
    bathroom: bool = Query(None, description="화장실 여부")
):
    filtered_data = []
    
    for item in fake_beach_data:
        if (
            (not city or item[0] == city) and
            (not county or item[1] == county) and
            (not name or item[2] == name) and
            (not area or item[3] == area) and
            (bathroom is None or item[5] == bathroom)
        ):
            filtered_data.append({
                "city": item[0],
                "county": item[1],
                "name": item[2],
                "area": item[3],
                "fee": item[4],
                "bathroom": item[5]
            })
    
    return filtered_data

fake_maskingtape_data = [
    ["파피아프랏츠", "토끼", "하늘색", 10, 15, "화지"],
    ["엠티", "수박", "초록", 7, 10, "셀로판지"],
    ["킹짐", "리본", "투명", 8, 20, "화지"],
    ["도레미", "잎사귀", "연두", 10, 15, "셀로판지"],
    ["에코드소울", "액자", "오방색", 15, 20, "화지"]
]

@app.get("/maskingtape")
async def filter_maskingtape(
    brand: str = Query(..., description="제조사"),
    pattern: str = Query(None, description="문양"),
    color: str = Query(None, description="색깔"),
    length: float = Query(None, description="길이"),
    qualityOfMtrl: str = Query(None, description="재질")
):
    filtered_data = []
    
    for item in fake_maskingtape_data:
        if (
            (not brand or item[0] == brand) and
            (not pattern or item[1] == pattern) and
            (not color or item[2] == color) and
            (length is None or item[3] == length) and
            (not qualityOfMtrl or item[5] == qualityOfMtrl)
        ):
            filtered_data.append({
                "brand": item[0],
                "pattern": item[1],
                "color": item[2],
                "length": item[3],
                "extent": item[4],
                "qualityOfMtrl": item[5]
            })
    
    return filtered_data

fake_acrylicpaint_data = [
    ["신한", "빨강색", 10, 3, 3, False],
    ["종이나라", "파랑색", 20, 2, 3, True],
    ["알파", "보라색", 50, 1, 2, True],
    ["아트구루", "검정색", 30, 2, 4, False],
    ["몽마르아트", "흰색", 20, 4, 3, True]
]

@app.get("/acrylicpaint")
async def filter_acrylicpaint(
    brand: str = Query(..., description="제조사"),
    color: str = Query(None, description="색상"),
    capacity: int = Query(None, description="용량"),
    color_development: int = Query(None, description="발색력"),
    expert: bool = Query(None, description="전문가용유무")
):
    filtered_data = []
    
    for item in fake_acrylicpaint_data:
        if (
            (not brand or item[0] == brand) and
            (not color or item[1] == color) and
            (capacity is None or item[2] == capacity) and
            (color_development is None or item[3] == color_development) and
            (expert is None or item[5] == expert)
        ):
            filtered_data.append({
                "brand": item[0],
                "color": item[1],
                "capacity": item[2],
                "color_development": item[3],
                "grades": item[4],
                "expert": item[5]
            })
    
    return filtered_data

fake_abandoneddog_data = [
    ["후추", "진돗개", "단모종", "중형견", 5, False],
    ["두부", "요크셔테리아", "단모종", "소형견", 3, False],
    ["토비", "믹스", "장모종", "중형견", 2, True],
    ["사피나", "말티즈", "장모종", "소형견", 3, False],
    ["블루", "푸들", "장모종", "소형견", 6, True]
]

@app.get("/abandoneddog")
async def filter_abandoneddog(
    name: str = Query(..., description="이름"),
    variety: str = Query(None, description="품종"),
    hair: str = Query(None, description="털"),
    size: str = Query(None, description="크기"),
    disease: bool = Query(None, description="질병여부")
):
    filtered_data = []
    
    for item in fake_abandoneddog_data:
        if (
            (not name or item[0] == name) and
            (not variety or item[1] == variety) and
            (not hair or item[2] == hair) and
            (not size or item[3] == size) and
            (disease is None or item[5] == disease)
        ):
            filtered_data.append({
                "name": item[0],
                "variety": item[1],
                "hair": item[2],
                "size": item[3],
                "age": item[4],
                "disease": item[5]
            })
    
    return filtered_data

fake_childhome_data = [
    ["미술놀이", True, 3, 4, 55000],
    ["뜯어만들기", True, 4, 4, 45000],
    ["스티커붙이기", False, 3, 2, 17000],
    ["색연필놀이", False, 5, 4, 31000],
    ["종이접기", False, 3, 3, 23000]
]

@app.get("/Childhome")
async def filter_childhome(
    name: str = Query(..., description="이름"),
    set: bool = Query(None, description="세트유무"),
    usability: int = Query(None, description="간편함", ge=0, le=5),
    safety: int = Query(None, description="안전성", ge=0, le=5),
    min_price: int = Query(None, description="최소 가격 (단위: 원)"),
    max_price: int = Query(None, description="최대 가격 (단위: 원)")
):
    filtered_data = []
    
    for item in fake_childhome_data:
        if (
            (not name or item[0] == name) and
            (set is None or item[1] == set) and
            (usability is None or item[2] == usability) and
            (safety is None or item[3] == safety) and
            (min_price is None or item[4] >= min_price) and
            (max_price is None or item[4] <= max_price)
        ):
            filtered_data.append({
                "name": item[0],
                "set": item[1],
                "usability": item[2],
                "safety": item[3],
                "price": item[4]
            })
    
    return filtered_data

fake_summerdehumidification_data = [
    ["생활공작소", "차량 제습제", "대", 250, "원통형", 1],
    ["살림백서", "옷장 제습제", "중", 50, "옷걸이형", 2],
    ["온다숲", "운동화 제습제", "소", 30, "봉지형", 1],
    ["홈스타", "방 제습제", "중", 530, "사각형", 3],
    ["노브랜드", "집안 제습제", "소", 250, "원통형", 2]
]

@app.get("/summerdehumidification")
async def filter_summerdehumidification(
    brand: str = Query(..., description="브랜드"),
    product: str = Query(None, description="제품"),
    size: str = Query(None, description="크기"),
    capacity: int = Query(None, description="용량 (단위: ml)"),
    dampingpower: int = Query(None, description="제습력", ge=1, le=5)
):
    filtered_data = []
    
    for item in fake_summerdehumidification_data:
        if (
            (item[0] == brand) and
            (product is None or item[1] == product) and
            (size is None or item[2] == size) and
            (capacity is None or item[3] == capacity) and
            (dampingpower is None or item[5] == dampingpower)
        ):
            filtered_data.append({
                "brand": item[0],
                "product": item[1],
                "size": item[2],
                "capacity": item[3],
                "shape": item[4],
                "dampingpower": item[5]
            })
    
    return filtered_data

fake_mildew_data = [
    ["온다숲", "운동화용", 1, 30, "봉지형", 20000],
    ["홈스타", "방용", 3, 530, "사각형", 15000],
    ["노브랜드", "집안용", 3, 250, "원통형", 16000],
    ["아스토니쉬", "욕실용", 4, 350, "원통형", 9000],
    ["피죤", "베란다용", 1, 250, "테이프형", 12000]
]

@app.get("/Mildew")
async def filter_mildew(
    brand: str = Query(..., description="브랜드"),
    use: str = Query(None, description="용도"),
    detergency: int = Query(None, description="세정력", ge=1, le=5),
    capacity: int = Query(None, description="용량 (단위: ml)"),
    min_price: int = Query(None, description="최소 가격 (단위: 원)", ge=0),
    max_price: int = Query(None, description="최대 가격 (단위: 원)", ge=0)
):
    filtered_data = []
    
    for item in fake_mildew_data:
        if (
            (item[0] == brand) and
            (use is None or item[1] == use) and
            (detergency is None or item[2] == detergency) and
            (capacity is None or item[3] == capacity) and
            (min_price is None or item[5] >= min_price) and
            (max_price is None or item[5] <= max_price)
        ):
            filtered_data.append({
                "brand": item[0],
                "use": item[1],
                "detergency": item[2],
                "capacity": item[3],
                "shape": item[4],
                "price": item[5]
            })
    
    return filtered_data

fake_childdesk_data = [
    ["이케아", "플라스틱", 2, 4, "미술", False],
    ["리바트", "원목", 4, 5, "식사", False],
    ["프렌디아", "세라믹", 3, 3, "이유식", True],
    ["아가드", "스테인레스", 4, 3, "식사", False],
    ["마마루", "플라스틱", 3, 5, "독서", True]
]

@app.get("/Childdesk")
async def filter_childdesk(
    brand: str = Query(..., description="브랜드"),
    material: str = Query(None, description="소재"),
    safety: int = Query(None, description="안전성", ge=1, le=5),
    age: int = Query(None, description="연령"),
    freeshipping: bool = Query(None, description="무료배송여부")
):
    filtered_data = []
    
    for item in fake_childdesk_data:
        if (
            (item[0] == brand) and
            (material is None or item[1] == material) and
            (safety is None or item[2] == safety) and
            (age is None or item[3] == age) and
            (freeshipping is None or item[5] == freeshipping)
        ):
            filtered_data.append({
                "brand": item[0],
                "material": item[1],
                "safety": item[2],
                "age": item[3],
                "use": item[4],
                "freeshipping": item[5]
            })
    
    return filtered_data

fake_recyclingbin_data = [
    [5, "직사각형", "S", "플라스틱", 3, "베이지"],
    [4, "사각형", "M", "원목", 10, "흰색"],
    [3, "원통형", "L", "스테인레스", 5, "파랑색"],
    [2, "사각형", "M", "플라스틱", 7, "흰색"],
    [4, "원통형", "L", "스테인레스", 3, "회색"]
]

@app.get("/Recyclingbin")
async def filter_recyclingbin(
    porcelainmargin: int = Query(..., description="간편성", ge=1, le=5),
    shape: str = Query(None, description="모양"),
    size: str = Query(None, description="크기"),
    material: str = Query(None, description="소재"),
    color: str = Query(None, description="색상")
):
    filtered_data = []
    
    for item in fake_recyclingbin_data:
        if (
            (item[0] == porcelainmargin) and
            (shape is None or item[1] == shape) and
            (size is None or item[2] == size) and
            (material is None or item[3] == material) and
            (color is None or item[5] == color)
        ):
            filtered_data.append({
                "porcelainmargin": item[0],
                "shape": item[1],
                "size": item[2],
                "material": item[3],
                "capacity": item[4],
                "color": item[5]
            })
    
    return filtered_data

fake_childbed_data = [
    ["한샘", "원목", 3, 5, "벙커침대", False],
    ["일룸", "플라스틱", 2, 4, "싱글침대", False],
    ["소르니아", "파티클보드", 3, 4, "이층침대", True],
    ["이케아", "스테인레스", 5, 6, "벙커침대", True],
    ["에보니아", "원목", 4, 4, "이층침대", False]
]

@app.get("/childbed")
async def filter_childbed(
    brand: str = Query(..., description="브랜드"),
    material: str = Query(None, description="소재"),
    safety: int = Query(None, description="안전성", ge=1, le=5),
    age: int = Query(None, description="연령"),
    shape: str = Query(None, description="형태")
):
    filtered_data = []
    
    for item in fake_childbed_data:
        if (
            item[0] == brand and
            (material is None or item[1] == material) and
            (safety is None or item[2] == safety) and
            (age is None or item[3] == age) and
            (shape is None or item[4] == shape)
        ):
            filtered_data.append({
                "brand": item[0],
                "material": item[1],
                "safety": item[2],
                "age": item[3],
                "shape": item[4],
                "freeshipping": item[5]
            })
    
    return filtered_data

fake_performance_data = [
    ["2023.03.15", "민속극장 풍류", 0, "김지홍", "문화재청", True],
    ["2023.02.22", "얼쑤마루 공연장", 10000, "김재민", "국립무형유산원", True],
    ["2022.09.18", "민속극장 풍류", 0, "백진희", "한국문화재재단", False],
    ["2022.11.04", "강원감영 선화당 앞마당", 0, "배수지", "문화재청", False],
    ["2023.01.27", "민속극장 풍류", 10000, "김세돌", "한국문화재재단", True]
]

@app.get("/Korealionperformance")
async def filter_Korealionperformance(
    date: str = Query(..., description="날짜 (YYYY.MM.DD 형식)"),
    place: str = Query(None, description="장소"),
    entrancefee: int = Query(None, description="입장료"),
    cast: str = Query(None, description="출연진"),
    holiday: bool = Query(None, description="휴일공연여부")
):
    filtered_data = []
    
    for item in fake_performance_data:
        if (
            item[0] == date and
            (place is None or item[1] == place) and
            (entrancefee is None or item[2] == entrancefee) and
            (cast is None or item[3] == cast) and
            (holiday is None or item[4] == holiday)
        ):
            filtered_data.append({
                "date": item[0],
                "place": item[1],
                "entrancefee": item[2],
                "cast": item[3],
                "sponsor": item[4],
                "holiday": item[5]
            })
    
    return filtered_data

fake_capsule_coffee_data = [
    ["일리", "브라질 세하도", 10, False, 4, False],
    ["스타벅스", "콜롬비아 수프리모", 8, True, 3, True],
    ["드롱기", "에디오피아 예가체프", 12, True, 4, True],
    ["돌체구스토", "케냐에이에이", 8, False, 3, True],
    ["라바짜", "수프리모 디카페인", 6, False, 2, True]
]

@app.get("/Capsulecoffee")
async def filter_Capsulecoffee(
    brand: str = Query(..., description="브랜드"),
    taste: str = Query(None, description="맛"),
    quantity: int = Query(None, description="한팩 갯수"),
    compatibility: bool = Query(None, description="타기기호환여부"),
    freeshipping: bool = Query(None, description="무료배송여부")
):
    filtered_data = []
    
    for item in fake_capsule_coffee_data:
        if (
            item[0] == brand and
            (taste is None or item[1] == taste) and
            (quantity is None or item[2] == quantity) and
            (compatibility is None or item[3] == compatibility) and
            (freeshipping is None or item[5] == freeshipping)
        ):
            filtered_data.append({
                "brand": item[0],
                "taste": item[1],
                "quantity": item[2],
                "compatibility": item[3],
                "rated": item[4],
                "freeshipping": item[5]
            })
    
    return filtered_data

fake_piano_data = [
    ["영창", "해머건반", "업라이트피아노", True, 3, True],
    ["야마하", "하드건반", "디지털피아노", False, 4, True],
    ["삼익", "웨이티드건반", "디지털피아노", False, 2, True],
    ["롤랜드", "해머건반", "디지털피아노", True, 5, True],
    ["스타인웨이", "해머건반", "그랜드피아노", True, 4, False]
]

@app.get("/piano")
async def filter_piano(
    brand: str = Query(..., description="브랜드"),
    keyboard: str = Query(None, description="건반종류"),
    type: str = Query(None, description="타입"),
    freeshipping: bool = Query(None, description="무료배송여부"),
    free_exchange: bool = Query(None, description="무료교환여부")
):
    filtered_data = []
    
    for item in fake_piano_data:
        if (
            item[0] == brand and
            (keyboard is None or item[1] == keyboard) and
            (type is None or item[2] == type) and
            (freeshipping is None or item[3] == freeshipping) and
            (free_exchange is None or item[5] == free_exchange)
        ):
            filtered_data.append({
                "brand": item[0],
                "keyboard": item[1],
                "type": item[2],
                "freeshipping": item[3],
                "star": item[4],
                "free_exchange": item[5]
            })
    
    return filtered_data

fake_deal_data = [
    ["에스템 규조토", 500, False, False, 3],
    ["문화연필 보드마카", 1000, False, True, 4],
    ["교보문고 디퓨저", 27600, False, False, 5],
    ["코스트코 닌자 프로페셔널 블렌더", 180000, True, False, 1],
    ["폴로 여성 린넨 셔츠", 99000, True, False, 3]
]

@app.get("/deal")
async def filter_deal(
    itemNm: str = Query(..., description="상품명"),
    min_price: int = Query(None, description="최소 가격 (단위: 원)"),
    max_price: int = Query(None, description="최대 가격 (단위: 원)"),
    free_shipping: bool = Query(None, description="무료배송여부"),
    stock: int = Query(None, description="남은수량 (단위: 개)")
):
    filtered_data = []
    
    for item in fake_deal_data:
        if (
            item[0] == itemNm and
            (min_price is None or item[1] >= min_price) and
            (max_price is None or item[1] <= max_price) and
            (free_shipping is None or item[2] == free_shipping) and
            (stock is None or item[4] == stock)
        ):
            filtered_data.append({
                "itemNm": item[0],
                "price": item[1],
                "free_shipping": item[2],
                "restock": item[3],
                "stock": item[4]
            })
    
    return filtered_data

fake_tumbler_data = [
    ["스타벅스", 200, "강화유리", "사무실용", "gray", False],
    ["스탠리", 250, "스테인레스", "운동용", "silver", True],
    ["락앤락", 350, "스테인레스", "운동용", "silver", True],
    ["킨토", 350, "세라믹", "차량용", "white", True],
    ["모슈", 500, "플라스틱", "사무실용", "green", True]
]

@app.get("/tumbler")
async def filter_tumbler(
    brand: str = Query(..., description="브랜드"),
    capacity: int = Query(None, description="용량 (단위: ml)"),
    material: str = Query(None, description="재질"),
    use: str = Query(None, description="용도"),
    coldreserving: bool = Query(None, description="보냉여부")
):
    filtered_data = []
    
    for item in fake_tumbler_data:
        if (
            item[0] == brand and
            (capacity is None or item[1] == capacity) and
            (material is None or item[2] == material) and
            (use is None or item[3] == use) and
            (coldreserving is None or item[5] == coldreserving)
        ):
            filtered_data.append({
                "brand": item[0],
                "capacity": item[1],
                "material": item[2],
                "use": item[3],
                "color": item[4],
                "coldreserving": item[5]
            })
    
    return filtered_data

fake_tumbler_data = [
    ["스타벅스", 200, "강화유리", "사무실용", "gray", False],
    ["스탠리", 250, "스테인레스", "운동용", "silver", True],
    ["락앤락", 350, "스테인레스", "운동용", "silver", True],
    ["킨토", 350, "세라믹", "차량용", "white", True],
    ["모슈", 500, "플라스틱", "사무실용", "green", True]
]

@app.get("/tumbler")
async def filter_tumbler(
    brand: str = Query(..., description="브랜드"),
    capacity: int = Query(None, description="용량 (단위: ml)"),
    material: str = Query(None, description="재질"),
    use: str = Query(None, description="용도"),
    coldreserving: bool = Query(None, description="보냉여부")
):
    filtered_data = []
    
    for item in fake_tumbler_data:
        if (
            item[0] == brand and
            (capacity is None or item[1] == capacity) and
            (material is None or item[2] == material) and
            (use is None or item[3] == use) and
            (coldreserving is None or item[5] == coldreserving)
        ):
            filtered_data.append({
                "brand": item[0],
                "capacity": item[1],
                "material": item[2],
                "use": item[3],
                "color": item[4],
                "coldreserving": item[5]
            })
    
    return filtered_data

fake_carpet_data = [
    ["한스갤러리", "L", "사각형", "국내산", False, False],
    ["한일카페트", "M", "원형", "이란산", False, True],
    ["이케아", "M", "사각형", "이란산", True, False],
    ["아망떼", "S", "원형", "국내산", False, True],
    ["러그마켓", "S", "사각형", "수입산", True, True]
]

@app.get("/carpet")
async def filter_carpet(
    brand: str = Query(..., description="브랜드"),
    size: str = Query(None, description="크기 (ex: S, M, L)"),
    shape: str = Query(None, description="형태"),
    origin: str = Query(None, description="원산지"),
    freeshipping: bool = Query(None, description="무료배송여부")
):
    filtered_data = []
    
    for item in fake_carpet_data:
        if (
            item[0] == brand and
            (size is None or item[1] == size) and
            (shape is None or item[2] == shape) and
            (origin is None or item[3] == origin) and
            (freeshipping is None or item[5] == freeshipping)
        ):
            filtered_data.append({
                "brand": item[0],
                "size": item[1],
                "shape": item[2],
                "origin": item[3],
                "sale": item[4],
                "free_shipping": item[5]
            })
    
    return filtered_data

fake_pin_data = [
    ["아즈나브르", "집게형", "노란색", "리본", False, True],
    ["수스다", "자동핀형", "파란색", "무지", True, False],
    ["아르뉴", "클립형", "하늘색", "보석", False, False],
    ["돌리타이", "똑딱이형", "흰색", "플라워", True, True],
    ["로렌스", "꽂이형", "검정색", "밍크", False, False]
]

@app.get("/Pin")
async def filter_pin(
    brand: str = Query(..., description="브랜드"),
    fixity: str = Query(None, description="고정형태"),
    color: str = Query(None, description="색깔"),
    point: str = Query(None, description="포인트"),
    free_shipping: bool = Query(None, description="무료배송여부")
):
    filtered_data = []
    
    for item in fake_pin_data:
        if (
            item[0] == brand and
            (fixity is None or item[1] == fixity) and
            (color is None or item[2] == color) and
            (point is None or item[3] == point) and
            (free_shipping is None or item[5] == free_shipping)
        ):
            filtered_data.append({
                "brand": item[0],
                "fixity": item[1],
                "color": item[2],
                "point": item[3],
                "free_exchange": item[4],
                "free_shipping": item[5]
            })
    
    return filtered_data

fake_gold_anklet_data = [
    ["로이드", "체인형", "화이트", "에스알마감", False, True],
    ["로즈몽", "매듭형", "골드", "붕어마감", True, False],
    ["제이에스티나", "뱅글형", "로즈", "에스알마감", True, True],
    ["준쥬얼리", "매듭형", "골드", "붕어마감", False, False],
    ["골드리아", "레이어드형", "화이트", "에스알마감", True, False]
]

@app.get("/goldanklet")
async def filter_gold_anklet(
    brand: str = Query(..., description="브랜드"),
    style: str = Query(None, description="스타일"),
    color: str = Query(None, description="색상"),
    finish: str = Query(None, description="마감"),
    freeShipping: bool = Query(None, description="무료배송여부")
):
    filtered_data = []
    
    for item in fake_gold_anklet_data:
        if (
            item[0] == brand and
            (style is None or item[1] == style) and
            (color is None or item[2] == color) and
            (finish is None or item[3] == finish) and
            (freeShipping is None or item[5] == freeShipping)
        ):
            filtered_data.append({
                "brand": item[0],
                "style": item[1],
                "color": item[2],
                "finish": item[3],
                "freeAS": item[4],
                "freeShipping": item[5]
            })
    
    return filtered_data

fake_birthday_ring_data = [
    ["금아당", 1, "호랑이", True, True, False],
    ["한국금거래소", 1.875, "토끼", False, True, False],
    ["종로골드", 3.75, "쥐", True, False, True],
    ["모리케이", 1, "원숭이" ,False, False, True],
    ["뽀르띠", 1.875, "말", True, True, False]
]

@app.get("/birthdayring")
async def filter_birthday_ring(
    brand: str = Query(..., description="브랜드"),
    weight: float = Query(None, description="중량 (단위: g)"),
    shape: str = Query(None, description="모양"),
    pack: bool = Query(None, description="포장여부"),
    freechange: bool = Query(None, description="무료교환반품여부")
):
    filtered_data = []
    
    for item in fake_birthday_ring_data:
        if (
            item[0] == brand and
            (weight is None or item[1] == weight) and
            (shape is None or item[2] == shape) and
            (pack is None or item[3] == pack) and
            (freechange is None or item[5] == freechange)
        ):
            filtered_data.append({
                "brand": item[0],
                "weight": item[1],
                "shape": item[2],
                "pack": item[3],
                "desiredDtDelivery": item[4],
                "freechange": item[5]
            })
    
    return filtered_data

fake_chickpeas_data = [
    ["현대농산", 500, "비닐", "생콩", False, "국내산"],
    ["미이랑", 3000, "상자", "건조", False, "캐나다산"],
    ["진솔그레인", 6000, "비닐", "자숙", True, "캐나다산"],
    ["힘찬농부오달봉", 500, "비닐", "건조", True, "국내산"],
    ["코스트코", 7000, "비닐", "건조", False, "캐나다산"]
]

@app.get("/chickPeas")
async def filter_chick_peas(
    brand: str = Query(..., description="브랜드"),
    weight: float = Query(None, description="무게 (단위: g)"),
    packing: str = Query(None, description="포장"),
    form: str = Query(None, description="형태"),
    origin: str = Query(None, description="원산지")
):
    filtered_data = []
    
    for item in fake_chickpeas_data:
        if (
            item[0] == brand and
            (weight is None or item[1] == weight) and
            (packing is None or item[2] == packing) and
            (form is None or item[3] == form) and
            (origin is None or item[5] == origin)
        ):
            filtered_data.append({
                "brand": item[0],
                "weight": item[1],
                "packing": item[2],
                "form": item[3],
                "freeshipping": item[4],
                "origin": item[5]
            })
    
    return filtered_data

fake_paintmarkers_data = [
    ["모나미", 1, "하얀색", "아크릴용", False, False],
    ["펜텔", 2, "노란색", "목재용", False, True],
    ["문화연필", 3, "하늘색", "칠판용", True, False],
    ["문교", 1.5, "회색", "산업용", True, True],
    ["코메론", 1, "흰색", "공작용", True, True]
]

@app.get("/paintmarkers")
async def filter_paintmarkers(
    brand: str = Query(..., description="브랜드"),
    thickness: float = Query(..., description="심굵기 (단위: mm)"),
    color: str = Query(None, description="색깔"),
    use: str = Query(None, description="용도"),
    set: bool = Query(None, description="세트유무")
):
    filtered_data = []
    
    for item in fake_paintmarkers_data:
        if (
            item[0] == brand and
            item[1] == thickness and
            (color is None or item[2] == color) and
            (use is None or item[3] == use) and
            (set is None or item[5] == set)
        ):
            filtered_data.append({
                "brand": item[0],
                "thickness": item[1],
                "color": item[2],
                "use": item[3],
                "freeshipping": item[4],
                "set": item[5]
            })
    
    return filtered_data

fake_hamsterfeed_data = [
    ["패러그린", 500, "혼합형", False, False, 10000],
    ["리프패럿", 650, "단독형", False, True, 15000],
    ["펫스토리", 400, "혼합형", True, True, 13000],
    ["아마존", 350, "단독형", False, True, 12000],
    ["에밀리펫", 900, "혼합형", True, False, 11000]
]

@app.get("/hamsterfeed")
async def filter_hamsterfeed(
    brand: str = Query(..., description="브랜드"),
    weight: int = Query(None, description="무게 (단위: g)"),
    type: str = Query(None, description="타입"),
    freeshipping: bool = Query(None, description="무료배송여부"),
    price: int = Query(None, description="가격 (단위: 원)")
):
    filtered_data = []
    
    for item in fake_hamsterfeed_data:
        if (
            item[0] == brand and
            (weight is None or item[1] == weight) and
            (type is None or item[2] == type) and
            (freeshipping is None or item[3] == freeshipping) and
            (price is None or item[5] == price)
        ):
            filtered_data.append({
                "brand": item[0],
                "weight": item[1],
                "type": item[2],
                "freeshipping": item[3],
                "vinylpacking": item[4],
                "price": item[5]
            })
    
    return filtered_data

fake_ballpoint_data = [
    ["모나미", 0.7, "블랙", "플라스틱", False, False],
    ["제트스트림", 0.5, "블루", "플라스틱", False, True],
    ["파카", 0.3, "레드", "알루미늄", True, False],
    ["라미", 0.7, "블랙", "플라스틱", True, True],
    ["유니", 0.5, "블루", "스테인레스", False, True]
]

@app.get("/ballpoint")
async def filter_ballpoint(
    name: str = Query(..., description="제조사"),
    thickness: float = Query(None, description="굵기 (단위: mm)"),
    color: str = Query(None, description="색깔"),
    material: str = Query(None, description="재질"),
    freeshipping: bool = Query(None, description="무료배송여부")
):
    filtered_data = []
    
    for item in fake_ballpoint_data:
        if (
            item[0] == name and
            (thickness is None or item[1] == thickness) and
            (color is None or item[2] == color) and
            (material is None or item[3] == material) and
            (freeshipping is None or item[5] == freeshipping)
        ):
            filtered_data.append({
                "name": item[0],
                "thickness": item[1],
                "color": item[2],
                "material": item[3],
                "point": item[4],
                "freeshipping": item[5]
            })
    
    return filtered_data

fake_picture_frame_data = [
    ["핀픽", 10.1, 15.2, "나무", "탁상용", 15200],
    ["핀픽", 28, 35.4, "알루미늄", "벽면용", 21100],
    ["크라스", 29.7, 42, "아크릴", "탁상용", 26500],
    ["유어그라피", 50, 50, "나무", "벽면용", 34000],
    ["르누아", 10.2, 15.2, "알루미늄", "탁상용", 9500]
]

@app.get("/picture_frame")
async def filter_picture_frame(
    brand: str = Query(None, description="브랜드"),
    min_width: float = Query(None, description="최소 가로길이 (단위: cm)"),
    max_width: float = Query(None, description="최대 가로길이 (단위: cm)"),
    min_height: float = Query(None, description="최소 세로길이 (단위: cm)"),
    max_height: float = Query(None, description="최대 세로길이 (단위: cm)"),
    material: str = Query(None, description="재질"),
    use: str = Query(..., description="용도"),
    min_price: int = Query(None, description="최소 가격 (단위: 원)"),
    max_price: int = Query(None, description="최대 가격 (단위: 원)")
):
    filtered_data = []
    
    for item in fake_picture_frame_data:
        if (
            (brand is None or item[0] == brand) and
            (min_width is None or item[1] >= min_width) and
            (max_width is None or item[1] <= max_width) and
            (min_height is None or item[2] >= min_height) and
            (max_height is None or item[2] <= max_height) and
            (material is None or item[3] == material) and
            item[4] == use and
            (min_price is None or item[5] >= min_price) and
            (max_price is None or item[5] <= max_price)
        ):
            filtered_data.append({
                "brand": item[0],
                "width": item[1],
                "height": item[2],
                "material": item[3],
                "use": item[4],
                "price": item[5]
            })
    
    return filtered_data

fake_dehumidifier_data = [
    ["씽크", 16, 2, 19, 1, 179000],
    ["삼성전자", 18, 3.5, 21, 1, 203500],
    ["위닉스", 20, 5, 30, 2, 218000],
    ["엘지전자", 25, 8, 32, 2, 280000],
    ["캐리어", 21, 7, 29, 3, 198000]
]

@app.get("/dehumidifier")
async def filter_dehumidifier(
    brand: str = Query(..., description="브랜드"),
    min_dhmdAmntPerDay: float = Query(None, description="최소 1일제습량 (단위: L)"),
    min_bucketSize: float = Query(None, description="최소 물통용량 (단위: L)"),
    min_area: float = Query(None, description="최소 사용면적 (단위: 평)"),
    max_area: float = Query(None, description="최대 사용면적 (단위: 평)"),
    min_energyEff: int = Query(None, description="최소 에너지소비효율"),
    max_energyEff: int = Query(None, description="최대 에너지소비효율"),
    min_price: int = Query(None, description="최소 가격 (단위: 원)"),
    max_price: int = Query(None, description="최대 가격 (단위: 원)")
):
    filtered_data = []
    
    for item in fake_dehumidifier_data:
        if (
            item[0] == brand and
            (min_dhmdAmntPerDay is None or item[1] >= min_dhmdAmntPerDay) and
            (min_bucketSize is None or item[2] >= min_bucketSize) and
            (min_area is None or item[3] >= min_area) and
            (max_area is None or item[3] <= max_area) and
            (min_energyEff is None or item[4] >= min_energyEff) and
            (max_energyEff is None or item[4] <= max_energyEff) and
            (min_price is None or item[5] >= min_price) and
            (max_price is None or item[5] <= max_price)
        ):
            filtered_data.append({
                "brand": item[0],
                "dhmdAmntPerDay": item[1],
                "bucketSize": item[2],
                "area": item[3],
                "energyEff": item[4],
                "price": item[5]
            })
    
    return filtered_data

fake_diary_data = [
    ["오브스레코드", True, False, 4.5, ["yearly", "monthly", "note"], 13800],
    ["온유어마인드", False, True, 5.8, ["monthly", "check list"], 23500],
    ["비온뒤", True, False, 6, ["daily"], 9800],
    ["산리오", False, False, 9, ["monthly", "daily"], 28000],
    ["솜곰", True, True, 8.2, ["yearly", "bucketlist", "note"], 24300]
]

@app.get("/diary")
async def filter_diary(
    brand: str = Query(..., description="브랜드"),
    foreverTF: bool = Query(..., description="만년다이어리 여부"),
    springTF: bool = Query(..., description="스프링형 여부"),
    min_size: float = Query(None, description="최소 사이즈 (단위: inch)"),
    consist: str = Query(None, description="구성 (영어 소문자로 적어주세요. ex: yearly, monthly, daily, note, bucketlist, check list 등)"),
    min_price: int = Query(None, description="최소 가격 (단위: 원)"),
    max_price: int = Query(None, description="최대 가격 (단위: 원)")
):
    filtered_data = []
    
    for item in fake_diary_data:
        if (
            item[0] == brand and
            item[1] == foreverTF and
            item[2] == springTF and
            (min_size is None or item[3] >= min_size) and
            (consist is None or consist in item[4]) and
            (min_price is None or item[5] >= min_price) and
            (max_price is None or item[5] <= max_price)
        ):
            filtered_data.append({
                "brand": item[0],
                "foreverTF": item[1],
                "springTF": item[2],
                "size": item[3],
                "consist": item[4],
                "price": item[5]
            })
    
    return filtered_data

fake_smart_watch_data = [
    ["삼성전자", "Galaxy Watch5", "와이파이", 30.1, 1.5, 233380],
    ["애플", "AppleWatch SE", "셀룰러", 44, 2, 330000],
    ["샤오미", "Mi Band7", "와이파이", 40.6, 0.5, 53800],
    ["샤오미", "Mi Watch", "와이파이", 30.53, 0.8, 88760],
    ["큐씨와이", "GTS1080", "와이파이", 46.9, 0.5, 29800]
]

@app.get("/smart_watch")
async def filter_smart_watch(
    manufacture: str = Query(..., description="제조사"),
    network: str = Query(..., description="네트워크"),
    min_screenSize: float = Query(None, description="최소 화면크기 (단위: mm)"),
    max_screenSize: float = Query(None, description="최대 화면크기 (단위: mm)"),
    min_ram: float = Query(None, description="최소 메모리용량 (단위: GB)"),
    min_price: int = Query(None, description="최소 가격 (단위: 원)"),
    max_price: int = Query(None, description="최대 가격 (단위: 원)")
):
    filtered_data = []
    
    for item in fake_smart_watch_data:
        if (
            item[0] == manufacture and
            item[2] == network and
            (min_screenSize is None or item[3] >= min_screenSize) and
            (max_screenSize is None or item[3] <= max_screenSize) and
            (min_ram is None or item[4] >= min_ram) and
            (min_price is None or item[5] >= min_price) and
            (max_price is None or item[5] <= max_price)
        ):
            filtered_data.append({
                "manufacture": item[0],
                "modelName": item[1],
                "network": item[2],
                "screenSize": item[3],
                "ram": item[4],
                "price": item[5]
            })
    
    return filtered_data

fake_digital_camera_data = [
    ["후지필름", "GFX100S", 1200, 900, True, 1200000],
    ["캐논", "EOSR50", 2420, 375, True, 852000],
    ["소니", "A5000", 2010, 269, True, 133770],
    ["소니", "A7c", 2420, 305, False, 1880000],
    ["캐논", "EOSR10", 2010, 429, False, 1037000]
]

@app.get("/digital_camera")
async def filter_digital_camera(
    manufacture: str = Query(..., description="제조사"),
    min_pixel: int = Query(None, description="최소 화소 (단위: 만 화소)"),
    max_weight: float = Query(None, description="최대 무게 (단위: g)"),
    imageStabilTF: bool = Query(None, description="손떨림방지기능 여부"),
    min_price: int = Query(None, description="최소 가격 (단위: 원)"),
    max_price: int = Query(None, description="최대 가격 (단위: 원)")
):
    filtered_data = []
    
    for item in fake_digital_camera_data:
        if (
            item[0] == manufacture and
            (min_pixel is None or item[2] >= min_pixel) and
            (max_weight is None or item[3] <= max_weight) and
            (imageStabilTF is None or item[4] == imageStabilTF) and
            (min_price is None or item[5] >= min_price) and
            (max_price is None or item[5] <= max_price)
        ):
            filtered_data.append({
                "manufacture": item[0],
                "modelName": item[1],
                "pixel": item[2],
                "weight": item[3],
                "imageStabilTF": item[4],
                "price": item[5]
            })
    
    return filtered_data

fake_swim_fins_data = [
    ["아레나", "숏핀", 33.5, 293, ["TPR", "PP"], 36900],
    ["아레나", "롱핀", 55.5, 414, ["TPR", "PP"], 53100],
    ["디엠씨", "숏핀", 29, 266, ["SILICON"], 59000],
    ["티어", "숏핀", 28.4, 256, ["SILICON"], 49000],
    ["마레스", "롱핀", 57.8, 510, ["SBS", "TECHNOPOLYMER"], 48600]
]

@app.get("/swim_fins")
async def filter_swim_fins(
    brand: str = Query(..., description="브랜드"),
    category: str = Query(..., description="카테고리"),
    min_length: float = Query(None, description="최소 길이 (단위: cm)"),
    max_length: float = Query(None, description="최대 길이 (단위: cm)"),
    max_weight: float = Query(None, description="최대 무게 (단위: g)"),
    material: str = Query(None, description="재질"),
    min_price: int = Query(None, description="최소 가격 (단위: 원)"),
    max_price: int = Query(None, description="최대 가격 (단위: 원)")
):
    filtered_data = []
    
    for item in fake_swim_fins_data:
        if (
            item[0] == brand and
            item[1] == category and
            (min_length is None or item[2] >= min_length) and
            (max_length is None or item[2] <= max_length) and
            (max_weight is None or item[3] <= max_weight) and
            (material is None or material in item[4]) and
            (min_price is None or item[5] >= min_price) and
            (max_price is None or item[5] <= max_price)
        ):
            filtered_data.append({
                "brand": item[0],
                "category": item[1],
                "length": item[2],
                "weight": item[3],
                "material": item[4],
                "price": item[5]
            })
    
    return filtered_data

fake_egg_tart_data = [
    ["히히히","경기","고양시",2800,"포르투갈식 에그타르트",4.64],
    ["인포메이션카페","서울","강남구",3700,"바닐라빈 에그타르트",4.46],
    ["벵봉","대구","중구",3700,"포르투갈식 에그타르트",4.5],
    ["고메","부산","부산진구",3200,"홍콩식 에그타르트",4.58],
    ["맘앤타르트","전북","전주시",3500,"시나몬 에그타르트",4.42]
]

@app.get("/egg_tart")
async def filter_egg_tart(
    name: str = Query(None, description="업체명"),
    city: str = Query(..., description="광역시도"),
    district: str = Query(None, description="시군구"),
    max_price: int = Query(None, description="최대 가격 (단위: 원)"),
    menu: str = Query(None, description="메뉴")
):
    filtered_data = []
    
    for item in fake_egg_tart_data:
        if (
            (name is None or item[0] == name) and
            item[1] == city and
            (district is None or item[2] == district) and
            (max_price is None or item[3] <= max_price) and
            (menu is None or item[4] == menu)
        ):
            filtered_data.append({
                "name": item[0],
                "city": item[1],
                "district": item[2],
                "price": item[3],
                "menu": item[4],
                "rating": item[5]
            })
    
    return filtered_data

fake_insec_plant_data = [
    ["구문초","소",2400,False,"쉬움"],
    ["세라니아","중",15000,True,"쉬움"],
    ["파리지옥","소",4700,True,"중간"],
    ["긴잎끈끈이주걱","소",4700,True,"어려움"],
    ["네펜데스","중",5600,True,"어려움"]
]

@app.get("/insec_plant")
async def filter_insec_plant(
    plant_name: str = Query(None, description="식물명"),
    size: str = Query(None, description="크기"),
    max_price: int = Query(None, description="최대 가격 (단위: 원)"),
    min_price: int = Query(None, description="최소 가격 (단위: 원)"),
    sunshine: bool = Query(None, description="일조량 여부"),
    difficulty: str = Query(..., description="관리 난이도")
):
    filtered_data = []
    
    for item in fake_insec_plant_data:
        if (
            (plant_name is None or item[0] == plant_name) and
            (size is None or item[1] == size) and
            (max_price is None or item[2] <= max_price) and
            (min_price is None or item[2] >= min_price) and
            (sunshine is None or item[3] == sunshine) and
            item[4] == difficulty
        ):
            filtered_data.append({
                "plant_name": item[0],
                "size": item[1],
                "price": item[2],
                "sunshine": item[3],
                "difficulty": item[4]
            })
    
    return filtered_data

fake_graphic_card_data = [
    ["NVIDIA RTX3070",2022,385000,4.5,"아이티젠"],
    ["Colorful RTX4060",2023,470000,4.7,"11번가"],
    ["MSI RTX 3060",2021,420000,4.6,"정은씨앤에스"],
    ["Galaxy GTX1650",2019,220000,4.3,"11번가"],
    ["ASUS RTX 2060",2019,480000,4.45,"인터파크"]
]

@app.get("/graphic_card")
async def filter_graphic_card(
    name: str = Query(None, description="상품명"),
    year: int = Query(..., description="출시연도"),
    max_price: int = Query(None, description="최대 가격 (단위: 원)"),
    min_price: int = Query(None, description="최소 가격 (단위: 원)"),
    min_rating: float = Query(None, description="최소 평점", ge=0, le=5)
):
    filtered_data = []
    
    for item in fake_graphic_card_data:
        if (
            (name is None or item[0] == name) and
            item[1] == year and
            (max_price is None or item[2] <= max_price) and
            (min_price is None or item[2] >= min_price) and
            (min_rating is None or item[3] >= min_rating)
        ):
            filtered_data.append({
                "name": item[0],
                "year": item[1],
                "price": item[2],
                "rating": item[3],
                "seller": item[4]
            })
    
    return filtered_data

fake_toeic_lecture_data = [
    ["와이비엠","박혜원",750,64000,True,60],
    ["와이비엠","최윤선",600,78400,False,62],
    ["해커스","한승태",850,199000,False,45],
    ["해커스","김혜미",550,99000,False,45],
    ["파고다","라수진",900,110000,True,47]
]

@app.get("/TOEIC_lecture")
async def filter_toeic_lecture(
    brand: str = Query(..., description="브랜드"),
    teacher: str = Query(None, description="강사명"),
    level: int = Query(None, description="레벨", ge=0, le=990),
    max_price: int = Query(None, description="최대 가격 (단위: 원)", ge=0),
    textbook: bool = Query(None, description="교재 포함여부"),
    course_period: int = Query(None, description="수강기간 (단위: 일)")
):
    filtered_data = []
    
    for item in fake_toeic_lecture_data:
        if (
            item[0] == brand and
            (teacher is None or item[1] == teacher) and
            (level is None or item[2] == level) and
            (max_price is None or item[3] <= max_price) and
            (textbook is None or item[4] == textbook) and
            (course_period is None or item[5] == course_period)
        ):
            filtered_data.append({
                "brand": item[0],
                "teacher": item[1],
                "level": item[2],
                "price": item[3],
                "textbook": item[4],
                "course_period": item[5]
            })
    
    return filtered_data

fake_kitchen_utensils_data = [
    ["스타우브","컵",32500,4.9,["생각보다 크고 튼튼해서 막쓰기 좋습니다.","예쁘고 마음에 들어요!"]],
    ["로망키친","양념통",2900,4.6,["용기가 유리라 좋아요.","수저가 붙어있어서 편해요."]],
    ["한샘","양념통",10000,4.7,["가볍게 사용하기 편해요.","용량도 크고 안정감있게 사용하기 좋아요."]],
    ["파블로","도마",46800,4.9,["은은한 나무향이 납니다.","디자인이 고급스럽고 예쁩니다."]],
    ["맘스스틸","도마",26000,4.7,["내구성이 좋아요.","열탕소독 가능해서 청결하게 사용가능해요."]]
]

@app.get("/kitchen_utensils")
async def filter_kitchen_utensils(
    brand: str = Query(..., description="브랜드"),
    type: str = Query(..., description="종류"),
    max_price: int = Query(None, description="최대 가격 (단위: 원)", ge=0),
    min_price: int = Query(None, description="최소 가격 (단위: 원)", ge=0),
    min_rating: float = Query(None, description="최소 평점", ge=0, le=5)
):
    filtered_data = []
    
    for item in fake_kitchen_utensils_data:
        if (
            item[0] == brand and
            item[1] == type and
            (max_price is None or item[2] <= max_price) and
            (min_price is None or item[2] >= min_price) and
            (min_rating is None or item[3] >= min_rating)
        ):
            filtered_data.append({
                "brand": item[0],
                "type": item[1],
                "price": item[2],
                "rating": item[3],
                "review": item[4]
            })
    
    return filtered_data

kitchen_utensils_data = [
    ["스타우브", "컵", 32500, 4.9, ["생각보다 크고 튼튼해서 막쓰기 좋습니다.", "예쁘고 마음에 들어요!"]],
    ["로망키친", "양념통", 2900, 4.6, ["용기가 유리라 좋아요.", "수저가 붙어있어서 편해요."]],
    ["한샘", "양념통", 10000, 4.7, ["가볍게 사용하기 편해요.", "용량도 크고 안정감있게 사용하기 좋아요."]],
    ["파블로", "도마", 46800, 4.9, ["은은한 나무향이 납니다.", "디자인이 고급스럽고 예쁩니다."]],
    ["맘스스틸", "도마", 26000, 4.7, ["내구성이 좋아요.", "열탕소독 가능해서 청결하게 사용가능해요."]]
]

@app.get("/kitchen_utensils")
async def filter_kitchen_utensils(
    brand: Optional[str] = Query(None, description="브랜드"),
    type: str = Query(..., description="종류"),
    max_price: Optional[int] = Query(None, description="최대 가격 (단위: 원)", ge=0),
    min_price: Optional[int] = Query(None, description="최소 가격 (단위: 원)", ge=0),
    min_rating: Optional[float] = Query(None, description="최소 평점", ge=0, le=5)
):
    filtered_data = []

    for item in kitchen_utensils_data:
        if (
            (brand is None or item[0] == brand) and
            item[1] == type and
            (max_price is None or item[2] <= max_price) and
            (min_price is None or item[2] >= min_price) and
            (min_rating is None or item[3] >= min_rating)
        ):
            filtered_data.append({
                "brand": item[0],
                "type": item[1],
                "price": item[2],
                "rating": item[3],
                "review": item[4]
            })

    return filtered_data

fabric_softener_data = [
    ["다우니", "고농축", 5.03, 17000, "일반드럼겸용", False],
    ["다우니", "고농축", 8, 19000, "드럼세탁용", False],
    ["피죤", "일반", 2.1, 2000, "일반드럼겸용", True],
    ["샤프란", "일반", 2.1, 1900, "일반드럼겸용", True],
    ["살림백서", "고농축", 1, 5000, "일반드럼겸용", False]
]

@app.get("/fabric_softener")
async def filter_fabric_softener(
    brand: Optional[str] = Query(None, description="브랜드"),
    category: str = Query(..., description="유형"),
    min_capacity: Optional[float] = Query(None, description="최소 용량 (단위: L)", ge=0),
    max_price: Optional[int] = Query(None, description="최대 가격 (단위: 원)", ge=0),
    washing_machine_type: Optional[str] = Query(None, description="세탁기 유형"),
    refill: Optional[bool] = Query(None, description="리필 여부")
):
    filtered_data = []

    for item in fabric_softener_data:
        if (
            (brand is None or item[0] == brand) and
            item[1] == category and
            (min_capacity is None or item[2] >= min_capacity) and
            (max_price is None or item[3] <= max_price) and
            (washing_machine_type is None or item[4] == washing_machine_type) and
            (refill is None or item[5] == refill)
        ):
            filtered_data.append({
                "brand": item[0],
                "category": item[1],
                "capacity": item[2],
                "price": item[3],
                "washing_machine_type": item[4],
                "refill": item[5]
            })

    return filtered_data

meat_substitute_products_data = [
    ["고기대신 비건 떡갈비", "떡갈비", 550, 17900, True, "쿠팡"],
    ["비건 대체육 불고기 땡초 김밥", "김밥", 440, 16100, True, "11번가"],
    ["언리미트 슬라이스", "불고기", 480, 15900, True, "위메프"],
    ["이노센트 팔라펠", "팔라펠", 800, 24900, False, "이마트몰"],
    ["디보션 비건 돈까스", "돈까스", 750, 25900, False, "허닭"]
]

@app.get("/meat_substitute_products")
async def filter_meat_substitute_products(
    name: Optional[str] = Query(None, description="상품이름"),
    category: str = Query(..., description="식품종류"),
    min_amount: Optional[float] = Query(None, description="최소 용량 (단위: g)", ge=0),
    max_amount: Optional[float] = Query(None, description="최대 용량 (단위: g)", ge=0),
    min_price: Optional[int] = Query(None, description="최소 가격 (단위: 원)", ge=0),
    max_price: Optional[int] = Query(None, description="최대 가격 (단위: 원)", ge=0),
    free_delivery: Optional[bool] = Query(None, description="무료배송여부")
):
    filtered_data = []

    for item in meat_substitute_products_data:
        if (
            (name is None or item[0] == name) and
            item[1] == category and
            (min_amount is None or item[2] >= min_amount) and
            (max_amount is None or item[2] <= max_amount) and
            (min_price is None or item[3] >= min_price) and
            (max_price is None or item[3] <= max_price) and
            (free_delivery is None or item[4] == free_delivery)
        ):
            filtered_data.append({
                "name": item[0],
                "category": item[1],
                "amount": item[2],
                "price": item[3],
                "free_delivery": item[4],
                "seller": item[5]
            })

    return filtered_data

jeon_store_menu_data = [
    ["소고기육전", ["소고기", "채끝살", "마늘", "달걀"], 1, 22000, "진짜 맛있어요", True],
    ["감자전", ["감자", "양파", "전분"], 2, 19000, "쫀득하고 슴슴해서 좋아요", True],
    ["김치전", ["김치", "양파", "부침가루", "달걀"], 2, 17000, "여기 신김치가 맛있는 거 같아요", True],
    ["오징어파전", ["오징어", "쪽파", "홍고추", "달걀"], 3, 20000, "오징어가 가득", True],
    ["깻잎전", ["소고기", "돼지고기", "깻잎", "마늘", "달걀"], 1, 20000, "한정 수량이라 꼭 먹어야 함", False]
]

@app.get("/jeon_store_menu")
async def filter_jeon_store_menu(
    m_name: Optional[str] = Query(None, description="메뉴이름"),
    stuff: List[str] = Query(..., description="재료"),
    amount: Optional[int] = Query(None, description="양 (단위: 인분)"),
    min_price: Optional[int] = Query(None, description="최소 가격 (단위: 원)", ge=0),
    max_price: Optional[int] = Query(None, description="최대 가격 (단위: 원)", ge=0),
    available: Optional[bool] = Query(None, description="판매가능여부")
):
    filtered_data = []

    for item in jeon_store_menu_data:
        if (
            (m_name is None or item[0] == m_name) and
            all(ingredient in item[1] for ingredient in stuff) and
            (amount is None or item[2] == amount) and
            (min_price is None or item[3] >= min_price) and
            (max_price is None or item[3] <= max_price) and
            (available is None or item[5] == available)
        ):
            filtered_data.append({
                "m_name": item[0],
                "stuff": item[1],
                "amount": item[2],
                "price": item[3],
                "review": item[4],
                "available": item[5]
            })

    return filtered_data

jeju_island_souvenirs_data = [
    ["제주 갈매기 풍경", "장식품", 23000, 4.8, "정말 귀여워요", True],
    ["한라산 유리컵", "식기", 13000, 4.6, "유리가 얇아서 불안해요", True],
    ["제주애퐁당 실리콘 네임택", "장식품", 13000, 4.8, "먼지가 잘 붙지만 귀여워요", True],
    ["큐테라 풋귤 크림", "스킨케어", 29000, 4.9, "향도 좋고 매장 판매 에디션 용기가 예뻐요", False],
    ["수제 한라봉 비누", "비누", 8000, 4.6, "장식해두려고 샀어요", True]
]

@app.get("/jeju_island_souvenirs")
async def filter_jeju_island_souvenirs(
    name: Optional[str] = Query(None, description="상품이름"),
    category: str = Query(..., description="종류"),
    min_price: Optional[int] = Query(None, description="최소 가격 (단위: 원)", ge=0),
    max_price: Optional[int] = Query(None, description="최대 가격 (단위: 원)", ge=0),
    min_rating: Optional[float] = Query(None, description="최소 평점"),
    max_rating: Optional[float] = Query(None, description="최대 평점"),
    online: Optional[bool] = Query(None, description="온라인판매여부")
):
    filtered_data = []

    for item in jeju_island_souvenirs_data:
        if (
            (name is None or item[0] == name) and
            item[1] == category and
            (min_price is None or item[2] >= min_price) and
            (max_price is None or item[2] <= max_price) and
            (min_rating is None or item[3] >= min_rating) and
            (max_rating is None or item[3] <= max_rating) and
            (online is None or item[5] == online)
        ):
            filtered_data.append({
                "name": item[0],
                "category": item[1],
                "price": item[2],
                "rating": item[3],
                "review": item[4],
                "online": item[5]
            })

    return filtered_data

yeosu_specialty_food_data = [
    ["언니네 돌산갓김치", "김치", 28000, 4.8, "정말 맛있어요", True],
    ["현진이네 돌게장", "반찬", 49000, 4.6, "가격대비 양이 적어요", True],
    ["여수당 쑥 초코파이", "간식", 15000, 4.8, "단맛이 적절해요", True],
    ["여수 딸기모찌", "간식", 19000, 4.9, "선물용으로 아주 좋아요", False],
    ["진선 일호 서대회", "수산물", 48000, 4.6, "당일배송이 좋아요", True]
]

@app.get("/yeosu_specialty_food")
async def filter_yeosu_specialty_food(
    name: Optional[str] = Query(None, description="상품이름"),
    category: str = Query(..., description="종류"),
    min_price: Optional[int] = Query(None, description="최소 가격 (단위: 원)", ge=0),
    max_price: Optional[int] = Query(None, description="최대 가격 (단위: 원)", ge=0),
    min_rating: Optional[float] = Query(None, description="최소 평점"),
    max_rating: Optional[float] = Query(None, description="최대 평점"),
    free_delivery: Optional[bool] = Query(None, description="무료배송여부")
):
    filtered_data = []

    for item in yeosu_specialty_food_data:
        if (
            (name is None or item[0] == name) and
            item[1] == category and
            (min_price is None or item[2] >= min_price) and
            (max_price is None or item[2] <= max_price) and
            (min_rating is None or item[3] >= min_rating) and
            (max_rating is None or item[3] <= max_rating) and
            (free_delivery is None or item[5] == free_delivery)
        ):
            filtered_data.append({
                "name": item[0],
                "category": item[1],
                "price": item[2],
                "rating": item[3],
                "review": item[4],
                "free_delivery": item[5]
            })

    return filtered_data

deodorant_data = [
    ["스웨트 블락", "티슈", 24500, "효과 좋아요", False],
    ["디올 데오도란트 소바쥬", "스프레이", 51000, "향도 깔끔하고 좋아요", True],
    ["이솝 데오도란트 허벌 롤-온", "롤온", 37000, "성분이 좋아서 쓰고 있어요", True],
    ["러쉬 데오도란트 파우더", "파우더", 45500, "사용법이 조금 번거롭네요", True],
    ["질레트 클린 드라이 테크", "롤온", 34500, "자극이 적고 효과가 좋아요", False]
]

@app.get("/deodorant")
async def filter_deodorant(
    name: Optional[str] = Query(None, description="상품이름"),
    formula: str = Query(..., description="제형"),
    min_price: Optional[int] = Query(None, description="최소 가격 (단위: 원)", ge=0),
    max_price: Optional[int] = Query(None, description="최대 가격 (단위: 원)", ge=0),
    aroma: Optional[bool] = Query(None, description="향기여부")
):
    filtered_data = []

    for item in deodorant_data:
        if (
            (name is None or item[0] == name) and
            item[1] == formula and
            (min_price is None or item[2] >= min_price) and
            (max_price is None or item[2] <= max_price) and
            (aroma is None or item[4] == aroma)
        ):
            filtered_data.append({
                "name": item[0],
                "formula": item[1],
                "price": item[2],
                "review": item[3],
                "aroma": item[4]
            })

    return filtered_data

nipple_patch_data = [
    ["루트비 방탄꼭지 걸프리쉬 실리콘 믹스매치", False, 68, 8, 14700, "잘 세정해서 보관하면 1매당 최대 20일 정도 재사용할 수 있다."],
    ["라이프토템 니플밴드", True, 48, 104, 8500, "방수 기능 덕분에 땀을 흘려도 안전하다."],
    ["리무브 브라이트 스킨브라", False, 80, 2, 18000, "제품 착용 시 해당 부위의 유수분을 제거한 뒤 붙여줄 것. 깨끗하게 세척해 잘 말려 보관하면 30회 이상 착용할 수 있다."],
    ["와니즈 니플 실리콘", False, 70, 10, 9500, "사용 후에는 제품을 깨끗하게 클렌징한 뒤 비닐에 붙여 보관한다."],
    ["지니코리아 땡큐밴드랩", True, 35, 188, 11500, "당기면 1매씩 쏙 나오는 슬라이딩 케이스로 사용이 편리하다."]
]

@app.get("/nipple_patch")
async def filter_nipple_patch(
    name: Optional[str] = Query(None, description="상품이름"),
    disposable: bool = Query(..., description="일회용여부"),
    min_size: Optional[float] = Query(None, description="최소크기 (단위: mm)", ge=0),
    max_size: Optional[float] = Query(None, description="최대크기 (단위: mm)", ge=0),
    min_price: Optional[int] = Query(None, description="최소 가격 (단위: 원)", ge=0),
    max_price: Optional[int] = Query(None, description="최대 가격 (단위: 원)", ge=0)
):
    filtered_data = []

    for item in nipple_patch_data:
        if (
            (name is None or item[0] == name) and
            item[1] == disposable and
            (min_size is None or item[2] >= min_size) and
            (max_size is None or item[2] <= max_size) and
            (min_price is None or item[4] >= min_price) and
            (max_price is None or item[4] <= max_price)
        ):
            filtered_data.append({
                "name": item[0],
                "disposable": item[1],
                "size": item[2],
                "number": item[3],
                "price": item[4],
                "desc": item[5]
            })

    return filtered_data

movie_data = [
    ["라라랜드", 2016, "드라마", "라이언고슬링", "판씨네마(주)", "데이미언셔젤"],
    ["해운대", 2009, "모험", "설경구", "CJENM", "윤제균"],
    ["기생충", 2019, "드라마", "송강호", "CJENM", "봉준호"],
    ["살인의추억", 2003, "범죄", "송강호", "CJENM", "봉준호"],
    ["극한직업", 2019, "코미디", "류승룡", "CJENM", "이병헌"]
]

@app.get("/Movie")
async def filter_movie(
    title: str = Query(..., description="영화제목 (한글로 적어주세요)"),
    released_year: Optional[int] = Query(None, description="개봉연도"),
    genre: Optional[str] = Query(None, description="장르 (ex: 코미디, 드라마, 모험, 범죄 등)"),
    main_actor: Optional[str] = Query(None, description="주연배우명"),
    director: Optional[str] = Query(None, description="감독명")
):
    filtered_data = []

    for item in movie_data:
        if (
            item[0] == title and
            (released_year is None or item[1] == released_year) and
            (genre is None or item[2] == genre) and
            (main_actor is None or item[3] == main_actor) and
            (director is None or item[5] == director)
        ):
            filtered_data.append({
                "title": item[0],
                "released_year": item[1],
                "genre": item[2],
                "main_actor": item[3],
                "distributor": item[4],
                "director": item[5]
            })

    return filtered_data

congressman_data = [
    ["강기윤", "남", "국민의힘", 1960, 2, 21],
    ["강대식", "남", "국민의힘", 1959, 1, 21],
    ["강득구", "남", "더불어민주당", 1963, 1, 21],
    ["강민국", "남", "국민의힘", 1971, 1, 21],
    ["강민정", "여", "더불어민주당", 1961, 1, 21]
]

@app.get("/Congressman")
async def filter_congressman(
    name: str = Query(..., description="성명 (한글로 적어주세요)"),
    sex: Optional[str] = Query(None, description="성별 (남 or 여)"),
    polparty: Optional[str] = Query(None, description="소속정당"),
    nth_Congress: Optional[int] = Query(None, description="대수 (단위: 대)"),
    seniority: Optional[int] = Query(None, description="당선횟수 (단위: 번, 회)")
):
    filtered_data = []

    for item in congressman_data:
        if (
            item[0] == name and
            (sex is None or item[1] == sex) and
            (polparty is None or item[2] == polparty) and
            (nth_Congress is None or item[5] == nth_Congress) and
            (seniority is None or item[4] == seniority)
        ):
            filtered_data.append({
                "name": item[0],
                "sex": item[1],
                "polparty": item[2],
                "birthyear": item[3],
                "seniority": item[4],
                "nth_Congress": item[5]
            })

    return filtered_data

bestseller_data = [
    ["세이노의 가르침", "세이노", "자기계발", 9791168473690, "데이원", True, 2023],
    ["문과 남자의 과학 공부", "유시민", "인문", 9791192836188, "돌베개", False, 2023],
    ["인생을 결정짓는 내 안의 감정 패턴", "황시투안", "자기계발", 9791158741969, "미디어숲", False, 2023],
    ["해커스 토익 기출보카 토익 보카 단어장", "데이티브 초", "외국어", 9788965422785, "해커스어학연구소", True, 2019],
    ["역행자", "자청", "자기계발", 9788901272580, "웅진지식하우스", True, 2023]
]

@app.get("/BestsellerBook")
async def filter_bestseller_book(
    title: Optional[str] = Query(None, description="제목 (한글로 적어주세요)"),
    author: str = Query(..., description="작가 (한글로 적어주세요)"),
    category: Optional[str] = Query(None, description="카테고리"),
    sale: Optional[bool] = Query(None, description="세일여부"),
    published_year: Optional[int] = Query(None, description="출간연도")
):
    filtered_data = []

    for item in bestseller_data:
        if (
            item[1] == author and
            (title is None or item[0] == title) and
            (category is None or item[2] == category) and
            (sale is None or item[5] == sale) and
            (published_year is None or item[6] == published_year)
        ):
            filtered_data.append({
                "title": item[0],
                "author": item[1],
                "category": item[2],
                "ISBN": item[3],
                "publisher": item[4],
                "sale": item[5],
                "published_year": item[6]
            })

    return filtered_data

cultural_properties_data = [
    ["서울 숭례문", "국보", "서울 중구 세종대로 40(남대문로4가)", "조선시대", "국유"],
    ["서울 원각사지 십층석탑", "국보", "서울 종로구 종로 99 (종로2가)", "조선시대", "국유"],
    ["서울 북한산 신라 진흥왕 순수비", "국보", "서울 용산구 서빙고로 137, 국립중앙박물관 (용산동6가)", "삼국시대", "국유"],
    ["여주 고달사지 승탑", "국보", "경기도 여주시 북내면 상교리 411-1", "고려시대", "국유"],
    ["보은 법주사 쌍사자 석등", "국보", "충북 보은군 속리산면 법주사로 379, 법주사 (사내리)", "통일신라시대", "법주사"]
]

@app.get("/CulturalProperties")
async def filter_cultural_properties(
    name: Optional[str] = Query(None, description="문화재명 (한글로 적어주세요)"),
    category: str = Query(..., description="지정종목 (ex: 국보, 보물, 사적)"),
    location: Optional[str] = Query(None, description="소재지를 바탕으로 검색하는 키워드"),
    built_age: Optional[str] = Query(None, description="축조시대 (ex: 조선시대, 고려시대, 삼국시대, 통일신라시대 등)"),
    owner: Optional[str] = Query(None, description="소유자 (ex: 국유, 법주사 등)")
):
    filtered_data = []

    for item in cultural_properties_data:
        if (
            item[1] == category and
            (name is None or item[0] == name) and
            (location is None or location in item[2]) and
            (built_age is None or item[3] == built_age) and
            (owner is None or item[4] == owner)
        ):
            filtered_data.append({
                "name": item[0],
                "category": item[1],
                "location": item[2],
                "built_age": item[3],
                "owner": item[4]
            })

    return filtered_data

new_music_data = [
    ["스파이시", "에스파", "댄스", "루드비그 에버스", "방혜현", "문샤인"],
    ["이티에이", "뉴진스", "댄스", "이오공", "임성빈", "이오공"],
    ["아이엠", "아이브", "댄스", "라이언 전", "김이나", "라이언 전"],
    ["여름이 들려", "오마이걸", "댄스", "라이언 전", "이스란", "라이언 전"],
    ["허니문", "트웰브", "알앤비", "트웰브", "트웰브", "트웰브"]
]

@app.get("/NewMusic")
async def filter_new_music(
    title: Optional[str] = Query(None, description="곡제목 (한글로 적어주세요)"),
    singer: str = Query(..., description="가수명 (한글로 적어주세요)"),
    lyricist: Optional[str] = Query(None, description="작사가명 (한글로 적어주세요)"),
    composer: Optional[str] = Query(None, description="작곡가명 (한글로 적어주세요)"),
    genre: Optional[str] = Query(None, description="음악장르 (한글로 적어주세요. ex: 댄스, 알앤비 등)")
):
    filtered_data = []

    for item in new_music_data:
        if (
            item[1] == singer and
            (title is None or item[0] == title) and
            (lyricist is None or item[4] == lyricist) and
            (composer is None or item[3] == composer) and
            (genre is None or item[2] == genre)
        ):
            filtered_data.append({
                "title": item[0],
                "singer": item[1],
                "genre": item[2],
                "composer": item[3],
                "lyricist": item[4],
                "arranger": item[5]
            })

    return filtered_data

drama_data = [
    ["비밀의숲2", "tvN", "스튜디오드래곤", 9.4, "안창호", "이수연"],
    ["닥터차정숙", "JTBC", "(주)스튜디오앤뉴", 18.5, "임종화", "정여랑"],
    ["마당이 있는 집", "ENA", "스튜디오드래곤", 3.0, "김하나", "지아니"],
    ["미스터 선샤인", "tvN", "화앤담픽쳐스", 18.1, "이응복", "김은숙"],
    ["구미호뎐1938", "tvN", "스튜디오드래곤", 8.0, "나지현", "한우리"]
]

@app.get("/Drama")
async def filter_drama(
    title: Optional[str] = Query(None, description="제목 (한글과 숫자만을 사용해서 적어주세요)"),
    tvchannel: str = Query(..., description="편성채널(영어로 적어주세요. ex: tvN, JTBC, ENA 등)"),
    min_rating: Optional[float] = Query(None, description="최소 시청률 (단위: %)"),
    director: Optional[str] = Query(None, description="감독명 (한글로 적어주세요)"),
    writer: Optional[str] = Query(None, description="작가명 (한글로 적어주세요)")
):
    filtered_data = []

    for item in drama_data:
        if (
            item[1] == tvchannel and
            (title is None or item[0] == title) and
            (min_rating is None or item[3] >= min_rating) and
            (director is None or item[4] == director) and
            (writer is None or item[5] == writer)
        ):
            filtered_data.append({
                "title": item[0],
                "tvchannel": item[1],
                "production": item[2],
                "rating": item[3],
                "director": item[4],
                "writer": item[5]
            })

    return filtered_data

suncare_data = [
    [50, "셀퓨전씨", "선크림", 45, "대한민국"],
    [50, "에스트라", "선크림", 40, "대한민국"],
    [50, "라로슈포제", "선크림", 30, "프랑스"],
    [50, "피지오겔", "선로션", 100, "대한민국"],
    [50, "셀퓨전씨", "선스틱", 19, "대한민국"]
]

@app.get("/Suncare")
async def filter_suncare(
    spf: int = Query(..., description="SPF지수"),
    brand: Optional[str] = Query(None, description="브랜드 (한글로 적어주세요)"),
    capacity: Optional[int] = Query(None, description="최소 용량 (단위: ml)"),
    manufacturing_country: Optional[str] = Query(None, description="제조국 (한글로 적어주세요)"),
    type: Optional[str] = Query(None, description="제형 (ex: 선크림, 선로션, 선스틱 등)")
):
    filtered_data = []

    for item in suncare_data:
        if (
            item[0] == spf and
            (brand is None or item[1] == brand) and
            (capacity is None or item[3] >= capacity) and
            (manufacturing_country is None or item[4] == manufacturing_country) and
            (type is None or item[2] == type)
        ):
            filtered_data.append({
                "spf": item[0],
                "brand": item[1],
                "type": item[2],
                "capacity": item[3],
                "manufacturing_country": item[4]
            })

    return filtered_data

airconditioner_data = [
    ["엘지 투인원 에어컨", "엘지전자", "멀티형", 3, 7200],
    ["엘지 휘센", "엘지전자", "스탠드형", 3, 7000],
    ["삼성전자 무풍클래식", "삼성전자", "멀티형", 2, 7000],
    ["캐리어 클라윈드", "캐리어", "벽걸이형", 5, 2300],
    ["위니아 인버터 벽걸이에어컨", "위니아", "벽걸이형", 5, 2300]
]

@app.get("/Airconditioner")
async def filter_airconditioner(
    brand: Optional[str] = Query(None, description="브랜드 (한글로 적어주세요)"),
    type: str = Query(..., description="상품유형 (한글로 적어주세요. ex: 멀티형, 벽걸이형, 스탠드형 등)"),
    energy_grade: Optional[int] = Query(None, description="에너지효율등급"),
    min_capacity: Optional[int] = Query(None, description="냉방능력"),
    max_capacity: Optional[int] = Query(None, description="냉방능력")
):
    filtered_data = []

    for item in airconditioner_data:
        if (
            (brand is None or item[1] == brand) and
            item[2] == type and
            (energy_grade is None or item[3] == energy_grade) and
            (min_capacity is None or item[4] >= min_capacity) and
            (max_capacity is None or item[4] <= max_capacity)
        ):
            filtered_data.append({
                "name": item[0],
                "brand": item[1],
                "type": item[2],
                "energy_grade": item[3],
                "capacity": item[4]
            })

    return filtered_data

fan_data = [
    [True, "비티글로벌", "스탠드형", "BLDC", True],
    [True, "신일전자", "스탠드형", "BLDC", True],
    [False, "듀플렉스", "스탠드형", "AC", True],
    [True, "한일전기", "벽걸이형", "AC", False],
    [False, "스타일리스", "서큘레이터", "DC", False]
]

@app.get("/Fan")
async def filter_fan(
    remote: Optional[bool] = Query(None, description="리모컨여부"),
    brand: Optional[str] = Query(None, description="제조사 (한글로 적어주세요)"),
    type: str = Query(..., description="상품유형 (한글로 적어주세요. ex: 스탠드형, 서큘레이터, 벽걸이형 등)"),
    motor_type: Optional[str] = Query(None, description="모터종류 (영어로 적어주세요. ex: DC, BLDC, AC)"),
    freeshipping: Optional[bool] = Query(None, description="무료배송여부")
):
    filtered_data = []

    for item in fan_data:
        if (
            (remote is None or item[0] == remote) and
            (brand is None or item[1] == brand) and
            item[2] == type and
            (motor_type is None or item[3] == motor_type) and
            (freeshipping is None or item[4] == freeshipping)
        ):
            filtered_data.append({
                "remote": item[0],
                "brand": item[1],
                "type": item[2],
                "motor_type": item[3],
                "freeshipping": item[4]
            })

    return filtered_data

dryer_data = [
    ["에이씨모터", "보만", 3, True, 850],
    ["에이씨모터", "위닉스", 4, True, 950],
    ["인버터모터", "삼성전자", 19, True, 2400],
    ["인버터모터", "엘지전자", 10, False, 950],
    ["인버터모터", "엘지전자", 19, True, 950]
]

@app.get("/Dryer")
async def filter_dryer(
    motortype: Optional[str] = Query(None, description="모터종류 (한글로 적어주세요. ex: 인버터모터, 에이씨모터)"),
    brand: Optional[str] = Query(None, description="제조사 (한글로 적어주세요)"),
    capacity: int = Query(..., description="건조용량 (단위: kg)"),
    max_powerCnsmptn: Optional[int] = Query(None, description="최대 소비전력 (단위: kW)"),
    freeshipping: Optional[bool] = Query(None, description="무료배송여부")
):
    filtered_data = []

    for item in dryer_data:
        if (
            (motortype is None or item[0] == motortype) and
            (brand is None or item[1] == brand) and
            item[2] == capacity and
            (max_powerCnsmptn is None or item[4] <= max_powerCnsmptn) and
            (freeshipping is None or item[3] == freeshipping)
        ):
            filtered_data.append({
                "motortype": item[0],
                "brand": item[1],
                "capacity": item[2],
                "freeshipping": item[3],
                "powerCnsmptn": item[4]
            })

    return filtered_data

sneakers_data = [
    ["나이키", [260, 270, 280], 270000, "보라색", "농구화"],
    ["아디다스", [240, 245, 250], 230000, "파란색", "농구화"],
    ["뉴발란스", [250, 240, 245], 190000, "검정색", "런닝화"],
    ["호카", [260, 265, 270], 200000, "형광노랑색", "트래킹화"],
    ["휠라", [240, 245, 250], 150000, "노랑색", "런닝화"]
]

@app.get("/Sneakers")
async def filter_sneakers(
    brand: Optional[str] = Query(None, description="브랜드 (한글로 적어주세요. ex: 나이키, 아디다스, 호카 등)"),
    size: int = Query(..., description="사이즈"),
    category: Optional[str] = Query(None, description="카테고리 (한글로 적어주세요. ex: 농구화, 런닝화, 트래킹화 등)"),
    min_price: Optional[int] = Query(None, description="최소 가격 (단위: 원)"),
    max_price: Optional[int] = Query(None, description="최대 가격 (단위: 원)")
):
    filtered_data = []

    for item in sneakers_data:
        if (
            (brand is None or item[0] == brand) and
            size in item[1] and
            (category is None or item[4] == category) and
            (min_price is None or item[2] >= min_price) and
            (max_price is None or item[2] <= max_price)
        ):
            filtered_data.append({
                "brand": item[0],
                "size": item[1],
                "category": item[4],
                "price": item[2],
                "color": item[3]
            })

    return filtered_data

microphone_data = [
    ["MXL", "콘덴서 마이크", "실버", "청량감 있는 고음역대를 충분하게 수음할 수 있다", "머리 착용", 190000],
    ["Sennheiser", "다이나믹 마이크", "블랙", "여러 거리에서도 음성이 풍부하고 생생하게 전달된다", "반원 타입", 250000],
    ["BOYA", "무선 마이크", "블랙", "2.4GHz 주파수를 이용하는 초소형 마이크", "클립 타입", 99000],
    ["SHURE", "다이나믹 마이크", "블랙", "원음의 비범한 소리를 언제 어디서나 바로 들을 수 있다", "손잡이 타입", 210000],
    ["RODE", "콘덴서 마이크", "블랙", "스튜디오 수준의 사운드를 매우 간단하게 구현할 수 있는 전문적인 마이크이다.", "유에스비 타입", 310000]
]

@app.get("/Microphone")
async def filter_microphone(
    brand: Optional[str] = Query(None, description="브랜드 (영어로 적어주세요. ex: MXL, Sennheiser 등)"),
    type: str = Query(..., description="종류 (한글로 적어주세요. ex: 콘덴서 마이크, 다이나믹 마이크, 무선 마이크 등)"),
    color: Optional[str] = Query(None, description="색상 (한글로 적어주세요. ex: 실버, 블랙 등)"),
    shape: Optional[str] = Query(None, description="형태 (한글로 적어주세요. ex: 머리 착용, 반원 타입, 유에스비 타입 등)"),
    min_price: Optional[int] = Query(None, description="최소 가격 (단위: 원)"),
    max_price: Optional[int] = Query(None, description="최대 가격 (단위: 원)")
):
    filtered_data = []

    for item in microphone_data:
        if (
            (brand is None or item[0] == brand) and
            item[1] == type and
            (color is None or item[2] == color) and
            (shape is None or item[4] == shape) and
            (min_price is None or item[5] >= min_price) and
            (max_price is None or item[5] <= max_price)
        ):
            filtered_data.append({
                "brand": item[0],
                "type": item[1],
                "color": item[2],
                "desc": item[3],
                "shape": item[4],
                "price": item[5]
            })

    return filtered_data

strawboard_data = [
    ["A4", "국내산", 350, "흰색", False],
    ["A5", "수입산", 350, "흰색", True],
    ["A3", "중국산", 250, "크림색", True],
    ["A3", "일본산", 450, "아이보리색", True],
    ["B4", "국내산", 300, "회색", False]
]

@app.get("/strawboard")
async def filter_strawboard(
    standard: str = Query(..., description="규격 (영어 대문자와 숫자 조합으로 적어주세요. ex: A4, A3 등)"),
    origin: Optional[str] = Query(None, description="원산지 (한글로 적어주세요. ex: 국내산, 수입산, 중국산, 일본산 등)"),
    min_weight: Optional[int] = Query(None, description="최소 무게 (단위: g)"),
    max_weight: Optional[int] = Query(None, description="최대 무게 (단위: g)"),
    color: Optional[str] = Query(None, description="색상 (한글로 적어주세요. ex: 크림색, 아이보리색, 흰색 등)"),
    pearl: Optional[bool] = Query(None, description="펄 여부")
):
    filtered_data = []

    for item in strawboard_data:
        if (
            item[0] == standard and
            (origin is None or item[1] == origin) and
            (min_weight is None or item[2] >= min_weight) and
            (max_weight is None or item[2] <= max_weight) and
            (color is None or item[3] == color) and
            (pearl is None or item[4] == pearl)
        ):
            filtered_data.append({
                "standard": item[0],
                "origin": item[1],
                "weight": item[2],
                "color": item[3],
                "pearl": item[4]
            })

    return filtered_data

musical_data = [
    ["샤롯데씨어터", 7, "조승우", "A", 90000, True],
    ["플러스씨어터", 8, "정민", "B", 60000, False],
    ["드림아트센터", 9, "정동화", "S", 110000, False],
    ["예술의전당 오페라극장", 9, "유준상", "R", 140000, True],
    ["블루스퀘어 신한카드홀", 10, "전동석", "A", 90000, True]
]

@app.get("/musical")
async def filter_musical(
    theater: str = Query(..., description="공연장 (한글로 적어주세요. ex: 샤롯데씨어터, 플러스씨어터, 드림아트센터, 예술의전당 오페라극장, 블루스퀘어 신한카드홀 등)"),
    month: Optional[int] = Query(None, description="날짜 (단위: 월)"),
    cast: Optional[str] = Query(None, description="캐스팅 (한글로 적어주세요.)"),
    seat: Optional[str] = Query(None, description="좌석 (영어 대문자로 적어주세요. ex: B, A, S, R)"),
    min_price: Optional[int] = Query(None, description="최소 가격 (단위: 원)"),
    max_price: Optional[int] = Query(None, description="최대 가격 (단위: 원)")
):
    filtered_data = []

    for item in musical_data:
        if (
            item[0] == theater and
            (month is None or item[1] == month) and
            (cast is None or item[2] == cast) and
            (seat is None or item[3] == seat) and
            (min_price is None or item[4] >= min_price) and
            (max_price is None or item[4] <= max_price)
        ):
            filtered_data.append({
                "theater": item[0],
                "month": item[1],
                "cast": item[2],
                "seat": item[3],
                "price": item[4],
                "freeInstallment": item[5]
            })

    return filtered_data

performance_data = [
    ["종이 꽃밭 두할망본풀이", True, 70, "달오름극장", 3],
    ["알로하나의엄마들", True, 170, "해오름극장", 35],
    ["자유항", False, 70, "달오름극장", 23],
    ["장단", True, 70, "하늘극장", 1],
    ["럴 유영", False, 70, "달오름극장", 9]
]

@app.get("/nationaltheaterofkoreaperformance")
async def filter_performance(
    name: str = Query(..., description="공연 이름 (한글로 적어주세요.)"),
    weekend: Optional[bool] = Query(None, description="주말 공연 여부"),
    min_runningTM: Optional[int] = Query(None, description="최소 관람시간 (단위: 분)"),
    max_runningTM: Optional[int] = Query(None, description="최대 관람시간 (단위: 분)"),
    theater: Optional[str] = Query(None, description="극장 (한글로 적어주세요. ex: 달오름극장, 해오름극장, 하늘극장 등)")
):
    filtered_data = []

    for item in performance_data:
        if (
            item[0] == name and
            (weekend is None or item[1] == weekend) and
            (min_runningTM is None or item[2] >= min_runningTM) and
            (max_runningTM is None or item[2] <= max_runningTM) and
            (theater is None or item[3] == theater)
        ):
            filtered_data.append({
                "name": item[0],
                "weekend": item[1],
                "runningTm": item[2],
                "theater": item[3],
                "emptySeats": item[4]
            })

    return filtered_data

leggings_data = [
    ["안다르", "M", "화이트", False, 45000],
    ["안다르", "S", "블랙", True, 37000],
    ["젝시믹스", "L", "그레이", True, 25000],
    ["젝시믹스", "S", "화이트", False, 31000],
    ["젝시믹스", "XL", "그레이", False, 54000]
]

@app.get("/leggings")
async def filter_leggings(
    brand: str = Query(..., description="브랜드 (한글로 적어주세요. ex: 안다르, 젝시믹스 등)"),
    size: Optional[str] = Query(None, description="사이즈 (영어 대문자로 적어주세요. ex: S, M, L, XL)"),
    color: Optional[str] = Query(None, description="색상 (한글로 적어주세요. ex: 화이트, 블랙, 그레이 등)"),
    pocket: Optional[bool] = Query(None, description="주머니 여부"),
    min_price: Optional[int] = Query(None, description="최소 가격 (단위: 원)"),
    max_price: Optional[int] = Query(None, description="최대 가격 (단위: 원)")
):
    filtered_data = []

    for item in leggings_data:
        if (
            item[0] == brand and
            (size is None or item[1] == size) and
            (color is None or item[2] == color) and
            (pocket is None or item[3] == pocket) and
            (min_price is None or item[4] >= min_price) and
            (max_price is None or item[4] <= max_price)
        ):
            filtered_data.append({
                "brand": item[0],
                "size": item[1],
                "color": item[2],
                "pocket": item[3],
                "price": item[4]
            })

    return filtered_data

stamp_collecting_data = [
    [25000, "한혜진", "여성", 25, 5972],
    [15000, "정우성", "남성", 37, 4612],
    [10000, "양희은", "여성", 70, 4324],
    [25000, "김서희", "남성", 46, 7694],
    [18000, "남희석", "남성", 34, 4943]
]

@app.get("/stampcollecting")
async def filter_stamp_collecting(
    subscriptionFee: int = Query(..., description="구독료 (단위: 원)"),
    name: Optional[str] = Query(None, description="이름 (한글로 적어주세요.)"),
    sex: Optional[str] = Query(None, description="성별 (한글로 적어주세요. 여성 or 남성)"),
    min_age: Optional[int] = Query(None, description="최소 나이 (단위: 세, 살)"),
    max_age: Optional[int] = Query(None, description="최대 나이 (단위: 세, 살)")
):
    filtered_data = []

    for item in stamp_collecting_data:
        if (
            item[0] == subscriptionFee and
            (name is None or item[1] == name) and
            (sex is None or item[2] == sex) and
            (min_age is None or item[3] >= min_age) and
            (max_age is None or item[3] <= max_age)
        ):
            filtered_data.append({
                "subscriptionFee": item[0],
                "name": item[1],
                "sex": item[2],
                "age": item[3],
                "phonenumber": item[4]
            })

    return filtered_data

scissors_data = [
    ["모나미", "사무용", 30, "장인방식의 따라 글라인더 방식을 기초로 우수한 가위를 생산합니다.", "은색", 3500],
    ["파울", "조리용", 23, "손에 힘안들이고도 잘리는 초강력 절삭력", "검정색", 7000],
    ["잘라가위", "주방용", 33, "플라스틱 없는 친환경올스텐 소재로 반영구적으로 사용할 수 있습니다.", "은색", 5000],
    ["토리베", "조리용", 25, "세련된 디자인과 뛰어난 절삭력", "은색", 12000],
    ["세수", "조리용", 30, "곡선절단이 깔끔하여 강력한 절삭력을 가져다줍니다.", "흰색", 9900]
]

@app.get("/scissors")
async def filter_scissors(
    brand: Optional[str] = Query(None, description="브랜드 (한글로 적어주세요. ex: 모나미, 파울 등)"),
    use: str = Query(..., description="용도 (한글로 적어주세요. ex: 사무용, 주방용, 조리용 등)"),
    size: Optional[int] = Query(None, description="사이즈 (단위: cm)"),
    color: Optional[str] = Query(None, description="색상 (한글로 적어주세요. ex: 은색, 검정색, 흰색 등)"),
    min_price: Optional[int] = Query(None, description="최소 가격 (단위: 원)"),
    max_price: Optional[int] = Query(None, description="최대 가격 (단위: 원)")
):
    filtered_data = []

    for item in scissors_data:
        if (
            (brand is None or item[0] == brand) and
            item[1] == use and
            (size is None or item[2] == size) and
            (color is None or item[4] == color) and
            (min_price is None or item[5] >= min_price) and
            (max_price is None or item[5] <= max_price)
        ):
            filtered_data.append({
                "brand": item[0],
                "use": item[1],
                "size": item[2],
                "desc": item[3],
                "color": item[4],
                "price": item[5]
            })

    return filtered_data

newspaper_data = [
    ["2023.04.17", "중앙일보", "문화", "오세진", 12545],
    ["2023.02.22", "한겨례", "정치", "김돌돌", 55612],
    ["2023.06.03", "조선일보", "사회", "유지태", 110000],
    ["2023.05.12", "문화일보", "국제", "박수현", 45675],
    ["2023.07.05", "경향신문", "스포츠", "이빈", 75642]
]

@app.get("/newspaper")
async def filter_newspaper(
    date: Optional[str] = Query(None, description="날짜 (YYYY.MM.DD 형식)"),
    name: str = Query(..., description="신문명 (한글로 적어주세요. ex: 중앙일보, 한겨례 등)"),
    category: Optional[str] = Query(None, description="카테고리 (한글로 적어주세요. ex: 정치, 사회, 국제)"),
    reporter: Optional[str] = Query(None, description="기자 (한글로 적어주세요.)"),
    min_comments: Optional[int] = Query(None, description="최소 댓글수 (단위: 개)"),
    max_comments: Optional[int] = Query(None, description="최대 댓글수 (단위: 개)")
):
    filtered_data = []

    for item in newspaper_data:
        if (
            (date is None or item[0] == date) and
            item[1] == name and
            (category is None or item[2] == category) and
            (reporter is None or item[3] == reporter) and
            (min_comments is None or item[4] >= min_comments) and
            (max_comments is None or item[4] <= max_comments)
        ):
            filtered_data.append({
                "date": item[0],
                "name": item[1],
                "category": item[2],
                "reporter": item[3],
                "comments": item[4]
            })

    return filtered_data














### 0719 Update ###

cake_data = [
    {
        "name": "블랙포레스트",
        "stuff": ["체리", "생크림", "초콜릿"],
        "size": "2호",
        "price": 38000,
        "calorie": 395,
        "desc": "상큼한 생체리, 부드러운 초콜릿스폰지에 가나슈와 생크림의 조화"
    },
    {
        "name": "얼그레이케이크",
        "stuff": ["얼그레이 크림", "생크림", "초콜릿"],
        "size": "1호",
        "price": 31000,
        "calorie": 345,
        "desc": "얼그레이 향이 푸부한 생크림에 초콜릿크런치를 바닥에 깔아 심플하면서도 홍차맛 가득한 베스트 케이크"
    },
    {
        "name": "말차케이크",
        "stuff": ["말차", "생크림", "팥앙금"],
        "size": "조각",
        "price": 8000,
        "calorie": 295,
        "desc": "진한 말차와 팥앙금을 넣어서 맛의 조화를 시도한 녹차 매니아에게는 축복인 진한 맛의 케이크"
    },
    {
        "name": "가또쇼콜라",
        "stuff": ["건포도", "럼", "다크초콜릿"],
        "size": "2호",
        "price": 42000,
        "calorie": 385,
        "desc": "다크초콜릿 가나슈와 럼에절인 건포도를 바닥에 조금 넣어서 기호에따라 건포도를 빼서 먹을수 있는 다크초콜릿케이크"
    },
    {
        "name": "마롱케이크",
        "stuff": ["머랭과자", "밤크림", "팥앙금"],
        "size": "2호",
        "price": 43000,
        "calorie": 355,
        "desc": "바삭하게 구운 머랭과자, 팥앙금과 밤크림을 샌드한 밤맛과 머랭의 바삭한 식감이 살아있는 정성가득 손이 많아가는 케이크"
    }
]

@app.get("/CakeMenuSearch")
async def filter_cake_menu_search(
    name: Optional[str] = Query(None, description="케이크명"),
    stuff: Optional[str] = Query(None, description="재료 (예: 레몬, 체리, 복숭아, 생크림, 초콜릿 등)"),
    size: Optional[str] = Query(None, description="크기 (예: 조각, 1호, 2호, 4호)"),
    min_price: Optional[float] = Query(None, ge=0, description="최소 가격"),
    max_price: Optional[float] = Query(None, ge=0, description="최대 가격"),
    min_calorie: Optional[float] = Query(None, ge=0, description="최저칼로리 (1인 분량 당 칼로리)"),
    max_calorie: Optional[float] = Query(None, ge=0, description="최고저칼로리 (1인 분량 당 칼로리)")
):
    filtered_cakes = []
    for cake in cake_data:
        if name and name != cake["name"]:
            continue
        if stuff and stuff not in cake["stuff"]:
            continue
        if size and size != cake["size"]:
            continue
        if min_price is not None and cake["price"] < min_price:
            continue
        if max_price is not None and cake["price"] > max_price:
            continue
        if min_calorie is not None and cake["calorie"] < min_calorie:
            continue
        if max_calorie is not None and cake["calorie"] > max_calorie:
            continue
        filtered_cakes.append(cake)
    
    return filtered_cakes

flower_seed_data = [
    {
        "name": "백일홍 더블살몬",
        "color": "다홍색",
        "trait": ["1년생"],
        "month": [3, 4, 5, 6, 7],
        "price": 3000,
        "amount": 10,
        "desc": "꽃은 반겹꽃, 겹꽃, 홑꽃 모두 나옵니다."
    },
    {
        "name": "오드리에타 스카이블루",
        "color": "하늘색",
        "trait": ["2년생", "다년생"],
        "month": [9, 10],
        "price": 3000,
        "amount": 10,
        "desc": "비탈길이나 돌계단에 잘 어울립니다."
    },
    {
        "name": "델피늄 썸머블루스",
        "color": "하늘색",
        "trait": ["다년생", "전국 노지월동"],
        "month": [5, 6, 7, 8, 9, 10],
        "price": 3500,
        "amount": 20,
        "desc": "2년생 이상부터 꽃을 볼 수 있습니다."
    },
    {
        "name": "매발톱 로즈화이트 윙키",
        "color": "분홍색",
        "trait": ["다년생", "전국 노지월동"],
        "month": [9, 10, 11, 12],
        "price": 3600,
        "amount": 10,
        "desc": "첫해에는 보온 월동이 필요합니다."
    },
    {
        "name": "아르메니아 발레리나",
        "color": "흰색",
        "trait": ["다년생", "제주 노지월동"],
        "month": [9, 10, 11, 12, 1, 2, 3],
        "price": 3800,
        "amount": 10,
        "desc": "발아시 촉촉함 유지가 중요합니다."
    }
]

@app.get("/FlowerSeed")
async def filter_flower_seed(
    name: Optional[str] = Query(None, description="꽃이름"),
    color: Optional[str] = Query(None, description="색상 (예: 흰색, 분홍색 등)"),
    trait: Optional[str] = Query(None, description="특성 (예: 1년생, 2년생, 다년생, 전국 노지월동 등)"),
    month: Optional[int] = Query(None, description="파종시기 (예: (달 기준)1, 2, 3 등)"),
    min_price: Optional[float] = Query(None, ge=0, description="최소 가격"),
    max_price: Optional[float] = Query(None, ge=0, description="최대 가격")
):
    filtered_flower_seeds = []
    for flower_seed in flower_seed_data:
        if name and name != flower_seed["name"]:
            continue
        if color and color != flower_seed["color"]:
            continue
        if trait and trait not in flower_seed["trait"]:
            continue
        if month is not None and month not in flower_seed["month"]:
            continue
        if min_price is not None and flower_seed["price"] < min_price:
            continue
        if max_price is not None and flower_seed["price"] > max_price:
            continue
        filtered_flower_seeds.append(flower_seed)
    
    return filtered_flower_seeds

coffee_bean_regular_delivery_data = [
    {
        "name": "에스쇼콜라",
        "period": "1주",
        "taste": ["밀크초콜릿", "밸런스", "크리미"],
        "roasting": "중",
        "price": 14000,
        "desc": "다크초콜릿을 한입 베어먹은 듯한 여운과 함께 크리미한 질감, 스윗니스와 바디감"
    },
    {
        "name": "에스쇼콜라",
        "period": "2주",
        "taste": ["밀크초콜릿", "밸런스", "크리미"],
        "roasting": "중",
        "price": 22000,
        "desc": "다크초콜릿을 한입 베어먹은 듯한 여운과 함께 크리미한 질감, 스윗니스와 바디감"
    },
    {
        "name": "므쵸베리",
        "period": "1달",
        "taste": ["믹스베리", "체리", "초콜릿"],
        "roasting": "강",
        "price": 15000,
        "desc": "에티오피아, 브라질 두 산지의 내추럴 커피로 조성되었으며, 초콜렛의 단맛을 베이스로 믹스베리, 체리 등 다양한 베리류의 향미"
    },
    {
        "name": "므쵸베리",
        "period": "2달",
        "taste": ["믹스베리", "체리", "초콜릿"],
        "roasting": "강",
        "price": 30000,
        "desc": "에티오피아, 브라질 두 산지의 내추럴 커피로 조성되었으며, 초콜렛의 단맛을 베이스로 믹스베리, 체리 등 다양한 베리류의 향미"
    },
    {
        "name": "프루티봉봉",
        "period": "1달",
        "taste": ["베르가못", "자스민", "만다린", "카라멜"],
        "roasting": "약",
        "price": 16000,
        "desc": "프루티 봉봉은 이름처럼 과일, 꽃을 연상시키는 향미와 새콤달콤함을 가짐"
    }
]

@app.get("/CoffeeBeanRegularDelivery")
async def filter_coffee_bean_regular_delivery(
    name: Optional[str] = Query(None, description="원두상품이름"),
    period: Optional[str] = Query(None, description="배달주기 (예: 1달, 2달,2주,1주)"),
    taste: Optional[str] = Query(None, description="맛 (예: 크리미, 카라멜, 베리 등의 맛 표현)"),
    roasting: Optional[str] = Query(None, description="로스팅 정도 (예: 강, 중, 약)"),
    min_price: Optional[float] = Query(None, ge=0, description="최소 가격"),
    max_price: Optional[float] = Query(None, ge=0, description="최대 가격")
):
    filtered_coffee_beans = []
    for coffee_bean in coffee_bean_regular_delivery_data:
        if name and name != coffee_bean["name"]:
            continue
        if period and period != coffee_bean["period"]:
            continue
        if taste and taste not in coffee_bean["taste"]:
            continue
        if roasting and roasting != coffee_bean["roasting"]:
            continue
        if min_price is not None and coffee_bean["price"] < min_price:
            continue
        if max_price is not None and coffee_bean["price"] > max_price:
            continue
        filtered_coffee_beans.append(coffee_bean)
    
    return filtered_coffee_beans

vegetable_delivery_data = [
    {
        "name": "신선꾸러미",
        "period": "1주",
        "constitute": ["두부", "애호박", "쌈채소", "유정란"],
        "price": 29000,
        "desc": "4인 가구에게 추천하는 매주 배송 상품"
    },
    {
        "name": "제철꾸러미",
        "period": "2주",
        "constitute": ["두부", "애호박", "쌈채소", "유정란", "과일", "해조류"],
        "price": 35000,
        "desc": "4인가구에게 추천하는 과일과 해조류를 포함한 상품"
    },
    {
        "name": "1인꾸러미",
        "period": "1달",
        "constitute": ["두부", "과일", "쌈채소", "밑반찬"],
        "price": 25000,
        "desc": "1인가구에게 추천하는 상품. 농가공 반찬 포함."
    },
    {
        "name": "요리도우미꾸러미",
        "period": "2달",
        "constitute": ["과일", "나물", "유정란", "밑반찬"],
        "price": 30000,
        "desc": "신선 나물이 포함된 상품."
    },
    {
        "name": "채식꾸러미",
        "period": "1달",
        "constitute": ["두부", "애호박", "오이", "고추", "쌈채소"],
        "price": 28000,
        "desc": "채식 생활을 도와주는 상품."
    }
]

@app.get("/vegetable_delivery")
async def filter_vegetable_delivery(
    name: Optional[str] = Query(None, description="상품이름"),
    period: Optional[str] = Query(None, description="배달주기 (예: 1달, 2달, 2주, 1주)"),
    constitute: Optional[str] = Query(None, description="구성품목 (예: 애호박, 쌈채소, 두부 등)"),
    min_price: Optional[float] = Query(None, ge=0, description="최소 가격"),
    max_price: Optional[float] = Query(None, ge=0, description="최대 가격")
):
    filtered_vegetables = []
    for vegetable in vegetable_delivery_data:
        if name and name != vegetable["name"]:
            continue
        if period and period != vegetable["period"]:
            continue
        if constitute and constitute not in vegetable["constitute"]:
            continue
        if min_price is not None and vegetable["price"] < min_price:
            continue
        if max_price is not None and vegetable["price"] > max_price:
            continue
        filtered_vegetables.append(vegetable)
    
    return filtered_vegetables

egg_menu_data = [
    {
        "name": "날달걀밥",
        "category": "밥",
        "stuff": ["밥", "간장"],
        "difficulty": 1,
        "desc": "신선한 날달걀을 따끈한 밥 위에 얹어서 간장을 곁들인다. 추가적으로 명란젓이나 김치, 아보카도를 곁들여도 좋다."
    },
    {
        "name": "에그베네딕트",
        "category": "빵",
        "stuff": ["잉글리시 머핀", "토마토", "베이컨", "상추", "버터", "소금", "후추", "레몬즙"],
        "difficulty": 2,
        "desc": "/홀랜다이즈 소스/ 1. 무염버터를 전자레인지에서 약 40초 가열해서 녹인다. 2. 거기에 레몬즙을 약간 추가하고 버터를 조금씩 더 넣어가면서 거품을 낸다. 걸쭉해지면 소금과 후추를 넣는다. /에그 베네딕트/ 1. 냄비에 물을 넣고 끓인다. 2. 물이 끓으면 약불로 줄이고 소금과 식초를 약간 넣은 뒤에 계란을 넣어 수란을 만든다. 3. 베이컨과 잉글리시 머핀을 구운 뒤에 홀랜다이즈 소스와 상추, 토마로를 얹는다."
    },
    {
        "name": "달걀국",
        "category": "국",
        "stuff": ["육수", "간장", "소금", "파"],
        "difficulty": 2,
        "desc": "1. 날달걀을 볼에 깨뜨려 넣고 잘 풀어준다. 2. 육수를 냄비에 넣고 불에 올려 데운 뒤에 간장과 소금으로 간을 한다. 3. 물이 끓어오르면 계란을 풀어서 넣어주고 잘게 썬 파를 넣는다."
    },
    {
        "name": "푸딩",
        "category": "디저트",
        "stuff": ["설탕", "우유", "생크림", "카라멜소스"],
        "difficulty": 4,
        "desc": "1. 카라멜소스를 푸딩 틀에 넣어준다. 2. 달걀 노른자 3개와 생크림과 우유를 넣고 거품기로 거품이 일지 않게 잘 섞어준다. 3. 푸딩 틀에 계란물을 조심스럽게 넣어주고 160도로 예열한 오븐에서 45분 가량 구워준다. 오븐 팬에는 푸딩틀이 약간 잠길 정도로 뜨거운 물을 넣는다. 4. 한 김 식으면 냉장고에 넣어 차게 만든다."
    },
    {
        "name": "토마토달걀볶음",
        "category": "반찬",
        "stuff": ["토마토", "마늘", "소금", "파", "양파", "참기름"],
        "difficulty": 2,
        "desc": "1. 볼에 달걀을 넣고 깨뜨려 잘 풀어놓는다. 2. 프라이펜에 참기름을 둘러 달군 뒤에 마늘을 넣고 볶다가 약불로 줄인다. 3. 토마토와 파와 양파를 썰어논 것을 같이 볶는다. 4. 계란물을 넣고 약한 불에 같이 볶아주며 소금으로 간을 한다."
    }
]

@app.get("/EggMenu")
async def filter_egg_menu(
    name: Optional[str] = Query(None, description="요리이름"),
    category: Optional[str] = Query(None, description="요리종류 (예: 밥, 반찬, 국, 빵, 디저트 등)"),
    stuff: Optional[str] = Query(..., description="재료 (예: 밥, 간장, 설탕, 양파 등)"),
    min_difficulty: Optional[float] = Query(None, ge=1, le=5, description="최저난이도(1에서 5까지)"),
    max_difficulty: Optional[float] = Query(None, ge=1, le=5, description="최고난이도(1에서 5까지)")
):
    filtered_menus = []
    for menu in egg_menu_data:
        if name and name != menu["name"]:
            continue
        if category and category != menu["category"]:
            continue
        if stuff and stuff not in menu["stuff"]:
            continue
        if min_difficulty is not None and menu["difficulty"] < min_difficulty:
            continue
        if max_difficulty is not None and menu["difficulty"] > max_difficulty:
            continue
        filtered_menus.append(menu)
    
    return filtered_menus

greek_yogurt_data = [
    {
        "name": "그릭데이",
        "gooey": 4,
        "price": 14000,
        "protein": 11.42,
        "sugar": 1.86
    },
    {
        "name": "오디오시",
        "gooey": 5,
        "price": 19500,
        "protein": 6.6,
        "sugar": 2
    },
    {
        "name": "요즘",
        "gooey": 3,
        "price": 16500,
        "protein": 11.42,
        "sugar": 2.4
    },
    {
        "name": "룩스 아이슬란딕",
        "gooey": 1,
        "price": 9000,
        "protein": 3,
        "sugar": 10.6
    },
    {
        "name": "매일 바이오",
        "gooey": 1,
        "price": 6500,
        "protein": 5,
        "sugar": 4.5
    }
]

@app.get("/GreekYogurt")
async def filter_greek_yogurt(
    name: str = Query(..., description="상품명"),
    min_gooey: Optional[float] = Query(None, ge=0, le=5, description="최저꾸덕함(1에서 5까지)"),
    max_gooey: Optional[float] = Query(None, ge=0, le=5, description="최고꾸덕함(1에서 5까지)"),
    min_price: Optional[float] = Query(None, ge=0, description="최소가격(500g기준)"),
    max_price: Optional[float] = Query(None, ge=0, description="최대가격(500g기준)"),
    min_protein: Optional[float] = Query(None, ge=0, description="최소단백질함량(100g 기준)"),
    max_protein: Optional[float] = Query(None, ge=0, description="최대단백질함량(100g 기준)")
):
    filtered_yogurts = []
    for yogurt in greek_yogurt_data:
        if name != yogurt["name"]:
            continue
        if min_gooey is not None and yogurt["gooey"] < min_gooey:
            continue
        if max_gooey is not None and yogurt["gooey"] > max_gooey:
            continue
        if min_price is not None and yogurt["price"] < min_price:
            continue
        if max_price is not None and yogurt["price"] > max_price:
            continue
        if min_protein is not None and yogurt["protein"] < min_protein:
            continue
        if max_protein is not None and yogurt["protein"] > max_protein:
            continue
        filtered_yogurts.append(yogurt)
    
    return filtered_yogurts


toilet_paper_data = [
    {
        "name": "깨끗한나라 순수 시그니처",
        "sheets": "3겹",
        "aroma": True,
        "natural": True,
        "non_fluore": True,
        "length": 28,
        "price": 21500,
        "review": "먼지 적고 좋아요"
    },
    {
        "name": "노브랜드 서프라이즈",
        "sheets": "3겹",
        "aroma": False,
        "natural": True,
        "non_fluore": False,
        "length": 30,
        "price": 18500,
        "review": "가성비가 좋아요"
    },
    {
        "name": "모나리자 자연이 좋은",
        "sheets": "4겹",
        "aroma": False,
        "natural": True,
        "non_fluore": True,
        "length": 27,
        "price": 25500,
        "review": "도톰해요"
    },
    {
        "name": "잘풀리는집 클래식 데코 플러스",
        "sheets": "3겹",
        "aroma": True,
        "natural": False,
        "non_fluore": False,
        "length": 28,
        "price": 23500,
        "review": "향이 괜찮아요"
    },
    {
        "name": "코디 에코그린 바스티슈",
        "sheets": "4겹",
        "aroma": False,
        "natural": False,
        "non_fluore": True,
        "length": 30,
        "price": 28500,
        "review": "환경 생각하며 샀어요"
    }
]

@app.get("/ToiletPaper")
async def filter_toilet_paper(
    name: str = Query(None, description="상품명"),
    sheets: str = Query(..., description="겹수 (예: 2겹, 3겹, 4겹 등)"),
    aroma: Optional[bool] = Query(None, description="향여부"),
    natural: Optional[bool] = Query(None, description="천연펄프여부"),
    non_fluore: Optional[bool] = Query(None, description="무형광여부"),
    min_length: Optional[float] = Query(None, ge=0, description="최소길이(m단위)"),
    max_length: Optional[float] = Query(None, ge=0, description="최대길이(m단위)"),
    min_price: Optional[float] = Query(None, ge=0, description="최소가격"),
    max_price: Optional[float] = Query(None, ge=0, description="최대가격")
):
    filtered_toilet_papers = []
    for toilet_paper in toilet_paper_data:
        if name is not None and name != toilet_paper["name"]:
            continue
        if sheets != toilet_paper["sheets"]:
            continue
        if aroma is not None and aroma != toilet_paper["aroma"]:
            continue
        if natural is not None and natural != toilet_paper["natural"]:
            continue
        if non_fluore is not None and non_fluore != toilet_paper["non_fluore"]:
            continue
        if min_length is not None and toilet_paper["length"] < min_length:
            continue
        if max_length is not None and toilet_paper["length"] > max_length:
            continue
        if min_price is not None and toilet_paper["price"] < min_price:
            continue
        if max_price is not None and toilet_paper["price"] > max_price:
            continue
        filtered_toilet_papers.append(toilet_paper)
    
    return filtered_toilet_papers

baby_fabric_data = [
    {
        "name": "토끼띠 배냇저고리 세트",
        "category": "의류",
        "gift": ["출산"],
        "price": 132000,
        "organic_cottonn": False,
        "desc": "2023년 토끼의 해 배냇저고리를 선보입니다."
    },
    {
        "name": "사슴 자수 매트",
        "category": "침구",
        "gift": ["출산", "백일", "일상"],
        "price": 32000,
        "organic_cottonn": False,
        "desc": "갓난 아기부터, 배변 훈련을 시작한 유아기까지 유용하게 사용됩니다."
    },
    {
        "name": "가제 손수건",
        "category": "일상용품",
        "gift": ["출산", "백일", "일상"],
        "price": 12000,
        "organic_cottonn": True,
        "desc": "활용도가 좋은 가제 손수건. 자수가 놓여 있습니다."
    },
    {
        "name": "사슴 딸랑이 인형",
        "category": "장난감",
        "gift": ["출산", "백일", "일상"],
        "price": 72000,
        "organic_cottonn": True,
        "desc": "사슴 모양의 딸랑이 인형. 아기가 물고 빨아도 괜찮습니다."
    },
    {
        "name": "유아 배꼽 이불",
        "category": "침구",
        "gift": ["출산", "백일", "일상", "돌"],
        "price": 29000,
        "organic_cottonn": False,
        "desc": "여름이불이나 외출 이불로 적합합니다."
    }
]

@app.get("/BabyFabric")
async def filter_baby_fabric(
    name: Optional[str] = Query(None, description="상품명"),
    category: str = Query(..., description="상품종류 (예: 의류, 침구, 장난감 등)"),
    gift: Optional[str] = Query(None, description="선물용도 (예: 출산, 백일, 돌, 일상 등)"),
    min_price: Optional[float] = Query(None, ge=0, description="최소가격"),
    max_price: Optional[float] = Query(None, ge=0, description="최대가격"),
    organic_cottonn: Optional[bool] = Query(None, description="오가닉코튼여부")
):
    filtered_baby_fabrics = []
    for baby_fabric in baby_fabric_data:
        if name is not None and name != baby_fabric["name"]:
            continue
        if category != baby_fabric["category"]:
            continue
        if gift is not None and gift not in baby_fabric["gift"]:
            continue
        if min_price is not None and baby_fabric["price"] < min_price:
            continue
        if max_price is not None and baby_fabric["price"] > max_price:
            continue
        if organic_cottonn is not None and organic_cottonn != baby_fabric["organic_cottonn"]:
            continue
        filtered_baby_fabrics.append(baby_fabric)
    
    return filtered_baby_fabrics

seasonal_vegetables_data = [
    {
        "name": "토마토",
        "month": [7, 8, 9],
        "menu": ["토마토 샐러드", "토마토 마리네이드", "스튜", "카레"],
        "calorie": 14,
        "desc": "레드푸드의 선두주자 토마토! 토마토는 과일일까요? 채소일까요? 정답은 채소!! 동맥경화와 간경화에 특히 좋습니다."
    },
    {
        "name": "옥수수",
        "month": [7, 8, 9],
        "menu": ["옥수수 샐러드", "스프", "옥수수빠스", "옥수수죽"],
        "calorie": 106,
        "desc": "톡톡 터지는 알갱이가 씹는 맛을 주는 여름철 간식 옥수수. 옥수수만 먹지 말고 옥수수수염도 차로 끓여 드셔 보세요. 이뇨 효과에 아주 좋답니다."
    },
    {
        "name": "고구마",
        "month": [8, 9, 10],
        "menu": ["고구마 튀김", "고구마밥", "고무마 맛탕", "고구마 케이크"],
        "calorie": 128,
        "desc": "식이섬유소가 풍부한 고구마는 영양간식으로 손색이 없답니다."
    },
    {
        "name": "배추",
        "month": [11, 12],
        "menu": ["배추김치", "배추볶음", "구이", "배춧국"],
        "calorie": 12,
        "desc": "잎, 줄기, 뿌리를 모두 식용하며, 비타민이 풍부하게 함유되어 있어 버릴것이 없는 채소랍니다."
    },
    {
        "name": "우엉",
        "month": [1, 2, 3],
        "menu": ["우엉 튀김", "우엉 잡채", "우엉차", "우엉 파스타"],
        "calorie": 62,
        "desc": "아삭아삭 씹는 맛이 매력인 뿌리채소 우엉! 당질의 일종인 이눌린이 풍부해 신장기능을 높여주고 풍부한 섬유소질이 배변을 촉진한답니다."
    }
]

@app.get("/SeasonalVegetables")
async def filter_seasonal_vegetables(
    name: str = Query(..., description="채소이름"),
    month: Optional[int] = Query(None, description="제철시기 (월 숫자로 표현)"),
    menu: Optional[str] = Query(None, description="활용요리 (예: 토마토 마리네이드, 가지 절임 등)"),
    min_calorie: Optional[float] = Query(None, ge=0, description="최저칼로리(100g 기준)"),
    max_calorie: Optional[float] = Query(None, ge=0, description="최고칼로리(100g 기준)")
):
    filtered_seasonal_vegetables = []
    for vegetable in seasonal_vegetables_data:
        if name != vegetable["name"]:
            continue
        if month is not None and month not in vegetable["month"]:
            continue
        if menu is not None and menu not in vegetable["menu"]:
            continue
        if min_calorie is not None and vegetable["calorie"] < min_calorie:
            continue
        if max_calorie is not None and vegetable["calorie"] > max_calorie:
            continue
        filtered_seasonal_vegetables.append(vegetable)
    
    return filtered_seasonal_vegetables

cat_scratcher_data = [
    {
        "name": "네네린도 우드 수직",
        "material": "합판, 종이",
        "category": "패드형",
        "price": 25000,
        "review": "리필형이라 좋아요"
    },
    {
        "name": "가또나인 평판",
        "material": "종이",
        "category": "패드형",
        "price": 18000,
        "review": "가성비가 좋아요"
    },
    {
        "name": "옥희독희 숨숨집",
        "material": "종이",
        "category": "하우스형",
        "price": 39000,
        "review": "디자인이 귀여워요"
    },
    {
        "name": "따스넉 벽 스크래처",
        "material": "카페트",
        "category": "패드형",
        "price": 45000,
        "review": "공간 활용에 좋아요"
    },
    {
        "name": "도레미파 냥오름",
        "material": "카페트",
        "category": "기둥형",
        "price": 75000,
        "review": "오래 쓸 수 있어요"
    }
]

@app.get("/CatScratcher")
async def filter_cat_scratcher(
    name: Optional[str] = Query(None, description="상품명"),
    material: str = Query(..., description="재질 (예: 박스, 카페트 등)"),
    category: Optional[str] = Query(None, description="형태종류 (예: 패드형, 기둥형, 하우스형 등)"),
    min_price: Optional[float] = Query(None, ge=0, description="최소가격"),
    max_price: Optional[float] = Query(None, ge=0, description="최대가격")
):
    filtered_cat_scratcher = []
    for scratcher in cat_scratcher_data:
        if name is not None and name != scratcher["name"]:
            continue
        if material != scratcher["material"]:
            continue
        if category is not None and category != scratcher["category"]:
            continue
        if min_price is not None and scratcher["price"] < min_price:
            continue
        if max_price is not None and scratcher["price"] > max_price:
            continue
        filtered_cat_scratcher.append(scratcher)
    
    return filtered_cat_scratcher

cat_toy_data = [
    {
        "name": "네네린도 쥐꼬리 막대",
        "material": "깃털, 끈",
        "category": "낚싯대",
        "price": 25000,
        "review": "리필형이라 좋아요"
    },
    {
        "name": "가또나인 팡팡솜인형",
        "material": "섬유",
        "category": "인형",
        "price": 18000,
        "review": "가성비가 좋아요"
    },
    {
        "name": "옥희독희 데구르 볼",
        "material": "플라스틱",
        "category": "공",
        "price": 9000,
        "review": "디자인이 귀여워요"
    },
    {
        "name": "따스넉 바스락 터널",
        "material": "섬유",
        "category": "터널",
        "price": 45000,
        "review": "공간 활용에 좋아요"
    },
    {
        "name": "도레미파 레이저",
        "material": "금속",
        "category": "레이저포인터",
        "price": 25000,
        "review": "오래 쓸 수 있어요"
    }
]

@app.get("/CatToy")
async def filter_cat_toy(
    name: Optional[str] = Query(None, description="상품명"),
    material: Optional[str] = Query(None, description="재질 (예: 깃털, 끈, 원목, 종이, 플라스틱 등)"),
    category: str = Query(..., description="종류 (예: 낚싯대, 인형, 공, 터널, 주머니, 레이저포인터 등)"),
    min_price: Optional[float] = Query(None, ge=0, description="최소가격"),
    max_price: Optional[float] = Query(None, ge=0, description="최대가격")
):
    filtered_cat_toy = []
    for toy in cat_toy_data:
        if name is not None and name != toy["name"]:
            continue
        if material is not None and material != toy["material"]:
            continue
        if category != toy["category"]:
            continue
        if min_price is not None and toy["price"] < min_price:
            continue
        if max_price is not None and toy["price"] > max_price:
            continue
        filtered_cat_toy.append(toy)
    
    return filtered_cat_toy

rose_cut_flower_data = [
    {
        "name": "언포켓터블",
        "origin": "콜롬비아",
        "aroma": "과일향",
        "color": "아이보리",
        "price": 29000,
        "stock": 21
    },
    {
        "name": "스노우플레이크",
        "origin": "한국",
        "aroma": "없음",
        "color": "화이트",
        "price": 19000,
        "stock": 71
    },
    {
        "name": "오렌지 크러쉬",
        "origin": "볼리비아",
        "aroma": "없음",
        "color": "오렌지",
        "price": 21000,
        "stock": 51
    },
    {
        "name": "푸에고",
        "origin": "콜롬비아",
        "aroma": "꽃향",
        "color": "레드",
        "price": 23000,
        "stock": 11
    },
    {
        "name": "하젤",
        "origin": "한국",
        "aroma": "과일향",
        "color": "핑크",
        "price": 21000,
        "stock": 91
    }
]

@app.get("/RoseCutFlower")
async def filter_rose_cut_flower(
    name: Optional[str] = Query(None, description="장미명"),
    origin: Optional[str] = Query(None, description="원산지"),
    aroma: Optional[str] = Query(None, description="향기"),
    color: str = Query(..., description="색상 (예: 레드, 핑크, 화이트 등)"),
    min_price: Optional[float] = Query(None, ge=0, description="최소가격"),
    max_price: Optional[float] = Query(None, ge=0, description="최대가격")
):
    filtered_rose_cut_flower = []
    for flower in rose_cut_flower_data:
        if name is not None and name != flower["name"]:
            continue
        if origin is not None and origin != flower["origin"]:
            continue
        if aroma is not None and aroma != flower["aroma"]:
            continue
        if color != flower["color"]:
            continue
        if min_price is not None and flower["price"] < min_price:
            continue
        if max_price is not None and flower["price"] > max_price:
            continue
        filtered_rose_cut_flower.append(flower)
    
    return filtered_rose_cut_flower

rose_plants_data = [
    {
        "name": "라이온스",
        "origin": "독일",
        "category": "관목",
        "color": "아이보리",
        "price": 16000,
        "winter_t": -15,
        "desc": "우아한 연살구빛, 화분용 추천"
    },
    {
        "name": "헤리티지",
        "origin": "영국",
        "category": "덩굴",
        "color": "핑크",
        "price": 40000,
        "winter_t": -5,
        "desc": "데이비드 오스틴사의 핑크빛 장미"
    },
    {
        "name": "클레어 오스틴",
        "origin": "영국",
        "category": "덩굴",
        "color": "화이트",
        "price": 42000,
        "winter_t": -10,
        "desc": "데이비드 오스틴사의 내병성 좋은 흰색 장미"
    },
    {
        "name": "스칼렛 메이앙",
        "origin": "프랑스",
        "category": "관목",
        "color": "레드",
        "price": 35000,
        "winter_t": -15,
        "desc": "메이앙사의 관목형 미니 장미"
    },
    {
        "name": "레이니 블루",
        "origin": "일본",
        "category": "관목",
        "color": "퍼플",
        "price": 76000,
        "winter_t": -0,
        "desc": "까다롭지만 아름다운 연보라색 장미"
    }
]

@app.get("/RosePlants")
async def filter_rose_plants(
    name: Optional[str] = Query(None, description="장미명"),
    origin: Optional[str] = Query(None, description="원산지"),
    category: Optional[str] = Query(None, description="형태종류 (예: 덩굴, 관목)"),
    color: str = Query(..., description="색상 (예: 레드, 핑크, 화이트 등)"),
    min_price: Optional[float] = Query(None, ge=0, description="최소가격"),
    max_price: Optional[float] = Query(None, ge=0, description="최대가격"),
    min_winter_t: Optional[float] = Query(None, description="최소월동온도(섭씨 기준)"),
    max_winter_t: Optional[float] = Query(None, description="최대월동온도(섭씨 기준)")
):
    filtered_rose_plants = []
    for plant in rose_plants_data:
        if name is not None and name != plant["name"]:
            continue
        if origin is not None and origin != plant["origin"]:
            continue
        if category is not None and category != plant["category"]:
            continue
        if color != plant["color"]:
            continue
        if min_price is not None and plant["price"] < min_price:
            continue
        if max_price is not None and plant["price"] > max_price:
            continue
        if min_winter_t is not None and plant["winter_t"] < min_winter_t:
            continue
        if max_winter_t is not None and plant["winter_t"] > max_winter_t:
            continue
        filtered_rose_plants.append(plant)
    
    return filtered_rose_plants

door_to_door_parcel_reservation_data = [
    {
        "name": "이진서",
        "address": "서울시 마포구 연남로 43-2",
        "tel": "010-0000-0001",
        "size": "소",
        "weight": "소",
        "date": "2023-07-14",
        "pay": True
    },
    {
        "name": "서유림",
        "address": "서울시 마포구 연남동 390-56",
        "tel": "010-0000-0002",
        "size": "소",
        "weight": "소",
        "date": "2023-07-15",
        "pay": False
    },
    {
        "name": "윤진형",
        "address": "서울시 관악구 인헌로 43-12",
        "tel": "010-0000-0003",
        "size": "소",
        "weight": "중",
        "date": "2023-07-25",
        "pay": True
    },
    {
        "name": "김준영",
        "address": "제주시 탑동로2길 3",
        "tel": "010-0000-0004",
        "size": "대",
        "weight": "소",
        "date": "2023-07-19",
        "pay": True
    },
    {
        "name": "박선화",
        "address": "제주시 한림읍 명랑로 8",
        "tel": "010-0000-0005",
        "size": "대",
        "weight": "대",
        "date": "2023-07-24",
        "pay": False
    }
]

@app.get("/DoorToDoorParcelReservation")
async def filter_door_to_door_parcel_reservation(
    name: str = Query(..., description="발송자"),
    location: Optional[str] = Query(None, description="발송지 (구단위, 예: 마포구, 구로구 등)"),
    tel: Optional[str] = Query(None, description="연락처 (발송자 연락처)"),
    size: Optional[str] = Query(None, description="택배크기분류(소, 중, 대)"),
    weight: Optional[str] = Query(None, description="택배중량분류(소, 중, 대)"),
    date: Optional[str] = Query(None, description="예약일 (발송예약일 예: 2023-07-28)")
):
    filtered_reservations = []
    for reservation in door_to_door_parcel_reservation_data:
        if reservation["name"] != name:
            continue
        if location is not None and reservation["address"].find(location) == -1:
            continue
        if tel is not None and reservation["tel"] != tel:
            continue
        if size is not None and reservation["size"] != size:
            continue
        if weight is not None and reservation["weight"] != weight:
            continue
        if date is not None and reservation["date"] != date:
            continue
        filtered_reservations.append(reservation)
    
    return filtered_reservations

apartment_management_data = [
    {
        "name": "이진서",
        "age": 39,
        "room_number": 102,
        "f_number": 2,
        "non_pay": 0,
        "tel": "010-0000-0001"
    },
    {
        "name": "서유림",
        "age": 28,
        "room_number": 101,
        "f_number": 1,
        "non_pay": 0,
        "tel": "010-0000-0002"
    },
    {
        "name": "윤진형",
        "age": 45,
        "room_number": 202,
        "f_number": 4,
        "non_pay": 0,
        "tel": "010-0000-0003"
    },
    {
        "name": "김준영",
        "age": 37,
        "room_number": 201,
        "f_number": 1,
        "non_pay": 23000,
        "tel": "010-0000-0004"
    },
    {
        "name": "박선화",
        "age": 51,
        "room_number": 301,
        "f_number": 3,
        "non_pay": 11000,
        "tel": "010-0000-0005"
    }
]

@app.get("/ApartmentManagement")
async def filter_apartment_management(
    name: Optional[str] = Query(None, description="대표자이름"),
    age: Optional[int] = Query(None, description="대표자나이"),
    room_number: int = Query(..., description="호수"),
    f_number: Optional[int] = Query(None, description="거주자수"),
    non_pay: Optional[int] = Query(None, description="관리비미납내역(총액, 원 단위 표기)")
):
    filtered_apartments = []
    for apartment in apartment_management_data:
        if name is not None and apartment["name"] != name:
            continue
        if age is not None and apartment["age"] != age:
            continue
        if apartment["room_number"] != room_number:
            continue
        if f_number is not None and apartment["f_number"] != f_number:
            continue
        if non_pay is not None and apartment["non_pay"] != non_pay:
            continue
        filtered_apartments.append(apartment)
    
    return filtered_apartments

korean_traditional_wedding_data = [
    {
        "name": "민속촌 종가집",
        "address": "제주도 서귀포시 표선면 민속해안로 631-34",
        "people": 300,
        "price": 60000,
        "desc": "하객 한복대여 가능",
        "tel": "064-000-0000"
    },
    {
        "name": "광주향교",
        "address": "광주 남구 중앙로107번길 5",
        "people": 280,
        "price": 54000,
        "desc": "숙소 대여도 가능",
        "tel": "062-672-7008"
    },
    {
        "name": "삼청각",
        "address": "서울 성북구 성북동 330-115",
        "people": 400,
        "price": 80000,
        "desc": "여러가지 스타일의 예식 컨셉 선택 가능",
        "tel": "02-765-3700"
    },
    {
        "name": "한국의 집",
        "address": "서울 중구 필동 2가 80-2",
        "people": 800,
        "price": 50000,
        "desc": "전통 고증을 걸친 내용의 혼례",
        "tel": "02-2270-1120~3"
    },
    {
        "name": "궁중의례원",
        "address": "서울 용산구 용산동1가 8번지",
        "people": 200,
        "price": 49000,
        "desc": "비가 와도 실내에서 예식 진행 가능",
        "tel": "02-3141-5400"
    }
]

@app.get("/KoreanTraditionalWedding")
async def filter_korean_traditional_wedding(
    name: Optional[str] = Query(None, description="식장이름"),
    location: str = Query(..., description="지역(예: 서울, 인천, 제주 등)"),
    min_people: Optional[int] = Query(None, description="최소수용가능인원"),
    max_people: Optional[int] = Query(None, description="최대수용가능인원"),
    min_price: Optional[int] = Query(None, description="최소음식가격(1인 기준)"),
    max_price: Optional[int] = Query(None, description="최대음식가격(1인 기준)")
):
    filtered_weddings = []
    for wedding in korean_traditional_wedding_data:
        if name is not None and wedding["name"] != name:
            continue
        if wedding["address"].startswith(location):
            if min_people is not None and wedding["people"] < min_people:
                continue
            if max_people is not None and wedding["people"] > max_people:
                continue
            if min_price is not None and wedding["price"] < min_price:
                continue
            if max_price is not None and wedding["price"] > max_price:
                continue
            filtered_weddings.append(wedding)
    
    return filtered_weddings

bagel_store_data = [
    {
        "name": "포비",
        "address": "서울특별시 종로구 종로3길 17",
        "parking": True,
        "rating": 4.3,
        "review": "세트가 가성비가 좋다"
    },
    {
        "name": "에브리띵베이글",
        "address": "서울특별시 서대문구 연희로11길 29",
        "parking": True,
        "rating": 4.2,
        "review": "쫄깃한 식감"
    },
    {
        "name": "코끼리베이글",
        "address": "서울특별시 영등포구 선유로 176",
        "parking": False,
        "rating": 4.1,
        "review": "화덕 탓인지 아주 맛있는 빵 맛"
    },
    {
        "name": "훕훕베이글",
        "address": "경기도 광명시 시청로 124",
        "parking": True,
        "rating": 3.9,
        "review": "다채로운 종류의 토핑"
    },
    {
        "name": "만동제과",
        "address": "강원도 강릉시 금성로 6",
        "parking": False,
        "rating": 3.8,
        "review": "짭쪼름한 맛"
    }
]

@app.get("/BagelStore")
async def filter_bagel_store(
    name: Optional[str] = Query(None, description="업체명"),
    location: str = Query(..., description="지역(구 단위, 예: 성동구, 구로구 등)"),
    parking: Optional[bool] = Query(None, description="주차가능여부"),
    min_rating: Optional[float] = Query(None, description="최소평점(1에서 5)"),
    max_rating: Optional[float] = Query(None, description="최대평점(1에서 5)")
):
    filtered_stores = []
    for store in bagel_store_data:
        if name is not None and store["name"] != name:
            continue
        if store["address"].startswith(location):
            if parking is not None and store["parking"] != parking:
                continue
            if min_rating is not None and store["rating"] < min_rating:
                continue
            if max_rating is not None and store["rating"] > max_rating:
                continue
            filtered_stores.append(store)
    
    return filtered_stores

eco_friendly_packaging_data = [
    {
        "name": "버블페이퍼",
        "category": "완충재",
        "material": "종이",
        "price": 23000,
        "desc": "크라프트 종이로 된 완충재"
    },
    {
        "name": "옥수수방울이",
        "category": "완충재",
        "material": "옥수수전분",
        "price": 54000,
        "desc": "물에 잘 녹는 옥수수 전분으로 만든 완충재"
    },
    {
        "name": "메가페이퍼",
        "category": "택배봉투",
        "material": "종이",
        "price": 28000,
        "desc": "크라프트 종이로 된 완충재가 들어간 안전 봉투"
    },
    {
        "name": "생분해 친구봉투",
        "category": "택배봉투",
        "material": "생분해성 비닐",
        "price": 53000,
        "desc": "생분해성 비닐을 이용해서 비가 오는 날도 안전하게"
    },
    {
        "name": "친환경 크라프트테이프",
        "category": "테이프",
        "material": "종이",
        "price": 26000,
        "desc": "크라프트 종이와 실리콘으로 만들어져서 종이로 분류해서 버리는 종이테이프"
    }
]

@app.get("/EcoFriendlyPackaging")
async def filter_eco_friendly_packaging(
    name: Optional[str] = Query(None, description="상품명"),
    category: str = Query(..., description="종류(예: 완충재, 택배봉투 등)"),
    material: Optional[str] = Query(None, description="재질 (예: 종이, 생분해성 비닐 등)"),
    min_price: Optional[float] = Query(None, description="최소가격"),
    max_price: Optional[float] = Query(None, description="최대가격")
):
    filtered_packaging = []
    for packaging in eco_friendly_packaging_data:
        if name is not None and packaging["name"] != name:
            continue
        if packaging["category"] == category:
            if material is not None and packaging["material"] != material:
                continue
            if min_price is not None and packaging["price"] < min_price:
                continue
            if max_price is not None and packaging["price"] > max_price:
                continue
            filtered_packaging.append(packaging)
    
    return filtered_packaging

cordless_electric_fan_data = [
    {
        "name": "미니아 무선 선풍기 무소음",
        "category": "스탠드형",
        "mode": ["초미풍", "초초미풍", "수면풍"],
        "price": 149000,
        "review": "파워도 좋고 아주 편리해요"
    },
    {
        "name": "듀플랙스 미니미 화이트",
        "category": "탁상형",
        "mode": ["초미풍"],
        "price": 39000,
        "review": "디자인이 좋아요"
    },
    {
        "name": "윈드프로 핸디",
        "category": "휴대용",
        "mode": ["초미풍"],
        "price": 29000,
        "review": "충전을 자주 해야해서 번거롭네요"
    },
    {
        "name": "캠퍼프로 윈디",
        "category": "탁상형",
        "mode": ["수면풍"],
        "price": 129000,
        "review": "철제 디자인이라 좋아요"
    },
    {
        "name": "접이식 오아 선풍기",
        "category": "스탠드형",
        "mode": ["초미풍", "초초미풍"],
        "price": 249000,
        "review": "접이식으로 작게 축소할 수 있어요"
    }
]

@app.get("/CordlessElectricFan")
async def filter_cordless_electric_fan(
    name: Optional[str] = Query(None, description="상품명"),
    category: str = Query(..., description="종류(예: 스탠드형, 탁상형, 휴대용 등)"),
    mode: Optional[List[str]] = Query(None, description="바람모드 (예: 초미풍, 초초미풍, 수면풍)"),
    min_price: Optional[float] = Query(None, description="최소가격"),
    max_price: Optional[float] = Query(None, description="최대가격")
):
    filtered_fans = []
    for fan in cordless_electric_fan_data:
        if name is not None and fan["name"] != name:
            continue
        if fan["category"] == category:
            if mode is not None and not set(mode).issubset(set(fan["mode"])):
                continue
            if min_price is not None and fan["price"] < min_price:
                continue
            if max_price is not None and fan["price"] > max_price:
                continue
            filtered_fans.append(fan)
    
    return filtered_fans


jjamppong_data = [
    {
        "menu": "기본짬뽕",
        "spicy": 1,
        "stuff": ["오징어", "홍합", "양파", "당근"],
        "price": 7000,
        "review": "적당히 매워서 좋아요"
    },
    {
        "menu": "쟁반짬뽕",
        "spicy": 2,
        "stuff": ["갑오징어", "버섯", "오징어", "홍합", "양파", "당근"],
        "price": 9000,
        "review": "불맛나는 볶음짬뽕 맛있어요"
    },
    {
        "menu": "차돌짬뽕",
        "spicy": 3,
        "stuff": ["차돌박이", "버섯", "양파", "당근"],
        "price": 11000,
        "review": "국물이 아주 좋아요"
    },
    {
        "menu": "굴짬뽕",
        "spicy": 2,
        "stuff": ["오징어", "홍합", "굴", "양파", "당근"],
        "price": 10000,
        "review": "굴이 들어가서 아주 시원해요"
    },
    {
        "menu": "불짬뽕",
        "spicy": 5,
        "stuff": ["오징어", "홍합", "양파", "당근", "콩나물"],
        "price": 9000,
        "review": "속이 풀리는 매운맛"
    }
]

@app.get("/Jjamppong")
async def filter_jjamppong(
    menu: Optional[str] = Query(None, description="메뉴명"),
    spicy: Optional[int] = Query(None, description="맵기정도(1에서 5까지)"),
    stuff: str = Query(..., description="재료 (예: 차돌박이, 오징어, 굴 등)"),
    min_price: Optional[float] = Query(None, description="최소가격"),
    max_price: Optional[float] = Query(None, description="최대가격")
):
    filtered_jjamppong = []
    for jjamppong in jjamppong_data:
        if menu is not None and jjamppong["menu"] != menu:
            continue
        if jjamppong["spicy"] == spicy:
            if stuff is not None and stuff not in jjamppong["stuff"]:
                continue
            if min_price is not None and jjamppong["price"] < min_price:
                continue
            if max_price is not None and jjamppong["price"] > max_price:
                continue
            filtered_jjamppong.append(jjamppong)
    
    return filtered_jjamppong

home_shopping_data = [
    {
        "type": "식품",
        "name": "오늘담근 포기김치",
        "price": 35000,
        "discount": True,
        "rating": 4.2
    },
    {
        "type": "뷰티",
        "name": "도브 데오드란트",
        "price": 11000,
        "discount": False,
        "rating": 4.7
    },
    {
        "type": "패션",
        "name": "바캉스 원피스",
        "price": 17500,
        "discount": True,
        "rating": 4.1
    },
    {
        "type": "식품",
        "name": "카무트 쌀",
        "price": 7900,
        "discount": False,
        "rating": 4.6
    },
    {
        "type": "패션",
        "name": "토리버치 샌들",
        "price": 95000,
        "discount": True,
        "rating": 4.8
    }
]

@app.get("/HomeShopping")
async def filter_home_shopping(
    type: Optional[str] = Query(None, description="제품 유형 ex) 식품, 패션, 리빙, 뷰티"),
    name: Optional[str] = Query(None, description="상품명"),
    min_price: Optional[int] = Query(None, description="최소 가격"),
    max_price: Optional[int] = Query(None, description="최대 가격"),
    discount: bool = Query(..., description="할인여부")
):
    filtered_items = []
    for item in home_shopping_data:
        if type is not None and item["type"] != type:
            continue
        if name is not None and item["name"] != name:
            continue
        if min_price is not None and item["price"] < min_price:
            continue
        if max_price is not None and item["price"] > max_price:
            continue
        if item["discount"] != discount:
            continue
        filtered_items.append(item)
    
    return filtered_items

electric_car_data = [
    {
        "brand": "TESLA",
        "country": "미국",
        "founder": "일론 머스크",
        "market_cap": "950조원",
        "ranking": 1,
        "model": "모델 Y"
    },
    {
        "brand": "Volkswagen",
        "country": "독일",
        "founder": "아돌프 히틀러",
        "market_cap": "117조원",
        "ranking": 2,
        "model": "ID.4"
    },
    {
        "brand": "Hyundai Kia",
        "country": "한국",
        "founder": "정주영",
        "market_cap": "41조원",
        "ranking": 3,
        "model": "아이오닉6"
    },
    {
        "brand": "Stellantis",
        "country": "네덜란드",
        "founder": "잔니 아넬리",
        "market_cap": "73조원",
        "ranking": 4,
        "model": "램 1500"
    },
    {
        "brand": "RNM",
        "country": "네덜란드",
        "founder": "장 도미니크 세나르",
        "market_cap": "37조원",
        "ranking": 5,
        "model": "트위지"
    }
]

@app.get("/ElectricCar")
async def filter_electric_car(
    brand: Optional[str] = Query(None, description="브랜드 영문명"),
    country: str = Query(..., description="자동차를 만든 제조 국가"),
    founder: Optional[str] = Query(None, description="브랜드 창립자"),
    market_cap: Optional[str] = Query(None, description="브랜드 시가 총액 (예: 31조. 910억 등)"),
    ranking: Optional[int] = Query(None, description="인도량 순위")
):
    filtered_cars = []
    for car in electric_car_data:
        if brand is not None and car["brand"] != brand:
            continue
        if car["country"] != country:
            continue
        if founder is not None and car["founder"] != founder:
            continue
        if market_cap is not None and car["market_cap"] != market_cap:
            continue
        if ranking is not None and car["ranking"] != ranking:
            continue
        filtered_cars.append(car)
    
    return filtered_cars

coffee_brand_data = [
    {
        "brand": "스타벅스",
        "price": 4500,
        "ranking": 1,
        "market_cap": 1200,
        "preference": 25.7
    },
    {
        "brand": "투썸플레이스",
        "price": 4100,
        "ranking": 2,
        "market_cap": 1000,
        "preference": 6.9
    },
    {
        "brand": "메가커피",
        "price": 1500,
        "ranking": 3,
        "market_cap": 1232,
        "preference": 14.3
    },
    {
        "brand": "이디야커피",
        "price": 3200,
        "ranking": 4,
        "market_cap": 3000,
        "preference": 6.8
    },
    {
        "brand": "빽다방",
        "price": 1500,
        "ranking": 5,
        "market_cap": 750,
        "preference": 8
    }
]

@app.get("/CoffeeBrands")
async def filter_coffee_brands(
    brand: Optional[str] = Query(None, description="브랜드"),
    min_price: Optional[int] = Query(None, description="최소가격"),
    max_price: Optional[int] = Query(None, description="최대가격"),
    ranking: int = Query(..., description="순위"),
    stores_max: Optional[int] = Query(None, description="최대 매장수")
):
    filtered_brands = []
    for coffee_brand in coffee_brand_data:
        if brand is not None and coffee_brand["brand"] != brand:
            continue
        if min_price is not None and coffee_brand["price"] < min_price:
            continue
        if max_price is not None and coffee_brand["price"] > max_price:
            continue
        if coffee_brand["ranking"] != ranking:
            continue
        if stores_max is not None and coffee_brand["market_cap"] > stores_max:
            continue
        filtered_brands.append(coffee_brand)
    
    return filtered_brands

counseling_center_data = [
    {
        "name": "박혜인",
        "subject": "개인상담",
        "center": "미소담심리상담센터",
        "num": 17514,
        "gender": "여성",
        "doctor_name": "김도희"
    },
    {
        "name": "주석진",
        "subject": "집단상담",
        "center": "디딤돌심리상담센터",
        "num": 59815,
        "gender": "남성",
        "doctor_name": "이주안"
    },
    {
        "name": "김도영",
        "subject": "부부상담",
        "center": "미소담심리센터",
        "num": 15899,
        "gender": "남성",
        "doctor_name": "최석호"
    },
    {
        "name": "이지선",
        "subject": "개인상담",
        "center": "솔숲심리상담센터",
        "num": 49868,
        "gender": "여성",
        "doctor_name": "김지우"
    },
    {
        "name": "진소하",
        "subject": "부부상담",
        "center": "디딤돌상담센터",
        "num": 17985,
        "gender": "여성",
        "doctor_name": "유미래"
    }
]

@app.get("/CounselingCenter")
async def filter_counseling_center(
    name: Optional[str] = Query(None, description="고객명"),
    subject: str = Query(..., description="주제"),
    center: Optional[str] = Query(None, description="상담센터명"),
    num: Optional[int] = Query(None, description="고객 등록 번호"),
    gender: Optional[str] = Query(None, description="고객 성별")
):
    filtered_customers = []
    for customer in counseling_center_data:
        if name is not None and customer["name"] != name:
            continue
        if customer["subject"] != subject:
            continue
        if center is not None and customer["center"] != center:
            continue
        if num is not None and customer["num"] != num:
            continue
        if gender is not None and customer["gender"] != gender:
            continue
        filtered_customers.append(customer)
    
    return filtered_customers

pantone_color_data = [
    {
        "number": "18-1750",
        "name": "비바 마젠타(Viva Magenta)",
        "year": 2023,
        "series": "레드",
        "matt": False
    },
    {
        "number": "13-1106",
        "name": "샌드 달러(Sand dollar)",
        "year": 2006,
        "series": "브라운",
        "matt": True
    },
    {
        "number": "19-4052",
        "name": "클래식 블루(Classic Blue)",
        "year": 2020,
        "series": "블루",
        "matt": True
    },
    {
        "number": "18-2120",
        "name": "탠저린 탱고(Tangerine Tango)",
        "year": 2012,
        "series": "레드",
        "matt": True
    },
    {
        "number": "19-1664",
        "name": "True Red(트루 레드)",
        "year": 2002,
        "series": "레드",
        "matt": False
    }
]

@app.get("/PantoneColor")
async def filter_pantone_color(
    number: Optional[str] = Query(None, description="컬러번호"),
    name_KOR: Optional[str] = Query(None, description="한글명"),
    name_ENG: Optional[str] = Query(None, description="영문명"),
    year: Optional[int] = Query(None, description="선정 연도"),
    series: str = Query(..., description="계열"),
    matte: Optional[bool] = Query(None, description="유무광구분")
):
    filtered_colors = []
    for color in pantone_color_data:
        if number is not None and color["number"] != number:
            continue
        if name_KOR is not None and color["name"].split('(')[0] != name_KOR:
            continue
        if name_ENG is not None and color["name"].split('(')[1][:-1] != name_ENG:
            continue
        if year is not None and color["year"] != year:
            continue
        if color["series"] != series:
            continue
        if matte is not None and bool(matte) != bool(matte):
            continue
        filtered_colors.append(color)
    
    return filtered_colors

@app.get("/CVSPB")
async def filter_CVSPB(
    CVS_name: str = Query(..., description="편의점명"),
    type: str = Query(None, description="상품종류 ex) 스낵, 음료, 도시락"),
    product_name: str = Query(None, description="상품명"),
    max_price: int = Query(None, ge=0, description="최대 가격"),
    discount: float = Query(None, description="할인율"),
):
    # 편의점 PB 상품 데이터
    CVSPB = [
        ["CU", "스낵", "콘소메맛 팝콘", 2000, 10],
        ["GS25", "도시락", "김혜자 도시락", 3900, 20],
        ["GS25", "음료", "카페 25", 2100, 50],
        ["CU", "음료", "GET 커피", 2000, 90],
        ["CU", "스낵", "HEYROO감자칩", 2500, 20],
    ]

    filtered_products = []

    for product in CVSPB:
        if (
            (product[0] == CVS_name) and
            (product[1] == type if type else True) and
            (product[2] == product_name if product_name else True) and
            (product[3] <= max_price if max_price else True) and
            (product[4] == discount if discount else True)
        ):
            filtered_products.append({
                "CVS_name": product[0],
                "type": product[1],
                "product_name": product[2],
                "price": product[3],
                "discount": product[4]
            })

    return filtered_products

atm_data = [
    {
        "name": "신협은행",
        "city": "충청북도",
        "district": "청주시",
        "town": "상당구",
        "available": True,
        "operating_time": "매일 07:00 - 24:00"
    },
    {
        "name": "신한은행",
        "city": "경기도",
        "district": "안산시",
        "town": "상록구",
        "available": False,
        "operating_time": "매일 07:00 - 23:30"
    },
    {
        "name": "우리은행",
        "city": "경기도",
        "district": "수원시",
        "town": "권선구",
        "available": True,
        "operating_time": "매일 09:00 - 24:00"
    },
    {
        "name": "농협은행",
        "city": "경기도",
        "district": "수원시",
        "town": "팔달구",
        "available": False,
        "operating_time": "매일 07:00 - 23:00"
    },
    {
        "name": "하나은행",
        "city": "경기도",
        "district": "안양시",
        "town": "만안구",
        "available": True,
        "operating_time": "매일 08:00 - 24:00"
    }
]

@app.get("/ATM")
async def filter_atm(
    name: str = Query(None, description="은행명"),
    city: str = Query(None, description="광역시도"),
    district: str = Query(None, description="시군구"),
    town: str = Query(None, description="읍면동"),
    available: bool = Query(..., description="24시간 운영 여부")
):
    filtered_atm = []
    for item in atm_data:
        if name is not None and item["name"] != name:
            continue
        if city is not None and item["city"] != city:
            continue
        if district is not None and item["district"] != district:
            continue
        if town is not None and item["town"] != town:
            continue
        if item["available"] != available:
            continue
        filtered_atm.append(item)
    
    return filtered_atm

netflix_data = [
    {
        "name": "하트시그널",
        "year": 2023,
        "director": "박철환",
        "genre": "리얼리티",
        "ranking": 6,
        "viewing_age": 15,
        "episodes": 14
    },
    {
        "name": "귀멸의 칼날",
        "year": 2021,
        "director": "소토자키 하루오",
        "genre": "애니",
        "ranking": 7,
        "viewing_age": 19,
        "episodes": 26
    },
    {
        "name": "마당이 있는집",
        "year": 2023,
        "director": "정지현",
        "genre": "드라마",
        "ranking": 2,
        "viewing_age": 15,
        "episodes": 8
    },
    {
        "name": "킹더랜드",
        "year": 2023,
        "director": "임현욱",
        "genre": "드라마",
        "ranking": 3,
        "viewing_age": 15,
        "episodes": 16
    },
    {
        "name": "사냥개들",
        "year": 2023,
        "director": "김주환",
        "genre": "드라마",
        "ranking": 4,
        "viewing_age": 18,
        "episodes": 8
    }
]

@app.get("/Netflix")
async def filter_netflix(
    name: str = Query(None, description="작품명"),
    year: int = Query(None, description="작품이 나온 연도"),
    director: str = Query(None, description="감독"),
    genre: str = Query(..., description="장르"),
    ranking: int = Query(None, gt=0, le=10, description="순위"),
    min_viewing_age: int = Query(None, gt=0, description="최소 관람연령")
):
    filtered_netflix = []
    for item in netflix_data:
        if name is not None and item["name"] != name:
            continue
        if year is not None and item["year"] != year:
            continue
        if director is not None and item["director"] != director:
            continue
        if item["genre"] != genre:
            continue
        if ranking is not None and item["ranking"] != ranking:
            continue
        if min_viewing_age is not None and item["viewing_age"] < min_viewing_age:
            continue
        filtered_netflix.append(item)
    
    return filtered_netflix

book_cafe_data = [
    {
        "cafe_name": "인덱스숍",
        "address": "서울시 광진구 자양동 17-1",
        "rating": 4.6,
        "Business_Hours": 11,
        "closing_time": 22,
        "review": ["구경하러 들어갔다가 책을 2권이나 사버렸어요.", "공간도 다양하고 책도 많고 볼거리도 많음"]
    },
    {
        "cafe_name": "이리카페",
        "address": "서울시 마포구 상수동 337-4",
        "rating": 4.5,
        "Business_Hours": 11,
        "closing_time": 24,
        "review": ["음료맛나고 분위기좋고 다음에또가고싶다", "넉넉히 대화할 수 있는 곳"]
    },
    {
        "cafe_name": "단편집",
        "address": "서울 마포구 동교동 179-10",
        "rating": 4.73,
        "Business_Hours": 12,
        "closing_time": 20,
        "review": ["따듯하다는 단어가 잘 어울리는 북카페입니다", "커피도 커피인데 책 맛집이예요."]
    },
    {
        "cafe_name": "카페꼼마",
        "address": "서울 영등포구 여의도동 34-8",
        "rating": 4.3,
        "Business_Hours": 7,
        "closing_time": 21,
        "review": ["힐링 할 수 있는 너무 좋은 북카페에요", "내부가 넓고 층고가 높아 마음 속이 시원해지는 곳이에요 :)"]
    },
    {
        "cafe_name": "밀크북",
        "address": "경기도 파주시 문발동 532-3",
        "rating": 4.44,
        "Business_Hours": 10,
        "closing_time": 20,
        "review": ["아이랑 같이 와서 책읽고 티타임하기 좋아요~", "주차하기 좋고 책도 많아요"]
    }
]

@app.get("/BookCafe")
async def filter_book_cafe(
    cafe_name: str = Query(None, description="카페 이름"),
    city: str = Query(..., description="광역시도"),
    district: str = Query(..., description="시군구"),
    town: str = Query(None, description="읍면동"),
    min_rating: float = Query(None, gt=0, le=5, description="최소평점"),
    opening_hours: int = Query(None, description="영업시작시간 (예: 5, 7, 11(시간))"),
    closing_time: int = Query(None, description="영업마감시간 (예: 5, 7, 11(시간))")
):
    filtered_book_cafe = []
    for item in book_cafe_data:
        if cafe_name is not None and item["cafe_name"] != cafe_name:
            continue
        if item["address"].startswith(city) and item["address"].find(district) != -1:
            if town is not None and item["address"].find(town) == -1:
                continue
        else:
            continue
        if min_rating is not None and item["rating"] < min_rating:
            continue
        if opening_hours is not None and item["Business_Hours"] != opening_hours:
            continue
        if closing_time is not None and item["closing_time"] != closing_time:
            continue
        filtered_book_cafe.append(item)
    
    return filtered_book_cafe

fruit_data = [
    {
        "name": "사과",
        "type": "빨간색",
        "nutrient": "리코펜",
        "efficacy": "암예방",
        "calories": 57
    },
    {
        "name": "파파야",
        "type": "주황색",
        "nutrient": "베타카로틴",
        "efficacy": "심장 및 눈 질환 예방",
        "calories": 25
    },
    {
        "name": "레몬",
        "type": "노란색",
        "nutrient": "리모넨",
        "efficacy": "혈관 강화",
        "calories": 31
    },
    {
        "name": "키위",
        "type": "녹색",
        "nutrient": "이소시아닌",
        "efficacy": "암예방",
        "calories": 50
    },
    {
        "name": "자두",
        "type": "보라색",
        "nutrient": "안토시아닌",
        "efficacy": "기억력 향상",
        "calories": 34
    },
    {
        "name": "블랙베리",
        "type": "보라색",
        "nutrient": "안토시아닌",
        "efficacy": "기억력 향상",
        "calories": 37
    }
]

@app.get("/fruitsearch")
async def filter_fruit_search(
    name: str = Query(None, description="과일 이름"),
    color: str = Query(..., description="과일의 색 ex) 빨간색, 주황색, 보라색 등"),
    nutrient: str = Query(None, description="영양소 ex) 베타카로틴, 리코펜 등"),
    efficacy: str = Query(None, description="효능 ex) 암예방, 혈관 강화 등"),
    min_calories: int = Query(None, ge=0, description="최소 칼로리")
):
    filtered_fruit = []
    for item in fruit_data:
        if name is not None and item["name"] != name:
            continue
        if item["type"] != color:
            continue
        if nutrient is not None and item["nutrient"] != nutrient:
            continue
        if efficacy is not None and item["efficacy"] != efficacy:
            continue
        if min_calories is not None and item["calories"] < min_calories:
            continue
        filtered_fruit.append(item)
    
    return filtered_fruit

@app.get("/NewBookList")
async def filter_new_book_list(
    BookName: str = Query(None, description="책이름"),
    author: str = Query(None, description="작가명"),
    publisher: str = Query(None, description="출판사"),
    field: str = Query(..., description="분야"),
    max_pages: int = Query(None, ge=0, description="최대 쪽수"),
    min_pages: int = Query(None, ge=0, description="최소 쪽수")
):
    # 신간 책 데이터
    books = [
        ["꽁꽁꽁 캠핑","윤정주","책읽는곰","유아 동화",44,9791158364120],
        ["중대재해처벌법","이상국","대명출판사","사회/정치",564,9791198214829],
        ["마루는 강쥐 1","모죠","문페이스","만화",308,9791191841466],
        ["구덩이","루이스 새커","창비","청소년 문학",333,9788936456023],
        ["역사논문 작성법","임경석","푸른역사","역사",216,9791156122494]
    ]

    filtered_books = []

    for book in books:
        if (
            (BookName is None or book[0] == BookName) and
            (author is None or book[1] == author) and
            (publisher is None or book[2] == publisher) and
            (field == book[3]) and
            (max_pages is None or book[4] <= max_pages) and
            (min_pages is None or book[4] >= min_pages)
        ):
            filtered_books.append({
                "BookName": book[0],
                "author": book[1],
                "publisher": book[2],
                "field": book[3],
                "pages": book[4],
                "ISBN": book[5]
            })

    return filtered_books

@app.get("/Butter")
async def filter_butter(
    brand: str = Query(None, description="브랜드"),
    salt: bool = Query(..., description="소금첨가유무"),
    wrapped: bool = Query(None, description="개별포장 유무"),
    max_weight: float = Query(None, ge=0, description="최대 무게"),
    min_weight: float = Query(None, ge=0, description="최소 무게"),
    origin: str = Query(None, description="원산지")
):
    # 버터 데이터
    butters = [
        ["폰테라", False, False, 454, "뉴질랜드"],
        ["발렌타인", False, True, 7, "호주"],
        ["이즈니", False, True, 10, "프랑스"],
        ["루어팍", True, True, 10, "덴마크"],
        ["라꽁비에뜨", True, False, 450, "프랑스"],
        ["오뚜기", True, True, 10, "한국"]
    ]

    filtered_butters = []

    for butter in butters:
        if (
            (brand is None or butter[0] == brand) and
            (salt == butter[1]) and
            (wrapped is None or butter[2] == wrapped) and
            (max_weight is None or butter[3] <= max_weight) and
            (min_weight is None or butter[3] >= min_weight) and
            (origin is None or butter[4] == origin)
        ):
            filtered_butters.append({
                "brand": butter[0],
                "salt": butter[1],
                "wrapped": butter[2],
                "weight": butter[3],
                "origin": butter[4]
            })

    return filtered_butters

@app.get("/RealEstate")
async def filter_real_estate(
    city: str = Query(..., description="광역시도"),
    district: str = Query(None, description="시군구"),
    town: str = Query(None, description="읍면동"),
    ForSale: str = Query(None, description="매물명"),
    type: str = Query(None, description="종류 ex)아파트, 오피스텔, 주택 등"),
    max_price: int = Query(None, description="최대 가격"),
    min_price: int = Query(None, description="최소 가격"),
    max_size: int = Query(None, ge=0, description="최대 평수"),
    min_size: int = Query(None, ge=0, description="최소 평수")
):
    # 부동산 매물 데이터
    real_estates = [
        ["충청북도 음성군 맹동면 본성리 360-25", "음성아이파크", "아파트", 330000000, 33],
        ["서울시 은평구 녹번동 144-28", "은평빌라", "빌라", 225000000, 11],
        ["서울시 은평구 녹번동 81-17", "CS아르체", "오피스텔", 245000000, 20],
        ["경상북도 상주시 가장동 739", "다가구4층", "주택", 580000000, 70],
        ["제주도 제주시 이도2동 1011-3", "영도갤럭시타운", "아파트", 170000000, 10]
    ]

    filtered_real_estates = []

    for real_estate in real_estates:
        if (
            (city == real_estate[0].split()[0]) and
            (district is None or district == real_estate[0].split()[1]) and
            (town is None or town == real_estate[0].split()[2]) and
            (ForSale is None or ForSale == real_estate[1]) and
            (type is None or type == real_estate[2]) and
            (max_price is None or real_estate[3] <= max_price) and
            (min_price is None or real_estate[3] >= min_price) and
            (max_size is None or real_estate[4] <= max_size) and
            (min_size is None or real_estate[4] >= min_size)
        ):
            filtered_real_estates.append({
                "address": real_estate[0],
                "ForSale": real_estate[1],
                "type": real_estate[2],
                "price": real_estate[3],
                "size": real_estate[4]
            })

    return filtered_real_estates

@app.get("/DaisoProducts")
async def filter_daiso_products(
    category: str = Query(..., description="상품 카테고리 ex) 주방, 욕실, 미용 등"),
    product_name: str = Query(None, description="상품명"),
    size: float = Query(None, description="크기"),
    max_price: int = Query(None, ge=0, description="최대 가격"),
    min_price: int = Query(None, ge=0, description="최소 가격"),
    manufacture_country: str = Query(None, description="제조국")
):
    # 다이소 상품 데이터
    daiso_products = [
        ["주방", "무광스텐볼", 20, 3000, "중국", 86759],
        ["욕실", "다회용 샤워캡", 16.5, 2000, "중국", 1022687],
        ["주방", "전자렌지보관용기", 12, 1000, "한국", 1023012],
        ["미용", "모공세안브러시", 7.5, 5000, "중국", 61627],
        ["인테리어", "엔틱도어벨", 30, 3000, "한국", 66354],
        ["수납", "와이드박스", 23.5, 2000, "일본", 949180031]
    ]

    filtered_daiso_products = []

    for daiso_product in daiso_products:
        if (
            (category == daiso_product[0]) and
            (product_name is None or product_name == daiso_product[1]) and
            (size is None or size == daiso_product[2]) and
            (max_price is None or daiso_product[3] <= max_price) and
            (min_price is None or daiso_product[3] >= min_price) and
            (manufacture_country is None or manufacture_country == daiso_product[4])
        ):
            filtered_daiso_products.append({
                "category": daiso_product[0],
                "product_name": daiso_product[1],
                "size": daiso_product[2],
                "price": daiso_product[3],
                "manufacture_country": daiso_product[4],
                "product_num": daiso_product[5]
            })

    return filtered_daiso_products

@app.get("/RainBoots")
async def filter_rain_boots(
    brand: str = Query(..., description="브랜드"),
    heel_height: float = Query(None, description="굽높이"),
    min_price: int = Query(None, ge=0, description="최소 가격"),
    max_price: int = Query(None, ge=0, description="최대 가격"),
    size: int = Query(None, description="사이즈"),
    min_rating: float = Query(None, ge=0, le=5, description="최소 평점")
):
    # 레인부츠 데이터
    rain_boots = [
        ["헌터", 3, 135000, [240, 250, 260], 4.8, ["무게감이 있어서 잘 벗겨지지 않네요.", "예뻐요. 사이즈는 반업하면 좋아요."]],
        ["락피쉬", 3.3, 75000, [230, 235, 240], 4.7, ["발이 아프지 않고 편안하며 디자인도 예쁩니다.", "좋은 가격으로 구매해서 좋아요."]],
        ["바버", 4, 119000, [255], 4.8, ["완전 예뻐용. 사이즈도 널널해요.", "안에도 부드럽고 착화감도 좋습니다."]],
        ["벤시몽", 2, 80000, [230, 240, 250], 4.5, ["가볍고 딱 맞는 느낌이에요", "색상이 튀지 않아서 만족해요."]],
        ["문스타", 3, 99000, [220], 4.8, ["디자인이 너무 귀엽고 착화감 푹신해서 좋아요.", "정사이즈하면 가볍고 좋아요"]]
    ]

    filtered_rain_boots = []

    for rain_boot in rain_boots:
        if (
            (brand == rain_boot[0]) and
            (heel_height is None or heel_height == rain_boot[1]) and
            (min_price is None or rain_boot[2] >= min_price) and
            (max_price is None or rain_boot[2] <= max_price) and
            (size is None or size in rain_boot[3]) and
            (min_rating is None or rain_boot[4] >= min_rating)
        ):
            filtered_rain_boots.append({
                "brand": rain_boot[0],
                "heel_height": rain_boot[1],
                "price": rain_boot[2],
                "size": rain_boot[3],
                "rating": rain_boot[4],
                "review": rain_boot[5]
            })

    return filtered_rain_boots

@app.get("/influencer")
async def filter_influencer(
    name: str = Query(None, description="인플루언서 활동명"),
    id: str = Query(None, description="인플루언서의 SNS 아이디"),
    followers: str = Query(None, description="SNS 팔로워 수 ex) 10.8만, 21만 등"),
    min_posts: int = Query(None, ge=0, description="최소 SNS 게시물 수"),
    field: str = Query(..., description="분야 ex) 패션, 뷰티. 여행 등"),
    platform: str = Query(None, description="활동플랫폼 ex) 유튜브, 인스타그램")
):
    # SNS 인플루언서 데이터
    influencers = [
        ["썸머썸머", "summerinbk", "7.9만", 1854, "뷰티", ["유튜브", "인스타그램"]],
        ["그래쓰", "kim.asha.1", "10.1만", 1059, "여행", ["유튜브", "인스타그램"]],
        ["김장미", "syllyworld", "19.6만", 2289, "패션", ["인스타그램"]],
        ["최이현", "yvesox", "22.6만", 190, "패션", ["인스타그램"]],
        ["노니유", "younonii", "21.5만", 1231, "패션", ["인스타그램"]]
    ]

    filtered_influencers = []

    for influencer in influencers:
        if (
            (name is None or influencer[0] == name) and
            (id is None or influencer[1] == id) and
            (followers is None or influencer[2] == followers) and
            (min_posts is None or influencer[3] >= min_posts) and
            (field == influencer[4]) and
            (platform is None or platform in influencer[5])
        ):
            filtered_influencers.append({
                "name": influencer[0],
                "id": influencer[1],
                "followers": influencer[2],
                "num": influencer[3],
                "field": influencer[4],
                "platform": influencer[5]
            })

    return filtered_influencers

@app.get("/DermReservation")
async def filter_derm_reservation(
    name: str = Query(None, description="예약자 이름"),
    reservation_date: str = Query(..., description="예약일자 ex) 2023.07.13"),
    reservation_time: str = Query(None, description="예약시간"),
    back_number: int = Query(None, description="예약자의 휴대폰 뒷번호"),
    surgical_name: str = Query(None, description="시술명"),
    number: int = Query(None, description="진행되는 시술 회차"),
    first_visit: bool = Query(None, description="초진여부")
):
    # 피부과 예약자 데이터
    derm_reservations = [
        ["김민희", "2023.06.28", "10시 30분", "010-0000-0000", "보톡스", 1, False],
        ["이민영", "2023.05.15", "18시", "010-1111-1111", "레이저토닝", 2, False],
        ["최나현", "2023.08.09", "11시", "010-2222-2222", "쥬베룩", 3, True],
        ["장민우", "2023.07.08", "14시 30분", "010-3333-3333", "레이저제모", 10, True],
        ["강선하", "2023.06.03", "15시", "010-4444-4444", "보톡스", 3, False]
    ]

    filtered_derm_reservations = []

    for reservation in derm_reservations:
        if (
            (name is None or reservation[0] == name) and
            (reservation_date == reservation[1]) and
            (reservation_time is None or reservation[2] == reservation_time) and
            (back_number is None or back_number == int(reservation[3][-4:])) and
            (surgical_name is None or reservation[4] == surgical_name) and
            (number is None or reservation[5] == number) and
            (first_visit is None or reservation[6] == first_visit)
        ):
            filtered_derm_reservations.append({
                "name": reservation[0],
                "reservation_date": reservation[1],
                "reservation_time": reservation[2],
                "phone_num": reservation[3],
                "surgical_name": reservation[4],
                "number": reservation[5],
                "first_visit": reservation[6]
            })

    return filtered_derm_reservations

@app.get("/UniversityStudents")
async def filter_university_students(
    name: str = Query(None, description="학생 이름"),
    student_id: int = Query(None, description="학번"),
    division: str = Query(None, description="학부 ex) 공과대학, 경영대학 등"),
    department: str = Query(..., description="학과 ex) 건축학과, 중국어학과 등"),
    admission_year: int = Query(None, description="입학연도 ex) 2017, 2019"),
    student_dues: bool = Query(None, description="학생회비 납부여부")
):
    # 대학교 학생 데이터
    university_students = [
        ["이민우", 12181563, "공과대학", "건축학과", 2018, True, "010-0000-0000"],
        ["최나라", 13191214, "경영대학", "국제통상학과", 2019, False, "010-1111-1111"],
        ["이민지", 12171025, "법학대학", "법학과", 2017, False, "010-2222-2222"],
        ["신기철", 22147988, "문과대학", "중국어학과", 2022, True, "010-3333-3333"],
        ["김민기", 23210439, "공과대학", "화학공학과", 2023, True, "010-4444-4444"]
    ]

    filtered_university_students = []

    for student in university_students:
        if (
            (name is None or student[0] == name) and
            (student_id is None or student[1] == student_id) and
            (division is None or student[2] == division) and
            (student[3] == department) and
            (admission_year is None or student[4] == admission_year) and
            (student_dues is None or student[5] == student_dues)
        ):
            filtered_university_students.append({
                "name": student[0],
                "Student_ID": student[1],
                "division": student[2],
                "department": student[3],
                "admission_year": student[4],
                "student_dues": student[5],
                "phone_number": student[6]
            })

    return filtered_university_students

@app.get("/PaidSubscribers")
async def filter_paid_subscribers(
    channel_name: str = Query(..., description="채널명"),
    subscriber_name: str = Query(None, description="구독자명"),
    subscription_date: str = Query(None, description="채널을 처음 구독한 일자 ex) 2021.07.08"),
    paid_subscription_date: str = Query(None, description="유료가입일자"),
    paid_num: int = Query(None, description="유료가입 회차")
):
    # 유튜브 유료 구독자 데이터
    paid_subscribers = [
        ["이티잡스", "김호식", "wlksdk23", "2021.07.08", "2021.08.15", 19],
        ["썸썸머", "이나라", "tttcbg347", "2022.03.28", "2023.04.01", 5],
        ["솔리웍스", "박나래", "pqmajdh", "2022.07.11", "2022.07.28", 8],
        ["스마티튜브", "김환", "rlaghks12457", "2017.04.23", "2021.03.31", 25],
        ["바바채널", "강은숙", "slkho63", "2018.02.04", "2019.07.12", 37]
    ]

    filtered_paid_subscribers = []

    for subscriber in paid_subscribers:
        if (
            subscriber[0] == channel_name and
            (subscriber[1] == subscriber_name if subscriber_name else True) and
            (subscriber[3] == subscription_date if subscription_date else True) and
            (subscriber[4] == paid_subscription_date if paid_subscription_date else True) and
            (subscriber[5] == paid_num if paid_num else True)
        ):
            filtered_paid_subscribers.append({
                "channel_name": subscriber[0],
                "subscriber_name": subscriber[1],
                "subscriber_id": subscriber[2],
                "subscription_date": subscriber[3],
                "paid_subscription_date": subscriber[4],
                "paid_Num": subscriber[5]
            })

    return filtered_paid_subscribers

@app.get("/SalonReservation")
async def filter_salon_reservation(
    name: str = Query(None, description="예약자명"),
    reservation_date: str = Query(..., description="예약일자 데이터형식 00월 00일"),
    reservation_time: str = Query(None, description="예약시간 데이터형식 00시 00분"),
    type: str = Query(None, description="헤어시술종류 ex) 커트, 펌, 염색 등"),
    back_num: int = Query(None, description="휴대폰 뒷번호")
):
    # 미용실 예약자 데이터
    salonreservations = [
        ["김나라", "08월 14일", "14시 30분", "커트", "010-5555-5555"],
        ["김국진", "07월 12일", "10시", "펌", "010-6666-6666"],
        ["이나영", "07월 14일", "16시", "염색", "010-7777-7777"],
        ["김미진", "07월 14일", "18시 30분", "펌", "010-8888-8888"],
        ["최진영", "07월 26일", "12시", "커트", "010-9999-9999"]
    ]

    filtered_salonreservations = []

    for reservation in salonreservations:
        if (
            (reservation[0] == name if name else True) and
            (reservation[1] == reservation_date) and
            (reservation[2] == reservation_time if reservation_time else True) and
            (reservation[3] == type if type else True) and
            (reservation[4] == back_num if back_num else True)
        ):
            filtered_salonreservations.append({
                "Name": reservation[0],
                "Reservation_date": reservation[1],
                "Reservation_time": reservation[2],
                "type": reservation[3],
                "phone_num": reservation[4]
            })

    return filtered_salonreservations

@app.get("/InteriorCompany")
async def filter_interior_company(
    name: str = Query(None, description="업체명"),
    city: str = Query(None, description="광역시도"),
    district: str = Query(None, description="시군구"),
    town: str = Query(None, description="읍면동"),
    expertise_field: str = Query(..., description="전문분야 ex) 미장, 타일, 방수공사, 도배 등")
):
    # 인테리어 업체 데이터
    interior_companies = [
        ["서초인테리어", "서울시", "서초구", "서초동", ["미장", "타일", "방수공사"], "02-594-7046"],
        ["홈테이인테리어", "서울시", "강남구", "역삼동", ["도배"], "0507-1336-9874"],
        ["백억인테리어", "경기도", "오산시", "원동", ["유리", "창호공사"], "0507-1333-6537"],
        ["가온인테리어", "전라북도", "전주시", "덕진동", ["미장", "타일", "방수공사"], "0507-1473-4433"],
        ["김씨인테리어", "경상북도", "김천시", "성내동", ["도배"], "054-435-0078"]
    ]

    filtered_interior_companies = []

    for company in interior_companies:
        if (
            (company[0] == name if name else True) and
            (company[1] == city if city else True) and
            (company[2] == district if district else True) and
            (company[3] == town if town else True) and
            (expertise_field in company[4])
        ):
            filtered_interior_companies.append({
                "name": company[0],
                "city": company[1],
                "district": company[2],
                "town": company[3],
                "expertise_field": company[4],
                "telephone_num": company[5]
            })

    return filtered_interior_companies

@app.get("/ReunionParticipant")
async def filter_reunion_participant(
    school_name: str = Query(..., description="졸업한 학교명"),
    name: str = Query(None, description="참여자 이름"),
    gender: str = Query(None, description="성별"),
    phone_num: str = Query(None, description="전화번호"),
    career: str = Query(None, description="직업이나 직급 ex) 부장, 은행지점장, 아나운서")
):
    # 동창회 참여자 데이터
    reunion_participants = [
        ["일신여자상업고등학교", "이미자", "여성", "010-0000-0000", "은행지점장", "농협"],
        ["일신여자상업고등학교", "김숙자", "여성", "010-1111-0000", "부장", "신한은행"],
        ["경북항공고등학교", "최석현", "남성", "010-2222-0000", "기장", "대한항공"],
        ["부평공업고등학교", "김상훈", "남성", "010-3333-0000", "과장", "삼성전자"],
        ["서울정화고등학교", "이나희", "여성", "010-4444-0000", "아나운서", "JTBC"]
    ]

    filtered_reunion_participants = []

    for participant in reunion_participants:
        if (
            (participant[0] == school_name) and
            (participant[1] == name if name else True) and
            (participant[2] == gender if gender else True) and
            (participant[3] == phone_num if phone_num else True) and
            (participant[4] == career if career else True)
        ):
            filtered_reunion_participants.append({
                "school_name": participant[0],
                "name": participant[1],
                "gender": participant[2],
                "phone_num": participant[3],
                "career": participant[4],
                "company": participant[5]
            })

    return filtered_reunion_participants

@app.get("/WalletSearch")
async def filter_wallet_search(
    brand: str = Query(None, description="브랜드"),
    type: str = Query(None, description="종류 ex) 반지갑, 장지갑, 카드지갑"),
    material: str = Query(None, description="소재 ex) 천연가죽, 인조가죽"),
    color: str = Query(None, description="색상 ex) Black, Camel, Green 등"),
    max_price: int = Query(None, description="최대 가격", ge=0),
    min_price: int = Query(None, description="최소 가격", ge=0)
):
    # 지갑 데이터
    wallets = [
        ["마땡킴", "반지갑", "천연가죽", "Green", 88000],
        ["생로랑", "카드지갑", "천연가죽", "Black", 190000],
        ["알파치노", "장지갑", "인조가죽", "Black", 99000],
        ["할리케이", "카드지갑", "인조가죽", "Camel", 59000],
        ["디랩", "반지갑", "천연가죽", "Gray", 25000]
    ]

    filtered_wallets = []

    for wallet in wallets:
        if (
            (wallet[0] == brand if brand else True) and
            (wallet[1] == type if type else True) and
            (wallet[2] == material if material else True) and
            (wallet[3] == color if color else True) and
            (max_price is None or wallet[4] <= max_price) and
            (min_price is None or wallet[4] >= min_price)
        ):
            filtered_wallets.append({
                "brand": wallet[0],
                "type": wallet[1],
                "material": wallet[2],
                "color": wallet[3],
                "price": wallet[4]
            })

    return filtered_wallets

@app.get("/market_store")
async def filter_market_store(
    category: str = Query(..., description="카테고리 ex) 폐백, 먹거리, 직물 등"),
    store_name: str = Query(None, description="상호명"),
    city: str = Query(None, description="광역시도"),
    district: str = Query(None, description="시군구"),
    town: str = Query(None, description="읍면동"),
    telephone_num: str = Query(None, description="연락처"),
    product: str = Query(None, description="판매상품 ex) 폐백음식, 명란젓, 맞춤정장 등")
):
    # 시장 점포 데이터
    market_stores = [
        ["폐백", "다만폐백", "서울특별시 종로구 예지동 6-1 광장시장 98호", "02-2279-4131", ["폐백음식", "이바지음식", "답례떡"]],
        ["먹거리", "순희네반찬", "서울특별시 종로구 예지동 6-1 광장시장내 65-1", "02-2279-1855", ["명란젓", "간장게장", "가자미식해", "더덕무침"]],
        ["직물", "진흥직물", "서울특별시 종로구 예지동 6-1 광장시장 147호", "0507-1475-9679", ["린넨까사", "린넨델가도", "린넨아미고"]],
        ["먹거리", "오지개분식", "서울특별시 마포구 망원동 414-108 망원시장 B구역", "02-333-3639", ["떡볶이", "각종 튀김", "김밥", "순대", "어묵"]],
        ["직물", "영성직물", "서울특별시 종로구 예지동 6-1 광장시장 1층 207호", "02-2267-3406", ["맞춤정장", "양복원단"]]
    ]

    filtered_stores = []

    for store in market_stores:
        if (
            store[0] == category and
            (store[1] == store_name if store_name else True) and
            (city in store[2] if city else True) and
            (district in store[2]  if district else True) and
            (town in store[2]  if town else True) and
            (store[3] == telephone_num if telephone_num else True) and
            (product in store[4] if product else True)
        ):
            filtered_stores.append({
                "category": store[0],
                "store_name": store[1],
                "detailed_address": store[2],
                "telephone_num": store[3],
                "product": store[4]
            })

    return filtered_stores

@app.get("/lego_goods")
async def filter_lego_goods(
    product_name: str = Query(None, description="상품명"),
    use_age: str = Query(..., description="사용연령 ex) 18세 이상, 8세 이상 등"),
    max_price: int = Query(None, ge=0, description="최대 가격"),
    min_price: int = Query(None, ge=0, description="최소 가격"),
    max_parts: int = Query(None, ge=0, description="최대 부품수"),
    min_parts: int = Query(None, ge=0, description="최소 부품수"),
    field: str = Query(None, description="분야 ex) 빌딩, 자동차, 동물 등")
):
    # 레고 상품 데이터
    lego_goods = [
        ["부티크 호텔", 10297, "18세 이상", 299900, 3066, "빌딩"],
        ["2022 포드 GT", 42154, "18세 이상", 159900, 1466, "자동차"],
        ["행운의 고양이", 40436, "10세 이상", 13500, 134, "동물"],
        ["아늑한 집", 31139, "8세 이상", 89900, 808, "빌딩"],
        ["경찰차", 60312, "5세 이상", 12900, 94, "자동차"]
    ]

    filtered_goods = []

    for goods in lego_goods:
        if (
            (goods[0] == product_name if product_name else True) and
            goods[2] == use_age and
            (goods[3] <= max_price if max_price else True) and
            (goods[3] >= min_price if min_price else True) and
            (goods[4] <= max_parts if max_parts else True) and
            (goods[4] >= min_parts if min_parts else True) and
            (goods[5] == field if field else True)
        ):
            filtered_goods.append({
                "product_name": goods[0],
                "product_num": goods[1],
                "use_age": goods[2],
                "price": goods[3],
                "Parts_num": goods[4],
                "field": goods[5]
            })

    return filtered_goods

@app.get("/used_goods")
async def filter_used_goods(
    category: str = Query(None, description="카테고리 ex) 여성잡화, 가공식품, 생활가전"),
    product_name: str = Query(None, description="상품명"),
    city: str = Query(..., description="광역시도"),
    district: str = Query(..., description="시군구"),
    town: str = Query(None, description="읍면동"),
    delivery_available: bool = Query(None, description="배송가능여부"),
    purchase_available: bool = Query(None, description="구매가능여부"),
    max_price: int = Query(None, ge=0, description="최대 가격")
):
    # 중고 물품 데이터
    used_goods = [
        ["여성잡화", "헬렌카민스키 마리나", "대전광역시 서구 도안동", True, True, 80000, "마리나 제품입니다. 구성품은 사진에 있는 것이 전부에요. 작년에 구매한 제품 입니다."],
        ["생활가전", "전자레인지", "서울시 강북구 수유3동", False, True, 15000, "2004년식이고 작동은 잘 돼요 사이즈는 가로 54 세로 31 깊이 37"],
        ["가공식품", "스팸선물세트 6호", "인천광역시 부평구 부평1동", False, False, 18000, "스팸 선물세트 6호 저렴하게 팔아요. 빠르게 연락주세요. 위치는 부평역 바로 앞 입니다."],
        ["생활가전", "위닉스제습기", "경기도 의정부시 산곡동", False, True, 60000, "요즘같은때 딱 필요한 위닉스제습기 DHC-167IPW. 조인성배우분이 광고했던 인기제품이죠."],
        ["여성잡화", "토리버치 크로스백", "경기도 수지구 성복동", True, True, 20000, "2번 들은 새상품급 깨끗한 상태입니다~ 미니 사이즈 크로스백 입니다. 사이즈 11x18"]
    ]

    filtered_goods = []

    for goods in used_goods:
        if (
            (goods[0] == category if category else True) and
            (goods[1] == product_name if product_name else True) and
            (city in goods[2] if city else True) and
            (district in goods[2]  if district else True) and
            (town in goods[2]  if town else True) and
            (goods[3] == delivery_available if delivery_available is not None else True) and
            (goods[4] == purchase_available if purchase_available is not None else True) and
            (goods[5] <= max_price if max_price else True)
        ):
            filtered_goods.append({
                "category": goods[0],
                "product_name": goods[1],
                "location": goods[2],
                "delivery_available": goods[3],
                "purchase_available": goods[4],
                "price": goods[5],
                "description": goods[6]
            })

    return filtered_goods

@app.get("/carrier_subscribers")
async def filter_carrier_subscribers(
    carrier: str = Query(..., description="통신사 ex) LG, SK, KT"),
    subscribers_name: str = Query(None, description="고객명"),
    subscription_date: str = Query(None, description="가입일 ex) 2019.02.11"),
    phone_plan: str = Query(None, description="요금제 ex) 5G 시그니처, 다이렉트 LTE 22"),
    amount: int = Query(None, description="청구금액"),
    payment_status: bool = Query(None, description="요금 납부여부")
):
    # 대학교 학생 데이터
    carrier_subscribers = [
        ["LG", "유민기", "2021.04.02", "5G 시그니처", 88000, True, "2023.07.08"],
        ["SK", "박미나", "2011.06.12", "T플랜 맥스", 69000, True, "2023.06.29"],
        ["LG", "지정화", "2019.02.11", "LTE 프리미어 에센셜", 72000, False, "없음"],
        ["KT", "김정식", "2012.05.23", "데이터ON", 43000, False, "없음"],
        ["SK", "이은숙", "2022.08.04", "다이렉트 LTE 22", 22000, True, "2023.07.12"]
    ]

    filtered_subscribers = []

    for subscriber in carrier_subscribers:
        if (
            subscriber[0] == carrier and
            (subscriber[1] == subscribers_name if subscribers_name else True) and
            (subscriber[2] == subscription_date if subscription_date else True) and
            (subscriber[3] == phone_plan if phone_plan else True) and
            (subscriber[4] == amount if amount else True) and
            (subscriber[5] == payment_status if payment_status is not None else True)
        ):
            filtered_subscribers.append({
                "carrier": subscriber[0],
                "subscribers_name": subscriber[1],
                "subscription_date": subscriber[2],
                "phone_plan": subscriber[3],
                "amount": subscriber[4],
                "Payment_status": subscriber[5],
                "payment_date": subscriber[6]
            })

    return filtered_subscribers

@app.get("/maternity_clinic")
async def filter_maternity_clinic(
    name: str = Query(None, description="병원명"),
    city: str = Query(None, description="광역시도"),
    district: str = Query(None, description="시군구"),
    town: str = Query(None, description="읍면동"),
    woman_doctor: bool = Query(..., description="여의사진료 유무"),
    min_doctor: int = Query(None, description="최소 전문의 수"),
    specialized_cure: str = Query(None, description="전문진료명 ex) 여성성형, 여성검진, 복강경수술 등")
):
    # 산부인과 데이터
    maternity_clinic = [
        ["다움산부인과의원", "서울 강남구 역삼동 825-9", True, 2, ["여성성형", "여성검진", "외음부케어"]],
        ["미래여성병원", "부산 부산진구 개금동 204-6", True, 10, ["여성성형", "여성검진"]],
        ["아산더편한산부인과의원", "경기 남양주시 호평동 641", True, 1, ["여성검진", "산모검진"]],
        ["이길완산부인과의원", "서울 은평구 대조동 6-5", False, 1, ["여성검진", "산모검진"]],
        ["아이제일산부인과의원", "서울 은평구 역촌동 15-7", True, 4, ["복강경수술", "요실금", "여성성형", "에스테틱"]]
    ]

    filtered_clinics = []

    for clinic in maternity_clinic:
        if (
            (clinic[0] == name if name else True) and
            (city in clinic[1]  if city else True) and
            (district in clinic[1]  if district else True) and
            (town in clinic[1]   if town else True) and
            clinic[2] == woman_doctor and
            (clinic[3] >= min_doctor if min_doctor else True) and
            (specialized_cure in clinic[4]  if specialized_cure else True)
        ):
            filtered_clinics.append({
                "name": clinic[0],
                "address": clinic[1],
                "woman_doctor": clinic[2],
                "doctor_num": clinic[3],
                "specialized_cure": clinic[4]
            })

    return filtered_clinics

@app.get("/ophthalmic_clinic")
async def filter_ophthalmic_clinic(
    name: str = Query(None, description="병원명"),
    city: str = Query(None, description="광역시도"),
    district: str = Query(None, description="시군구"),
    town: str = Query(None, description="읍면동"),
    min_doctor: int = Query(None, description="최소 전문의 수"),
    specialized_cure: str = Query(..., description="전문진료명 ex) 여성성형, 여성검진, 복강경수술 등")
):
    # 안과 데이터
    ophthalmic_clinic = [
        ["밝은눈안과의원", "서울시 서초구 서초동 1303-22", 8, ["백내장", "스마일라식", "라섹", "노안"], "1544-3994", "https://brighteyesclinic.com"],
        ["손안과의원", "서울시 동대문구 전농동 32-4", 1, ["드림렌즈", "시력교정", "백내장", "녹내장"], "02-2244-7300", "없음"],
        ["제일안과의원", "경기도 고양시 일산동구 장항동 895", 2, ["시력교정", "백내장", "드림렌즈", "노안"], "031-905-3357", "https://www.instagram.com/jeil_eye"],
        ["새봄안과의원", "대전광역시 유성구 봉명동 1016-3", 3, ["백내장", "라식", "노안", "녹내장", "황반변성"], "042-826-2475", "http://www.sbeye.co.kr"],
        ["푸른안과의원", "전라북도 전주시 덕진구 금암동 1588-6", 7, ["스마일라식", "라섹", "라식", "백내장"], "0507-1479-2124", "http://www.seenew.co.kr/"]
    ]

    filtered_clinics = []

    for clinic in ophthalmic_clinic:
        if (
            (clinic[0] == name if name else True) and
            (city in clinic[1]  if city else True) and
            (district in clinic[1]  if district else True) and
            (town in clinic[1]  if town else True) and
            (clinic[2] >= min_doctor if min_doctor else True) and
            specialized_cure in clinic[3] 
        ):
            filtered_clinics.append({
                "name": clinic[0],
                "address": clinic[1],
                "doctor_num": clinic[2],
                "specialized_cure": clinic[3],
                "telephone_num": clinic[4],
                "website_address": clinic[5]
            })

    return filtered_clinics

@app.get("/paid_app")
async def filter_paid_app(
    app_name: str = Query(None, description="어플명"),
    type: str = Query(..., description="종류 ex) 카메라, 가계부 등"),
    max_price: int = Query(None, description="최대 가격"),
    min_price: int = Query(None, description="최소 가격"),
    min_rating: float = Query(None, ge=0, le=5, description="최소 평점")
):
    # 유료 어플 데이터
    paid_apps = [
        ["화민필터", "카메라", 4400, 4.8, ["4400원이 안아까움", "필터들이 하나하나 다 예쁘고 이펙트 효과가 대박이라 소름 돋았어요."]],
        ["위플 가계부 Pro", "가계부", 7700, 4.8, ["이만큼 깔끔하고 사용하기 쉽게 만들어진 어플은 없는 것 같아요.", "26살 때부터 써서 35살인 지금도 잘 사용 중입니다."]],
        ["유니콘", "광고차단", 3300, 4.7, ["돈주고 앱사는건 인생처음입니다. 광고가 없어져서 너무 행복합니다", "광고를 확실하게 차단해줍니다! 추천!"]],
        ["Analog Tokyo", "카메라", 1100, 2.8, ["다 좋은데 앱이 계속 꺼져요", "업데이트 좀 해주세요."]],
        ["클머니가계부", "가계부", 5500, 3.2, ["동기화가 안됩나다. PC와 연동이 수일간 안되네요.", "진짜 너무 좋은데 업데이트가 안돼서 너무 아쉽습니다. 이만한 가계부 없는데...ㅠㅠ"]]
    ]

    filtered_apps = []

    for app in paid_apps:
        if (
            (app[0] == app_name if app_name else True) and
            app[1] == type and
            (app[2] <= max_price if max_price else True) and
            (app[2] >= min_price if min_price else True) and
            (app[3] >= min_rating if min_rating else True)
        ):
            filtered_apps.append({
                "app_name": app[0],
                "type": app[1],
                "price": app[2],
                "rating": app[3],
                "review": app[4]
            })

    return filtered_apps




#### 0718 Update ####

teachers = [
    ["김채윤", "하타요가", "010-7476-7552", "월요일", "19:00", 4],
    ["김민수", "힐링요가", "010-8636-7554", "화요일", "15:00", 2],
    ["박윤수", "하타요가", "010-5846-0045", "수요일", "16:00", 5],
    ["이송희", "반야사요가", "010-5124-7845", "목요일", "15:30", 7],
    ["김지은", "힐링요가", "010-7524-6588", "금요일", "12:20", 1]
]

@app.get("/yoga_teacher")
def filter_yoga_teacher(
    name: str = Query(None, description="강사의 이름"),
    class_name: str = Query(None, description="수업 이름", alias="class"),
    phone_num: str = Query(None, description="전화번호", alias="phoneNum"),
    day: str = Query(None, description="요일"),
    time: str = Query(None, description="시간"),
    career: int = Query(None, description="경력(년)")
):
    filtered_teachers = teachers

    if name:
        filtered_teachers = [teacher for teacher in filtered_teachers if teacher[0] == name]
    if class_name:
        filtered_teachers = [teacher for teacher in filtered_teachers if teacher[1] == class_name]
    if phone_num:
        filtered_teachers = [teacher for teacher in filtered_teachers if teacher[2] == phone_num]
    if day:
        filtered_teachers = [teacher for teacher in filtered_teachers if teacher[3] == day]
    if time:
        filtered_teachers = [teacher for teacher in filtered_teachers if teacher[4] == time]
    if career:
        filtered_teachers = [teacher for teacher in filtered_teachers if teacher[5] == career]

    return filtered_teachers

bikes = [
    ["310", "청계광장 옆", "서울 중구 태평로1가", 16, 4],
    ["4718", "광화문역 6번출구 옆 A ", "서울 종로구 세종로", 11, 8],
    ["318", "광교사거리 남측 ", "서울 중구 다동", 8, 14],
    ["368", "SK 서린빌딩 앞", "서울 종로구 서린동", 12, 9],
    ["316", "종각역 1번출구 앞", "서울 종로구 종로1가", 5, 4]
]

@app.get("/public_bike")
def filter_public_bike(
    spot_num: str = Query(None, description="대여장소 번호", alias="spotNum"),
    spot_name: str = Query(None, description="대여장소 이름", alias="spotName"),
    min_normal_bike: int = Query(None, description="최소 일반 자전거 대수", alias="min_normalBike"),
    min_small_bike: int = Query(None, description="최소 소형 자전거 대수", alias="min_smallBike"),
    keyword: str = Query(None, description="대여장소 주소를 검색하는 키워드")
):
    filtered_bikes = bikes

    if spot_num:
        filtered_bikes = [bike for bike in filtered_bikes if bike[0] == spot_num]
    if spot_name:
        filtered_bikes = [bike for bike in filtered_bikes if bike[1] == spot_name]
    if min_normal_bike:
        filtered_bikes = [bike for bike in filtered_bikes if bike[3] >= min_normal_bike]
    if min_small_bike:
        filtered_bikes = [bike for bike in filtered_bikes if bike[4] >= min_small_bike]
    if keyword:
        filtered_bikes = [bike for bike in filtered_bikes if keyword in bike[2]]

    return filtered_bikes


properties = [
    ["ab00001", "호반베르디움 아파트", 92, 11, 2, 1, "매매", 1.2],
    ["ab00002", "롯데캐슬 아파트", 34, 10, 3, 2, "매매", 1],
    ["ab00003", "우영 포레스티아 아파트", 55, 3, 2, 1, "전세", 0.5],
    ["ab00004", "롯데캐슬 아파트", 64, 2, 2, 1, "전세", 3],
    ["ab00005", "호반베르디움 아파트", 85, 7, 4, 2, "전세", 2]
]

@app.get("/property")
def filter_property(
    property_num: str = Query(None, description="매물 번호", alias="propertyNum"),
    property_name: str = Query(None, description="매물 이름", alias="propertyName"),
    min_square_meter: float = Query(None, description="최소 제곱미터", alias="min_squareMeter"),
    min_story: int = Query(None, description="최소 층수", alias="min_story"),
    min_room: int = Query(None, description="최소 방 갯수", alias="min_room"),
    min_toilet: int = Query(None, description="최소 화장실 갯수", alias="min_toilet"),
    buy_rent: str = Query(None, description="매매/전세 구분", alias="buyRent"),
    max_price: int = Query(None, description="최대 가격", alias="max_price")
):
    filtered_properties = properties

    if property_num:
        filtered_properties = [property for property in filtered_properties if property[0] == property_num]
    if property_name:
        filtered_properties = [property for property in filtered_properties if property[1] == property_name]
    if min_square_meter:
        filtered_properties = [property for property in filtered_properties if property[2] >= min_square_meter]
    if min_story:
        filtered_properties = [property for property in filtered_properties if property[3] >= min_story]
    if min_room:
        filtered_properties = [property for property in filtered_properties if property[4] >= min_room]
    if min_toilet:
        filtered_properties = [property for property in filtered_properties if property[5] >= min_toilet]
    if buy_rent:
        filtered_properties = [property for property in filtered_properties if property[6] == buy_rent]
    if max_price:
        filtered_properties = [property for property in filtered_properties if property[7] <= max_price]

    return filtered_properties

screen_golfs = [
    ["오투리조트 골프", "강원도 태백시 황지동", "10:00", "033-580-7000", True, 100000],
    ["휘닉스파크 골프", "강원도 평창군 봉평면 면온리", "09:00", "033-581-8850", True, 80000],
    ["샌드파인 골프", "강원도 춘천시 신동면 친전동길", "09:30", "033-260-0002", False, 110000],
    ["라비에벨 골프", "강원도 춘천시 동산면 조양리", "06:00", "033-766-1000", True, 70000],
    ["성문안 골프", "강원도 원주시 지정면 월송리", "07:00", "033-670-770", False, 120000]
]

@app.get("/screen_golf")
def filter_screen_golf(
    name: str = Query(None, description="골프장 이름"),
    address: str = Query(None, description="주소"),
    phone: str = Query(None, description="전화번호"),
    motion_plate: bool = Query(None, description="모션플레이트 유무"),
    min_price: int = Query(None, description="최소 가격"),
    max_price: int = Query(None, description="최대 가격")
):
    filtered_golfs = screen_golfs

    if name:
        filtered_golfs = [golf for golf in filtered_golfs if golf[0] == name]
    if address:
        filtered_golfs = [golf for golf in filtered_golfs if golf[1] == address]
    if phone:
        filtered_golfs = [golf for golf in filtered_golfs if golf[3] == phone]
    if motion_plate is not None:
        filtered_golfs = [golf for golf in filtered_golfs if golf[4] == motion_plate]
    if min_price:
        filtered_golfs = [golf for golf in filtered_golfs if golf[5] >= min_price]
    if max_price:
        filtered_golfs = [golf for golf in filtered_golfs if golf[5] <= max_price]

    return filtered_golfs

earphones = [
    ["엠지텍", "유선", "커널형", "블랙", 130000],
    ["엠지텍", "무선", "골전도형", "화이트", 108000],
    ["애플", "무선", "커널형", "퍼플", 160000],
    ["삼성전자", "무선", "커널형", "실버", 200000],
    ["QCY", "유선", "스피커형", "핑크", 60000]
]

@app.get("/earphones")
def filter_earphones(
    manufacture: str = Query(None, description="제조사"),
    wireless_or_not: str = Query(None, description="유선/무선", alias="wirelessOrNot"),
    earphone_type: str = Query(None, description="형태", alias="type"),
    color: str = Query(None, description="컬러"),
    min_price: int = Query(None, description="최소 가격"),
    max_price: int = Query(None, description="최대 가격")
):
    filtered_earphones = earphones

    if manufacture:
        filtered_earphones = [earphone for earphone in filtered_earphones if earphone[0] == manufacture]
    if wireless_or_not:
        filtered_earphones = [earphone for earphone in filtered_earphones if earphone[1] == wireless_or_not]
    if earphone_type:
        filtered_earphones = [earphone for earphone in filtered_earphones if earphone[2] == earphone_type]
    if color:
        filtered_earphones = [earphone for earphone in filtered_earphones if earphone[3] == color]
    if min_price:
        filtered_earphones = [earphone for earphone in filtered_earphones if earphone[4] >= min_price]
    if max_price:
        filtered_earphones = [earphone for earphone in filtered_earphones if earphone[4] <= max_price]

    return filtered_earphones

senior_centers = [
    ["김형원", "1945.01.12", "101동", "103호", True, "010-5554-0001"],
    ["박지수", "1940.05.04", "102동", "1011호", True, "010-1145-0002"],
    ["이준기", "1932.04.01", "103동", "204호", True, "010-5552-0088"],
    ["박민교", "1942.03.02", "104동", "1021호", False, "010-0021-0003"],
    ["은소정", "1938.11.24", "117동", "503호", False, "010-0654-8523"]
]

@app.get("/senior_center")
def filter_senior_center(
    name: str = Query(None, description="이름"),
    min_birthday: str = Query(None, description="최소 생일"),
    max_birthday: str = Query(None, description="최대 생일"),
    dong: str = Query(None, description="동"),
    ho: str = Query(None, description="호"),
    garden: bool = Query(None, description="텃밭 참여 여부", alias="garden"),
    phone: str = Query(None, description="전화번호")
):
    filtered_senior_centers = senior_centers

    if name:
        filtered_senior_centers = [center for center in filtered_senior_centers if center[0] == name]
    if min_birthday:
        filtered_senior_centers = [center for center in filtered_senior_centers if center[1] >= min_birthday]
    if max_birthday:
        filtered_senior_centers = [center for center in filtered_senior_centers if center[1] <= max_birthday]
    if dong:
        filtered_senior_centers = [center for center in filtered_senior_centers if center[2] == dong]
    if ho:
        filtered_senior_centers = [center for center in filtered_senior_centers if center[3] == ho]
    if garden is not None:
        filtered_senior_centers = [center for center in filtered_senior_centers if center[4] == garden]
    if phone:
        filtered_senior_centers = [center for center in filtered_senior_centers if center[5] == phone]

    return filtered_senior_centers

senior_care = [
    ["김복자", "이계순", "010-5447-7745", "리순자", "1947.01.11", ["치매", "허리통증"], "점심 안드심"],
    ["이말순", "김수황", "010-2235-4578", "박춘자", "1941.12.24", ["관절염", "치통"], "저녁약 복용"],
    ["박꽃순", "김예지", "010-2245-7412", "박춘자", "1939.08.20", ["골다공증"], "소변줄 착용"],
    ["진말자", "박수찬", "010-7789-1235", "박진구", "1933.05.18", ["수면장애", "당뇨", "고혈압"], "오후진료 예정"],
    ["백춘희", "백만임", "010-5556-8787", "박진구", "1936.08.16", ["관상동맥질환", "부동맥"], "바이탈 체크"]
]

@app.get("/senior_care")
def filter_senior_care(
    name: str = Query(None, description="이름"),
    guardian: str = Query(None, description="주보호자 이름"),
    phone: str = Query(None, description="전화번호"),
    care_worker: str = Query(None, description="담당 요양보호사"),
    birthday: str = Query(None, description="생년월일"),
    sickness: str = Query(None, description="질환명"),
    keyword: str = Query(None, description="특이사항을 검색하는 키워드")
):
    filtered_senior_care = senior_care

    if name:
        filtered_senior_care = [care for care in filtered_senior_care if care[0] == name]
    if guardian:
        filtered_senior_care = [care for care in filtered_senior_care if care[1] == guardian]
    if phone:
        filtered_senior_care = [care for care in filtered_senior_care if care[2] == phone]
    if care_worker:
        filtered_senior_care = [care for care in filtered_senior_care if care[3] == care_worker]
    if birthday:
        filtered_senior_care = [care for care in filtered_senior_care if care[4] == birthday]
    if sickness:
        filtered_senior_care = [care for care in filtered_senior_care if sickness in care[5]]
    if keyword:
        filtered_senior_care = [care for care in filtered_senior_care if keyword in care[6]]

    return filtered_senior_care

bus_line = [
    ["100", "간선", "05:00~20:00", 10, 20, "용산구청", "하계동", ["하계동", "인덕대학", "신용산역"]],
    ["101", "간선", "04:00~22:30", 5, 15, "우이동", "미아사거리", ["우이동", "수유역", "고대앞"]],
    ["130", "지선", "04:30~23:00", 20, 30, "면목동", "회기역", ["수유시장", "종암사거리입구", "경동시장", "길동"]],
    ["3313", "마을", "05:10~21:30", 17, 45, "송파공영차고지", "청량리", ["복정역환승센터", "세계로병원", "개롱역", "한양삼익아파트"]],
    ["N26", "심야", "06:30~20:40", 20, 40, "강서공영차고지", "중랑공영차고지", ["공항시장", "중량역", "당산역"]]
]

@app.get("/bus_line")
def filter_bus_line(
    busNum: str = Query(None, description="버스 번호"),
    category: str = Query(..., description="카테고리 ex) 마을, 지선, 간선, 광역"),
    time: str = Query(None, description="운행시간"),
    daysInterval: int = Query(None, description="평일 배차간격(분)"),
    weekendInterval: int = Query(None, description="주말 배차간격(분)"),
    garage: str = Query(None, description="차고지"),
    turning: str = Query(None, description="회차지점"),
    keyword: str = Query(None, description="주요 경유지를 검색하는 키워드 ex)정자역, 수내역")
):
    filtered_bus_line = bus_line

    if busNum:
        filtered_bus_line = [bus for bus in filtered_bus_line if bus[0] == busNum]
    if category:
        filtered_bus_line = [bus for bus in filtered_bus_line if bus[1] == category]
    if time:
        filtered_bus_line = [bus for bus in filtered_bus_line if bus[2] == time]
    if daysInterval:
        filtered_bus_line = [bus for bus in filtered_bus_line if bus[3] == daysInterval]
    if weekendInterval:
        filtered_bus_line = [bus for bus in filtered_bus_line if bus[4] == weekendInterval]
    if garage:
        filtered_bus_line = [bus for bus in filtered_bus_line if bus[5] == garage]
    if turning:
        filtered_bus_line = [bus for bus in filtered_bus_line if bus[6] == turning]
    if keyword:
        filtered_bus_line = [bus for bus in filtered_bus_line if keyword in bus[7]]

    return filtered_bus_line

gas_station = [
    ["직영소월길주유소", "서울특별시 용산구 소월로66", 1560, 1265, True, True],
    ["서계주유소", "서울특별시 용산구 청파로 367", 1460, 1365, True, False],
    ["신태성주유소", "서울특별시 용산구 원효로 147", 1265, 1553, False, True],
    ["금호주유소", "서울특별시 성동구 금호로 39", 1465, 1650, False, False],
    ["아이콘주유소", "서울특별시 성동구 고산자로 273", 1780, 1564, True, True]
]

@app.get("/gas_station")
def filter_gas_station(
    name: str = Query(None, description="주유소 이름"),
    max_gasoline: int = Query(None, description="최대 휘발유 가격"),
    max_diesel: int = Query(None, description="최대 경유 가격"),
    self: bool = Query(..., description="셀프 주유 여부"),
    carWash: bool = Query(None, description="세차장 유무"),
    keyword: str = Query(None, description="주소의 정보를 검색하는 키워드")
):
    filtered_gas_station = gas_station

    if name:
        filtered_gas_station = [station for station in filtered_gas_station if station[0] == name]
    if max_gasoline:
        filtered_gas_station = [station for station in filtered_gas_station if station[2] <= max_gasoline]
    if max_diesel:
        filtered_gas_station = [station for station in filtered_gas_station if station[3] <= max_diesel]
    if self:
        filtered_gas_station = [station for station in filtered_gas_station if station[4] == self]
    if carWash:
        filtered_gas_station = [station for station in filtered_gas_station if station[5] == carWash]
    if keyword:
        filtered_gas_station = [station for station in filtered_gas_station if keyword in station[1]]

    return filtered_gas_station

picking_staff = [
    ["a0001", "김남기", "010-1111-2236", "신선", "12:00", "08:00", "06:00"],
    ["a0002", "나영석", "010-2222-8897", "일반", "12:30", "07:00", "05:00"],
    ["a0003", "서인석", "010-2223-8889", "신선", "18:30", "14:20", "24:00"],
    ["a0004", "정원주", "010-4447-7777", "일반", "11:00", "06:25", "15:30"],
    ["a0005", "강나영", "010-1111-3321", "신선", "19:10", "15:30", "23:55"]
]

@app.get("/picking_staff")
def filter_picking_staff(
    staffId: str = Query(None, description="직원번호"),
    name: str = Query(None, description="직원 이름"),
    phone: str = Query(None, description="전화번호"),
    category: str = Query(..., description="카테고리 ex. 신선, 일반"),
    mealTime: str = Query(None, description="식사시간"),
    min_inTime: str = Query(None, description="최소 출근시간"),
    max_inTime: str = Query(None, description="최대 출근시간"),
    min_outTime: str = Query(None, description="최소 퇴근시간"),
    max_outTime: str = Query(None, description="최대 퇴근시간")
):
    filtered_staff = picking_staff

    if staffId:
        filtered_staff = [staff for staff in filtered_staff if staff[0] == staffId]
    if name:
        filtered_staff = [staff for staff in filtered_staff if staff[1] == name]
    if phone:
        filtered_staff = [staff for staff in filtered_staff if staff[2] == phone]
    if category:
        filtered_staff = [staff for staff in filtered_staff if staff[3] == category]
    if mealTime:
        filtered_staff = [staff for staff in filtered_staff if staff[4] == mealTime]
    if min_inTime:
        filtered_staff = [staff for staff in filtered_staff if staff[5] >= min_inTime]
    if max_inTime:
        filtered_staff = [staff for staff in filtered_staff if staff[5] <= max_inTime]
    if min_outTime:
        filtered_staff = [staff for staff in filtered_staff if staff[6] >= min_outTime]
    if max_outTime:
        filtered_staff = [staff for staff in filtered_staff if staff[6] <= max_outTime]

    return filtered_staff

tire_stores = [
    ["티스테이션 방배점", "서울특별시 서초구 서초동 1527-15", "02-3471-1918", ["금호 타이어", "한국 타이어"], "직원이 친절함"],
    ["타이어왕국", "서울특별시 동대문구 장안동 535-2", "02-335-8896", ["넥센타이어", "미쉐린 타이어"], "오픈시간이 늦음"],
    ["타이어프로", "서울특별시 구로구 구로동 1126-17", "02-830-7885", ["한국타이어"], "주차공간이 협소함"],
    ["타이어프로 신월IC점", "서울특별시 양천구 신월동 418-1", "02-2605-5550", ["한국 타이어", "금호 타이어"], "가격이 저렴해요"],
    ["금호타이어", "서울특별시 동대문구 장안동 413-5", "02-2244-2282", ["브리지스톤 타이어", "금호 타이어"], "사장님이 친근해요"]
]

@app.get("/tire_store")
def filter_tire_store(
    name: str = Query(..., description="매장 이름"),
    address: str = Query(None, description="주소"),
    phone: str = Query(None, description="전화번호"),
    goods: str = Query(None, description="취급 타이어"),
    keyword: str = Query(None, description="리뷰에 대한 정보를 검색하는 키워드")
):
    filtered_stores = tire_stores

    if name:
        filtered_stores = [store for store in filtered_stores if store[0] == name]
    if address:
        filtered_stores = [store for store in filtered_stores if store[1] == address]
    if phone:
        filtered_stores = [store for store in filtered_stores if store[2] == phone]
    if goods:
        filtered_stores = [store for store in filtered_stores if goods in store[3]]
    if keyword:
        filtered_stores = [store for store in filtered_stores if keyword in store[4]]

    return filtered_stores

rental_house_candidates = [
    ["00001", "김진기", "평택소사벌A", "010-8852-9645", 12, 2000000, 205],
    ["00003", "박민영", "파주운정3 A34BL", "010-7645-1123", 14, 2300000, 185],
    ["13525", "이혜연", "시흥시 목감7", "010-8856-7771", 35, 2300000, 450],
    ["18665", "진당소", "시흥시 목감7", "010-9963-0002", 23, 3500000, 495],
    ["00005", "전인화", "파주운정3 A34BL", "010-0023-7777", 25, 4500000, 455]
]

@app.get("/rental_house_candidate")
def filter_rental_house_candidate(
    Id: str = Query(None, description="지원번호"),
    name: str = Query(None, description="지원자명"),
    apartment: str = Query(..., description="주택명"),
    phone: str = Query(None, description="전화번호"),
    min_paymentFreq: int = Query(None, ge=1, description="최소 청약 납입 횟수"),
    min_paymentSum: int = Query(None, description="최소 청약 납입 금액"),
    min_finalScore: float = Query(None, description="최소 최종 점수")
):
    filtered_candidates = rental_house_candidates

    if Id:
        filtered_candidates = [candidate for candidate in filtered_candidates if candidate[0] == Id]
    if name:
        filtered_candidates = [candidate for candidate in filtered_candidates if candidate[1] == name]
    if apartment:
        filtered_candidates = [candidate for candidate in filtered_candidates if candidate[2] == apartment]
    if phone:
        filtered_candidates = [candidate for candidate in filtered_candidates if candidate[3] == phone]
    if min_paymentFreq:
        filtered_candidates = [candidate for candidate in filtered_candidates if candidate[4] >= min_paymentFreq]
    if min_paymentSum:
        filtered_candidates = [candidate for candidate in filtered_candidates if candidate[5] >= min_paymentSum]
    if min_finalScore:
        filtered_candidates = [candidate for candidate in filtered_candidates if candidate[6] >= min_finalScore]

    return filtered_candidates

salon_reservations = [
    ["김민희", "010-002-0009", "기존", "단발커트", "단발", "소민"],
    ["한이설", "010-8889-5556", "신규", "S컬 펌", "중단발", "한의종"],
    ["이종명", "010-7780-2201", "기존", "히피펌", "장발", "이한윤"],
    ["조윤수", "010-0003-0009", "신규", "일반커트", "숏", "소민"],
    ["조상경", "010-0001-0009", "기존", "영양클리닉", "단발", "한의종"]
]

@app.get("/salon_reservation")
def filter_salon_reservation(
    name: str = Query(None, description="이름"),
    phone: str = Query(None, description="전화번호"),
    new: str = Query(..., description="기존/신규"),
    length: str = Query(None, description="현재 기장"),
    designer: str = Query(None, description="담당 디자이너"),
    keyword: str = Query(None, description="희망 시술명을 조회하는 키워드 입니다.")
):
    filtered_reservations = salon_reservations

    if name:
        filtered_reservations = [reservation for reservation in filtered_reservations if reservation[0] == name]
    if phone:
        filtered_reservations = [reservation for reservation in filtered_reservations if reservation[1] == phone]
    if new:
        filtered_reservations = [reservation for reservation in filtered_reservations if reservation[2] == new]
    if length:
        filtered_reservations = [reservation for reservation in filtered_reservations if reservation[4] == length]
    if designer:
        filtered_reservations = [reservation for reservation in filtered_reservations if reservation[5] == designer]
    if keyword:
        filtered_reservations = [reservation for reservation in filtered_reservations if keyword in reservation[3]]

    return filtered_reservations

safe_drop_items = [
    ["한진택배", "101동", "1404호", "STL 운동복 의류", "2023.01.02", False, "박화선"],
    ["로젠택배", "102동", "203호", "최고심 짱의 조건 마우스 패드", "2023.05.23", False, "백경민"],
    ["CJ택배", "103동", "205호", "N9소형 선풍기", "2021.09.11", True, "은동기"],
    ["CJ택배", "108동", "504호", "애플 아이패드 프로 11inch", "2023.11.12", False, "이재성"],
    ["로젠택배", "1204동", "202호", "금광농장 사과 10kg", "2023.07.06", True, "이송희"]
]

@app.get("/safe_drop")
def filter_safe_drop(
    company: str = Query(..., description="택배사"),
    dong: str = Query(None, description="동"),
    ho: str = Query(None, description="호수"),
    itemName: str = Query(None, description="택배물"),
    min_date: str = Query(None, description="최소 도착 날짜"),
    freshTF: bool = Query(None, description="신선식품 여부"),
    name: str = Query(None, description="고객명")
):
    filtered_items = safe_drop_items

    if company:
        filtered_items = [item for item in filtered_items if item[0] == company]
    if dong:
        filtered_items = [item for item in filtered_items if item[1] == dong]
    if ho:
        filtered_items = [item for item in filtered_items if item[2] == ho]
    if itemName:
        filtered_items = [item for item in filtered_items if item[3] == itemName]
    if min_date:
        filtered_items = [item for item in filtered_items if item[4] >= min_date]
    if freshTF is not None:
        filtered_items = [item for item in filtered_items if item[5] == freshTF]
    if name:
        filtered_items = [item for item in filtered_items if item[6] == name]

    return filtered_items

auto_car_park_customers = [
    ["0001", "김성남", "010-1346-8432", "소형", "A01", "01:00", "02:00"],
    ["0002", "김일성", "010-0001-0002", "중형", "B02", "10:00", "14:00"],
    ["0003", "박이진", "010-0002-0003", "대형", "H03", "20:00", "23:00"],
    ["0005", "택무선", "010-1112-1114", "소형", "J05", "15:00", "06:00"],
    ["0008", "곽한소", "010-7789-0001", "중형", "C04", "12:00", "12:30"]
]

@app.get("/auto_car_park")
def filter_auto_car_park(
    carId: str = Query(None, description="차량 번호"),
    name: str = Query(None, description="차주"),
    phone: str = Query(None, description="전화번호"),
    category: str = Query(..., description="카테고리"),
    spotId: str = Query(None, description="주차 자리"),
    min_inTime: str = Query(None, description="최소 입차시간"),
    min_outTime: str = Query(None, description="최소 출차시간"),
):
    filtered_customers = auto_car_park_customers

    if carId:
        filtered_customers = [customer for customer in filtered_customers if customer[0] == carId]
    if name:
        filtered_customers = [customer for customer in filtered_customers if customer[1] == name]
    if phone:
        filtered_customers = [customer for customer in filtered_customers if customer[2] == phone]
    if category:
        filtered_customers = [customer for customer in filtered_customers if customer[3] == category]
    if spotId:
        filtered_customers = [customer for customer in filtered_customers if customer[4] == spotId]
    if min_inTime:
        filtered_customers = [customer for customer in filtered_customers if customer[5] >= min_inTime]
    if min_outTime:
        filtered_customers = [customer for customer in filtered_customers if customer[6] >= min_outTime]

    return filtered_customers

perform_stage_schedules = [
    [
        "베토벤 피아노 소나타 전곡 Ⅳ",
        "2023.07.06",
        "콘서트홀",
        "현존하는 최고 권위의 베토벤 스페셜리스트와 함께하는 7일간의 대장정",
        ["루돌프 부흐빈더", "김성진", "임수향"],
        ["S", "A", "B", "C"],
    ],
    [
        "타악듀오 모아티에 열두 번째 프로젝트",
        "2023.08.12",
        "IBK챔버홀",
        "김은혜와 한문경의 타악듀오 모아티에를 감상하세요",
        ["김은혜", "임마누엘 리"],
        ["A", "B"],
    ],
    [
        "플루트 리사이틀",
        "2024.12.03",
        "IBK챔버홀",
        "클래식 부문에서 10년 을 빛낼 100인으로 선정된 한여진의 연주!",
        ["한여진", "김아리", "강동하"],
        ["D", "E", "R"],
    ],
    [
        "아베끄 스트링 콰르텟",
        "2023.02.05",
        "브라움홀",
        "활발한 활동을 하고 있는 젊은 현악사중주의 다양항 레파토리를 선사하고자 한다",
        ["이석중", "김 다니엘"],
        ["R", "S"],
    ],
    [
        "이시윤 바로크 바이올린 귀국 독주회",
        "2023.02.03",
        "리사이틀홀",
        "독일 프랑크푸르트 국립 음악원의 영재 이시윤의 독주회!",
        ["이시윤", "유민호"],
        ["L", "N", "S"],
    ],
]

@app.get("/perform_stage")
def filter_perform_stage(
    name: str = Query(None, description="공연명"),
    date: str = Query(None, description="공연 날짜"),
    arena: str = Query(..., description="공연장 이름"),
    cast: str = Query(None, description="출연진"),
    seat: str = Query(None, description="좌석"),
    keyword: str = Query(None, description="공연 설명을 검색하는 키워드"),
):
    filtered_schedules = perform_stage_schedules

    if name:
        filtered_schedules = [schedule for schedule in filtered_schedules if schedule[0] == name]
    if date:
        filtered_schedules = [schedule for schedule in filtered_schedules if schedule[1] == date]
    if arena:
        filtered_schedules = [schedule for schedule in filtered_schedules if schedule[2] == arena]
    if cast:
        filtered_schedules = [schedule for schedule in filtered_schedules if cast in schedule[3]]
    if seat:
        filtered_schedules = [schedule for schedule in filtered_schedules if seat in schedule[4]]
    if keyword:
        filtered_schedules = [schedule for schedule in filtered_schedules if keyword in schedule[3]]

    return filtered_schedules

robot_cafe_orders = [
    [
        "잠실 롯데월드몰점",
        "아이스 아메이카노",
        5000,
        "10:00",
        1,
        "1001",
    ],
    [
        "현대백화점 판교지점",
        "아이스 카페라떼",
        5500,
        "11:00",
        2,
        "1002",
    ],
    [
        "현대백화점 판교지점",
        "레몬에이드",
        7000,
        "12:05",
        3,
        "1003",
    ],
    [
        "광양 파크랜드점",
        "카페모카",
        6000,
        "14:35",
        4,
        "1004",
    ],
    [
        "잠실 롯데월드몰점",
        "아이스티",
        6500,
        "15:08",
        5,
        "1005",
    ],
]

@app.get("/robot_cafe")
def filter_robot_cafe(
    cafeName: str = Query(..., description="매장명"),
    drink: str = Query(None, description="주문음료"),
    min_price: int = Query(None, description="최소 가격"),
    max_price: int = Query(None, description="최대 가격"),
    min_time: str = Query(None, description="최소 주문 시간"),
    turn: int = Query(None, description="순번"),
    pickupNum: str = Query(None, description="픽업번호"),
):
    filtered_orders = robot_cafe_orders

    if cafeName:
        filtered_orders = [order for order in filtered_orders if order[0] == cafeName]
    if drink:
        filtered_orders = [order for order in filtered_orders if order[1] == drink]
    if min_price:
        filtered_orders = [order for order in filtered_orders if order[2] >= min_price]
    if max_price:
        filtered_orders = [order for order in filtered_orders if order[2] <= max_price]
    if min_time:
        filtered_orders = [order for order in filtered_orders if order[3] >= min_time]
    if turn:
        filtered_orders = [order for order in filtered_orders if order[4] == turn]
    if pickupNum:
        filtered_orders = [order for order in filtered_orders if order[5] == pickupNum]

    return filtered_orders

refurbished_shop_products = [
    [
        "베스톰",
        "모양깍지",
        "반품",
        "제빵기구",
        8000,
        4000,
        4,
    ],
    [
        "삼광글라스",
        "글라스락",
        "포장불량",
        "주방용품",
        20000,
        15000,
        6,
    ],
    [
        "락앤락",
        "커트러리",
        "B급",
        "주방용품",
        15000,
        9000,
        4,
    ],
    [
        "피닉스",
        "미러수경",
        "포장불량",
        "수영용품",
        26000,
        12000,
        1,
    ],
    [
        "동서식품",
        "테이크핏",
        "반품",
        "식품",
        34900,
        10000,
        24,
    ],
]

@app.get("/refurbished_shop")
def filter_refurbished_shop(
    manufacture: str = Query(None, description="제조사"),
    name: str = Query(None, description="상품명"),
    category: str = Query(..., description="카테고리"),
    sort: str = Query(None, description="구분"),
    originPrice: int = Query(None, description="원가"),
    min_salePrice: int = Query(None, description="최소 할인가격"),
    max_salePrice: int = Query(None, description="최대 할인가격"),
    min_stock: int = Query(None, description="최소 수량"),
):
    filtered_products = refurbished_shop_products

    if manufacture:
        filtered_products = [product for product in filtered_products if product[0] == manufacture]
    if name:
        filtered_products = [product for product in filtered_products if product[1] == name]
    if sort:
        filtered_products = [product for product in filtered_products if product[2] == sort]
    if category:
        filtered_products = [product for product in filtered_products if product[3] == category]
    if originPrice:
        filtered_products = [product for product in filtered_products if product[4] == originPrice]
    if min_salePrice:
        filtered_products = [product for product in filtered_products if product[5] >= min_salePrice]
    if max_salePrice:
        filtered_products = [product for product in filtered_products if product[5] <= max_salePrice]
    if min_stock:
        filtered_products = [product for product in filtered_products if product[6] >= min_stock]

    return filtered_products

uni_hospital_nurse_schedules = [
    [
        "응급실",
        "데이",
        "00001",
        "김간호",
        "010-0001-0002",
        1,
    ],
    [
        "소아과",
        "나이트",
        "00002",
        "이희진",
        "010-0002-0005",
        2,
    ],
    [
        "병동 간호팀",
        "데이",
        "00003",
        "박예진",
        "010-0002-0009",
        3,
    ],
    [
        "신생아실",
        "나이트",
        "00004",
        "양예림",
        "010-0007-0001",
        4,
    ],
    [
        "신생아실",
        "데이",
        "00005",
        "김고은",
        "010-0007-0002",
        5,
    ],
]

@app.get("/uni_hospital_nurse")
def filter_university_hospital_nurse(
    belong: str = Query(..., description="소속"),
    day_schedule: str = Query(None, description="스케줄"),
    id: str = Query(None, description="사번"),
    name: str = Query(None, description="이름"),
    phone: str = Query(None, description="전화번호"),
    min_orderYear: int = Query(None, description="최소 연차"),
):
    filtered_schedules = uni_hospital_nurse_schedules

    filtered_schedules = [schedule for schedule in filtered_schedules if schedule[0] == belong]
    if day_schedule:
        filtered_schedules = [schedule for schedule in filtered_schedules if schedule[1] == day_schedule]
    if id:
        filtered_schedules = [schedule for schedule in filtered_schedules if schedule[2] == id]
    if name:
        filtered_schedules = [schedule for schedule in filtered_schedules if schedule[3] == name]
    if phone:
        filtered_schedules = [schedule for schedule in filtered_schedules if schedule[4] == phone]
    if min_orderYear:
        filtered_schedules = [schedule for schedule in filtered_schedules if schedule[5] >= min_orderYear]

    return filtered_schedules

tarot_fortune_shop_data = [
    [
        "타로매니아",
        "서울특별시 강남구 역삼동 817 11번지 용빌딩 3층",
        True,
        False,
        "루시",
        "010-0002-0001",
        "정말 잘 맞아요",
    ],
    [
        "타로사주블라썸",
        "신사동 596번지 청오빌딩 102호 강남구 서울특별시 KR",
        True,
        True,
        "헤이즐",
        "010-4213-8626",
        "주차공간이 없어요",
    ],
    [
        "사주천국",
        "자양동 13-1번지 2층 덕유빌딩 광진구",
        False,
        True,
        "케코아",
        "010-1112-1115",
        "오래봐주고 잘 친절해요",
    ],
    [
        "타로사주블라썸",
        "서울특별시 방이동 71-13번지",
        True,
        False,
        "지니",
        "010-2222-3333",
        "접근성이 좋아요",
    ],
    [
        "타로매니아",
        "서울특별시 삼전동 54-12번지",
        True,
        True,
        "미니",
        "010-9999-7223",
        "재방문 의사 있어요",
    ],
]

@app.get("/tarot_fortune_shop")
def filter_tarot_fortune_shop(
    name: str = Query(..., description="매장명"),
    tarot: bool = Query(None, description="타로 여부"),
    fortune: bool = Query(None, description="사주 여부"),
    teller: str = Query(None, description="텔러 이름"),
    phone: str = Query(None, description="전화번호"),
    keyword: str = Query(None, description="리뷰의 내용을 검색하는 키워드"),
):
    filtered_shops = tarot_fortune_shop_data

    filtered_shops = [shop for shop in filtered_shops if shop[0] == name]
    if tarot is not None:
        filtered_shops = [shop for shop in filtered_shops if shop[2] == tarot]
    if fortune is not None:
        filtered_shops = [shop for shop in filtered_shops if shop[3] == fortune]
    if teller:
        filtered_shops = [shop for shop in filtered_shops if shop[4] == teller]
    if phone:
        filtered_shops = [shop for shop in filtered_shops if shop[5] == phone]
    if keyword:
        filtered_shops = [shop for shop in filtered_shops if keyword in shop[6]]

    return filtered_shops

mouse_data = [
    ["HP", "925", True, False, "무선", 119000],
    ["녹스", "NX-M1", False, False, "유선", 0],
    ["삼성전자", "SPA-KMG1PUB", False, True, "유선", 49900],
    ["로지텍", "LIFT", True, True, "무선", 73090],
    ["로지텍", "M350", False, True, "무선", 18160],
]

@app.get("/mouse")
def filter_mouse(
    manufacture: str = Query(None, description="제조사"),
    name: str = Query(None, description="상품명"),
    vertical: bool = Query(..., description="버티컬 여부"),
    noNoise: bool = Query(None, description="무소음 여부"),
    wirelessOrWire: str = Query(None, description="유/무선"),
    min_price: int = Query(None, description="최소 가격"),
    max_price: int = Query(None, description="최대 가격"),
):
    filtered_mice = mouse_data

    if manufacture:
        filtered_mice = [mouse for mouse in filtered_mice if mouse[0] == manufacture]
    if name:
        filtered_mice = [mouse for mouse in filtered_mice if mouse[1] == name]
    filtered_mice = [mouse for mouse in filtered_mice if mouse[2] == vertical]
    if noNoise is not None:
        filtered_mice = [mouse for mouse in filtered_mice if mouse[3] == noNoise]
    if wirelessOrWire:
        filtered_mice = [mouse for mouse in filtered_mice if mouse[4] == wirelessOrWire]
    if min_price is not None:
        filtered_mice = [mouse for mouse in filtered_mice if mouse[5] >= min_price]
    if max_price is not None:
        filtered_mice = [mouse for mouse in filtered_mice if mouse[5] <= max_price]

    return filtered_mice

diaper_data = [
    ["하기스", 36, "팬티형", 100, 59900],
    ["팸퍼스", 24, "접착형", 156, 79900],
    ["페넬로페", 6, "팬티형", 20, 15880],
    ["마미포코", 12, "일자형", 52, 29580],
    ["하기스", 6, "팬티형", 44, 23780],
]

@app.get("/diaper")
def filter_diaper(
    brand: str = Query(None, description="브랜드"),
    age: int = Query(None, description="연령(개월)"),
    type: str = Query(..., description="형태"),
    number: int = Query(None, description="갯수"),
    min_price: int = Query(None, description="최소 가격"),
    max_price: int = Query(None, description="최대 가격"),
):
    filtered_diapers = diaper_data

    if brand:
        filtered_diapers = [diaper for diaper in filtered_diapers if diaper[0] == brand]
    if age is not None:
        filtered_diapers = [diaper for diaper in filtered_diapers if diaper[1] == age]
    filtered_diapers = [diaper for diaper in filtered_diapers if diaper[2] == type]
    if number is not None:
        filtered_diapers = [diaper for diaper in filtered_diapers if diaper[3] == number]
    if min_price is not None:
        filtered_diapers = [diaper for diaper in filtered_diapers if diaper[4] >= min_price]
    if max_price is not None:
        filtered_diapers = [diaper for diaper in filtered_diapers if diaper[4] <= max_price]

    return filtered_diapers

dishwasher_data = [
    ["SK매직", "DWA19C0P", 6, False, "애벌 설거지가 가능한 모델", 599000],
    ["LG전자", "DUBJ2EA", 12, True, "식기세척기와 전기레인지 세트 설치 가능", 1085530],
    ["삼성전자", "DW30A3030CE _KY", 6, True, "비스포크시리즈로 아름다운 키친테리어", 401228],
    ["LG전자", "DTC2NE", 12, False, "듀얼세척날개로 빈틈없는 설거지", 790000],
    ["쿠쿠전자", "CDW-A0611TS", 6, False, "급속모드로 빠른 세척 가능", 249760],
]

@app.get("/dishwasher")
def filter_dishwasher(
    manufacture: str = Query(None, description="제조사"),
    name: str = Query(None, description="상품명"),
    amount: int = Query(..., description="인용"),
    builtIn: bool = Query(None, description="빌트인 가능 여부"),
    min_price: int = Query(None, description="최소 가격"),
    max_price: int = Query(None, description="최대 가격"),
    keyword: str = Query(None, description="주요 특징을 검색하는 키워드"),
):
    filtered_dishwashers = dishwasher_data

    if manufacture:
        filtered_dishwashers = [dishwasher for dishwasher in filtered_dishwashers if dishwasher[0] == manufacture]
    if name:
        filtered_dishwashers = [dishwasher for dishwasher in filtered_dishwashers if dishwasher[1] == name]
    filtered_dishwashers = [dishwasher for dishwasher in filtered_dishwashers if dishwasher[2] == amount]
    if builtIn is not None:
        filtered_dishwashers = [dishwasher for dishwasher in filtered_dishwashers if dishwasher[3] == builtIn]
    if min_price is not None:
        filtered_dishwashers = [dishwasher for dishwasher in filtered_dishwashers if dishwasher[5] >= min_price]
    if max_price is not None:
        filtered_dishwashers = [dishwasher for dishwasher in filtered_dishwashers if dishwasher[5] <= max_price]
    if keyword:
        filtered_dishwashers = [dishwasher for dishwasher in filtered_dishwashers if keyword.lower() in dishwasher[4].lower()]

    return filtered_dishwashers

diving_pool_data = [
    ["올림픽수영장", "서울 송파구 올림픽로 424 올림픽수영장내 다이빙풀(잠수풀장)", 50, 74, ["스쿠버", "프리다이빙"], True, 12000],
    ["아르피아 잠수풀", "경기 용인시 수지구 포은대로 499 잠수풀장", 20, 30, ["스쿠버", "프리다이빙"], False, 10000],
    ["K26잠수풀", "경기 가평군 청평면 고재길 262-57", 26, 30, ["프리다이빙"], False, 33000],
    ["경기잠수연습장", "경기 평택시 오성면 오성서로 116-25", 15, 40, ["스쿠버", "프리다이빙"], True, 18000],
    ["류다이브", "서울 강동구 성내로 89 503호", 20, 30, ["스쿠버"], True, 10000],
]

@app.get("/diving_pool")
def filter_diving_pool(
    name: str = Query(None, description="잠수풀명"),
    depth: float = Query(None, description="수심(m)"),
    amount: int = Query(None, description="수용 인원"),
    class_: str = Query(None, description="강습 종류"),
    rental: bool = Query(..., description="장비 대여 여부"),
    max_price: int = Query(None, description="최대 입장료"),
    keyword: str = Query(None, description="주소를 검색하는 키워드"),
):
    filtered_diving_pools = diving_pool_data

    if name:
        filtered_diving_pools = [pool for pool in filtered_diving_pools if pool[0] == name]
    if depth is not None:
        filtered_diving_pools = [pool for pool in filtered_diving_pools if pool[2] == depth]
    if amount is not None:
        filtered_diving_pools = [pool for pool in filtered_diving_pools if pool[3] == amount]
    if class_ is not None:
        filtered_diving_pools = [pool for pool in filtered_diving_pools if class_ in pool[4]]
    filtered_diving_pools = [pool for pool in filtered_diving_pools if pool[5] == rental]
    if max_price is not None:
        filtered_diving_pools = [pool for pool in filtered_diving_pools if pool[6] <= max_price]
    if keyword:
        filtered_diving_pools = [pool for pool in filtered_diving_pools if keyword.lower() in pool[1].lower()]

    return filtered_diving_pools

idol_data = [
    ["YG", "블랙핑크", ["리사", "지수", "제니", "로제"], "걸그룹", 15, "2016.08.08"],
    ["HYBE", "BTS", ["진", "슈가", "제이홉", "RM", "지민", "뷔", "정국"], "보이그룹", 25, "2013.06.13"],
    ["DSPmedia", "KARD", ["J.Seph", "BM", "전소민", "전지우"], "혼성그룹", 6, "2017.07.19"],
    ["Starship", "IVE", ["안유진", "가을", "레이", "장원영", "리즈", "이서"], "걸그룹", 4, "2021.12.01"],
    ["SM Entertainment", "NCT Dream", ["마크", "런쥔", "제노", "해찬", "재민", "천러", "지성"], "보이그룹", 9, "2016,08.25"],
]

@app.get("/idol")
def filter_idol(
    companyName: str = Query(None, description="소속사명"),
    groupName: str = Query(None, description="그룹명"),
    member: str = Query(None, description="멤버"),
    category: str = Query(..., description="그룹 카테고리"),
    min_albumCount: int = Query(None, description="최소 앨범 갯수"),
    min_debut: str = Query(None, description="최소 데뷔일자"),
    max_debut: str = Query(None, description="최대 데뷔일자"),
):
    filtered_idols = idol_data

    if companyName:
        filtered_idols = [idol for idol in filtered_idols if idol[0] == companyName]
    if groupName:
        filtered_idols = [idol for idol in filtered_idols if idol[1] == groupName]
    if member:
        filtered_idols = [idol for idol in filtered_idols if member in idol[2]]
    filtered_idols = [idol for idol in filtered_idols if idol[3] == category]
    if min_albumCount is not None:
        filtered_idols = [idol for idol in filtered_idols if idol[4] >= min_albumCount]
    if min_debut:
        filtered_idols = [idol for idol in filtered_idols if idol[5] >= min_debut]
    if max_debut:
        filtered_idols = [idol for idol in filtered_idols if idol[5] <= max_debut]

    return filtered_idols

member_data = [
    ["김미연", 13, "6인실", 160, True],
    ["강선애", 30, "4인실", 240, False],
    ["김태연", 20, "4인실", 1000, True],
    ["양순일", 115, "6인실", 500, False],
    ["강민규", 201, "1인실", 700, False],
]

@app.get("/reading_room_member")
def filter_reading_room_member(
    name: str = Query(None, description="회원 이름"),
    seatId: int = Query(None, description="좌석 번호"),
    seatType: str = Query(..., description="좌석 형식"),
    min_time: int = Query(None, description="최소 잔여시간(분)"),
    max_time: int = Query(None, description="최대 잔여시간(분)"),
    nowOnSeat: bool = Query(None, description="현재 이용 여부"),
):
    filtered_members = member_data

    if name:
        filtered_members = [member for member in filtered_members if member[0] == name]
    if seatId:
        filtered_members = [member for member in filtered_members if member[1] == seatId]
    filtered_members = [member for member in filtered_members if member[2] == seatType]
    if min_time is not None:
        filtered_members = [member for member in filtered_members if member[3] >= min_time]
    if max_time is not None:
        filtered_members = [member for member in filtered_members if member[3] <= max_time]
    if nowOnSeat is not None:
        filtered_members = [member for member in filtered_members if member[4] == nowOnSeat]

    return filtered_members

noodles_data = [
    ["농심", "신라면", "빨간국물 라면", 500, 1500],
    ["농심", "짜파게티", "볶음면", 610, 1700],
    ["삼양", "불닭볶음면", "볶음면", 550, 1200],
    ["오뚜기", "진라면", "빨간국물 라면", 550, 1100],
    ["농심", "사리곰탕면", "하얀국물 라면", 475, 1800],
]

@app.get("/instant_noodles")
def filter_instant_noodles(
    manufacture: str = Query(None, description="제조사"),
    name: str = Query(None, description="상품명"),
    category: str = Query(..., description="카테고리"),
    max_calory: float = Query(None, description="최대 칼로리"),
    min_price: int = Query(None, description="최소 가격"),
    max_price: int = Query(None, description="최대 가격"),
):
    filtered_noodles = noodles_data

    if manufacture:
        filtered_noodles = [noodles for noodles in filtered_noodles if noodles[0] == manufacture]
    if name:
        filtered_noodles = [noodles for noodles in filtered_noodles if noodles[1] == name]
    filtered_noodles = [noodles for noodles in filtered_noodles if noodles[2] == category]
    if max_calory is not None:
        filtered_noodles = [noodles for noodles in filtered_noodles if noodles[3] <= max_calory]
    if min_price is not None:
        filtered_noodles = [noodles for noodles in filtered_noodles if noodles[4] >= min_price]
    if max_price is not None:
        filtered_noodles = [noodles for noodles in filtered_noodles if noodles[4] <= max_price]

    return filtered_noodles

dessertshop_data = [
    ["삼다도오메기떡집", "제주 제주시 남성로 127", ["팥오메기떡", "흑임자오메기떡", "콩가루오메기떡"], 4.6, False, False],
    ["서귀피안 베이커리", "제주 서귀포시 성산읍 신양로122번길 17 2F", ["소금빵", "플레인크로아상", "쿠앤크크림빵"], 3.8, True, True],
    ["호텔샌드", "제주 제주시 한림읍 한림로 339", ["선인장 몽테", "과일 타르트", "모래섬"], 4.39, True, False],
    ["우무", "제주 제주시 한림읍 한림로 542-1", ["커스터드 푸딩", "말차 푸딩", "오트 비건 푸딩"], 4.9, False, False],
    ["몽그레", "제주 제주시 도리로 84", ["말차맛 찰보리과자", "초코맛 찰보리과자", "우도 땅콩맛 찰보리과자"], 3.2, False, True],
]

@app.get("/jeju_dessertshop")
def filter_jeju_dessert_shop(
    name: str = Query(None, description="매장명"),
    dessertMenu: str = Query(None, description="디저트 메뉴"),
    min_grade: float = Query(None, ge=0, le=5, description="최소 평점"),
    drinkAvailable: bool = Query(None, description="음료 판매여부"),
    parkingAvailable: bool = Query(..., description="주차 가능 여부"),
    keyword: str = Query(None, description="주소를 검색하는 키워드"),
):
    filtered_dessertshops = dessertshop_data

    if name:
        filtered_dessertshops = [dessertshop for dessertshop in filtered_dessertshops if dessertshop[0] == name]
    if dessertMenu:
        filtered_dessertshops = [dessertshop for dessertshop in filtered_dessertshops if dessertMenu in dessertshop[2]]
    if min_grade is not None:
        filtered_dessertshops = [dessertshop for dessertshop in filtered_dessertshops if dessertshop[3] >= min_grade]
    if drinkAvailable is not None:
        filtered_dessertshops = [dessertshop for dessertshop in filtered_dessertshops if dessertshop[4] == drinkAvailable]
    filtered_dessertshops = [dessertshop for dessertshop in filtered_dessertshops if dessertshop[5] == parkingAvailable]
    if keyword:
        filtered_dessertshops = [dessertshop for dessertshop in filtered_dessertshops if keyword in dessertshop[1]]

    return filtered_dessertshops

zero_sugar_drink_data = [
    ["코카콜라", "코카콜라 제로", "수크랄로스 아세설팜칼룸", 190, 900],
    ["펩시", "펩시 제로 라임", "아스파탐", 355, 2100],
    ["동아오츠카", "나랑드 사이다", "수크랄로스와", 245, 1600],
    ["롯데칠성음료", "칠성사이다 제로", "아스파탐", 190, 950],
    ["코카콜라", "스프라이트 제로", "에리스리톨", 500, 2700],
]

@app.get("/zero_sugar_drink")
def filter_zero_sugar_drink(
    manufacture: str = Query(None, description="제조사명"),
    name: str = Query(None, description="상품명"),
    replaceSugar: str = Query(..., description="대체당 종류"),
    min_weight: float = Query(None, description="최소 용량(ml)"),
    max_price: int = Query(None, description="최대 가격"),
):
    filtered_drinks = zero_sugar_drink_data

    if manufacture:
        filtered_drinks = [drink for drink in filtered_drinks if drink[0] == manufacture]
    if name:
        filtered_drinks = [drink for drink in filtered_drinks if drink[1] == name]
    filtered_drinks = [drink for drink in filtered_drinks if drink[2] == replaceSugar]
    if min_weight is not None:
        filtered_drinks = [drink for drink in filtered_drinks if drink[3] >= min_weight]
    if max_price is not None:
        filtered_drinks = [drink for drink in filtered_drinks if drink[4] <= max_price]

    return filtered_drinks


blogger_data = [
    ["올라와 올라프", "올라", "맛집", ["성남 혼술은 바로 여기", "남한산성 맛집", "죽기전 반드시 먹어야 할 소금빵집 추천"], "2011.01.30"],
    ["화려함보다는 수수하게", "김콩팥", "일상", ["작게 시작하는 영농일기", "나만의 텃밭 가꾸는 법", "제로웨이스트 실천방법"], "2004.06.28"],
    ["멍이랑 나랑", "멍이누나", "반려동물", ["반려동물과 함께하면 좋을 서울의 핫플", "강아지 사료 리뷰", "실외배변 강아지 실내배변으로 바꾸는 법"], "2017.09.08"],
    ["오늘보다 내일 더 예뻐져요", "쁨랑이", "미용", ["상한 머릿결을 가꾸어주는 홈케어", "여드름 피부는 이렇게 하세요", "괄사마사지로 얼굴 1cm줄이는 방법"], "2019.08.13"],
    ["맛있는 음식을 먹어야 행복하다", "아지랑이", "맛집", ["수내역 라멘 맛집으로 안내합니다.", "충격적인 맛의 송파구 칼국수집", "밥보다 밀가루 많이 먹는 사람의 일주일 식단"], "2023.08.30"],
]

@app.get("/blogger")
def filter_blogger(
    blogName: str = Query(None, description="블로그명"),
    bloggerName: str = Query(None, description="블로거 이름"),
    category: str = Query(..., description="카테고리"),
    openDate: str = Query(None, description="최소 개설일자"),
    keyword: str = Query(None, description="작성글 제목을 조회하는 키워드"),
):
    filtered_bloggers = blogger_data

    if blogName:
        filtered_bloggers = [blogger for blogger in filtered_bloggers if blogger[0] == blogName]
    if bloggerName:
        filtered_bloggers = [blogger for blogger in filtered_bloggers if blogger[1] == bloggerName ]
    filtered_bloggers = [blogger for blogger in filtered_bloggers if blogger[2] == category]
    if openDate is not None:
        filtered_bloggers = [blogger for blogger in filtered_bloggers if blogger[4] == openDate]
    if keyword:
        filtered_bloggers = [blogger for blogger in filtered_bloggers if keyword in blogger[3]]

    return filtered_bloggers

yakgwa_data = [
    ["순심이네","경기 포천시 군내면 호국로 1578 1층",5500,"끈적하고 쫀득한 식감","000-0000-0001",False],
    ["버들골","강원 춘천시 서부대성로 12",15500,"바삭한 패스츄리","000-0000-0002",True],
    ["마쉿당","서울 강남구 논현로175길 61",32000,"유기농 조청과 고급스러운 포장","000-0000-0003",True],
    ["호운당","서울 강남구 압구정로34길 26",28000,"부드럽고 적당한 단맛","000-0000-0004",False],
    ["사슴약과","제주 서귀포시 중앙로48번길 9",9800,"부드럽고 바삭한 식감","000-0000-0005",True],
]

@app.get("/Yakgwa")
def filter_yakgwa(
    name: str = Query(None, description="상점명"),
    location: str = Query(..., description="지역"),
    min_price: float = Query(None, ge=0, description="최소 가격"),
    max_price: float = Query(None, ge=0, description="최대 가격"),
    desc: str = Query(None, description="설명"),
    parking_available: bool = Query(None, description="주차 가능 여부"),
):
    filtered_yakgwa = yakgwa_data

    if name:
        filtered_yakgwa = [shop for shop in filtered_yakgwa if shop[0] == name]
    filtered_yakgwa = [shop for shop in filtered_yakgwa if location in shop[1]]
    if min_price is not None:
        filtered_yakgwa = [shop for shop in filtered_yakgwa if shop[2] >= min_price]
    if max_price is not None:
        filtered_yakgwa = [shop for shop in filtered_yakgwa if shop[2] <= max_price]
    if desc:
        filtered_yakgwa = [shop for shop in filtered_yakgwa if desc in shop[3]]
    if parking_available is not None:
        filtered_yakgwa = [shop for shop in filtered_yakgwa if shop[5] == parking_available]

    return filtered_yakgwa

illustration_data = [
    ["키키키","키키키","소형","2023-08-01","동물, 캐릭터","귀여운 동물 캐릭터를 그립니다.","000-0000-0001"],
    ["오하요","요이","중형","2023-08-02","레트로, 타이포","레트로 타이포 디자인을 활용한 일러를 그립니다.","000-0000-0002"],
    ["가분수","분수","소형","2023-08-12","음식, 레트로","음식 일러스트레이션.","000-0000-0003"],
    ["쿠키공장","체리쿠기","대형","2023-08-01","동물, 캐릭터","귀여운 동물 캐릭터를 그립니다.","000-0000-0004"],
    ["띠요네","띠요","소형","2023-08-02","동화, 캐릭터","아동용 동화를 그립니다.","000-0000-0005"],
]

@app.get("/IllustrationFair")
def filter_illustration_fair(
    team: str = Query(None, description="팀이름, 부스이름"),
    artist: str = Query(None, description="아티스트이름"),
    booth_t: str = Query(None, description="부스종류"),
    date: str = Query(None, description="참가일"),
    genre: str = Query(..., description="분야"),
    desc: str = Query(None, description="설명"),
):
    filtered_illustration = illustration_data

    if team:
        filtered_illustration = [booth for booth in filtered_illustration if booth[0] == team]
    if artist:
        filtered_illustration = [booth for booth in filtered_illustration if booth[1] == artist]
    if booth_t:
        filtered_illustration = [booth for booth in filtered_illustration if booth[2] == booth_t]
    if date:
        filtered_illustration = [booth for booth in filtered_illustration if booth[3] == date]
    filtered_illustration = [booth for booth in filtered_illustration if genre in booth[4]]
    if desc:
        filtered_illustration = [booth for booth in filtered_illustration if desc in booth[5]]

    return filtered_illustration

@app.get("/KoreanChineseFood")
async def filter_KoreanChineseFood(
    menu: str = Query(None, description="메뉴이름"),
    food_stuff: List[str] = Query(..., description="재료 (예: 짜장, 춘장, 돼지고기 등)"),
    taste: str = Query(None, description="맛 (예: 단맛, 신맛 등)"),
    min_amount: float = Query(None, ge=0, description="최소인분 (양, 1인분 등)"),
    max_amount: float = Query(None, description="최대인분 (양, 1인분 등)"),
    min_price: float = Query(None, ge=0, description="최소가격"),
    max_price: float = Query(None, description="최대가격"),
):
    # 중식 메뉴 데이터
    KoreanChineseFood = [
        ["짜장면", ["면", "짜장", "춘장", "돼지고기"], "단맛", 1, 7500, "수타면을 사용한 짜장입니다."],
        ["짬뽕", ["면", "오징어", "홍합", "돼지고기"], "매운맛", 1, 7500, "불맛이 가득한 짬뽕입니다."],
        ["볶음밥", ["밥", "양파", "계란", "돼지고기"], "담백한맛", 1, 7500, "계란볶음밥. 짜장소스는 없습니다."],
        ["경장육사", ["오이", "건두부", "춘장", "돼지고기"], "짭짤한맛", 3, 25500, "건두부에 볶은 돼지고기를 싸먹는 요리입니다."],
        ["유산슬", ["계란", "새우", "오징어", "해삼"], "담백한맛", 3, 32000, "신선한 해산물을 가득 넣었습니다."]
    ]

    filtered_menus = []

    for menu_item in KoreanChineseFood:
        if (
            (menu_item[0] == menu if menu else True) and
            all(food in menu_item[1] for food in food_stuff) and
            (menu_item[2] == taste if taste else True) and
            (menu_item[3] >= min_amount if min_amount else True) and
            (menu_item[3] <= max_amount if max_amount else True) and
            (menu_item[4] >= min_price if min_price else True) and
            (menu_item[4] <= max_price if max_price else True)
        ):
            filtered_menus.append({
                "menu": menu_item[0],
                "food_stuff": menu_item[1],
                "taste": menu_item[2],
                "amount": menu_item[3],
                "price": menu_item[4],
                "desc": menu_item[5]
            })

    return filtered_menus

cat_sitter_member_data = [
    ["까망이","여",1,"없음","코숏","동결건조닭고기를 좋아함","000-0000-0001"],
    ["노랑이","남",6,"방광염","코숏","방광염 약 복용중","000-0000-0002"],
    ["단추","여",9,"알러지성 피부염","샴","알러지프리 간식만 먹음","000-0000-0003"],
    ["호야","여",10,"없음","코숏","공격성이 있음","000-0000-0004"],
    ["콩이","남",1,"결막염","페르시안","안약 투여 필요","000-0000-0005"]
]

@app.get("/CatSitterMember")
def filter_cat_sitter_member(
    name: str = Query(..., description="고양이이름"),
    gender: str = Query(None, description="성별"),
    age: int = Query(None, gt=0, description="나이"),
    disease: str = Query(None, description="질병"),
    breed: str = Query(None, description="품종"),
    other: str = Query(None, description="특이사항"),
):
    filtered_members = cat_sitter_member_data

    filtered_members = [member for member in filtered_members if member[0] == name]
    if gender:
        filtered_members = [member for member in filtered_members if member[1] == gender]
    if age:
        filtered_members = [member for member in filtered_members if member[2] == age]
    if disease:
        filtered_members = [member for member in filtered_members if member[3] == disease]
    if breed:
        filtered_members = [member for member in filtered_members if member[4] == breed]
    if other:
        filtered_members = [member for member in filtered_members if member[5] == other]

    return filtered_members

museum_goods_data = [
    ["반가사유상 미니어처","장식품",65000,"국립중앙박물관 특화상품입니다.",23],
    ["반가사유상 유선노트","노트",5000,"반가사유상 캐릭터가 그려진 노트입니다.",13],
    ["청화문 편지봉투","봉투",2000,"현금봉투로도 사용하기 좋은 편지봉투입니다.",123],
    ["의궤 마스킹테이프","테이프",6000,"의궤 가마 행렬 이미지로 만들어졌습니다.",93],
    ["토우 자개 스티커","스티커",15000,"천연자개가 들어간 스티커입니다.",83]
]

@app.get("/MuseumGoods")
def filter_museum_goods(
    name: str = Query(None, description="상품명"),
    type: str = Query(..., description="상품종류"),
    min_price: int = Query(None, gt=0, description="최소 가격"),
    max_price: int = Query(None, gt=0, description="최대 가격"),
    desc: str = Query(None, description="설명"),
):
    filtered_goods = museum_goods_data

    if name:
        filtered_goods = [goods for goods in filtered_goods if name in goods[0]]
    filtered_goods = [goods for goods in filtered_goods if goods[1] == type]
    if min_price:
        filtered_goods = [goods for goods in filtered_goods if goods[2] >= min_price]
    if max_price:
        filtered_goods = [goods for goods in filtered_goods if goods[2] <= max_price]
    if desc:
        filtered_goods = [goods for goods in filtered_goods if goods[3] == desc]

    return filtered_goods

photo_print_data = [
    ["일반사진","3x5","무광",1900,"사진앨범","소형 사진에 적합한 상품입니다."],
    ["증명사진","4x6","유광",2000,"증명사진용 키링","증명사진에 적합한 상품입니다."],
    ["일반사진","11x14","무광",5600,"아크릴액자","아크릴액자를 추가할 수 있는 상품입니다."],
    ["대형사진","12x17","유광",10900,"대형액자","대형 가족사진이나 웨딩사진에 적합한 상품입니다."],
    ["포스터","A4","유광",7900,"포스터용 테이프","포스터 제작에 적합한 상품입니다."]
]

@app.get("/PhotoPrint")
def filter_photo_print(
    type: str = Query(..., description="상품종류"),
    size: str = Query(None, description="사진크기"),
    coating: str = Query(None, description="코팅종류"),
    min_price: int = Query(None, gt=0, description="최소 가격"),
    max_price: int = Query(None, gt=0, description="최대 가격"),
):
    filtered_prints = photo_print_data

    filtered_prints = [print for print in filtered_prints if print[0] == type]
    if size:
        filtered_prints = [print for print in filtered_prints if print[1] == size]
    if coating:
        filtered_prints = [print for print in filtered_prints if print[2] == coating]
    if min_price:
        filtered_prints = [print for print in filtered_prints if print[3] >= min_price]
    if max_price:
        filtered_prints = [print for print in filtered_prints if print[3] <= max_price]

    return filtered_prints

tshirt_print_data = [
    ["일반 티셔츠","화이트","XS",19500,"기본적인 화이트 티셔츠입니다."],
    ["일반 티셔츠","블랙","XL",20500,"색이 진한 블랙 티셔츠입니다."],
    ["유기농면 티셔츠","아이보리","S",29900,"유기농 면화를 사용한 프리미엄 티셔츠입니다."],
    ["스포츠 티셔츠","레드","L",31000,"땀 흡수에 최적화된 스포츠 원단으로 만들어졌습니다."],
    ["오버사이즈 티셔츠","화이트","M",22000,"팔 길이가 긴 오버사이즈 티셔츠입니다."]
]

@app.get("/T-ShirtPrint")
def filter_tshirt_print(
    type: str = Query(..., description="상품종류"),
    color: str = Query(None, description="색상"),
    size: str = Query(None, description="크기"),
    min_price: int = Query(None, gt=0, description="최소 가격"),
    max_price: int = Query(None, gt=0, description="최대 가격"),
):
    filtered_tshirts = tshirt_print_data

    filtered_tshirts = [tshirt for tshirt in filtered_tshirts if tshirt[0] == type]
    if color:
        filtered_tshirts = [tshirt for tshirt in filtered_tshirts if tshirt[1] == color]
    if size:
        filtered_tshirts = [tshirt for tshirt in filtered_tshirts if tshirt[2] == size]
    if min_price:
        filtered_tshirts = [tshirt for tshirt in filtered_tshirts if tshirt[3] >= min_price]
    if max_price:
        filtered_tshirts = [tshirt for tshirt in filtered_tshirts if tshirt[3] <= max_price]

    return filtered_tshirts

coriander_food_data = [
    ["쏨땀","태국",["그린파파야","마늘","피시소스","라임즙"],"신맛","그린파파야향기로","서울특별시 관악구 봉천동 남부순환로234길 27"],
    ["가상냉채","중국",["포두부","마늘","흑초","당근","양파","오이"],"신맛","소백양샤브샤브","서울특별시 동작구 사당동 동작대로29길 8"],
    ["실란트로라임쉬림프샐러드","멕시코",["새우","아보카도","검은콩","라임즙"],"신맛","비아메렝게","서울시 서초구 방배로 42길 29"],
    ["고수케이크","한국",["자몽","생크림","제누아즈 시트","라임"],"단맛","원형들","서울특별시 중구 창경궁로1길 38"],
    ["똠얌꿍","태국",["새우","마늘","피시소스","라임즙","레몬그라스"],"신맛","쏨타이","서울특별시 강남구 테헤란로39길 51"]
]

@app.get("/Corianderfood")
def filter_coriander_food(
    food_name: str = Query(None, description="음식이름"),
    country: str = Query(None, description="국가"),
    stuff: str = Query(..., description="재료"),
    taste: str = Query(None, description="맛"),
    r_name: str = Query(None, description="음식점명"),
):
    filtered_foods = coriander_food_data

    if food_name:
        filtered_foods = [food for food in filtered_foods if food[0] == food_name]
    if country:
        filtered_foods = [food for food in filtered_foods if food[1] == country]
    if stuff:
        filtered_foods = [food for food in filtered_foods if stuff in food[2]]
    if taste:
        filtered_foods = [food for food in filtered_foods if food[3] == taste]
    if r_name:
        filtered_foods = [food for food in filtered_foods if food[4] == r_name]

    return filtered_foods

banchan_store_data = [
    ["콩자반",["검은콩","양조간장","물엿","설탕"],4000,"국내산 검은콩으로 만든 콩자반입니다.",43,False],
    ["두부계란부침",["두부","계란","쪽파","밀가루"],3500,"국내산 콩으로 만든 두부를 사용해서 맛이 좋습니다.",23,True],
    ["애호박전",["애호박","부침가루","계란","홍고추"],4000,"홍고추로 보양을 낸 제철 애호박전",41,False],
    ["계란장조림",["계란","양조간장","마늘","양파"],3000,"반숙계란장조림으로 맛이 좋습니다.",23,True],
    ["숙주나물",["숙주","마늘","소금","참깨"],2000,"숙주를 맛있게 무쳤습니다.",13,False]
]

@app.get("/BanchanStore")
def filter_banchan_store(
    food_name: str = Query(..., description="음식이름"),
    stuff: str = Query(None, description="재료"),
    min_price: int = Query(None, ge=0, description="최소 가격"),
    max_price: int = Query(None, ge=0, description="최대 가격"),
    desc: str = Query(None, description="설명"),
    discount: bool = Query(None, description="할인여부"),
):
    filtered_menu = banchan_store_data

    filtered_menu = [menu for menu in filtered_menu if menu[0] == food_name]
    if stuff:
        filtered_menu = [menu for menu in filtered_menu if stuff in menu[1]]
    if min_price is not None:
        filtered_menu = [menu for menu in filtered_menu if menu[2] >= min_price]
    if max_price is not None:
        filtered_menu = [menu for menu in filtered_menu if menu[2] <= max_price]
    if desc:
        filtered_menu = [menu for menu in filtered_menu if menu[3] == desc]
    if discount is not None:
        filtered_menu = [menu for menu in filtered_menu if menu[5] == discount]

    return filtered_menu

diary_note_data = [
    ["버섯위클리",6000,"일러스트",True,6,"백색모조지 100g"],
    ["투두 플레이 다이어리",16000,"포토",False,13,"백색모조지 120g"],
    ["에코 플래너",36000,"심플",True,13,"재생지 120g"],
    ["라이프 가드너",26000,"패턴",False,12,"백색모조지 100g"],
    ["쿨 타임 위클리",16000,"심플",True,6,"백색모조지 120g"]
]

@app.get("/DiaryNote")
def filter_diary_note(
    name: str = Query(None, description="상품명"),
    min_price: int = Query(None, ge=0, description="최소 가격"),
    max_price: int = Query(None, ge=0, description="최대 가격"),
    design: str = Query(..., description="디자인컨셉"),
    perpetual_diary: bool = Query(None, description="만년다이어리 여부"),
):
    filtered_products = diary_note_data

    if name:
        filtered_products = [product for product in filtered_products if product[0] == name]
    if min_price is not None:
        filtered_products = [product for product in filtered_products if product[1] >= min_price]
    if max_price is not None:
        filtered_products = [product for product in filtered_products if product[1] <= max_price]
    filtered_products = [product for product in filtered_products if product[2] == design]
    if perpetual_diary is not None:
        filtered_products = [product for product in filtered_products if product[3] == perpetual_diary]

    return filtered_products

vintage_store_data = [
    ["잼머","이윤희","서울시 마포구 연남로 43-2","월요일","식기와 커트러리 전문","10:00~20:00"],
    ["빈티지 이비","이선화","서울시 마포구 연남동 390-56","월, 화, 수","빈티지 의류 다수, 러블리한 취향","11:00~20:00"],
    ["봉황가게","김지영","서울시 관악구 인헌로 43-12","월요일","한국 빈티지 취급","10:00~20:00"],
    ["알멘드로이","윤나영","제주시 탑동로2길 3","월요일","빈티지 악세사리 취급","09:00~20:00"],
    ["디앤케이","김상혁","제주시 한림읍 명랑로 8","화, 수","생활용품과 가구","10:00~20:00"]
]

@app.get("/VintageStore")
def filter_vintage_store(
    s_name: str = Query(None, description="상점명"),
    o_name: str = Query(None, description="대표자명"),
    location: str = Query(..., description="지역"),
    dayoff: str = Query(None, description="휴무일"),
):
    filtered_stores = vintage_store_data

    if s_name:
        filtered_stores = [store for store in filtered_stores if store[0] == s_name]
    if o_name:
        filtered_stores = [store for store in filtered_stores if store[1] == o_name]
    filtered_stores = [store for store in filtered_stores if location in store[2] ]
    if dayoff:
        filtered_stores = [store for store in filtered_stores if store[3] == dayoff]

    return filtered_stores

plant_food_data = [
    ["타이포넥스","과립형","초기성장용","식물성 아미노산",11000,"500g","제품 뒷면 표를 참고하여 물에 희석하여 관수"],
    ["탑플랜트-311","과립형","성장용","질소, 인산, 칼륨",10000,"1kg","아침이나 저녁에 제품을 희석하여 엽면시비"],
    ["특다마","액상형","후기용","질소, 인산, 칼륨, 식물성 아미노산",20000,"500ml","양파 전용 비료, 제품 뒷면 표를 참고하여 물에 희석하여 관수"],
    ["결구탄","과립형","후기용","식물성 아미노산",11000,"500g","배추 전용. 희석 후 엽면 시비"],
    ["뿌리나라골드","액상형","뿌리발근용","붕소, 몰리브덴, 질소, 인산, 칼륨",9000,"300ml","발근이 필요한 식물체 줄기 침지법 실시"]
]

@app.get("/PlantFood")
def filter_plant_food(
    name: str = Query(None, description="상품명"),
    formula: str = Query(None, description="제형"),
    function: str = Query(..., description="용도"),
    component: str = Query(None, description="주성분"),
    min_price: float = Query(None, ge=0, description="최소 가격"),
    max_price: float = Query(None, ge=0, description="최대 가격"),
):
    filtered_foods = plant_food_data

    if name:
        filtered_foods = [food for food in filtered_foods if food[0] == name]
    if formula:
        filtered_foods = [food for food in filtered_foods if food[1] == formula]
    filtered_foods = [food for food in filtered_foods if food[2] == function]
    if component:
        filtered_foods = [food for food in filtered_foods if food[3] == component]
    if min_price:
        filtered_foods = [food for food in filtered_foods if food[4] >= min_price]
    if max_price:
        filtered_foods = [food for food in filtered_foods if food[4] <= max_price]

    return filtered_foods

coin_laundry_data = [
    ["코인워시24","서울특별시 동작구 노량진로6길 46",4000,True,"생활용품판매","02-000-0000","24시간"],
    ["워시엔조이","서울특별시 중구 회현동 121-4",3000,True,"무인카페","02-000-0001","24시간"],
    ["빨래터","서울특별시 관악구 청룡동 청룡10길 18",5000,True,"식료품판매","02-000-0002","07:00~23:00"],
    ["코인세탁365","서울특별시 용산구 이촌로18길 21",3000,False,"없음","02-000-0003","24시간"],
    ["코인크린","서울특별시 중구 동호로8길 5",4000,True,"운동화전용 세탁기기 구비","02-000-0004","07:00~22:00"]
]

@app.get("/CoinLaundry")
def filter_coin_laundry(
    name: str = Query(None, description="이름"),
    location: str = Query(..., description="지역"),
    min_price: float = Query(None, ge=0, description="최소 가격"),
    max_price: float = Query(None, ge=0, description="최대 가격"),
    wash_b: bool = Query(None, description="이불빨래 가능여부"),
    etc: str = Query(None, description="기타시설"),
):
    filtered_laundries = coin_laundry_data

    if name:
        filtered_laundries = [laundry for laundry in filtered_laundries if laundry[0] == name]
    filtered_laundries = [laundry for laundry in filtered_laundries if location in laundry[1]]
    if min_price:
        filtered_laundries = [laundry for laundry in filtered_laundries if laundry[2] >= min_price]
    if max_price:
        filtered_laundries = [laundry for laundry in filtered_laundries if laundry[2] <= max_price]
    if wash_b is not None:
        filtered_laundries = [laundry for laundry in filtered_laundries if laundry[3] == wash_b]
    if etc:
        filtered_laundries = [laundry for laundry in filtered_laundries if laundry[4] == etc]

    return filtered_laundries

kimbap_data = [
    ["바른키토김밥",4500,["계란지단","미나리","우엉","당근"],False,"저탄고지 기본 키토김밥"],
    ["베이컨키토김밥",5500,["계란지단","베이컨"],False,"국내산 베이컨이 들어간 키토김밥"],
    ["트리플치즈키토김밥",5200,["계란지단","체다치즈","까망베르치즈","크림치즈","우엉","당근"],False,"세 종류의 치즈가 들어간 키토김밥"],
    ["참치와사비키토김밥",6500,["계란지단","캔참치","와사비","당근"],False,"맵싸한 키토김밥"],
    ["바른현미김밥",4000,["현미밥","미나리","우엉","당근"],True,"현미밥을 사용한 건강한 김밥"]
]

@app.get("/KetogenicKimbap")
def filter_ketogenic_kimbap(
    name: str = Query(None, description="메뉴이름"),
    min_price: float = Query(None, ge=0, description="최소 가격"),
    max_price: float = Query(None, ge=0, description="최대 가격"),
    stuff: str = Query(..., description="재료"),
    rice: bool = Query(None, description="밥 유무"),
):
    filtered_kimbap = kimbap_data

    if name:
        filtered_kimbap = [k for k in filtered_kimbap if k[0] == name]
    if min_price:
        filtered_kimbap = [k for k in filtered_kimbap if k[1] >= min_price]
    if max_price:
        filtered_kimbap = [k for k in filtered_kimbap if k[1] <= max_price]
    filtered_kimbap = [k for k in filtered_kimbap if stuff in k[2]]
    if rice is not None:
        filtered_kimbap = [k for k in filtered_kimbap if k[3] == rice]

    return filtered_kimbap

veggie_data = [
    ["감자","뿌리채소",[3,4],2,False,"씨감자를 3월 하순에서 4월 상순까지 심는다. 관수에 주의한다."],
    ["완두","열매채소",[3,4],1,True,"모종 이식 후 지지대가 필요하다. 껍질완두의 경우에는 조금 더 빨리 수확한다."],
    ["무","뿌리채소",[8,9],3,False,"더운 시기에는 차광하여 키운다."],
    ["갓","잎채소",[8,9,10],2,True,"재배 간격에 주의하여 키운다."],
    ["시금치","잎채소",[9,10,11],2,False,"월동 시금치의 경우 중부 지역에서는 보온이 필요하다."]
]

@app.get("/VegetableGardenSeeding")
def filter_vegetable_garden_seeding(
    name: str = Query(..., description="이름"),
    category: str = Query(None, description="분류"),
    seeding_month: int = Query(None, description="파종시기"),
    degree_g: int = Query(None, ge=0, le=5, description="재배난이도"),
    young_plant: bool = Query(None, description="모종이식추천여부"),
):
    filtered_veggies = veggie_data

    if name:
        filtered_veggies = [v for v in filtered_veggies if v[0] == name]
    if category:
        filtered_veggies = [v for v in filtered_veggies if v[1] == category]
    if seeding_month:
        filtered_veggies = [v for v in filtered_veggies if seeding_month in v[2]]
    if degree_g:
        filtered_veggies = [v for v in filtered_veggies if v[3] == degree_g]
    if young_plant is not None:
        filtered_veggies = [v for v in filtered_veggies if v[4] == young_plant]

    return filtered_veggies

hanbok_data = [
    ["가온네","서울시 마포구 연남로 43-2",["혼주한복","남성한복","여성한복","아동한복"],"혼주한복 전문 샵입니다. 악세사리 대여 가능합니다.",4.5,"친절해요"],
    ["주단을깔고","서울시 마포구 연남동 390-56",["혼주한복","남성한복","여성한복","아동한복"],"웨딩 전문 샵입니다.",4.4,"가격이 높아요"],
    ["팔랑","서울시 관악구 인헌로 43-12",["공연의상","여성한복","남성한복"],"공연과 촬영의상 전문 샵입니다. 악세사리 대여 가능합니다.",4.8,"옷이 좋아요"],
    ["희영네","제주시 탑동로2길 3",["남성한복","여성한복","아동한복"],"돌잔치용 특화 샵.",4.2,"반납과정이 불편해요"],
    ["고궁의뜰","제주시 한림읍 명랑로 8",["남성한복","여성한복","전통한복"],"전통한복을 만들고 대여하는 샵.",4.2,"사이즈가 다양하지 않아요"]
]

@app.get("/HanbokRentalShop")
def filter_hanbok_rental_shop(
    shop_name: str = Query(None, description="상점명"),
    location: str = Query(..., description="지역"),
    category: str = Query(None, description="취급품목"),
    rating: float = Query(None, ge=0.0, le=5.0, description="최소평점"),
    desc: str = Query(None, description="설명"),
):
    filtered_hanbok = hanbok_data

    if shop_name:
        filtered_hanbok = [h for h in filtered_hanbok if h[0] == shop_name]
    if location:
        filtered_hanbok = [h for h in filtered_hanbok if location in h[1] ]
    if category:
        filtered_hanbok = [h for h in filtered_hanbok if category in h[2]]
    if rating:
        filtered_hanbok = [h for h in filtered_hanbok if h[4] >= rating]
    if desc:
        filtered_hanbok = [h for h in filtered_hanbok if h[5] == desc]

    return filtered_hanbok

hanbok_rental_data = [
    ["파란마음","파랑",["S","M"],90000,True,"버선"],
    ["초록물결","초록",["L","M"],100000,True,"비녀, 버선"],
    ["성균관","흰색",["S","M","L"],120000,False,"버선"],
    ["꼬까옷","노랑",["S","M"],80000,True,"버선, 허리띠"],
    ["진달래","분홍",["S","M"],70000,False,"버선"]
]

@app.get("/HanbokRentalList")
def filter_hanbok_rental_list(
    name: str = Query(None, description="상품명"),
    color: str = Query(..., description="색상"),
    size: str = Query(None, description="사이즈"),
    min_price: int = Query(None, ge=0, description="최소 가격"),
    max_price: int = Query(None, ge=0, description="최대 가격"),
    available: bool = Query(None, description="대여가능여부"),
):
    filtered_hanbok = hanbok_rental_data

    if name:
        filtered_hanbok = [h for h in filtered_hanbok if h[0] == name]
    if color:
        filtered_hanbok = [h for h in filtered_hanbok if h[1] == color]
    if size:
        filtered_hanbok = [h for h in filtered_hanbok if size in h[2]]
    if min_price is not None:
        filtered_hanbok = [h for h in filtered_hanbok if h[3] >= min_price]
    if max_price is not None:
        filtered_hanbok = [h for h in filtered_hanbok if h[3] <= max_price]
    if available is not None:
        filtered_hanbok = [h for h in filtered_hanbok if h[4] == available]

    return filtered_hanbok

woodworker_class_data = [
    ["요리조리 초보클래스","도마 제작","인천문화회관",50000,"2023-08-21",True,"우드카빙 도마를 만들고 관리하는 방법을 배웁니다."],
    ["귀여움이 가득한","목각인형 제작","구월산회관",80000,"2023-06-21",True,"수공구로 만드는 목각인형."],
    ["창업준비클래스","목공방 창업 수업","기린문화원",150000,"2023-09-21",True,"목공방 창업을 위한 노하우 클래스."],
    ["전통 소목장","소반 제작","대전문화회관",200000,"2023-08-21",False,"전통 방법으로 소반을 만듭니다."],
    ["원목가구와 짜임","서랍장 제작","청년청",250000,"2023-07-21",True,"중형 목가구와 짜임 수업입니다."]
]

@app.get("/WoodworkerClass")
def filter_woodworker_class(
    name: str = Query(None, description="강좌명"),
    contents: str = Query(..., description="내용"),
    location: str = Query(None, description="장소"),
    min_price: int = Query(None, ge=0, description="최소 가격"),
    max_price: int = Query(None, ge=0, description="최대 가격"),
    date: str = Query(None, description="강연일"),
    available: bool = Query(None, description="예약가능여부"),
):
    filtered_classes = woodworker_class_data

    if name:
        filtered_classes = [c for c in filtered_classes if c[0] == name]
    if contents:
        filtered_classes = [c for c in filtered_classes if c[1] == contents]
    if location:
        filtered_classes = [c for c in filtered_classes if c[2] == location]
    if min_price is not None:
        filtered_classes = [c for c in filtered_classes if c[3] >= min_price]
    if max_price is not None:
        filtered_classes = [c for c in filtered_classes if c[3] <= max_price]
    if date:
        filtered_classes = [c for c in filtered_classes if c[4] == date]
    if available is not None:
        filtered_classes = [c for c in filtered_classes if c[5] == available]

    return filtered_classes


book_funding_data = [
    ["갈라테이아","매들린 밀러",23000,"2023-07-31",True,"<키르케>의 저자가 전하는 오비디우스 <변신 이야기> 속 이야기."],
    ["명탐정의 제물","시라이 도모유키",19000,"2023-06-31",True,"미스터리 대상 수상."],
    ["나의 이상한 신발짝","김유인",21000,"2023-09-31",False,"어른을 위한 그림 동화."],
    ["연필의 모든 것","최연진",21000,"2023-07-12",True,"연필전문점을 운영하는 작가의 연필 도감"],
    ["설계의 슬픔","홍수인",25000,"2023-07-22",False,"건축가의 에세이."]
]

@app.get("/BookFunding")
def filter_book_funding(
    b_name: str = Query(None, description="도서명"),
    a_name: str = Query(..., description="저자명"),
    min_price: int = Query(None, ge=0, description="최소 가격"),
    max_price: int = Query(None, ge=0, description="최대 가격"),
    date: str = Query(None, description="펀딩 마감일"),
    desc: str = Query(None, description="설명 (도서 홍보 설명 등)"),
):
    filtered_fundings = book_funding_data

    if b_name:
        filtered_fundings = [f for f in filtered_fundings if f[0] == b_name]
    if a_name:
        filtered_fundings = [f for f in filtered_fundings if f[1] == a_name]
    if min_price is not None:
        filtered_fundings = [f for f in filtered_fundings if f[2] >= min_price]
    if max_price is not None:
        filtered_fundings = [f for f in filtered_fundings if f[2] <= max_price]
    if date:
        filtered_fundings = [f for f in filtered_fundings if f[3] == date]
    if desc:
        filtered_fundings = [f for f in filtered_fundings if desc in f[5]]

    return filtered_fundings

catering_services_data = [
    ["저스틴파티","핑거푸드",["서울시","인천시","경기도"],300000,"010-0000-0000",True,"비건 음식으로도 주문 가능합니다"],
    ["에블린이벤트","샌드위치",["강원도"],320000,"010-0000-0000",True,"샌드위치와 샐러드, 생과일 주스 전문"],
    ["일화당","한식, 중식",["서울시","인천시","경기도"],250000,"010-0000-0000",False,"호텔 조리장의 실력을 보여드립니다"],
    ["칠리페퍼","양식",["제주도"],380000,"010-0000-0000",True,"매콤한 양식 전문"],
    ["오늘의파티","디저트",["세종시","대전시"],400000,"010-0000-0000",True,"디저트 케이터링 전문"]
]

@app.get("/CateringServies")
def filter_catering_services(
    name: str = Query(None, description="업체명"),
    category: str = Query(..., description="음식종류 (예: 핑거푸드, 한식, 중식 등)"),
    location: str = Query(None, description="이용가능지역 (예: 서울시, 인천시, 경기도 등)"),
    min_price: int = Query(None, ge=0, description="최소 가격"),
    max_price: int = Query(None, ge=0, description="최대 가격"),
    available: bool = Query(None, description="예약가능여부"),
):
    filtered_services = catering_services_data

    if name:
        filtered_services = [s for s in filtered_services if s[0] == name]
    if category:
        filtered_services = [s for s in filtered_services if s[1] == category]
    if location:
        filtered_services = [s for s in filtered_services if location in s[2]]
    if min_price is not None:
        filtered_services = [s for s in filtered_services if s[3] >= min_price]
    if max_price is not None:
        filtered_services = [s for s in filtered_services if s[3] <= max_price]
    if available is not None:
        filtered_services = [s for s in filtered_services if s[5] == available]

    return filtered_services

catering_customer_list_data = [
    ["김희연","스테이크","지현문학상 시상식","2023-08-25",520000,True,"없음"],
    ["이상현","샌드위치","촬영회","2023-07-25",420000,True,"땅콩알러지"],
    ["박상훈","한식","한몽 교류 초청회","2023-08-25",720000,True,"없음"],
    ["김희지","디저트","폴댄스 발표회","2023-09-25",550000,False,"유당불내증"],
    ["이윤화","샐러드","마포 서점 연합회","2023-08-25",520000,True,"없음"]
]

@app.get("/CateringCustomerList")
def filter_catering_customer_list(
    name: str = Query(..., description="예약자명"),
    menu: str = Query(None, description="선택메뉴 (예: 한식, 디저트, 샐러드 등)"),
    party_name: str = Query(None, description="행사명"),
    date: str = Query(None, description="예약일"),
    pay: bool = Query(None, description="입금여부"),
    allergy: str = Query(None, description="알러지정보"),
):
    filtered_list = catering_customer_list_data

    if name:
        filtered_list = [l for l in filtered_list if l[0] == name]
    if menu:
        filtered_list = [l for l in filtered_list if l[1] == menu]
    if party_name:
        filtered_list = [l for l in filtered_list if l[2] == party_name]
    if date:
        filtered_list = [l for l in filtered_list if l[3] == date]
    if pay is not None:
        filtered_list = [l for l in filtered_list if l[5] == pay]
    if allergy:
        filtered_list = [l for l in filtered_list if l[6] == allergy]

    return filtered_list

@app.get("/NatureEducation")
async def filter_nature_education(
    name: str = Query(None, description="교육이름"),
    contents: List[str] = Query(None, description="내용", min_length=1),
    location: str = Query(None, description="장소 (예: 백련산, 인왕계곡 등)"),
    min_price: float = Query(None, description="최소 가격", ge=0),
    max_price: float = Query(None, description="최대 가격", ge=0),
    age: str = Query(None, description="교육대상연령 (예: 유아, 초등, 가족 등)"),
    available: bool = Query(None, description="예약가능여부"),
):
    # 자연체험교육 정보 데이터
    nature_educations = [
        {"name": "건강숲", "contents": ["산행", "체조"], "location": "백련산", "price": 40000, "age": "65세 이상", "available": True, "tal": "010-0000-0000"},
        {"name": "노르딕워킹", "contents": ["산행", "걷기코칭"], "location": "백련산", "price": 60000, "age": "일반성인", "available": True, "tal": "010-0000-0000"},
        {"name": "양서류교실", "contents": ["숲해설", "물놀이"], "location": "인산계곡", "price": 30000, "age": "유아, 초등, 가족", "available": True, "tal": "010-0000-0000"},
        {"name": "숲속보물찾기", "contents": ["숲해설", "자연탐방"], "location": "인왕어린이공원", "price": 20000, "age": "초등", "available": False, "tal": "010-0000-0000"},
        {"name": "매미탐험", "contents": ["숲해설", "매미관찰"], "location": "백련산", "price": 40000, "age": "초등, 가족", "available": True, "tal": "010-0000-0000"},
    ]

    filtered_nature_educations = []

    for edu in nature_educations:
        if (
            (edu["name"] == name if name else True) and
            (all(content in edu["contents"] for content in contents) if contents else True) and
            (edu["location"] == location if location else True) and
            (edu["price"] is None or (edu["price"] >= min_price if min_price else True)) and
            (edu["price"] is None or (edu["price"] <= max_price if max_price else True)) and
            (edu["age"] == age if age else True) and
            (edu["available"] == available if available is not None else True)
        ):
            filtered_nature_educations.append(edu)

    return filtered_nature_educations

birds_of_korea_data = [
    ["청둥오리","Anas platyrhynchos","WV, Res","오리과",["하천","하구","저수지","호수","해안","농경지"],59],
    ["황조롱이","Falco tinnunculus","Res","매과",["숲","개활지","도시","농경지"],38.5],
    ["검은머리물떼새","Haematopus ostralegus","Res","검은머리물떼새과",["해안","하구","갯벌"],45],
    ["곤줄박이","Sittiparus varius","Res","박새과",["숲","공원","정원"],14],
    ["직박구리","Hypsipetes amaurotis","Res","직박구리과",["숲","공원","정원"],28]
]

@app.get("/BirdsOfKorea")
def filter_birds_of_korea(
    k_name: str = Query(None, description="한글이름"),
    s_name: str = Query(None, description="학명"),
    arrival_s: str = Query(None, description="도래현황 약자 (예: Res, WV 등)"),
    family_n: str = Query(None, description="과 (예: 오리과, 매과 등)"),
    habitat: str = Query(..., description="서식지 (예: 하천, 하구, 숲 등)"),
    min_length: float = Query(None, gt=0, description="최소 몸길이(cm)"),
    max_length: float = Query(None, gt=0, description="최대 몸길이(cm)"),
):
    filtered_list = birds_of_korea_data

    if k_name:
        filtered_list = [l for l in filtered_list if l[0] == k_name]
    if s_name:
        filtered_list = [l for l in filtered_list if l[1] == s_name]
    if arrival_s:
        filtered_list = [l for l in filtered_list if l[2] == arrival_s]
    if family_n:
        filtered_list = [l for l in filtered_list if l[3] == family_n]
    if habitat:
        filtered_list = [l for l in filtered_list if habitat in l[4]]
    if min_length is not None:
        filtered_list = [l for l in filtered_list if l[5] >= min_length]
    if max_length is not None:
        filtered_list = [l for l in filtered_list if l[5] <= max_length]

    return filtered_list

birds_race_player_data = [
    ["이정혜","생물자원관","서울",46,True,"010-0000-0000","없음"],
    ["박혜진","개인","서울",26,True,"010-0000-0000","탐조 유튜버"],
    ["김정기","대구대","대구",22,True,"010-0000-0000","대학 연합 탐조 동아리"],
    ["장하연","개인","인천",36,False,"010-0000-0000","없음"],
    ["김승훈","네이쳐링","경기도",32,True,"010-0000-0000","없음"]
]

@app.get("/BirdsRacePlayer")
def filter_birds_race_player(
    name: str = Query(..., description="이름"),
    agency: str = Query(None, description="소속 (예: 생물자원관, 개인 등)"),
    location: str = Query(None, description="지역 (예: 서울, 대구, 인청 등)"),
    age: int = Query(None, description="나이"),
    pay: bool = Query(None, description="참가비입금여부"),
    tel: str = Query(None, description="연락처"),
):
    filtered_list = birds_race_player_data

    filtered_list = [l for l in filtered_list if l[0] == name]
    if agency:
        filtered_list = [l for l in filtered_list if l[1] == agency]
    if location:
        filtered_list = [l for l in filtered_list if l[2] == location]
    if age is not None:
        filtered_list = [l for l in filtered_list if l[3] == age]
    if pay is not None:
        filtered_list = [l for l in filtered_list if l[4] == pay]
    if tel:
        filtered_list = [l for l in filtered_list if l[5] == tel]

    return filtered_list

small_local_club_data = [
    ["SF독서자들","이승인","서울시 관악구","SF소설을 읽는 독서모임입니다.","2023-07-09",10000,"010-0000-0000","2주에 1번씩 모임이 진행됩니다."],
    ["마포구 농구모임","김혜인","서울시 마포구","농구 모임입니다. 초보자 환영합니다","2023-07-09",10000,"010-0000-0000","1주에 1번씩 모임이 진행됩니다."],
    ["커피를 배워요","정해나","서울시 종로구","바리스타 자격증 취득 모임","2023-07-10",30000,"010-0000-0000","1달에 1번 모임이 있고 오픈 카톡을 운영합니다."],
    ["진도친구들","박민아","서울시 중랑구","진도, 진도믹스를 키우는 견주 모임.","2023-07-09",10000,"010-0000-0000","매주 1번씩 중랑구 애견 놀이터에서 모입니다"],
    ["양천구 마작회","홍유정","서울시 양천구","마작을 배우며 함께 합니다.","2023-07-29",20000,"010-0000-0000","2주에 1번씩 모임이 진행됩니다."]
]

@app.get("/SmallLocalClub")
def filter_small_local_club(
    c_name: str = Query(None, description="모임명"),
    l_name: str = Query(None, description="대표자명"),
    location: str = Query(None, description="지역 (예: 서울특별시, 관악구, 마포구 등)"),
    contents: str = Query(..., description="활동내용"),
    date: str = Query(None, description="모임날짜"),
    min_price: int = Query(None, description="최소 가격"),
    max_price: int = Query(None, description="최대 가격"),
):
    filtered_list = small_local_club_data

    if c_name:
        filtered_list = [l for l in filtered_list if l[0] == c_name]
    if l_name:
        filtered_list = [l for l in filtered_list if l[1] == l_name]
    if location:
        filtered_list = [l for l in filtered_list if l[2] == location]
    if date:
        filtered_list = [l for l in filtered_list if l[4] == date]
    if min_price is not None:
        filtered_list = [l for l in filtered_list if l[5] >= min_price]
    if max_price is not None:
        filtered_list = [l for l in filtered_list if l[5] <= max_price]

    return filtered_list

@app.get("/ShampooSearch")
async def filter_shampoo_search(
    name: str = Query(None, description="제품명"),
    effect: List[str] = Query(..., description="기능키워드 (예: 비듬, 모근 등)", min_length=1),
    aroma: str = Query(None, description="향 (예: 코튼, 플로럴 등)"),
    min_price: float = Query(None, description="최소 가격", ge=0),
    max_price: float = Query(None, description="최대 가격", ge=0),
    size: float = Query(None, description="용량(ml)"),
    component: str = Query(None, description="성분 (예: 프로폴리스, 아르간 오일 등)"),
):
    # 샴푸 정보 데이터
    shampoos = [
        {"name": "두피스파 샴푸", "effect": ["비듬", "두피"], "aroma": "멘솔", "price": 12400, "size": 750, "component": "소듐라우레스설페이트", "desc": "시원한 쿨링감"},
        {"name": "모이스처 10 샴푸", "effect": ["두피", "모발", "건조"], "aroma": "코튼", "price": 15400, "size": 680, "component": "소듐라우레스설페이트", "desc": "촉촉함이 그대로 남는"},
        {"name": "자윤 모근강화 샴푸", "effect": ["모근", "지성", "두피"], "aroma": "한약재", "price": 17800, "size": 950, "component": "소듐라우레스설페이트", "desc": "한방 성분으로 모근을 더 건강하게"},
        {"name": "마이크로바이옴 효모 샴푸", "effect": ["두피", "가려움"], "aroma": "플로럴", "price": 29000, "size": 400, "component": "프로폴리스 추출물", "desc": "두피 장벽 개선"},
        {"name": "펩타이드 고영양 샴푸", "effect": ["손상모"], "aroma": "코코넛", "price": 19400, "size": 850, "component": "아르간 오일", "desc": "찰랑찰랑한 머릿결로 회복"},
    ]

    filtered_shampoos = []

    for shampoo in shampoos:
        if (
            (shampoo["name"] == name if name else True) and
            (all(keyword in shampoo["effect"] for keyword in effect)) and
            (shampoo["aroma"] == aroma if aroma else True) and
            (shampoo["price"] is None or (shampoo["price"] >= min_price if min_price else True)) and
            (shampoo["price"] is None or (shampoo["price"] <= max_price if max_price else True)) and
            (shampoo["size"] == size if size else True) and
            (shampoo["component"] == component if component else True)
        ):
            filtered_shampoos.append(shampoo)

    return filtered_shampoos

@app.get("/BouquetSearch")
async def filter_bouquet_search(
    name: str = Query(None, description="제품명"),
    f_name: str = Query(None, description="플로리스트 이름"),
    location: str = Query(..., description="지역 (예: 서울시, 인천시, 대전시 등)"),
    flower: str = Query(None, description="꽃종류 (예: 장미, 백합 등)"),
    color: str = Query(None, description="색상 (예: 분홍색, 흰색 등)"),
    min_price: float = Query(None, description="최소 가격", ge=0),
    max_price: float = Query(None, description="최대 가격", ge=0),
):
    # 꽃다발 정보 데이터
    bouquets = [
        {"name": "겨울의신부", "f_name": "이선화", "location": "서울시", "flower": "은방울꽃", "color": "흰색", "price": 250000, "tel": "010-0000-0000"},
        {"name": "트로피컬무드", "f_name": "이지현", "location": "인천시", "flower": "카라", "color": "주황색", "price": 200000, "tel": "010-0000-0000"},
        {"name": "5월의 특혜", "f_name": "김승혜", "location": "대전시", "flower": "작약", "color": "분홍색", "price": 230000, "tel": "010-0000-0000"},
        {"name": "붉은약속", "f_name": "박수현", "location": "부산시", "flower": "장미", "color": "빨간색", "price": 150000, "tel": "010-0000-0000"},
        {"name": "보라색 꿈", "f_name": "유혜진", "location": "세종시", "flower": "반다", "color": "보라색", "price": 200000, "tel": "010-0000-0000"},
    ]

    filtered_bouquets = []

    for bouquet in bouquets:
        if (
            (bouquet["name"] == name if name else True) and
            (bouquet["f_name"] == f_name if f_name else True) and
            (bouquet["location"] == location) and
            (bouquet["flower"] == flower if flower else True) and
            (bouquet["color"] == color if color else True) and
            (bouquet["price"] is None or (bouquet["price"] >= min_price if min_price else True)) and
            (bouquet["price"] is None or (bouquet["price"] <= max_price if max_price else True))
        ):
            filtered_bouquets.append(bouquet)

    return filtered_bouquets

fizzwater_data = [
    ["빅토리아","국내산",2000,500,"플레인","페트병"],
    ["일화초정탄산수","국내산",1700,350,"레몬","페트병"],
    ["씨그램","국내산",1400,350,"라임","페트병"],
    ["산펠레그리노","이탈리아",2400,500,"플레인","유리병"],
    ["싱하","태국",1300,325,"플레인","유리병"]
]

@app.get("/FizzWater")
def filter_fizzwater(
    name: str = Query(None, description="상품명"),
    origin: str = Query(None, description="원산지"),
    min_price: int = Query(None, description="최소가격"),
    max_price: int = Query(None, description="최대가격"),
    min_amount: int = Query(None, description="최소용량(ml)"),
    max_amount: int = Query(None, description="최대용량(ml)"),
    flavor: str = Query(..., description="맛 (예: 플레인, 라임 등)"),
    package: str = Query(None, description="포장종류 (예: 유리병, 페트병 등)"),
):
    filtered_list = fizzwater_data

    if name:
        filtered_list = [fw for fw in filtered_list if fw[0] == name]
    if origin:
        filtered_list = [fw for fw in filtered_list if fw[1] == origin]
    if min_price is not None:
        filtered_list = [fw for fw in filtered_list if fw[2] >= min_price]
    if max_price is not None:
        filtered_list = [fw for fw in filtered_list if fw[2] <= max_price]
    if min_amount is not None:
        filtered_list = [fw for fw in filtered_list if fw[3] >= min_amount]
    if max_amount is not None:
        filtered_list = [fw for fw in filtered_list if fw[3] <= max_amount]
    if flavor:
        filtered_list = [fw for fw in filtered_list if fw[4] == flavor]
    if package:
        filtered_list = [fw for fw in filtered_list if fw[5] == package]

    return filtered_list

preorder_customer_data = [
    ["이윤희","서울시 마포구 연남로 43-2","씰스티커",23000,True,True,"없음"],
    ["이선화","서울시 마포구 연남동 390-56","접이식 테이블",43000,True,True,"배송메모: 전화 후 배송"],
    ["김지영","서울시 관악구 인헌로 43-12","돗자리세트",32000,True,False,"문의:핑크 색상 여부"],
    ["윤나영","제주시 탑동로2길 3","캠핑 테이블",93000,False,False,"없음"],
    ["김상혁","제주시 한림읍 명랑로 8","타프 스트랩",19000,False,False,"없음"]
]

@app.get("/PreOrderCustomer")
def filter_preorder_customer(
    name: str = Query(..., description="이름"),
    address: str = Query(None, description="주소 (예: 서울시, 관악구, 마포구 등)"),
    product: str = Query(None, description="주문상품"),
    pay: bool = Query(None, description="입금여부"),
    sending: bool = Query(None, description="발송여부"),
):
    filtered_list = preorder_customer_data

    if name:
        filtered_list = [pc for pc in filtered_list if pc[0] == name]
    if address:
        filtered_list = [pc for pc in filtered_list if pc[1] == address]
    if product:
        filtered_list = [pc for pc in filtered_list if pc[2] == product]
    if pay is not None:
        filtered_list = [pc for pc in filtered_list if pc[4] == pay]
    if sending is not None:
        filtered_list = [pc for pc in filtered_list if pc[5] == sending]

    return filtered_list

printshop_customer_data = [
    ["이윤희","서울시 마포구 연남로 43-2","씰스티커",23000,True,"발송완료","없음"],
    ["이선화","서울시 마포구 연남동 390-56","포토카드",43000,True,"인쇄완료","배송메모: 전화 후 배송"],
    ["김지영","서울시 관악구 인헌로 43-12","포스터",32000,True,"인쇄중","문의:배송일 지정"],
    ["윤나영","제주시 탑동로2길 3","현수막",93000,False,"입금대기","없음"],
    ["김상혁","제주시 한림읍 명랑로 8","사진",19000,False,"입금대기","없음"]
]

@app.get("/PrintShopCustomer")
def filter_printshop_customer(
    name: str = Query(..., description="이름"),
    address: str = Query(None, description="주소 (예: 서울시, 관악구, 마포구 등)"),
    product: str = Query(None, description="주문상품"),
    pay: bool = Query(None, description="입금여부"),
    progress: str = Query(None, description="인쇄진행상태 (예: 입금대기, 인쇄중, 인쇄완료)"),
):
    filtered_list = printshop_customer_data

    if name:
        filtered_list = [pc for pc in filtered_list if pc[0] == name]
    if address:
        filtered_list = [pc for pc in filtered_list if pc[1] == address]
    if product:
        filtered_list = [pc for pc in filtered_list if pc[2] == product]
    if pay is not None:
        filtered_list = [pc for pc in filtered_list if pc[4] == pay]
    if progress:
        filtered_list = [pc for pc in filtered_list if pc[5] == progress]

    return filtered_list

houseplant_data = [
    ["초보자","드라세나 마지나타","madagascar dragon tree","백합과","아프리카",False,"폭이 좁고 가는잎"],
    ["전문가","박쥐란","common staghorn fern","고사리과","호주",False,"사슴뿔 모양"],
    ["초보자","개운죽","Sander's dracaena","백합과","아프리카",True,"대나무를 닮았으나 대나무 아님"],
    ["초보자","치자나무","common gardenia","꼭두서니과","아시아",True,"향기가 매우 강함"],
    ["경험자","공작야자","Fish tail palm","야자과","인도네시아",True,"열매색이 빨강색"]
]

@app.get("/houseplant")
def filter_houseplant(
    level: str = Query(..., description="관리 수준 ex) 초보자, 경험자"),
    name: str = Query(None, description="식물 한글명"),
    EnglishName: str = Query(None, description="식물 영문명"),
    family: str = Query(None, description="식물의 과"),
    origin: str = Query(None, description="원산지"),
    toxicity: bool = Query(None, description="독성 유무"),
):
    filtered_list = houseplant_data

    if level:
        filtered_list = [hp for hp in filtered_list if hp[0] == level]
    if name:
        filtered_list = [hp for hp in filtered_list if hp[1] == name]
    if EnglishName:
        filtered_list = [hp for hp in filtered_list if hp[2] == EnglishName]
    if family:
        filtered_list = [hp for hp in filtered_list if hp[3] == family]
    if origin:
        filtered_list = [hp for hp in filtered_list if hp[4] == origin]
    if toxicity is not None:
        filtered_list = [hp for hp in filtered_list if hp[5] == toxicity]

    return filtered_list

dietsupplements_data = [
    ["정","버닝올로지",35000,"체지방 감량","1일 1포"],
    ["젤리","테라미인 여리한 스틱",30000,"체지방 감량","1일 1포"],
    ["분말","속편한 다이어트",50000,"체지방 감량","1일 1포"],
    ["정","콜레올로지컷",30000,"콜레스트롤 감소","1일 1회 2정"],
    ["환","변한 슬림핏",35000,"체지방 감량","1일 2포"]
]

@app.get("/dietsupplements")
def filter_dietsupplements(
    type: str = Query(..., description="제품 유형 ex) 정, 젤리, 분말, 환"),
    name: str = Query(None, description="상품명"),
    min_price: int = Query(None, ge=0, description="최소 가격"),
    max_price: int = Query(None, ge=0, description="최대 가격"),
    efficacy: str = Query(None, description="효능"),
):
    filtered_list = dietsupplements_data

    if type:
        filtered_list = [ds for ds in filtered_list if ds[0] == type]
    if name:
        filtered_list = [ds for ds in filtered_list if ds[1] == name]
    if min_price is not None:
        filtered_list = [ds for ds in filtered_list if ds[2] >= min_price]
    if max_price is not None:
        filtered_list = [ds for ds in filtered_list if ds[2] <= max_price]
    if efficacy:
        filtered_list = [ds for ds in filtered_list if ds[3] == efficacy]

    return filtered_list

largecafe_data = [
    ["카페드첼시","경기도 김포시 통진읍 옹정리 81-30",True,"매일 10:00-21:00","0507-1368-7780"],
    ["골든트리","경기도 가평군 가평읍 북한강변로 326-124",True,"평일 10:00-19:00 주말 10:00-20:00","0507-1388-9872"],
    ["그릿비","울산광역시 울주군 서생면 신암해안1길 4",False,"매일 10:00-21:00","0507-1475-7021"],
    ["메이드림","인천광역시 중구 용유서로 479번길 42",True,"매일 10:00-21:30","0507-1351-1904"],
    ["오랑주리","경기도 양주시 백석읍 기산로 423-19",False,"매일 11:00-21:00","0507-1326-0615"]
]

@app.get("/largecafe")
def filter_largecafe(
    cafeName: str = Query(None, description="카페 이름"),
    city: str = Query(None, description="광역시도"),
    district: str = Query(None, description="시군구"),
    town: str = Query(None, description="읍면동"),
    no_kids_zone: bool = Query(..., description="노키즈존 유무"),
):
    filtered_list = largecafe_data

    if cafeName:
        filtered_list = [cafe for cafe in filtered_list if cafe[0] == cafeName]
    if city:
        filtered_list = [cafe for cafe in filtered_list if city in cafe[1]]
    if district:
        filtered_list = [cafe for cafe in filtered_list if district in cafe[1]]
    if town:
        filtered_list = [cafe for cafe in filtered_list if town in cafe[1]]
    if no_kids_zone:
        filtered_list = [cafe for cafe in filtered_list if cafe[2]]

    return filtered_list

indoordatespot_data = [
    ["라이크어시네마","카페",15000,"서울시 강서구 등촌동 513-21","평일 16:00 - 24:00 주말 12:30 - 24:00"],
    ["서울스카이","전망대",25000,"서울시 송파구 신천동 29","매일 10:30 - 22:00"],
    ["서울생활사박물관","박물관",0,"서울시 노원구 공릉동 622","매일 09:00 - 18:00"],
    ["인왕산숲속쉼터","시설",0,"서울시 종로구 청운동 산 4-36","매일 10:00 - 17:00"],
    ["청운문학도서관","도서관",0,"서울시 종로구 청운동 4-20","화목금 10:00 - 21:00 토일 10:00 - 19:00"]
]

@app.get("/indoordatespot")
def filter_indoordatespot(
    name: str = Query(None, description="장소명"),
    type: str = Query(..., description="장소 종류"),
    max_price: int = Query(..., gt=0, description="최대 가격"),
    district: str = Query(None, description="지역의 구"),
    town: str = Query(None, description="지역의 동"),
):
    filtered_list = indoordatespot_data

    if name:
        filtered_list = [spot for spot in filtered_list if spot[0] == name]
    if district:
        filtered_list = [spot for spot in filtered_list if district in spot[3]]
    if town:
        filtered_list = [spot for spot in filtered_list if town in spot[3]]
    filtered_list = [spot for spot in filtered_list if spot[2] <= max_price and spot[1] == type]

    return filtered_list

libraryborrower_data = [
    ["이미래","홍은도담도서관","돼지책","NY000065134","2023-05-07~2023-05-21"],
    ["김도훈","하나도서관","넛지","EM0000394742","2023-04-06~2023-04-20"],
    ["최미연","나래도서관","파라다이스","IM000041508","2023-06-14~2023-06-21"],
    ["김희영","두리도서관","이기적 유전자","JM0000355969","2023-03-25~2023-04-08"],
    ["지민호","미래도서관","나미야 잡화점의 기적","EMH000560219","2023-07-01~2023-07-08"]
]

@app.get("/libraryborrower")
def filter_libraryborrower(
    name: str = Query(..., description="대출자 이름"),
    library: str = Query(None, description="도서관 명"),
    book: str = Query(None, description="대출한 책 이름"),
    accession_number: str = Query(None, description="대출한 책 등록번호"),
    loan_date: str = Query(None, description="대출일"),
    due_date: str = Query(None, description="반납 예정일"),
):
    filtered_list = libraryborrower_data

    filtered_list = [borrower for borrower in filtered_list if borrower[0] == name]
    if library:
        filtered_list = [borrower for borrower in filtered_list if borrower[1] == library]
    if book:
        filtered_list = [borrower for borrower in filtered_list if borrower[2] == book]
    if accession_number:
        filtered_list = [borrower for borrower in filtered_list if borrower[3] == accession_number]
    if loan_date:
        filtered_list = [borrower for borrower in filtered_list if borrower[4].split("~")[0] == loan_date]
    if due_date:
        filtered_list = [borrower for borrower in filtered_list if borrower[4].split("~")[1] == due_date]

    return filtered_list

ruralrestaurant_data = [
    ["전라북도 진안군 부귀면 전진로 1947","마이담", ["홍삼시래기정식","마늘시래기정식","홍삼시래기특정식"], "월요일","11:30~21:00","063-433-5535"],
    ["경상북도 경주시 배동 산75-29","수정소반", ["수정소반정식","수정소반정식","청국장찌개"], "화요일","11:00~20:00","054-744-1851"],
    ["제주도 제주시 봉개동 389","명도암수다뜰", ["콩국 생선구이","두부 두루지기"], "연중무휴","09:00~18:00","064-723-2722"],
    ["경상북도 고령군 대가야읍 큰골길 208","참살이", ["참살이정식","정나눔정식","자연인정식"], "화요일","12:00~19:00","054-954-1466"],
    ["충청남도 보령시 주포면 밖강술길 15","석화촌", ["홍삼시래기정식","마늘시래기정식","홍삼시래기특정식"], "연중무휴","11:00~21:00","041-932-9005"]
]

@app.get("/ruralrestaurant")
def filter_ruralrestaurant(
    city: str = Query(..., description="광역시도"),
    district: str = Query(None, description="시군구"),
    town: str = Query(None, description="읍면동"),
    name: str = Query(None, description="식당명"),
    menu: str = Query(None, description="메뉴"),
    closed_days: str = Query(None, description="휴무일"),
):
    filtered_list = ruralrestaurant_data

    filtered_list = [restaurant for restaurant in filtered_list if restaurant[0].startswith(city)]
    if district:
        filtered_list = [restaurant for restaurant in filtered_list if district in restaurant[0]]
    if town:
        filtered_list = [restaurant for restaurant in filtered_list if town in restaurant[0]]
    if name:
        filtered_list = [restaurant for restaurant in filtered_list if name in restaurant[1]]
    if menu:
        filtered_list = [restaurant for restaurant in filtered_list if menu in restaurant[2]]
    if closed_days:
        filtered_list = [restaurant for restaurant in filtered_list if closed_days == restaurant[3]]

    return filtered_list

koreanbeef_data = [
    ["갈비", ["구이","찜","탕","갈비"], 60000,64.83,8.8,"근내지방이 많고 진한 맛이 난다."],
    ["등심", ["구이","스테이크","전골"], 85000,46.53,6,"식감이 부드럽고 연하다."],
    ["안심", ["구이","스테이크","전골"], 55000,7.48,1.01,"지방 함량이 낮고 고기즙은 많다."],
    ["채끝", ["스테이크","구이","샤브샤브"], 100000,9.39,1.26,"부드럽고 맛과 풍미가 뛰어난다."],
    ["사태", ["장조림","찜","육회","탕"], 35000,18.1,2.44,"색이 짙고 쫄깃하다."]
]

@app.get("/KoreanBeef")
def filter_koreanbeef(
    name: str = Query(None, description="부위명"),
    uses: str = Query(..., description="부위를 사용한 요리"),
    max_price: int = Query(None, ge=0, description="최대 가격"),
    min_price: int = Query(None, ge=0, description="최소 가격"),
    keyword: str = Query(None, description="한우 부위 특징에 관한 키워드"),
):
    filtered_list = koreanbeef_data

    if name:
        filtered_list = [beef for beef in filtered_list if name == beef[0]]
    filtered_list = [beef for beef in filtered_list if uses in beef[1]]
    if max_price:
        filtered_list = [beef for beef in filtered_list if beef[2] <= max_price]
    if min_price:
        filtered_list = [beef for beef in filtered_list if beef[2] >= min_price]
    if keyword:
        filtered_list = [beef for beef in filtered_list if keyword in beef[5]]

    return filtered_list

camping_site_data = [
    ["글램비","경기 화성시 서신면 해안길 64",False,True,3049],
    ["황석산캠핑장","경남 함양군 서하면 육십령로 2991",True,True,83],
    ["트리캠핑장","인천 옹진군 영흥면 선재로306번길 27-55",True,True,85],
    ["유식물원캠핑장","경기 포천시 신북면 간자동길 138-100",True,False,1198],
    ["덕풍계곡캠핑장","강원 삼척시 가곡면 덕풍길 44",False,True,173]
]

@app.get("/CampingSite")
def filter_camping_site(
    name: str = Query(None, description="캠핑장 이름"),
    city: str = Query(None, description="광역시도"),
    district: str = Query(..., description="시군구"),
    town: str = Query(None, description="읍면동"),
    pet_friendly: bool = Query(None, description="애견동반 가능여부"),
    Reservation_available: bool = Query(None, description="예약 가능여부"),
):
    filtered_list = camping_site_data

    if name:
        filtered_list = [site for site in filtered_list if name == site[0]]
    if city:
        filtered_list = [site for site in filtered_list if city in site[1]]
    filtered_list = [site for site in filtered_list if district in site[1]]
    if town:
        filtered_list = [site for site in filtered_list if town in site[1]]
    if pet_friendly is not None:
        filtered_list = [site for site in filtered_list if pet_friendly == site[2]]
    if Reservation_available is not None:
        filtered_list = [site for site in filtered_list if Reservation_available == site[3]]

    return filtered_list

dog_grooming_salon_data = [
    ["꽃냥","경기 안양시 만안구 태평로60번길 42 센트럴타워2, 4층 406호",80000,"오전 10시","오후 7시"],
    ["댕댕이 미용실","서울 은평구 서오릉로 29",75000,"오전 10시","오후 7시"],
    ["도리도리펫샵","서울 은평구 응암로 279 102호",40000,"오전 10시 30분","오후 6시"],
    ["메씨엘리","부산 연제구 중앙대로1054번길 8",40000,"오전 10시","오후 7시"],
    ["빵실빵실","전남 순천시 왕지4길 9-11",80000,"오전 9시","오후 8시"]
]

@app.get("/doggroomingsalon")
def filter_dog_grooming_salon(
    name: str = Query(..., description="업소명"),
    location: str = Query(None, description="위치"),
    max_price: int = Query(None, ge=0, description="최대 가격"),
    opening_time: str = Query(None, description="오픈 시간"),
    closed_time: str = Query(None, description="마감 시간"),
):
    filtered_list = dog_grooming_salon_data

    filtered_list = [salon for salon in filtered_list if name == salon[0]]
    if location:
        filtered_list = [salon for salon in filtered_list if location in salon[1]]
    if max_price is not None:
        filtered_list = [salon for salon in filtered_list if max_price >= salon[2]]
    if opening_time:
        filtered_list = [salon for salon in filtered_list if opening_time == salon[3]]
    if closed_time:
        filtered_list = [salon for salon in filtered_list if closed_time == salon[4]]

    return filtered_list

blue_ribbon_restaurant_data = [
    ["거대숯불구이","한식","부산 해운대구 달맞이길 22",2022,2],
    ["도원","중식","서울특별시 중구 소공로 119 (태평로2가) 더플라자 3층",2023,3],
    ["배리스키친","베이커리","광주광역시 광산구 임방울대로 324 (수완동) 1층",2023,1],
    ["새재할매집","한식","경북 문경시 문경읍 새재로 922",2021,0],
    ["모모야마","일식","서울특별시 중구 을지로 30 (소공동) 롯데호텔서울 본관 38층",2023,3]
]

@app.get("/BlueRibbonRestaurant")
def filter_blue_ribbon_restaurant(
    name: str = Query(None, description="맛집 이름"),
    type: str = Query(None, description="식당 종류"),
    city: str = Query(None, description="광역시도"),
    district: str = Query(None, description="시군구"),
    town: str = Query(None, description="읍면동"),
    year: int = Query(..., description="선정 연도"),
):
    filtered_list = blue_ribbon_restaurant_data

    if name:
        filtered_list = [restaurant for restaurant in filtered_list if name == restaurant[0]]
    if type:
        filtered_list = [restaurant for restaurant in filtered_list if type == restaurant[1]]
    if city:
        filtered_list = [restaurant for restaurant in filtered_list if city in restaurant[2]]
    if district:
        filtered_list = [restaurant for restaurant in filtered_list if district in restaurant[2]]
    if town:
        filtered_list = [restaurant for restaurant in filtered_list if town in restaurant[2]]
    filtered_list = [restaurant for restaurant in filtered_list if year == restaurant[3]]

    return filtered_list

auto_body_shop_data = [
    ["한수카센타","경기 안양시 만안구 안양4동",True,"7:50~19:00 일휴무","0507-1380-7414"],
    ["대성모터스","경기 부천시 옥길동",True,"9:00~19:00 일휴무","0507-1465-3057"],
    ["로이스자동차","서울 강남구 신사동",False,"10:00~18:00","02-3445-6140"],
    ["경원카공업사","울산 중구 반구동",True,"9:00~20:30 일휴무","0507-1470-1173"],
    ["동성카센타","전북 전주시 덕진구 금암동",True,"8:30~18:00 일휴무","0507-1442-5503"]
]

@app.get("/AutoBodyShop")
def filter_auto_body_shop(
    name: str = Query(None, description="업소명"),
    city: str = Query(None, description="광역시도"),
    district: str = Query(..., description="시군구"),
    town: str = Query(None, description="읍면동"),
    available: bool = Query(None, description="운영 여부"),
):
    filtered_list = auto_body_shop_data

    if name:
        filtered_list = [shop for shop in filtered_list if name == shop[0]]
    if city:
        filtered_list = [shop for shop in filtered_list if city in shop[1]]
    if district:
        filtered_list = [shop for shop in filtered_list if district in shop[1]]
    if town:
        filtered_list = [shop for shop in filtered_list if town in shop[1]]
    if available is not None:
        filtered_list = [shop for shop in filtered_list if available == shop[2]]

    return filtered_list

farm_experience_data = [
    ["꽃초린 힐링팜","경상남도 함안군",True, ["약초향 주머니 만들기","약초비누 만들기","꽃차 만들기","황톳길 맨발걷기"], "010-3564-4889"],
    ["군산하늘딸기","전라북도 군산시 ",False, ["딸기잼 만들기"], "010-8647-7890"],
    ["최은명자연꿀","경기도 화성시",True, ["벌 생태체험","밀랍초 만들기","프로폴리스 치약만들기","꿀 마사지 체험"], "010-2779-9458"],
    ["칠성농원","경기도 이천시",True, ["복숭아빙수 만들기 체험","복숭아젤리 만들기 체험"], "010-8700-8327"],
    ["청도곤충나라","경상북도 청도군",True, ["곤충피자 만들기 A코스","곤충피자 만들기 B코스"], "010-9380-0007"]
]

@app.get("/FarmExperience")
def filter_farm_experience(
    name: str = Query(None, description="체험장 이름"),
    city: str = Query(..., description="광역시도"),
    district: str = Query(None, description="시군구"),
    available: bool = Query(None, description="예약가능여부"),
    program: str = Query(None, description="체험프로그램"),
):
    filtered_list = farm_experience_data

    if name:
        filtered_list = [farm for farm in filtered_list if name == farm[0]]
    if city:
        filtered_list = [farm for farm in filtered_list if city in farm[1]]
    if district:
        filtered_list = [farm for farm in filtered_list if district in farm[1]]
    if available is not None:
        filtered_list = [farm for farm in filtered_list if available == farm[2]]
    if program:
        filtered_list = [farm for farm in filtered_list if program in farm[3]]

    return filtered_list

medical_center_data = [
    ["내일내과의원","서울 금천구 금하로 720 에벤에셀프라자 3층",True,"온라인","8:30~18:00","0507-1379-7556"],
    ["KMI한국의학연구소","경기 수원시 권선구 동수원로 232",False,"온라인","07:00~16:00","031-231-0114"],
    ["부평세림병원 건강검진센터","인천 부평구 부평대로 175",True,"방문접수","08:00~17:00","032-509-5555"],
    ["유성선병원국제검진센터","대전 유성구 북유성대로 93",True,"방문접수","09:00~18:00","1588-7011"],
    ["한국병원건강검진센타","충북 청주시 상당구 영운동 158-11",True,"전화","08:30~17:30","043-252-2900"]
]

@app.get("/MedicalCenter")
def filter_medical_center(
    name: str = Query(None, description="센터명"),
    location: str = Query(None, description="위치"),
    available: bool = Query(..., description="예약가능여부"),
    reservation_how: str = Query(None, description="예약 방법"),
    opening_time: str = Query(None, description="오픈 시간"),
    closed_time: str = Query(None, description="마감 시간"),
):
    filtered_list = medical_center_data

    if name:
        filtered_list = [center for center in filtered_list if name == center[0]]
    if location:
        filtered_list = [center for center in filtered_list if location in center[1]]
    if available is not None:
        filtered_list = [center for center in filtered_list if available == center[2]]
    if reservation_how:
        filtered_list = [center for center in filtered_list if reservation_how in center[3]]
    if opening_time:
        filtered_list = [center for center in filtered_list if opening_time in center[4]]
    if closed_time:
        filtered_list = [center for center in filtered_list if closed_time in center[5]]

    return filtered_list

self_studio_data = [
    ["청춘사진관","경기 안양시 만안구 안양동 676-91",50000,True,True],
    ["라포토스튜디오","부산 부산진구 전포동 654-1",20000,True,False],
    ["오디티모드","서울 송파구 송파동 54-8",45000,True,False],
    ["낭만포토","서울 노원구 상계동 349-2",25000,True,True],
    ["나무사진관","인천 부평구 삼산동 426-8",40000,True,True]
]

@app.get("/SelfStudio")
def filter_self_studio(
    name: str = Query(None, description="사진관 이름"),
    city: str = Query(..., description="광역시도"),
    district: str = Query(..., description="시군구"),
    town: str = Query(None, description="읍면동"),
    max_price: int = Query(None, description="최대 가격", ge=0),
    pet_friendly: bool = Query(None, description="애견동반 가능여부"),
):
    filtered_list = self_studio_data

    if name:
        filtered_list = [studio for studio in filtered_list if name == studio[0]]
    if city:
        filtered_list = [studio for studio in filtered_list if city in studio[1]]
    if district:
        filtered_list = [studio for studio in filtered_list if district in studio[1]]
    if town:
        filtered_list = [studio for studio in filtered_list if town in studio[1]]
    if max_price is not None:
        filtered_list = [studio for studio in filtered_list if studio[2] <= max_price]
    if pet_friendly is not None:
        filtered_list = [studio for studio in filtered_list if pet_friendly == studio[3]]

    return filtered_list

public_corporation_data = [
    ["한국전력공사","이정복","전라남도 나주시 전력로 55","송전 및 배전업",True,"123"],
    ["한국도로공사","함진규","경상북도 김천시 혁신8로 77","도로 및 관련시설 운영업",False,"1588-2504"],
    ["한국지역난방공사","정용기","경기도 성남시 분당구 분당로 368","냉온수 및 공기조절 공급업",True,"1688-2488"],
    ["한국철도공사","나희승","대전광역시 동구 중앙로 240","철도 여객 운송업",False,"1544-7788"],
    ["한국조폐공사","반장식","대전광역시 유성구 과학로 80-67 한국조폐공사기술연구소(화폐박물관)","재정 및 경제정책 행정",False,"1577-4321"]
]

@app.get("/PublicCorporation")
def filter_public_corporation(
    name: str = Query(..., description="기업명"),
    representative: str = Query(None, description="대표자"),
    head_office_location: str = Query(None, description="본사 위치"),
    sectors: str = Query(None, description="업종"),
    kospi: bool = Query(None, description="코스피 상장 여부"),
):
    filtered_list = public_corporation_data

    filtered_list = [corp for corp in filtered_list if name == corp[0]]
    if representative:
        filtered_list = [corp for corp in filtered_list if representative == corp[1]]
    if head_office_location:
        filtered_list = [corp for corp in filtered_list if head_office_location == corp[2]]
    if sectors:
        filtered_list = [corp for corp in filtered_list if sectors == corp[3]]
    if kospi is not None:
        filtered_list = [corp for corp in filtered_list if kospi == corp[4]]

    return filtered_list

certificate_data = [
    ["가스기사","국가기술자격","한국산업인력공단","안전관리",False,"100점을 만점으로 하여 평균 60점이상과 과목당 40점 이상"],
    ["정보통신기술사","국가기술자격","한국방송통신전파진흥원","정보통신",False,"100점을 만점으로 하여 60점이상"],
    ["감정평가사","국가전문자격","한국산업인력공단","감정평가",False,"100점을 만점으로 하여 평균 60점이상과 과목당 40점 이상"],
    ["건축목공기능사","국가기술자격","한국산업인력공단 ","건축",False,"100점을 만점으로 하여 60점이상"],
    ["청소년지도사","국가전문자격","한국산업인력공단",True,"청소년육성","100점을 만점으로 하여 평균 60점이상과 과목당 40점 이상"]
]

@app.get("/certificate")
def filter_certificate(
    name: str = Query(None, description="자격증명"),
    type: str = Query(None, description="자격증 종류"),
    issuing_authority: str = Query(None, description="시행처"),
    job_field: str = Query(..., description="직무 분야 ex) 안전관리, 건축 등"),
    level: bool = Query(None, description="급수 유무"),
):
    filtered_list = certificate_data

    if name:
        filtered_list = [cert for cert in filtered_list if name == cert[0]]
    if type:
        filtered_list = [cert for cert in filtered_list if type == cert[1]]
    if issuing_authority:
        filtered_list = [cert for cert in filtered_list if issuing_authority == cert[2]]
    if level is not None:
        filtered_list = [cert for cert in filtered_list if level == cert[4]]

    return filtered_list

extracurricular_data = [
    ["대웅바이오 서포터즈","경영","중견기업","대학생",True,"23.7.21 ~ 23.9.1"],
    ["사일런트디스코","체육","스타트업","일반인",True,"23.7.26 ~ 23.7.27"],
    ["네이버 숏폼 크리에이터","콘텐츠","대기업","일반인",False,"23.8.1 ~ 23.12.31"],
    ["템플스테이 체험단","여행","중소기업","외국인",True,"23.8.3 ~ 23.11.30"],
    ["신한 GYC","교육","대기업","일반인",True,"23.9.18 ~ 24.4.19"],
    ["월드잡플러스 서포터즈","언론/미디어","공기업","대학생",True,"23.7.21 ~ 23.11.30"]
]

@app.get("/ExtracurricularActivities")
def filter_extracurricular_activities(
    name: str = Query(None, description="대외활동명"),
    Interests: str = Query(None, description="관심분야 ex) 경영, 체육, 여행 등"),
    company_type: str = Query(None, description="기업 종류 ex) 대기업, 중견기업, 중소기업 등"),
    target: str = Query(..., description="대상 ex) 대학생, 일반인 등"),
    available: bool = Query(None, description="참여가능여부"),
):
    filtered_list = extracurricular_data

    if name:
        filtered_list = [activity for activity in filtered_list if name == activity[0]]
    if Interests:
        filtered_list = [activity for activity in filtered_list if Interests == activity[1]]
    if company_type:
        filtered_list = [activity for activity in filtered_list if company_type == activity[2]]
    if target:
        filtered_list = [activity for activity in filtered_list if target == activity[3]]
    if available is not None:
        filtered_list = [activity for activity in filtered_list if available == activity[4]]

    return filtered_list

emergency_call_data = [
    ["경찰청","112","범죄 신고","긴급신고","24시간","서울특별시 서대문구 통일로 97"],
    ["국민권익위원회","110","정부민원 신고","민원신고","24시간, 수화상담은 평일 9~18시","세종특별자치시 도움5로 20"],
    ["한국전력공사","123","전기 고장 신고","민원신고","24시간","전라남도 나주시 전력로 55"],
    ["미추홀콜센터","032-120","인천 생활정보","생활정보","24시간","인천광역시 남동구 정각로 29"],
    ["국군방첩사령부","1337","군사기밀 신고","긴급신고","24시간","경기도 과천시 과천우체국 사서함 80호"],
    ["검찰청","1301","마약 신고","긴급신고","24시간","서울특별시 서초구 반포대로 157"],
    ["청소년 사이버상담센터","1388","청소년 고민 상담","상담","24시간","부산광역시 해운대구 센텀중앙로79"]
]

@app.get("/EmergencyCall")
def filter_emergency_call(
    name: str = Query(None, description="관련기관명"),
    telephone_Num: str = Query(None, description="전화번호"),
    contents: str = Query(..., description="접수 내용 ex) 범죄 신고, 마약 신고, 전기 고장 신고 등"),
    type: str = Query(None, description="신고 종류 ex) 긴급신고, 생활정보, 민원신고, 상담"),
    Business_Hours: str = Query(None, description="신고 전화 운영시간"),
):
    filtered_list = emergency_call_data

    if name:
        filtered_list = [call for call in filtered_list if name == call[0]]
    if telephone_Num:
        filtered_list = [call for call in filtered_list if telephone_Num == call[1]]
    if contents:
        filtered_list = [call for call in filtered_list if contents == call[2]]
    if type:
        filtered_list = [call for call in filtered_list if type == call[3]]
    if Business_Hours:
        filtered_list = [call for call in filtered_list if Business_Hours == call[4]]

    return filtered_list

lotto_info_data = [
    [1070,"2023.06.03", [3,6,14,22,30,41,36],1859116929, ["나나복권","대박로또방","복권나라","무지개로또복권"], 14],
    [1069,"2023.0.27", [1,10,18,2228,31,44],1863217554, ["공항상회로또판매점","노다지복권","대박스타","시민슈퍼"], 14],
    [995,"2021.12.15", [1,4,13,29,38,39,7],3447271875, ["경이네복권마트","영약국","채널큐","찻잔에담긴행운"], 7],
    [986,"2021.10.23", [7,10,16,28,41,42,40],2375275125, ["공원슈퍼","투데이","프로토베팅샵","일등복권편의점"], 10],
    [907,"2020.04.18", [21,27,29,38,40,44,37],3165059036, ["로또삼성복권방","세종로또방","운수대통복권방","행복편의점"], 7]
]

@app.get("/LottoInfo")
def filter_lotto_info(
    number: int = Query(..., description="회차"),
    date: str = Query(None, description="당첨날짜"),
    amount: int = Query(None, description="당첨 금액"),
    store: str = Query(None, description="당첨 판매점"),
    lottery_Num: int = Query(None, description="당첨 복권 수"),
):
    filtered_list = lotto_info_data

    filtered_list = [info for info in filtered_list if number == info[0]]
    if date:
        filtered_list = [info for info in filtered_list if date == info[1]]
    if amount:
        filtered_list = [info for info in filtered_list if amount == info[3]]
    if store:
        filtered_list = [info for info in filtered_list if store in info[4]]
    if lottery_Num:
        filtered_list = [info for info in filtered_list if lottery_Num == info[5]]

    return filtered_list

local_specialties_data = [
    ["경상북도","청송군","과일류","사과",True,7],
    ["경상북도","청송군","축산물","한우",True,3],
    ["경기도","시흥시","과일류","포도",True,1],
    ["부산광역시","기장군","식량작물","흑미",False,0],
    ["전라남도","여수시","채소류","두릅",True,1],
    ["강원도","횡성군","축산물","한우",True,2]
]

@app.get("/LocalSpecialties")
def filter_local_specialties(
    city: str = Query(..., description="광역시도"),
    district: str = Query(..., description="시군구"),
    type: str = Query(None, description="특산물 종류"),
    name: str = Query(None, description="지역 특산물명"),
    brand_existence: bool = Query(None, description="브랜드 유무"),
):
    filtered_list = local_specialties_data

    filtered_list = [specialty for specialty in filtered_list if city == specialty[0]]
    filtered_list = [specialty for specialty in filtered_list if district == specialty[1]]
    if type:
        filtered_list = [specialty for specialty in filtered_list if type == specialty[2]]
    if name:
        filtered_list = [specialty for specialty in filtered_list if name == specialty[3]]
    if brand_existence is not None:
        filtered_list = [specialty for specialty in filtered_list if brand_existence == specialty[4]]

    return filtered_list

dept_store_vip_data = [
    ["김민희","블랙","010-1234-5678","여성","1억 5천만","2023.1.01","2025.01.31"],
    ["이민환","블루","010-1111-2222","남성","9천만","2022.1.01","2024.01.31"],
    ["이지영","그린","010-1111-3333","여성","1천만","2022.1.01","2024.01.31"],
    ["정혜민","블랙","010-2222-3333","여성","1억 2천만","2021.1.01","2023.01.31"],
    ["박찬수","블루","010-3333-4444","남성","8천만","2023.1.01","2025.01.31"]
]

@app.get("/DeptStoreVIP")
def filter_dept_store_vip(
    name: str = Query(None, description="고객명"),
    type: str = Query(..., description="VIP 등급 종류"),
    phone_Num: str = Query(None, description="전화번호"),
    gender: str = Query(None, description="성별"),
    purchase_amount: str = Query(None, description="구매 금액"),
    selected_period: str = Query(None, description="VIP 선정기간"),
):
    filtered_list = dept_store_vip_data

    if name:
        filtered_list = [vip for vip in filtered_list if name == vip[0]]
    filtered_list = [vip for vip in filtered_list if type == vip[1]]
    if phone_Num:
        filtered_list = [vip for vip in filtered_list if phone_Num == vip[2]]
    if gender:
        filtered_list = [vip for vip in filtered_list if gender == vip[3]]
    if purchase_amount:
        filtered_list = [vip for vip in filtered_list if purchase_amount == vip[4]]
    if selected_period:
        filtered_list = [vip for vip in filtered_list if selected_period == vip[5]]

    return filtered_list

world_regional_festival_data = [
    ["토마티나","스폐인 부뇰","토마토 축제",8,4.8],
    ["송끄란","태국 전지역","물 축제",4,4.5],
    ["옥토버페스트","독일 뮌헨","맥주 축제",9,4.6],
    ["리우 카니발","브라질 리우데자네이루","삼바 축제",2,4.7],
    ["나담","몽골 울란바토르","스포츠 축제",7,3.9]
]

@app.get("/WorldRegionalFestival")
def filter_world_regional_festival(
    name: str = Query(..., description="축제명"),
    nation: str = Query(None, description="국가"),
    region: str = Query(None, description="지역명"),
    contents: str = Query(None, description="축제 내용"),
    month: int = Query(None, description="축제 기간 중 월"),
    min_congestion: float = Query(None, description="최소 혼잡도", gt=0, le=5),
):
    filtered_list = world_regional_festival_data

    filtered_list = [festival for festival in filtered_list if name == festival[0]]
    if nation:
        filtered_list = [festival for festival in filtered_list if nation in festival[1]]
    if region:
        filtered_list = [festival for festival in filtered_list if region in festival[1]]
    if contents:
        filtered_list = [festival for festival in filtered_list if contents == festival[2]]
    if month:
        filtered_list = [festival for festival in filtered_list if month == festival[3]]
    if min_congestion:
        filtered_list = [festival for festival in filtered_list if min_congestion <= festival[4]]

    return filtered_list

camping_supplies_data = [
    ["코베아","휴대용가스레인지",30000,4.8, ["아주 가볍고 좋아용","간단하고 직결식이라 수납 좋아요"]],
    ["몬테라","캠핑 의자",54000,4.8, ["편하고 이뻐요","하나사고 좋아서 두개샀어요","완전 편해요. 만족합니다."]],
    ["헬리녹스","캠핑 테이블",34000,4.7, ["생각보다 가벼워요","가격대비 성능만족","조립도 편리해요"]],
    ["코베아","캠핑 의자",67000,4.8, ["튼튼하고 색도 예뻐니다","부피작고 가벼워서 아주 잘 사용해요"]],
    ["지라프","휴대용가스레인지",41000,4.5, ["화력도 좋고 디자인도 예뻐요","좋은 가격으로 구매했습니다 많이 파세요","슬림형이라 가볍네요"]]
]

@app.get("/CampingSupplies")
def filter_camping_supplies(
    brand: str = Query(..., description="브랜드"),
    type: str = Query(None, description="종류"),
    min_price: int = Query(None, description="최소 가격", ge=0),
    max_price: int = Query(None, description="최대 가격", ge=0),
    min_rating: float = Query(None, description="최소 평점", ge=0, le=5),
):
    filtered_list = camping_supplies_data

    filtered_list = [item for item in filtered_list if brand == item[0]]
    if type:
        filtered_list = [item for item in filtered_list if type == item[1]]
    if min_price:
        filtered_list = [item for item in filtered_list if item[2] >= min_price]
    if max_price:
        filtered_list = [item for item in filtered_list if item[2] <= max_price]
    if min_rating:
        filtered_list = [item for item in filtered_list if item[3] >= min_rating]

    return filtered_list


issuing_machine_data = [
    ["서울시","마포구","상암동","상암동주민센터","평일 08:00~20:00","상암동주민센터 출입구 안쪽"],
    ["서울시","구로구","온수동","온수역","매일 05:00~01:00","7호선 2번출구 매표소 앞"],
    ["경기도","수원시","영통동","영통역","매일 06:00~22:00","1번출구"],
    ["대전광역시","유성구","구즉동","송강동북대전농협","평일 09:00~16:00","농협내 입구 좌측"],
    ["제주도","서귀포시","영천동","영천동주민센터","매일 00:00~24:00","현관 우측 옥외부스"]
]

@app.get("/IssuingMachine")
def filter_issuing_machine(
    city: str = Query(..., description="광역시도"),
    district: str = Query(..., description="시군구"),
    town: str = Query(None, description="읍면동"),
    installed_location: str = Query(None, description="민원발급기 설치 장소"),
    operating_time: str = Query(None, description="운영시간"),
):
    filtered_list = issuing_machine_data

    filtered_list = [item for item in filtered_list if city == item[0]]
    filtered_list = [item for item in filtered_list if district == item[1]]
    if town:
        filtered_list = [item for item in filtered_list if town == item[2]]
    if installed_location:
        filtered_list = [item for item in filtered_list if installed_location == item[3]]
    if operating_time:
        filtered_list = [item for item in filtered_list if operating_time == item[4]]

    return filtered_list

seasonal_food_data = [
    [12,"해산물","굴",97, ["굴전","굴미역국","굴밥"], "바다의 우유라 불리는 굴은 영양이 가득한 재료입니다."],
    [5,"채소류","두릅",21, ["두릅무침","두릅전","두릅장아찌"], "따뜻한 봄날 나른하고 입맛이 없을 때 초고추장에 찍어 먹으면 없어졌던 입맛이 다시 돌아옵니다."],
    [8,"과일류","복숭아",34, ["복숭아잼","복숭아콤포트","복숭아버터케이크"], "쭈꾸미는 피로회복에 좋은 타우린도 풍부하여 영양만점입니다."],
    [4,"해산물","쭈꾸미",47, ["쭈꾸미볶음","쭈꾸미비빔밥","쭈꾸미파스타"], "농협내 입구 좌측"],
    [7,"과일류","수박",31, ["수박화채","수박샐러드","수박주스"], "수박의 시원한 과즙으로 이뇨작용에도 좋습니다."]
]

@app.get("/SeasonalFood")
def filter_seasonal_food(
    month: int = Query(..., description="기간 중 월"),
    type: str = Query(None, description="종류"),
    name: str = Query(None, description="제철 음식명"),
    min_calories: int = Query(None, description="최소 칼로리"),
    cooking_food: str = Query(None, description="활용 음식"),
):
    filtered_list = seasonal_food_data

    filtered_list = [item for item in filtered_list if month == item[0]]
    if type:
        filtered_list = [item for item in filtered_list if type == item[1]]
    if name:
        filtered_list = [item for item in filtered_list if name == item[2]]
    if min_calories:
        filtered_list = [item for item in filtered_list if item[3] >= min_calories]
    if cooking_food:
        filtered_list = [item for item in filtered_list if cooking_food in item[4]]

    return filtered_list

meal_kit_data = [
    ["애슐리 에그인헬","2인분","브런치",14500,4.8],
    ["손말이고기","3인분","캠핑용",16000,4.8],
    ["크림빠네파스타","3인분","브런치",15000,4.6],
    ["큰솥 해신탕","4인분","생일상",25000,4.5],
    ["백골뱅이탕","1인분","캠핑용",22000,4.7]
]

@app.get("/MealKit")
def filter_meal_kit(
    name: str = Query(None, description="상품명"),
    amount: str = Query(None, description="내용량"),
    theme: str = Query(..., description="테마"),
    max_price: int = Query(None, description="최대 가격"),
    min_rating: float = Query(None, description="최소 평점"),
):
    filtered_list = meal_kit_data

    if name:
        filtered_list = [item for item in filtered_list if name == item[0]]
    if amount:
        filtered_list = [item for item in filtered_list if amount == item[1]]
    filtered_list = [item for item in filtered_list if theme == item[2]]
    if max_price:
        filtered_list = [item for item in filtered_list if item[3] <= max_price]
    if min_rating:
        filtered_list = [item for item in filtered_list if item[4] >= min_rating]

    return filtered_list


animal_data = [
    ["서울시 강남구 역삼로 236 인근","개","수컷","흰색","한국동물구조관리협회"],
    ["부산광역시 강서구 호계로23","고양이","수컷","노란색","하얀비둘기"],
    ["인천광역시 계양구 작전동 계산119구조대","개","암컷","검회색","신영재동물병원"],
    ["대전광역시 서구 청사로 253 인근","개","암컷","갈색","대전동물보호센터"],
    ["경기도 김포시 통진읍 고정리 326-1 인근","개","수컷","흰색","한국동물구조관리협회"]
]

@app.get("/FindAnimals")
def filter_find_animals(
    city: str = Query(None, description="광역시도"),
    district: str = Query(None, description="시군구"),
    town: str = Query(None, description="읍면동"),
    species: str = Query(..., description="동물 종"),
    sex: str = Query(None, description="성별"),
    color: str = Query(None, description="털색"),
):
    filtered_list = animal_data

    if city:
        filtered_list = [item for item in filtered_list if city in item[0]]
    if district:
        filtered_list = [item for item in filtered_list if district in item[0]]
    if town:
        filtered_list = [item for item in filtered_list if town in item[0]]
    filtered_list = [item for item in filtered_list if species == item[1]]
    if sex:
        filtered_list = [item for item in filtered_list if sex == item[2]]
    if color:
        filtered_list = [item for item in filtered_list if color == item[3]]

    return filtered_list

seller_data = [
    ["나영지","여성","010-1111-2222","수공예 쥬얼리",True,"2023.06.08"],
    ["최지혜","여성","010-2222-3333","수제비누",False,"없음"],
    ["김희진","여성","010-3333-4444","독립출판",True,"2023.06.10"],
    ["최석훈","남성","010-4444-5555","목공예",True,"2023.06.28"],
    ["정수지","여성","010-5555-6666","수공예 쥬얼리",True,"2023.07.01"]
]

@app.get("/FleaMarketSeller")
def filter_flea_market_seller(
    name: str = Query(None, description="참여자명"),
    gender: str = Query(None, description="성별"),
    phone_Num: str = Query(None, description="전화번호"),
    sale_item: str = Query(..., description="판매품목"),
    participation_fee: bool = Query(None, description="참가비 지급 유무"),
):
    filtered_list = seller_data

    if name:
        filtered_list = [item for item in filtered_list if name in item[0]]
    if gender:
        filtered_list = [item for item in filtered_list if gender in item[1]]
    if phone_Num:
        filtered_list = [item for item in filtered_list if phone_Num in item[2]]
    filtered_list = [item for item in filtered_list if sale_item == item[3]]
    if participation_fee is not None:
        filtered_list = [item for item in filtered_list if participation_fee == item[4]]

    return filtered_list

winner_data = [
    [39,"김주희","여성","대상","롯데음료","010-1111-1111"],
    [39,"문준성","남성","대상","롯데음료","010-2222-2222"],
    [39,"이종헌","남성","은상","상상인증권","010-3333-3333"],
    [37,"남유경","여성","동상","컴버스","010-4444-4444"],
    [35,"박선희","여성","대상","한국관광공사","010-5555-5555"]
]

@app.get("/ContestWinner")
def filter_contest_winner(
    number: int = Query(None, description="공모전 회차"),
    name: str = Query(None, description="수상자명"),
    gender: str = Query(None, description="성별"),
    type: str = Query(..., description="상종류"),
    Participation_brand: str = Query(None, description="참여 브랜드"),
):
    filtered_list = winner_data

    if number:
        filtered_list = [item for item in filtered_list if number == item[0]]
    if name:
        filtered_list = [item for item in filtered_list if name in item[1]]
    if gender:
        filtered_list = [item for item in filtered_list if gender in item[2]]
    filtered_list = [item for item in filtered_list if type == item[3]]
    if Participation_brand:
        filtered_list = [item for item in filtered_list if Participation_brand in item[4]]

    return filtered_list

instrument_data = [
    ["만돌린","현악기","유럽","이탈리아","류트(Lute) 족의 현악기로, 손가락이나 피크로 현을 튕겨서 연주한다."],
    ["단소","관악기","아시아","한국","세로로 부는 악기로서 길이가 짧다는 뜻으로 지공이 뒤에 1개, 앞에 4개가 있다."],
    ["응고","타악기","아시아","한국","긴 통 같이 생긴 북을 틀에 매달아 놓고 치는 악기이다."],
    ["비올","현악기","유럽","스폐인","다리 사이에 악기를 끼우고 활로 켜서 연주한다."],
    ["끌롱뿟","관악기","아시아","베트남","베트남 중부 고원지역 바나 족의 전통 악기로, 음높이에 따라 나란히 배열된 여러 개의 대나무 관 앞에서 손뼉을 쳐서 관 속의 공기를 진동시켜 소리를 낸다."]
]

@app.get("/TraditionalInstruments")
def filter_traditional_instruments(
    name: str = Query(None, description="악기명"),
    type: str = Query(..., description="악기 종류"),
    first_continent: str = Query(None, description="최초 사용지역 대륙"),
    first_nation: str = Query(None, description="최초 사용지역 국가"),
    keyword: str = Query(None, description="악기 설명에 대한 키워드"),
):
    filtered_list = instrument_data

    if name:
        filtered_list = [item for item in filtered_list if name in item[0]]
    filtered_list = [item for item in filtered_list if type == item[1]]
    if first_continent:
        filtered_list = [item for item in filtered_list if first_continent in item[2]]
    if first_nation:
        filtered_list = [item for item in filtered_list if first_nation in item[3]]
    if keyword:
        filtered_list = [item for item in filtered_list if keyword in item[4]]

    return filtered_list

singing_room_data = [
    ["세븐스타노래연습장", "경기 성남시 분당구 야탑로69번길 24-6 두만프라자 지하 3층 세븐스타", True, True, "2곡", 1000],
    ["짱노래연습장", "경기 성남시 수정구 산성대로255번길 5-1", False, False, "30분", 5000],
    ["질러노래연습장", "경기 성남시 분당구 성남대로926번길 6 대덕구프라자 313", False, True, "1시간", 25000],
    ["세븐스타노래연습장", "경기 성남시 분당구 성남대로331번길 9-6 3층", True, False, "2곡", 1000],
    ["타임앤노래연습장", "경기 성남시 분당구 판교로 445 미라보상가 지하1층 5호, 6호", True, True, "1곡", 500]
]

@app.get("/singing_room")
def filter_singing_room(
    name: str = Query(None, description="매장명"),
    coinTF: bool = Query(..., description="코인노래방 여부"),
    undergroundTF: bool = Query(None, description="지하 여부"),
    unit: str = Query(None, description="요금 단위"),
    min_price: int = Query(None, description="최소 가격"),
    max_price: int = Query(None, description="최대 가격"),
):
    filtered_list = singing_room_data

    if name:
        filtered_list = [item for item in filtered_list if name in item[0]]
    filtered_list = [item for item in filtered_list if coinTF == item[2]]
    if undergroundTF is not None:
        filtered_list = [item for item in filtered_list if undergroundTF == item[3]]
    if unit:
        filtered_list = [item for item in filtered_list if unit in item[4]]
    if min_price is not None:
        filtered_list = [item for item in filtered_list if item[5] >= min_price]
    if max_price is not None:
        filtered_list = [item for item in filtered_list if item[5] <= max_price]

    return filtered_list



coin_laundromat_data = [
    ["크린토피아 크린워시", "경기 성남시 수정구 복정로42번길 2", 4, 6, 3000, 4000, False],
    ["크린토피아 크린워시", "경기 성남시 분당구 미금일로90번길 11 (금성백조빌라 정문 앞)", 6, 7, 4000, 5000, False],
    ["코인워시24", "경기 성남시 수정구 산성대로515번길 3", 4, 3, 3500, 4000, True],
    ["코리아런드리 워시앤조이", "경기 성남시 수정구 성남대로1480번길 16 1층", 5, 4, 4000, 4500, False],
    ["뽀송뽀송코인워시 홈플러스", "경기 성남시 분당구 탄천상로151번길 20 홈플러스 지하1층 셀프빨래방", 9, 8, 3500, 5000, True]
]

@app.get("/coin_laundromat")
def filter_coin_laundromat(
    name: str = Query(..., description="매장명"),
    address: str = Query(None, description="주소"),
    min_washerCount: int = Query(None, description="최소 세탁기 갯수"),
    min_dryerCount: int = Query(None, description="최소 건조기 갯수"),
    washerPrice: int = Query(None, description="세탁기 이용 가격"),
    dryerPrice: int = Query(None, description="건조기 이용 가격"),
    cleanserTF: bool = Query(None, description="세제 제공 여부"),
):
    filtered_list = coin_laundromat_data

    filtered_list = [item for item in filtered_list if name in item[0]]
    if address:
        filtered_list = [item for item in filtered_list if address in item[1]]
    if min_washerCount is not None:
        filtered_list = [item for item in filtered_list if item[2] >= min_washerCount]
    if min_dryerCount is not None:
        filtered_list = [item for item in filtered_list if item[3] >= min_dryerCount]
    if washerPrice is not None:
        filtered_list = [item for item in filtered_list if item[4] >= washerPrice]
    if dryerPrice is not None:
        filtered_list = [item for item in filtered_list if item[5] >= dryerPrice]
    if cleanserTF is not None:
        filtered_list = [item for item in filtered_list if cleanserTF == item[6]]

    return filtered_list

paint_data = [
    ["삼화페인트", "아이생각 친환경 수성내부프로", ["화이트"], 4, 14900, 10],
    ["삼화페인트", "홈스타 월페이퍼 무광", ["베이지", "브라운", "그레이"], 4, 52400, 200],
    ["노루페인트", "순앤수100 친환경 수성페인트 무광", ["화이트"], 4, 10900, 30],
    ["노루페인트", "친환경 프리미엄 팬톤페인트", ["핑크", "퍼플", "그린"], 1, 13500, 100],
    ["베어", "그래나이트 그립", ["아이보리", "오렌지", "올리브"], 4, 109000, 40]
]

@app.get("/paint")
def filter_paint(
    manufacture: str = Query(..., description="제조사"),
    name: str = Query(None, description="상품명"),
    color: str = Query(None, description="색상"),
    min_weight: float = Query(None, description="최소 용량(kg)"),
    max_weight: float = Query(None, description="최대 용량(kg)"),
    min_price: int = Query(None, description="최소 가격"),
    max_price: int = Query(None, description="최대 가격"),
    min_stock: int = Query(None, description="최소 재고"),
):
    filtered_list = paint_data

    filtered_list = [item for item in filtered_list if manufacture in item[0]]
    if name:
        filtered_list = [item for item in filtered_list if name in item[1]]
    if color:
        filtered_list = [item for item in filtered_list if color in item[2]]
    if min_weight is not None:
        filtered_list = [item for item in filtered_list if item[3] >= min_weight]
    if max_weight is not None:
        filtered_list = [item for item in filtered_list if item[3] <= max_weight]
    if min_price is not None:
        filtered_list = [item for item in filtered_list if item[4] >= min_price]
    if max_price is not None:
        filtered_list = [item for item in filtered_list if item[4] <= max_price]
    if min_stock is not None:
        filtered_list = [item for item in filtered_list if item[5] >= min_stock]

    return filtered_list

wallpaper_data = [
    ["현대벽지", "HD5016", ["라이트그레이", "딥그레이", "민트"], "합지", True, 93, 35500],
    ["신한벽지", "SH70259", ["화이트", "그린"], "실크", True, 106, 38500],
    ["현대벽지", "HD5034", ["퍼플", "그레이"], "실크", False, 106, 38500],
    ["신한벽지", "SH70256", ["지베르니"], "실크", 95, 41000],
    ["개나리벽지", "G77309", ["화이트", "라이트그레이", "베이지"], "합지", False, 106, 38000]
]

@app.get("/wallpaper")
def filter_wallpaper(
    manufacture: str = Query(None, description="제조사"),
    name: str = Query(None, description="상품명"),
    color: str = Query(None, description="색상"),
    category: str = Query(..., description="카테고리 ex) 합지, 실크"),
    glueTF: bool = Query(None, description="풀바름 여부"),
    min_width: float = Query(None, description="최소 폭(cm)"),
    min_price: int = Query(None, description="최소 가격"),
    max_price: int = Query(None, description="최대 가격"),
):
    filtered_list = wallpaper_data

    if manufacture:
        filtered_list = [item for item in filtered_list if manufacture in item[0]]
    if name:
        filtered_list = [item for item in filtered_list if name in item[1]]
    if color:
        filtered_list = [item for item in filtered_list if color in item[2]]
    filtered_list = [item for item in filtered_list if category in item[3]]
    if glueTF is not None:
        filtered_list = [item for item in filtered_list if item[4] == glueTF]
    if min_width is not None:
        filtered_list = [item for item in filtered_list if item[5] >= min_width]
    if min_price is not None:
        filtered_list = [item for item in filtered_list if item[6] >= min_price]
    if max_price is not None:
        filtered_list = [item for item in filtered_list if item[6] <= max_price]

    return filtered_list

singing_room_song_data = [
    ["83490", "헤어지자말해요", "박재정", "발라드", ["여자", "남자"], "03:41"],
    ["83138", "심", "DK(디셈버)", "발라드", ["남자"], "04:10"],
    ["83434", "I AM", "IVE", "K-POP", ["여자"], "03:30"],
    ["83602", "퀸카(Queencard)", "(여자)아이들", "K-POP", ["여자"], "03:55"],
    ["80548", "사랑은늘도망가(신사와아가씨OST)", "임영웅", "트로트", ["여자", "남자"], "04:20"],
]

@app.get("/singing_room_song")
def filter_singing_room_song(
    songNum: str = Query(None, description="곡 번호"),
    title: str = Query(None, description="곡 제목"),
    musician: str = Query(None, description="가수"),
    genre: str = Query(..., description="장르"),
    key: str = Query(None, description="노래 키 구분 ex)여자, 남자"),
    max_time: float = Query(None, description="최대 반주시간"),
):
    filtered_list = singing_room_song_data

    if songNum:
        filtered_list = [item for item in filtered_list if songNum in item[0]]
    if title:
        filtered_list = [item for item in filtered_list if title in item[1]]
    if musician:
        filtered_list = [item for item in filtered_list if musician in item[2]]
    filtered_list = [item for item in filtered_list if genre in item[3]]
    if key:
        filtered_list = [item for item in filtered_list if key in item[4]]
    if max_time is not None:
        filtered_list = [item for item in filtered_list if item[5] <= max_time]

    return filtered_list

korea_sauna_data = [
    ["힐링수 사우나&찜질방", "경기 성남시 분당구 내정로113번길 4 지하1층", "031-0000-0001", True, 100000, "00:00-24:00"],
    ["위례파크24시사우나", "경기 성남시 수정구 위례광장로 19 아이페리온 지하1층", "031-0000-0002", True, 11000, "05:00-22:00"],
    ["크란츠스파랜드", "경기 성남시 중원구 둔촌대로 388 크란츠 테크노", "031-0000-0003", False, 9000, "00:00-24:00"],
    ["쑥이랑 본점", "경기 성남시 분당구 성남대로 168 6층 605호", "031-0000-0004", False, 50000, "09:00-20:00"],
    ["모란스파사우나", "경기 성남시 중원구 성남대로 1126 메가프라자", "031-0000-0005", True, 8000, "06:00-23:00"],
]

@app.get("/korea_sauna")
def filter_korea_sauna(
    name: str = Query(None, description="매장명"),
    address: str = Query(None, description="주소"),
    phone: str = Query(None, description="전화번호"),
    recreationRoomYN: bool = Query(..., description="놀이방 유무"),
    max_price: int = Query(None, description="최대 입장료"),
    time: str = Query(None, description="영업시간"),
):
    filtered_list = korea_sauna_data

    if name:
        filtered_list = [item for item in filtered_list if name in item[0]]
    if address:
        filtered_list = [item for item in filtered_list if address in item[1]]
    if phone:
        filtered_list = [item for item in filtered_list if phone in item[2]]
    filtered_list = [item for item in filtered_list if item[3] == recreationRoomYN]
    if max_price is not None:
        filtered_list = [item for item in filtered_list if item[4] <= max_price]
    if time:
        filtered_list = [item for item in filtered_list if time in item[5]]

    return filtered_list

air_fryer_data = [
    ["쿠쿠전자", "CAF-G0610DW", "바스켓형", 5, 78720, "레트로 감성, 후면 공기 배출구"],
    ["아이닉", "AO-16L", "오븐형", 16, 177990, "저소음, 논슬립 패드"],
    ["디디오랩", "DAP-I14DH", "오븐형", 14, 155990, "식기세척기 사용 가능"],
    ["재원전자", "FM1800", "오븐형", 8, 124000, "자동 전원 차단 기능"],
    ["보만", "AF41EG1I", "바스켓형", 4, 129000, "유리 바스켓"],
]

@app.get("/air_fryer")
def filter_air_fryer(
    manufacture: str = Query(None, description="제조사"),
    name: str = Query(None, description="모델명"),
    type: str = Query(..., description="형태 ex)앞문 개방형, 서랍형"),
    min_capacity: float = Query(None, description="최저 용량(L)"),
    min_price: int = Query(None, description="최소 가격"),
    max_price: int = Query(None, description="최대 가격"),
    keyword: str = Query(None, description="에어프라이어의 특징을 검색하는 키워드입니다."),
):
    filtered_list = air_fryer_data

    if manufacture:
        filtered_list = [item for item in filtered_list if manufacture in item[0]]
    if name:
        filtered_list = [item for item in filtered_list if name in item[1]]
    filtered_list = [item for item in filtered_list if item[2] == type]
    if min_capacity is not None:
        filtered_list = [item for item in filtered_list if item[3] >= min_capacity]
    if min_price is not None:
        filtered_list = [item for item in filtered_list if item[4] >= min_price]
    if max_price is not None:
        filtered_list = [item for item in filtered_list if item[4] <= max_price]
    if keyword:
        filtered_list = [item for item in filtered_list if keyword in item[5]]

    return filtered_list

dog_harness_data = [
    ["바잇미", "Y형", ["s", "m", "l"], 32900, "두껍고 튼튼한 웨빙"],
    ["후르타", "L형", ["xs", "s", "m", "l", "2l"], 51000, "탈부착 리플렉터"],
    ["후르타", "Y형", ["sm", "m", "l", "3l"], 51000, "손잡이 부착"],
    ["인히어런트", "Y형", ["xs", "s", "m"], 17000, "아세탈 재질로 충격완화 가능"],
    ["하울고", "L형", ["l", "2l"], 14000, "국내 생산 고급 부자재"],
]

@app.get("/dog_harness")
def filter_dog_harness(
    brand: str = Query(None, description="브랜드"),
    type: str = Query(..., description="형태 ex)H형, L형, Y형"),
    size: str = Query(None, description="사이즈 ex) xs, s, m, l, 2l"),
    min_price: int = Query(None, description="최소 가격"),
    max_price: int = Query(None, description="최대 가격"),
    keyword: str = Query(None, description="하네스의 특징을 검색하는 키워드입니다."),
):
    filtered_list = dog_harness_data

    if brand:
        filtered_list = [item for item in filtered_list if brand in item[0]]
    filtered_list = [item for item in filtered_list if item[1] == type]
    if size:
        filtered_list = [item for item in filtered_list if size in item[2]]
    if min_price is not None:
        filtered_list = [item for item in filtered_list if item[3] >= min_price]
    if max_price is not None:
        filtered_list = [item for item in filtered_list if item[3] <= max_price]
    if keyword:
        filtered_list = [item for item in filtered_list if keyword in item[4]]

    return filtered_list

accommodations_reservation_data = [
    ["부킹닷컴", "김비안", "010-0000-0001", 5, "2023.08.01", "2023.08.05", True, 580000],
    ["에어비앤비", "강수인", "010-0000-0002", 2, "2023.08.03", "2023.08.05", False, 320000],
    ["아고다", "안지영", "010-0000-0003", 3, "2023.08.13", "2023.08.19", False, 800000],
    ["아고다", "공성철", "010-0000-0004", 4, "2023.08.15", "2023.08.16", True, 150000],
    ["에어비앤비", "한다름", "010-0000-0005", 6, "2023.08.06", "2023.08.08", True, 310000],
]

@app.get("/accommodations_reservation")
def filter_accommodations_reservation(
    route: str = Query(..., description="숙소 예약 경로 ex) 아고다, 부킹닷컴, 에어비앤비"),
    name: str = Query(None, description="예약자명"),
    phone: str = Query(None, description="전화번호"),
    min_people: int = Query(None, description="최소 예약인원"),
    min_inDay: str = Query(None, description="최소 입실일"),
    max_outDay: str = Query(None, description="최대 퇴실일"),
    petTF: bool = Query(None, description="반려동물 동반 여부"),
    min_price: int = Query(None, description="최소 가격"),
):
    filtered_list = accommodations_reservation_data

    filtered_list = [item for item in filtered_list if item[0] == route]
    if name:
        filtered_list = [item for item in filtered_list if name in item[1]]
    if phone:
        filtered_list = [item for item in filtered_list if phone in item[2]]
    if min_people is not None:
        filtered_list = [item for item in filtered_list if item[3] >= min_people]
    if min_inDay:
        filtered_list = [item for item in filtered_list if item[4] >= min_inDay]
    if max_outDay:
        filtered_list = [item for item in filtered_list if item[5] <= max_outDay]
    if petTF is not None:
        filtered_list = [item for item in filtered_list if item[6] == petTF]
    if min_price is not None:
        filtered_list = [item for item in filtered_list if item[7] >= min_price]

    return filtered_list

apptech_reward_data = [
    ["모니모", "출석", 41, "2023.08.01", False, True],
    ["페이북", "구독", 30, "2023.08.01", True, True],
    ["모니모", "걷기", 24, "2023.08.02", False, True],
    ["국민은행", "퀴즈", 20, "2023.08.05", False, True],
    ["캐시워크", "걷기", 100, "2023.08.02", True, False],
]

@app.get("/apptech_reward")
def filter_apptech_reward(
    appName: str = Query(None, description="어플 이름 ex)캐시워크, 모니모, 캐시닥, 국민은행"),
    category: str = Query(..., description="카테고리 ex) 출석체크, 퀴즈, 미션, 구독"),
    min_reward: int = Query(None, description="최소 리워드"),
    max_reward: int = Query(None, description="최대 리워드"),
    date: str = Query(None, description="참여일자"),
    goodsExchangeTF: bool = Query(None, description="상품 교환 가능 여부"),
    cashExchangeTF: bool = Query(None, description="현금 교환 가능 여부"),
):
    filtered_list = apptech_reward_data

    if appName:
        filtered_list = [item for item in filtered_list if item[0] == appName]
    filtered_list = [item for item in filtered_list if item[1] == category]
    if min_reward is not None:
        filtered_list = [item for item in filtered_list if item[2] >= min_reward]
    if max_reward is not None:
        filtered_list = [item for item in filtered_list if item[2] <= max_reward]
    if date:
        filtered_list = [item for item in filtered_list if item[3] == date]
    if goodsExchangeTF is not None:
        filtered_list = [item for item in filtered_list if item[4] == goodsExchangeTF]
    if cashExchangeTF is not None:
        filtered_list = [item for item in filtered_list if item[5] == cashExchangeTF]

    return filtered_list

train_line_data = [
    ["SRT", "569", "천안", "대전", "08:15", "08:30", 7200, 152],
    ["무궁화호", "447", "대구", "용산", "17:00", "22:30", 19000, 301],
    ["KTX", "1523", "수원", "전주", "15:42", "17:15", 31000, 15],
    ["ITX", "778", "대전", "부산", "18:00", "19:46", 21000, 50],
    ["KTX", "1671", "순천", "천안", "10:00", "11:10", 23500, 3],
]

@app.get("/train_line")
def filter_train_line(
    trainType: str = Query(None, description="열차 종류 ex) KTX, SRT, 무궁화호, ITX"),
    trainNum: str = Query(None, description="열차 번호"),
    departure: str = Query(None, description="출발지"),
    arrival: str = Query(..., description="도착지"),
    min_departureTime: str = Query(None, description="최소 출발시간"),
    max_arrivalTime: str = Query(None, description="최대 도착시간"),
    max_price: int = Query(None, description="최대 가격"),
    min_availableSeat: int = Query(None, description="최소 예약가능한 좌석 수"),
):
    filtered_list = train_line_data

    if trainType:
        filtered_list = [item for item in filtered_list if item[0] == trainType]
    if trainNum:
        filtered_list = [item for item in filtered_list if item[1] == trainNum]
    if departure:
        filtered_list = [item for item in filtered_list if item[2] == departure]
    filtered_list = [item for item in filtered_list if item[3] == arrival]
    if min_departureTime:
        filtered_list = [item for item in filtered_list if item[4] >= min_departureTime]
    if max_arrivalTime:
        filtered_list = [item for item in filtered_list if item[5] <= max_arrivalTime]
    if max_price:
        filtered_list = [item for item in filtered_list if item[6] <= max_price]
    if min_availableSeat:
        filtered_list = [item for item in filtered_list if item[7] >= min_availableSeat]

    return filtered_list

mobile_sub_brand_data = [
    ["슈가 모바일", 11, 300, 50, "U+", "LTE", 38000],
    ["이지 모바일", 25, 500, 500, "KT", "5G", 45000],
    ["인스 모바일", 5, 200, 200, "SKT", "LTE", 12000],
    ["티 플러스", 2, 100, 50, "U+", "LTE", 4500],
    ["모빙", 30, 500, 1000, "KT", "5G", 53000],
]

@app.get("/mobile_sub_brand")
def filter_mobile_sub_brand(
    telCompany: str = Query(None, description="통신사 ex) 스노우 모바일, 헬로우 모바일"),
    min_data: float = Query(None, description="최소 데이터(GB)"),
    min_call: int = Query(None, description="최소 통화(분)"),
    min_message: int = Query(None, description="최소 문자"),
    network: str = Query(..., description="사용 망 ex) KT, SKT, U+"),
    lte5G: str = Query(None, description="데이터 종류 ex) LTE or 5G"),
    max_price: int = Query(None, description="최대 월요금"),
):
    filtered_list = mobile_sub_brand_data

    if telCompany:
        filtered_list = [item for item in filtered_list if item[0] == telCompany]
    if min_data:
        filtered_list = [item for item in filtered_list if item[1] >= min_data]
    if min_call:
        filtered_list = [item for item in filtered_list if item[2] >= min_call]
    if min_message:
        filtered_list = [item for item in filtered_list if item[3] >= min_message]
    filtered_list = [item for item in filtered_list if item[4] == network]
    if lte5G:
        filtered_list = [item for item in filtered_list if item[5] == lte5G]
    if max_price:
        filtered_list = [item for item in filtered_list if item[6] <= max_price]

    return filtered_list

pod_cast_data = [
    ["손에 잡히는 경제", "MBC", "비즈니스", "매일", 4.7, 742],
    ["송은이 김숙의 비밀보장", "컨텐츠랩비보", "코미디", "화요일", 4.4, 420],
    ["여둘톡", "여둘톡", "일기", "수요일", 4.8, 60],
    ["주제넘는 데이트", "kyunakimberly", "예술", "금요일", 3.2, 10],
    ["김동환 이진우 정영진의 신과함께", "이브로드캐스팅", "비즈니스", "화요일", 3.9, 275],
]

@app.get("/pod_cast")
def filter_pod_cast(
    programName: str = Query(None, description="프로그램 이름 ex) 손에 잡히는 경제, 북저널리즘, 듣똑라"),
    copyright: str = Query(None, description="저작권"),
    category: str = Query(..., description="카테고리 ex) 코미디, 비즈니스, 투자, 교육"),
    updatePeriod: str = Query(None, description="업데이트 주기 ex) 매일, 월요일, 수요일"),
    min_grade: float = Query(None, description="최소 평점", ge=0, le=5),
    min_episodeNum: int = Query(None, description="최소 에피소드 수"),
):
    filtered_list = pod_cast_data

    if programName:
        filtered_list = [item for item in filtered_list if item[0] == programName]
    if copyright:
        filtered_list = [item for item in filtered_list if item[1] == copyright]
    filtered_list = [item for item in filtered_list if item[2] == category]
    if updatePeriod:
        filtered_list = [item for item in filtered_list if item[3] == updatePeriod]
    if min_grade:
        filtered_list = [item for item in filtered_list if item[4] >= min_grade]
    if min_episodeNum:
        filtered_list = [item for item in filtered_list if item[5] >= min_episodeNum]

    return filtered_list

olympic_accomodation_data = [
    ["벨기에", "알파인 스키", 3, ["샘 마스", "아르망 마르샹", "드리스 판덴브루커"], "101동", "201호"],
    ["우크라이나", "알파인 스키", 6, ["이반 코프바스니유크", "아나스타샤 셰필렌코"], "102동", "101호"],
    ["브라질", "봅슬레이", 6, ["에드송 루케스 빈딜라티", "에릭 길손 비안나 제로니모", "에드송 히카르두 마륭스", "하파에우 수자 다시우", "재클린 모라우"], "201동", "301호"],
    ["이스라엘", "피겨 스케이팅", 2, ["알렉세이 바이첸코"], "102동", "501호"],
    ["벨라루스", "스피드 스케이팅", 4, ["이그나트 골로바추크", "한나 니판타바", "에카테리나 슬로에바", "야우헤니야 바라뵤바"], "101동", "103호"],
]

@app.get("/olympic_accomodation")
def filter_olympic_accomodation(
    country: str = Query(None, description="나라"),
    events: str = Query(..., description="종목 ex) 스케이트, 양궁, 피겨 스케이팅, 축구"),
    min_people: int = Query(None, description="최소 인실"),
    player: str = Query(None, description="선수"),
    dong: str = Query(None, description="동"),
    ho: str = Query(None, description="호"),
):
    filtered_list = olympic_accomodation_data

    if country:
        filtered_list = [item for item in filtered_list if item[0] == country]
    filtered_list = [item for item in filtered_list if item[1] == events]
    if min_people:
        filtered_list = [item for item in filtered_list if item[2] >= min_people]
    if player:
        filtered_list = [item for item in filtered_list if player in item[3]]
    if dong:
        filtered_list = [item for item in filtered_list if item[4] == dong]
    if ho:
        filtered_list = [item for item in filtered_list if item[5] == ho]

    return filtered_list

olympic_play_data = [
    ["양궁", "2020.07.24", "16:45", "16:00", ["한국", "일본"], ["SBS", "KBS", "MBC"]],
    ["수영", "2020.07.07", "10:43", "11:45", ["미국", "한국", "중국", "러시아"], ["SBS"]],
    ["남자 축구", "2020.07.23", "17:30", "19:25", ["한국", "온두라스"], ["KBS", "SBS"]],
    ["여자 배구", "2020.07.28", "21:40", "23:20", ["한국", "브라질"], ["MBC"]],
    ["태권도 여자", "2020.07.27", "21:30", "23:15", ["한국", "우크라이나", "그리스", "이탈리아", "가나", "프랑스"], ["KBS"]],
]

@app.get("/olympic_play")
def filter_olympic_play(
    events: str = Query(..., description="종목 ex) 스케이트, 양궁, 피겨 스케이팅, 축구"),
    min_date: str = Query(None, description="최소 날짜"),
    min_startTime: str = Query(None, description="최소 시작시간"),
    max_endTime: str = Query(None, description="최대 종료시간"),
    country: str = Query(None, description="출전 나라"),
    broadcast: str = Query(None, description="방영 채널"),
):
    filtered_list = olympic_play_data

    filtered_list = [item for item in filtered_list if item[0] == events]
    if min_date:
        filtered_list = [item for item in filtered_list if item[1] >= min_date]
    if min_startTime:
        filtered_list = [item for item in filtered_list if item[2] >= min_startTime]
    if max_endTime:
        filtered_list = [item for item in filtered_list if item[3] <= max_endTime]
    if country:
        filtered_list = [item for item in filtered_list if country in item[4]]
    if broadcast:
        filtered_list = [item for item in filtered_list if broadcast in item[5]]

    return filtered_list

delivery_order_data = [
    ["요기요", "불고기전골2", "서울 송파구 송파대로 32길 8 가락우성아파트", True, True, False, 35000],
    ["배달의 민족", "훈제구이 삼겹살(중)", "서울 송파구 중대로 24", True, False, False, 41000],
    ["쿠팡 잇츠", "고기주는 비빔냉면2+고기주는 물냉면2", "서울 송파구 동남로8길 25", True, True, True, 51000],
    ["배달의 민족", "고기듬뿍 도시락2+제육덮밥1", "서울 송파구 송파대로 345 헬리오시티", True, False, False, 28000],
    ["쿠팡 잇츠", "닭갈비정식1+제육덮밥", "서울 송파구 송파대로 39길", False, False, False, 18000],
]

@app.get("/delivery_order")
def filter_delivery_order(
    route: str = Query(..., description="주문 경로 ex) 배달의 민족, 요기요, 쿠팡잇츠"),
    cookingTF: bool = Query(None, description="조리 여부"),
    driverContectTF: bool = Query(None, description="배차 여부"),
    deliveryTF: bool = Query(None, description="배달완료 여부"),
    min_price: int = Query(None, description="최소 가격"),
    keyword: str = Query(None, description="주문 메뉴와 주소를 검색하는 키워드입니다."),
):
    filtered_list = delivery_order_data

    filtered_list = [item for item in filtered_list if item[0] == route]
    if cookingTF is not None:
        filtered_list = [item for item in filtered_list if item[3] == cookingTF]
    if driverContectTF is not None:
        filtered_list = [item for item in filtered_list if item[4] == driverContectTF]
    if deliveryTF is not None:
        filtered_list = [item for item in filtered_list if item[5] == deliveryTF]
    if min_price:
        filtered_list = [item for item in filtered_list if item[6] >= min_price]
    if keyword:
        filtered_list = [item for item in filtered_list if keyword in item[1] or keyword in item[2]]

    return filtered_list


cafeteria_menu_data = [
    ["2023.08.01", "한식", ["된장국", "계란말이", "새우볶음"], ["새우", "계란"], 450],
    ["2023.08.02", "중식", ["중국식 냉면", "볶음밥", "꽃빵"], ["땅콩", "계란"], 700],
    ["2023.08.02", "양식", ["알리오 올리오", "복숭아 샐러드", "함박스테이크"], ["복숭아"], 765],
    ["2023.08.05", "분식", ["떡볶이", "튀김", "순대"], ["새우"], 550],
    ["2023.08.06", "한식", ["김치찌개", "오이무침", "땅콩조림"], ["땅콩", "오이"], 380],
]

@app.get("/cafeteria_menu")
def filter_cafeteria_menu(
    date: str = Query(None, description="날짜"),
    category: str = Query(..., description="카테고리 ex) 한식, 중식, 일식, 양식"),
    menu: str = Query(None, description="메뉴 ex) 김치찌개, 우동"),
    allergyContain: str = Query(None, description="알레르기 유발 음식"),
    max_calory: int = Query(None, description="최대 칼로리"),
):
    filtered_list = cafeteria_menu_data

    if date is not None:
        filtered_list = [item for item in filtered_list if item[0] == date]
    filtered_list = [item for item in filtered_list if item[1] == category]
    if menu is not None:
        filtered_list = [item for item in filtered_list if menu in item[2]]
    if allergyContain is not None:
        filtered_list = [item for item in filtered_list if allergyContain in item[3]]
    if max_calory is not None:
        filtered_list = [item for item in filtered_list if item[4] <= max_calory]

    return filtered_list


game_grade_data = [
    [2, "Bronze", "Beginner", 400, 400],
    [16, "Silver", "Beginner", 5200, 22500],
    [48, "Bronze", "Veteran", 4600, 84500],
    [81, "Gold", "Veteran", 4800, 291100],
    [97, "Bronze", "Expert", 8400, 403900],
]

@app.get("/game_grade")
def filter_game_grade(
    level: int = Query(None, description="레벨"),
    medalColor: str = Query(..., description="메달색 ex) Bronze, Silver, Gold"),
    medalName: str = Query(None, description="메달 칭호 ex) Beginner, Veteran, Expert"),
    min_needExPoint: int = Query(None, description="최소 필요 경험치"),
    min_totalExPoint: int = Query(None, description="최소 총 경험치"),
    max_totalExPoint: int = Query(None, description="최대 총 경험치"),
):
    filtered_list = game_grade_data

    if level is not None:
        filtered_list = [item for item in filtered_list if item[0] == level]
    filtered_list = [item for item in filtered_list if item[1] == medalColor]
    if medalName is not None:
        filtered_list = [item for item in filtered_list if item[2] == medalName]
    if min_needExPoint is not None:
        filtered_list = [item for item in filtered_list if item[3] >= min_needExPoint]
    if min_totalExPoint is not None:
        filtered_list = [item for item in filtered_list if item[4] >= min_totalExPoint]
    if max_totalExPoint is not None:
        filtered_list = [item for item in filtered_list if item[4] <= max_totalExPoint]

    return filtered_list

form_roller_data = [
    ["파비츠", "하드", "EVA", 33, 14, True, 25600],
    ["이화에스엠피", "소프트", "EPP", 90, 60, False, 15900],
    ["뉴포츠", "소프트", "EVA", 35, 11.5, True, 12900],
    ["무브먼트", "하드", "EPP", 45, 8, False, 12000],
    ["고무나라", "하드", "EVA", 80, 15, False, 21000],
]

@app.get("/form_roller")
def filter_form_roller(
    brand: str = Query(None, description="브랜드"),
    hardSoft: str = Query(..., description="하드/소프트"),
    material: str = Query(None, description="재질 ex) EVA, EPP"),
    min_length: float = Query(None, description="최소 길이(cm)"),
    max_length: float = Query(None, description="최대 길이(cm)"),
    min_diameter: float = Query(None, description="최소 지름"),
    max_diameter: float = Query(None, description="최대 지름"),
    massageTF: bool = Query(None, description="지압형 여부"),
    max_price: int = Query(None, description="최대 가격"),
):
    filtered_list = form_roller_data

    if brand is not None:
        filtered_list = [item for item in filtered_list if item[0] == brand]
    filtered_list = [item for item in filtered_list if item[1] == hardSoft]
    if material is not None:
        filtered_list = [item for item in filtered_list if item[2] == material]
    if min_length is not None:
        filtered_list = [item for item in filtered_list if item[3] >= min_length]
    if max_length is not None:
        filtered_list = [item for item in filtered_list if item[3] <= max_length]
    if min_diameter is not None:
        filtered_list = [item for item in filtered_list if item[4] >= min_diameter]
    if max_diameter is not None:
        filtered_list = [item for item in filtered_list if item[4] <= max_diameter]
    if massageTF is not None:
        filtered_list = [item for item in filtered_list if item[5] == massageTF]
    if max_price is not None:
        filtered_list = [item for item in filtered_list if item[6] <= max_price]

    return filtered_list

weather_forecast_data = [
    ["2023.08.01", "서울", 30, 10, 24, 31],
    ["2023.08.01", "대전", 80, 75, 21, 28],
    ["2023.08.02", "부산", 90, 90, 28, 34],
    ["2023.08.03", "부산", 10, 5, 29, 35],
    ["2023.08.03", "서울", 20, 60, 25, 31],
]

@app.get("/weather_forecast")
def filter_weather_forecast(
    date: str = Query(..., description="날짜"),
    area: str = Query(None, description="지역"),
    amRainPer: float = Query(None, description="오전 강수 확률"),
    pmRainPer: float = Query(None, description="오후 강수 확률"),
    min_lowTemper: float = Query(None, description="최소 최저기온"),
    max_lowTemper: float = Query(None, description="최대 최저기온"),
    min_highTemper: float = Query(None, description="최소 최고기온"),
    max_highTemper: float = Query(None, description="최대 최고기온"),
):
    filtered_list = weather_forecast_data

    filtered_list = [item for item in filtered_list if item[0] == date]
    if area is not None:
        filtered_list = [item for item in filtered_list if item[1] == area]
    if amRainPer is not None:
        filtered_list = [item for item in filtered_list if item[2] == amRainPer]
    if pmRainPer is not None:
        filtered_list = [item for item in filtered_list if item[3] == pmRainPer]
    if min_lowTemper is not None:
        filtered_list = [item for item in filtered_list if item[4] >= min_lowTemper]
    if max_lowTemper is not None:
        filtered_list = [item for item in filtered_list if item[4] <= max_lowTemper]
    if min_highTemper is not None:
        filtered_list = [item for item in filtered_list if item[5] >= min_highTemper]
    if max_highTemper is not None:
        filtered_list = [item for item in filtered_list if item[5] <= max_highTemper]

    return filtered_list

spam_call_data = [
    ["02-0000-0001", "보이스피싱", 765, 1402, "검찰을 사칭해서 개인정보 요구"],
    ["042-0000-0001", "보험판매", 21, 85, "치아보험 가입 권유"],
    ["031-0000-0001", "보험판매", 55, 40, "한국생명 보험 가입 권유"],
    ["054-0000-0001", "휴대폰판매", 112, 358, "공짜폰인 것 처럼 휴대폰 판매"],
    ["02-0000-0002", "투자", 275, 120, "비트코인 포인트를 지급한다며 접근"],
]

@app.get("/spam_call")
def filter_spam_call(
    phoneNum: str = Query(None, description="스팸전화번호"),
    type: str = Query(..., description="신고유형 ex) 대출안내, 보험 판매, 보이스피싱"),
    min_reportCnt: int = Query(None, description="최소 스팸신고건수"),
    min_blockUserCnt: int = Query(None, description="최소 차단한 사용자 수"),
    keyword: str = Query(None, description="신고 내용을 검색하는 키워드입니다."),
):
    filtered_list = spam_call_data

    if phoneNum is not None:
        filtered_list = [item for item in filtered_list if item[0] == phoneNum]
    filtered_list = [item for item in filtered_list if item[1] == type]
    if min_reportCnt is not None:
        filtered_list = [item for item in filtered_list if item[2] >= min_reportCnt]
    if min_blockUserCnt is not None:
        filtered_list = [item for item in filtered_list if item[3] >= min_blockUserCnt]
    if keyword is not None:
        filtered_list = [item for item in filtered_list if keyword in item[4]]

    return filtered_list

power_strip_data = [
    ["AEGIS", 4, 1.5, True, True, 23862],
    ["모노케어", 4, 3, True, False, 7500],
    ["써지오", 3, 2, False, False, 5800],
    ["스윗홈", 6, 1.5, False, False, 7900],
    ["아이정", 2, 0.3, False, True, 15000],
]

@app.get("/power_strip")
def filter_power_strip(
    manufacture: str = Query(None, description="제조사"),
    min_holeCnt: int = Query(None, description="최소 멀티탭 구의 갯수"),
    max_holeCnt: int = Query(None, description="최대 멀티탭 구의 갯수"),
    min_length: float = Query(None, description="최저 길이(m)"),
    eachEnergy: bool = Query(..., description="개별절전 여부"),
    fireplugTF: bool = Query(None, description="자동소화기능 유무"),
    min_price: int = Query(None, description="최소 가격"),
    max_price: int = Query(None, description="최대 가격"),
):
    filtered_list = power_strip_data

    if manufacture is not None:
        filtered_list = [item for item in filtered_list if item[0] == manufacture]
    if min_holeCnt is not None:
        filtered_list = [item for item in filtered_list if item[1] >= min_holeCnt]
    if max_holeCnt is not None:
        filtered_list = [item for item in filtered_list if item[1] <= max_holeCnt]
    if min_length is not None:
        filtered_list = [item for item in filtered_list if item[2] >= min_length]
    filtered_list = [item for item in filtered_list if item[3] == eachEnergy]
    if fireplugTF is not None:
        filtered_list = [item for item in filtered_list if item[4] == fireplugTF]
    if min_price is not None:
        filtered_list = [item for item in filtered_list if item[5] >= min_price]
    if max_price is not None:
        filtered_list = [item for item in filtered_list if item[5] <= max_price]

    return filtered_list

package_forwarding_data = [
    ["김나영", "아레나 수영복", "스포츠", "미국", 1.2, 4500],
    ["안정아", "강아지 노즈워크 장난감", "반려동물", "캐나다", 3, 13000],
    ["유호식", "가정용 로봇청소기", "전자기기", "중국", 8, 21500],
    ["강순철", "텃밭가꾸기 공구 세트", "잡화", "미국", 15, 38000],
    ["임한빛", "어린이 영양젤리", "식품", "캐나다", 0.5, 4200],
]

@app.get("/package_forwarding")
def filter_package_forwarding(
    name: str = Query(None, description="주문자명"),
    product: str = Query(None, description="주문상품"),
    category: str = Query(None, description="카테고리 ex) 의류, 반려동물용품, 식품"),
    country: str = Query(..., description="나라"),
    min_weight: float = Query(None, description="최소 무게(kg)"),
    max_weight: float = Query(None, description="최대 무게(kg)"),
    min_deliverFee: int = Query(None, description="최소 택배비"),
    max_deliverFee: int = Query(None, description="최대 택배비"),
):
    filtered_list = package_forwarding_data

    if name is not None:
        filtered_list = [item for item in filtered_list if item[0] == name]
    if product is not None:
        filtered_list = [item for item in filtered_list if item[1] == product]
    if category is not None:
        filtered_list = [item for item in filtered_list if item[2] == category]
    filtered_list = [item for item in filtered_list if item[3] == country]
    if min_weight is not None:
        filtered_list = [item for item in filtered_list if item[4] >= min_weight]
    if max_weight is not None:
        filtered_list = [item for item in filtered_list if item[4] <= max_weight]
    if min_deliverFee is not None:
        filtered_list = [item for item in filtered_list if item[5] >= min_deliverFee]
    if max_deliverFee is not None:
        filtered_list = [item for item in filtered_list if item[5] <= max_deliverFee]

    return filtered_list

bank_deposit_data = [
    ["농협은행", "위례중앙점", 12, 3.2, 50],
    ["국민은행", "성남시청점", 12, 4.5, 20],
    ["국민은행", "강남구청점", 24, 6.1, 50],
    ["기업은행", "경주중앙점", 30, 5.5, 100],
    ["농협은행", "문정동지점", 24, 4.3, 30],
]

@app.get("/bank_deposit")
def filter_bank_deposit(
    bank: str = Query(..., description="은행이름"),
    spot: str = Query(None, description="지점명 ex)종로광장, 춘천"),
    duration: int = Query(None, description="납부기간(개월)"),
    min_rate: float = Query(None, description="최저 이율"),
    min_limit: int = Query(None, description="최소 월 입금 한도(만원)"),
):
    filtered_list = bank_deposit_data

    filtered_list = [item for item in filtered_list if item[0] == bank]
    if spot is not None:
        filtered_list = [item for item in filtered_list if item[1] == spot]
    if duration is not None:
        filtered_list = [item for item in filtered_list if item[2] == duration]
    if min_rate is not None:
        filtered_list = [item for item in filtered_list if item[3] >= min_rate]
    if min_limit is not None:
        filtered_list = [item for item in filtered_list if item[4] >= min_limit]

    return filtered_list

question_investigation_data = [
    ["사회", "지역축제 바가지 요금 논란", 2000, 54785, 15, True],
    ["경제", "라면값 인하", 1500, 335424, 5, False],
    ["경제", "금융사기 가해자에 대한 처벌방법", 2500, 11247667, 35, True],
    ["연예", "오징어게임2 과연 흥행할까?", 5000, 45778354, 20, True],
    ["사회", "강력범죄 가해자의 신상공개", 3000, 1523444, 10, False],
]

@app.get("/question_investigation")
def filter_question_investigation(
    category: str = Query(..., description="카테고리 ex)사회, 정치, 경제, 연예"),
    question_name: str = Query(None, description="설문조사명"),
    min_total_people: int = Query(None, description="최소 최대인원(만명)"),
    min_join_people: int = Query(None, description="최소 현재 참여자 수"),
    max_join_people: int = Query(None, description="최대 현재 참여자 수"),
    max_question: int = Query(None, description="최대 문항 수"),
    join_tf: bool = Query(None, description="참여 여부"),
):
    filtered_list = question_investigation_data

    filtered_list = [item for item in filtered_list if item[0] == category]
    if question_name is not None:
        filtered_list = [item for item in filtered_list if question_name in item[1] ]
    if min_total_people is not None:
        filtered_list = [item for item in filtered_list if item[2] >= min_total_people]
    if min_join_people is not None:
        filtered_list = [item for item in filtered_list if item[2] >= min_join_people]
    if max_join_people is not None:
        filtered_list = [item for item in filtered_list if item[3] <= max_join_people]
    if max_question is not None:
        filtered_list = [item for item in filtered_list if item[4] <= max_question]
    if join_tf is not None:
        filtered_list = [item for item in filtered_list if item[5] == join_tf]

    return filtered_list

swimming_goggles_data = [
    ["미즈노", True, True, False, 38000],
    ["나이키스윔", False, True, True, 45000],
    ["스피도", True, False, False, 29000],
    ["아레나", True, False, True, 32500],
    ["피닉스", False, True, True, 15000],
]

@app.get("/swimming_goggles")
def filter_swimming_goggles(
    brand: str = Query(None, description="브랜드"),
    mirror_tf: bool = Query(None, description="미러 유무"),
    packing_tf: bool = Query(..., description="패킹 유무"),
    strong_tf: bool = Query(None, description="도수가능여부"),
    min_price: int = Query(None, description="최소 가격"),
    max_price: int = Query(None, description="최대 가격"),
):
    filtered_list = swimming_goggles_data

    if brand is not None:
        filtered_list = [item for item in filtered_list if item[0] == brand]
    if mirror_tf is not None:
        filtered_list = [item for item in filtered_list if item[1] == mirror_tf]
    if strong_tf is not None:
        filtered_list = [item for item in filtered_list if item[3] == strong_tf]
    if min_price is not None:
        filtered_list = [item for item in filtered_list if item[4] >= min_price]
    if max_price is not None:
        filtered_list = [item for item in filtered_list if item[4] <= max_price]

    return filtered_list

@app.get("/bank_savings")
async def filter_bank_savings(
    bank: str = Query(..., description="은행"),
    spot: str = Query(None, description="지점명"),
    min_interest: float = Query(None, description="최소 금리(%)"),
    max_interest: float = Query(None, description="최대 금리(%)"),
    duration: int = Query(None, description="가입기간(개월)"),
    min_contLimit: int = Query(None, description="최소 계약금액한도(만원)"),
    max_contLimit: int = Query(None, description="최대 계약금액한도(만원)"),
    signWay: str = Query(None, description="가입 방법(대면/비대면)"),
):
    # 예금 상품 정보 데이터
    bank_savings = [
        {"bank": "새마을금고", "spot": "파주", "interest": 5.7, "duration": 12, "contLimit": 5000, "signWay": "대면"},
        {"bank": "농협은행", "spot": "안양", "interest": 4.5, "duration": 24, "contLimit": 3000, "signWay": "비대면"},
        {"bank": "새마을금고", "spot": "강북", "interest": 3.8, "duration": 12, "contLimit": 10000, "signWay": "비대면"},
        {"bank": "신협", "spot": "춘천", "interest": 2.1, "duration": 6, "contLimit": 7000, "signWay": "대면"},
        {"bank": "우리은행", "spot": "단대오거리", "interest": 6.1, "duration": 36, "contLimit": 10000, "signWay": "비대면"},
    ]

    filtered_savings = []

    for saving in bank_savings:
        if (
            (saving["bank"] == bank) and
            (saving["spot"] == spot if spot else True) and
            (saving["interest"] >= min_interest if min_interest is not None else True) and
            (saving["interest"] <= max_interest if max_interest is not None else True) and
            (saving["duration"] == duration if duration is not None else True) and
            (saving["contLimit"] >= min_contLimit if min_contLimit is not None else True) and
            (saving["contLimit"] <= max_contLimit if max_contLimit is not None else True) and
            (saving["signWay"] == signWay if signWay else True)
        ):
            filtered_savings.append(saving)

    return filtered_savings

exchange_student_data = [
    ["김유라", "미국", "정치외교", "2211342", 4.12, 950],
    ["김형식", "영국", "경영", "220115", 4.30, 800],
    ["안재훈", "호주", "영어영문", "222704", 2.93, 980],
    ["한현화", "미국", "경영", "223085", 3.52, 700],
    ["차영혜", "호주", "산업공학", "222784", 3.14, 650],
]

@app.get("/exchange_student")
def filter_exchange_student(
    name: str = Query(None, description="이름"),
    country: str = Query(..., description="희망국가"),
    major: str = Query(None, description="학과"),
    student_id: str = Query(None, description="학번"),
    min_grade: float = Query(None, ge=0, le=5, description="최소 성적"),
    max_grade: float = Query(None, ge=0, le=5, description="최대 성적"),
    min_eng_score: int = Query(None, le=990, description="최소 영어점수"),
):
    filtered_list = exchange_student_data

    if name is not None:
        filtered_list = [item for item in filtered_list if item[0] == name]
    filtered_list = [item for item in filtered_list if item[1] == country]
    if major is not None:
        filtered_list = [item for item in filtered_list if item[2] == major]
    if student_id is not None:
        filtered_list = [item for item in filtered_list if item[3] == student_id]
    if min_grade is not None:
        filtered_list = [item for item in filtered_list if item[4] >= min_grade]
    if max_grade is not None:
        filtered_list = [item for item in filtered_list if item[4] <= max_grade]
    if min_eng_score is not None:
        filtered_list = [item for item in filtered_list if item[5] >= min_eng_score]

    return filtered_list

used_trading_data = [
    ["하얀마음", "송파동", "반려동물", "강아지하네스+리쉬", 45000, False, "판매중"],
    ["김두팔", "가락동", "의류", "한번 시착한 여름 원피스", 25600, True, "예약중"],
    ["지지언니", "문정동", "전자기기", "아이폰13 미니 스타라이트", 300000, False, "거래완료"],
    ["유리아빠다", "송파동", "전자기기", "소니 영상용 카메라", 500000, True, "판매중"],
    ["문정야구팬", "문정동", "스포츠", "야구공+글로브 세트", 10000, False, "판매중"],
]

@app.get("/used_trading")
def filter_used_trading(
    name: str = Query(None, description="거래자명"),
    region: str = Query(..., description="거래지역(동)"),
    category: str = Query(None, description="카테고리 ex)가전제품, 가구, 식품, 의류"),
    product_name: str = Query(None, description="상품명"),
    min_price: int = Query(None, description="최소 가격"),
    max_price: int = Query(None, description="최대 가격"),
    discount_tf: bool = Query(None, description="가격제안여부"),
    state: str = Query(None, description="거래상태 ex) 판매중, 예약중, 거래완료"),
):
    filtered_list = used_trading_data

    if name is not None:
        filtered_list = [item for item in filtered_list if item[0] == name]
    filtered_list = [item for item in filtered_list if item[1] == region]
    if category is not None:
        filtered_list = [item for item in filtered_list if item[2] == category]
    if product_name is not None:
        filtered_list = [item for item in filtered_list if item[3] == product_name]
    if min_price is not None:
        filtered_list = [item for item in filtered_list if item[4] >= min_price]
    if max_price is not None:
        filtered_list = [item for item in filtered_list if item[4] <= max_price]
    if discount_tf is not None:
        filtered_list = [item for item in filtered_list if item[5] == discount_tf]
    if state is not None:
        filtered_list = [item for item in filtered_list if item[6] == state]

    return filtered_list

sidedish_grocery_data = [
    ["진미채 오징어볶음", "마른반찬", ["땅콩"], "2023.08.01", "2023.08.21", 260],
    ["어묵탕", "탕", ["새우", "꽃게"], "2023.08.02", "2023.08.09", 450],
    ["갈비찜", "고기반찬", ["밤"], "2023.08.01", "2023.08.16", 700],
    ["꽃게 된장국", "국", ["꽃게"], "2023.08.02", "2023.08.05", 330],
    ["오이소박이", "김치", ["오이", "복숭아"], "2023.08.03", "2023.09.03", 625],
]

@app.get("/sidedish_grocery")
def filter_sidedish_grocery(
    name: str = Query(None, description="상품명"),
    category: str = Query(None, description="카테고리 ex)국, 김치, 고기반찬, 마른반찬"),
    allergy_contain: str = Query(None, description="알레르기 성분"),
    min_product_date: str = Query(None, description="최소 만든 날짜 (ex. XXXX.YY.ZZ)"),
    max_exp_date: str = Query(None, description="최대 섭취날짜 (ex. XXXX.YY.ZZ)"),
    min_calory: float = Query(None, description="최소 칼로리"),
    max_calory: float = Query(None, description="최대 칼로리"),
):
    filtered_list = sidedish_grocery_data

    if name is not None:
        filtered_list = [item for item in filtered_list if item[0] == name]
    if category is not None:
        filtered_list = [item for item in filtered_list if item[1] == category]
    if allergy_contain is not None:
        filtered_list = [item for item in filtered_list if allergy_contain in item[2]]
    if min_product_date is not None:
        filtered_list = [item for item in filtered_list if item[3] >= min_product_date]
    if max_exp_date is not None:
        filtered_list = [item for item in filtered_list if item[4] <= max_exp_date]
    if min_calory is not None:
        filtered_list = [item for item in filtered_list if item[5] >= min_calory]
    if max_calory is not None:
        filtered_list = [item for item in filtered_list if item[5] <= max_calory]

    return filtered_list

talent_market_data = [
    ["건강", 4.1, 60000, "힙따봉", 1, "개인"],
    ["미용", 3.85, 50000, "퍼스널상담소", 2, "기업"],
    ["공예", 4.7, 45000, "라탄연구소", 3, "기업"],
    ["건강", 3.2, 60000, "런닝메이트 훈", 1, "개인"],
    ["공예", 3.6, 65000, "공블리", 5, "개인"],
]

@app.get("/talent_market")
def filter_talent_market(
    category: str = Query(None, description="카테고리 ex)it, 공예, 마케팅, 인테리어"),
    min_grade: float = Query(None, description="최소 평점", ge=0, le=5),
    max_price: int = Query(None, description="최대 가격"),
    name: str = Query(None, description="전문가 이름"),
    max_answer_time: float = Query(None, description="최대 평균응답시간(시간)"),
    sort: str = Query(None, description="회원구분 ex)개인/기업"),
):
    filtered_list = talent_market_data

    if category is not None:
        filtered_list = [item for item in filtered_list if item[0] == category]
    if min_grade is not None:
        filtered_list = [item for item in filtered_list if item[1] >= min_grade]
    if max_price is not None:
        filtered_list = [item for item in filtered_list if item[2] <= max_price]
    if name is not None:
        filtered_list = [item for item in filtered_list if item[3] == name]
    if max_answer_time is not None:
        filtered_list = [item for item in filtered_list if item[4] <= max_answer_time]
    if sort is not None:
        filtered_list = [item for item in filtered_list if item[5] == sort]

    return filtered_list

parttime_job_data = [
    ["김훈사무실", "사무", ["수요일", "금요일"], "09:00", "18:00", 1, 10000],
    ["독서의민족", "IT", ["화요일"], "08:30", "17:30", 6, 12000],
    ["서울대 수학학원", "교육", ["월요일", "수요일", "금요일"], "14:00", "20:00", 5, 15000],
    ["김영 영어학원", "교육", ["화요일", "목요일"], "09:00", "15:00", 12, 20000],
    ["떡볶이연구소", "사무", ["월요일"], "15:00", "19:00", 3, 9500],
]

@app.get("/parttime_job")
def filter_parttime_job(
    company: str = Query(None, description="회사명"),
    category: str = Query(None, description="카테고리 ex) 교육, 요식업, IT"),
    day: str = Query(None, description="요일"),
    min_in_time: str = Query(None, description="최소 출근시간"),
    max_out_time: str = Query(None, description="최대 퇴근시간"),
    max_duration: int = Query(None, description="최대 기간(개월)"),
    min_pay: int = Query(None, description="최소 시급(만원)"),
):
    filtered_list = parttime_job_data

    if company is not None:
        filtered_list = [item for item in filtered_list if item[0] == company]
    if category is not None:
        filtered_list = [item for item in filtered_list if item[1] == category]
    if day is not None:
        filtered_list = [item for item in filtered_list if day in item[2]]
    if min_in_time is not None:
        filtered_list = [item for item in filtered_list if item[3] >= min_in_time]
    if max_out_time is not None:
        filtered_list = [item for item in filtered_list if item[4] <= max_out_time]
    if max_duration is not None:
        filtered_list = [item for item in filtered_list if item[5] <= max_duration]
    if min_pay is not None:
        filtered_list = [item for item in filtered_list if item[6] >= min_pay]

    return filtered_list


betta_fish_data = [
    ["하프문", "수컷", "화이트", 50000, "덤보, 빅이어 종류로 순백색 베타입니다", True],
    ["크라운", "수컷", "블랙", 58000, "블랙과 화이트가 섞인 블랙 드래손 크라운 베타입니다", True],
    ["플라캇", "암컷", "캔디", 60000, "캔디 색상으로 불리는 조합의 베타입니다", True],
    ["롱테일", "수컷", "블루", 110000, "야생 베타 롱테일 핀 종류입니다", False],
    ["더블테일", "암컷", "레드", 70000, "더블테일의 레드 발색이 진한 베타입니다", True],
]

@app.get("/BettaFish")
def filter_betta_fish(
    category: str = Query(..., description="종류 (예: 하프문, 크라운 등)"),
    sex: str = Query(None, description="성별"),
    color: str = Query(None, description="색상 (예: 화이트, 블랙, 캔디 등)"),
    min_price: int = Query(None, description="최소 가격"),
    max_price: int = Query(None, description="최대 가격"),
    available: bool = Query(None, description="예약가능여부"),
):
    filtered_list = betta_fish_data

    filtered_list = [item for item in filtered_list if item[0] == category]

    if sex is not None:
        filtered_list = [item for item in filtered_list if item[1] == sex]
    if color is not None:
        filtered_list = [item for item in filtered_list if item[2] == color]
    if min_price is not None:
        filtered_list = [item for item in filtered_list if item[3] >= min_price]
    if max_price is not None:
        filtered_list = [item for item in filtered_list if item[3] <= max_price]
    if available is not None:
        filtered_list = [item for item in filtered_list if item[5] == available]

    return filtered_list

water_plant_data = [
    ["크립토코리네 팔바", "전경수초", True, 13000, "키가 작은 크립토코리네이며 다른 종보다 더 많은 빛을 필요로 합니다."],
    ["미크란테뭄 몬테카를로", "전경수초", True, 11000, "적은 광량에서도 성장하지만 예쁜 모습을 위해서는 높은 광량이 좋습니다."],
    ["알테란테라 레이넥키 미니", "중경수초", True, 13000, "짙은 빨강을 유지하려면 높은 빛을 필요로 합니다."],
    ["아포노게톤 마다가스카렌시스", "후경수초", False, 25000, "대형으로 자라는 레이스 플랜트입니다."],
    ["발리스네리아 나나", "후경수초", True, 15000, "가는 줄기를 가진 식물입니다. 작은 수조에도 잘 어울립니다."]
]

@app.get("/WaterPlant")
def filter_water_plant(
    name: str = Query(None, description="수초이름"),
    use: str = Query(..., description="용도 (예: 전경수초, 중경수초, 후경수초 등)"),
    tissue_culture: bool = Query(None, description="조직배양수초여부"),
    min_price: int = Query(None, description="최소 가격"),
    max_price: int = Query(None, description="최대 가격"),
):
    filtered_list = water_plant_data

    if name is not None:
        filtered_list = [item for item in filtered_list if item[0] == name]

    filtered_list = [item for item in filtered_list if item[1] == use]

    if tissue_culture is not None:
        filtered_list = [item for item in filtered_list if item[2] == tissue_culture]
    if min_price is not None:
        filtered_list = [item for item in filtered_list if item[3] >= min_price]
    if max_price is not None:
        filtered_list = [item for item in filtered_list if item[3] <= max_price]

    return filtered_list

pajama_data = [
    ["블루 스트라이프", "반팔 반바지 세트", ["S", "M", "L"], "여성", "순면", 45000, "순면 소재의 시원한 색감."],
    ["꼬빠", "반팔 반바지 세트", ["S", "M"], "여성", "면 혼방", 55000, "레트로하고 귀여운 무드."],
    ["마레", "반팔 반바지 세트", ["S", "M", "L", "XL"], "공용", "순면", 65000, "플로럴 패턴이 들어간 남여공용 파자마."],
    ["여름느낌", "반팔 긴바지 세트", ["S", "M", "L"], "남성", "거즈면", 55000, "거즈면 소재로 시원함"],
    ["블랑 셋업", "나시 긴바지 세트", ["S", "M", "L"], "여성", "레이온", 75000, "고급스러운 무드."]
]

@app.get("/Pajama")
def filter_pajama(
    name: str = Query(None, description="상품이름"),
    category: str = Query(..., description="종류 (예: 반팔 반바지 세트, 나시 긴바지 세트 등)"),
    size: str = Query(None, description="사이즈 (예: S, M, L 등)"),
    gender: str = Query(None, description="성별 (예: 남성, 여성)"),
    texture: str = Query(None, description="소재 (예: 순면, 면 혼방 등)"),
    min_price: int = Query(None, description="최소 가격"),
    max_price: int = Query(None, description="최대 가격"),
):
    filtered_list = pajama_data

    if name is not None:
        filtered_list = [item for item in filtered_list if item[0] == name]

    filtered_list = [item for item in filtered_list if item[1] == category]

    if size is not None:
        filtered_list = [item for item in filtered_list if size in item[2]]

    if gender is not None:
        filtered_list = [item for item in filtered_list if item[3] == gender]

    if texture is not None:
        filtered_list = [item for item in filtered_list if item[4] == texture]

    if min_price is not None:
        filtered_list = [item for item in filtered_list if item[5] >= min_price]

    if max_price is not None:
        filtered_list = [item for item in filtered_list if item[5] <= max_price]

    return filtered_list


@app.get("/NonCaffeine")
async def filter_non_caffeine(
    name: str = Query(None, description="음료이름"),
    stuff: str = Query(..., description="재료 (예: 보리, 우엉 등)"),
    cold: bool = Query(None, description="찬음료가능여부"),
    min_price: int = Query(None, description="최소 가격"),
    max_price: int = Query(None, description="최대 가격"),
):
    # 논카페인 음료 정보 데이터
    non_caffeine_drinks = [
        {"name": "진한 보리차", "stuff": ["보리"], "cold": True, "price": 4000, "desc": "국내산 보리를 직접 볶아서 진하게 끓여낸 보리차입니다."},
        {"name": "루이보스티", "stuff": ["루이보스"], "cold": False, "price": 4500, "desc": "프리미엄 루이보스를 사용하였습니다."},
        {"name": "검은콩차", "stuff": ["검은콩"], "cold": False, "price": 4500, "desc": "국내산 검은콩을 직접 볶아서 진하게 끓여낸 보리차입니다."},
        {"name": "우엉차", "stuff": ["우엉"], "cold": False, "price": 4500, "desc": "국내산 우엉을 사용한 차입니다."},
        {"name": "트로피컬 루이보스차", "stuff": ["루이보스", "레몬", "베르가못"], "cold": True, "price": 6000, "desc": "프리미엄 루이보스와 레몬필이 들어간 블랜딩 티입니다."},
    ]

    filtered_drinks = []

    for drink in non_caffeine_drinks:
        if (
            (drink["name"] == name if name else True) and
            (stuff in drink["stuff"]) and
            (drink["cold"] == cold if cold is not None else True) and
            (drink["price"] >= min_price if min_price is not None else True) and
            (drink["price"] <= max_price if max_price is not None else True)
        ):
            filtered_drinks.append(drink)

    return filtered_drinks

donator_data = [
    ["이윤희", "서울시", "없음", 33, 450000, False, "010-0000-0000"],
    ["이선화", "서울시", "환경연합", 53, 1200000, True, "010-0000-0000"],
    ["김지영", "인천시", "시민의숲", 45, 2300000, True, "010-0000-0000"],
    ["윤나영", "제주시", "없음", 23, 850000, False, "010-0000-0000"],
    ["김상혁", "제주시", "제주푸른터", 65, 4300000, True, "010-0000-0000"],
]

@app.get("/Donator")
def filter_donator(
    name: str = Query(None, description="성명"),
    location: str = Query(None, description="지역 (예: 서울시, 인천시 등)"),
    agency: str = Query(None, description="소속 (예: 없음, 환경연합 등)"),
    min_age: int = Query(None, description="최저연령"),
    max_age: int = Query(None, description="최고연령"),
    min_price: int = Query(None, description="최소금액"),
    max_price: int = Query(None, description="최대금액"),
    periodic: bool = Query(..., description="정기기부여부"),
):
    filtered_list = donator_data

    if name is not None:
        filtered_list = [item for item in filtered_list if item[0] == name]

    if location is not None:
        filtered_list = [item for item in filtered_list if item[1] == location]

    if agency is not None:
        filtered_list = [item for item in filtered_list if item[2] == agency]

    if min_age is not None:
        filtered_list = [item for item in filtered_list if item[3] >= min_age]

    if max_age is not None:
        filtered_list = [item for item in filtered_list if item[3] <= max_age]

    if min_price is not None:
        filtered_list = [item for item in filtered_list if item[4] >= min_price]

    if max_price is not None:
        filtered_list = [item for item in filtered_list if item[4] <= max_price]

    filtered_list = [item for item in filtered_list if item[5] == periodic]

    return filtered_list



volunteer_data = [
    ["이윤희", "서울시", "없음", 33, False, "2023-08-01", "010-0000-0000"],
    ["이선화", "서울시", "환경연합", 53, True, "2023-08-01", "010-0000-0000"],
    ["김지영", "인천시", "시민의숲", 45, True, "2023-08-02", "010-0000-0000"],
    ["윤나영", "제주시", "없음", 23, False, "2023-08-02", "010-0000-0000"],
    ["김상혁", "제주시", "제주푸른터", 65, True, "2023-08-03", "010-0000-0000"],
]

@app.get("/AnimalShelterVolunteer")
def filter_animal_shelter_volunteer(
    name: str = Query(None, description="성명"),
    location: str = Query(..., description="지역 (예: 서울시, 인천시 등)"),
    agency: str = Query(None, description="소속 (예: 없음, 환경연합 등)"),
    min_age: int = Query(None, description="최저연령"),
    max_age: int = Query(None, description="최고연령"),
    pet: bool = Query(None, description="반려동물여부"),
    date: str = Query(None, description="자원봉사일"),
):
    filtered_list = volunteer_data

    if name is not None:
        filtered_list = [item for item in filtered_list if item[0] == name]

    if agency is not None:
        filtered_list = [item for item in filtered_list if item[2] == agency]

    if min_age is not None:
        filtered_list = [item for item in filtered_list if item[3] >= min_age]

    if max_age is not None:
        filtered_list = [item for item in filtered_list if item[3] <= max_age]

    if pet is not None:
        filtered_list = [item for item in filtered_list if item[4] == pet]

    if date is not None:
        filtered_list = [item for item in filtered_list if item[5] == date]

    return filtered_list


customer_data = [
    ["이윤희", "서울시 마포구 연남로 43-2", "씰스티커", 23000, True, True, "010-0000-0000"],
    ["이선화", "서울시 마포구 연남동 390-56", "접이식 테이블", 43000, True, True, "010-0000-0000"],
    ["김지영", "서울시 관악구 인헌로 43-12", "돗자리세트", 32000, True, False, "010-0000-0000"],
    ["윤나영", "제주시 탑동로2길 3", "캠핑 테이블", 93000, False, False, "010-0000-0000"],
    ["김상혁", "제주시 한림읍 명랑로 8", "타프 스트랩", 19000, False, False, "010-0000-0000"],
]

@app.get("/GroupBuying")
def filter_group_buying(
    name: str = Query(None, description="성명"),
    location: str = Query(None, description="지역 (예: 서울시, 관악구, 마포구 등)"),
    product: str = Query(None, description="구매상품"),
    pay: bool = Query(..., description="입금여부"),
    delivery: bool = Query(None, description="발송여부"),
):
    filtered_list = customer_data

    if name is not None:
        filtered_list = [item for item in filtered_list if item[0] == name]

    if location is not None:
        filtered_list = [item for item in filtered_list if item[1] == location]

    if product is not None:
        filtered_list = [item for item in filtered_list if item[2] == product]

    if delivery is not None:
        filtered_list = [item for item in filtered_list if item[5] == delivery]

    return filtered_list


product_data = [
    ["레이스 양산", "화이트", "3단", True, False, 56000, 35],
    ["쿨링 제로퍼제로", "네이비", "5단", True, True, 75000, 15],
    ["눈꽃코팅", "화이트", "5단", False, False, 36000, 35],
    ["초경량 암막 양산", "블랙", "3단", True, True, 46000, 25],
    ["캐릭터 양산", "옐로우", "5단", True, False, 66000, 15],
]

@app.get("/SunUmbrella")
def filter_sun_umbrella(
    name: str = Query(None, description="상품명"),
    color: str = Query(..., description="색상 (예: 화이트, 네이비 등)"),
    category: str = Query(None, description="접이식종류 (예: 3단, 5단 등)"),
    uv_protection: bool = Query(None, description="자외선차단여부"),
    umbrella: bool = Query(None, description="우양산여부"),
    min_price: float = Query(None, ge=0, description="최소 가격"),
    max_price: float = Query(None, ge=0, description="최대 가격"),
):
    filtered_list = product_data

    if name is not None:
        filtered_list = [item for item in filtered_list if item[0] == name]

    if color is not None:
        filtered_list = [item for item in filtered_list if item[1] == color]

    if category is not None:
        filtered_list = [item for item in filtered_list if item[2] == category]

    if uv_protection is not None:
        filtered_list = [item for item in filtered_list if item[3] == uv_protection]

    if umbrella is not None:
        filtered_list = [item for item in filtered_list if item[4] == umbrella]

    if min_price is not None:
        filtered_list = [item for item in filtered_list if item[5] >= min_price]

    if max_price is not None:
        filtered_list = [item for item in filtered_list if item[5] <= max_price]

    return filtered_list

sticker_data = [
    ["레트로 다이어리 데코팩", "스몰데코", "모조지", 12000, 132],
    ["못난이 MBTI", "빅포인트", "유포지", 8000, 32],
    ["캘리 알파벳 숫자 세트", "손글씨", "PVC", 6500, 232],
    ["마음사진 세트 팩", "포토", "모조지", 8000, 92],
    ["피피 라벨링 스티커", "라벨", "모조지", 3000, 182],
]

@app.get("/StickerSearch")
def filter_sticker_search(
    name: str = Query(None, description="상품명"),
    d_category: str = Query(..., description="디자인종류 (예: 스몰데코, 빅포인트, 패턴, 포토,라벨, 손글씨 등)"),
    material: str = Query(None, description="재질 (예: 모조지, PVC 등)"),
    min_price: float = Query(None, ge=0, description="최소 가격"),
    max_price: float = Query(None, ge=0, description="최대 가격"),
):
    filtered_list = sticker_data

    if name is not None:
        filtered_list = [item for item in filtered_list if item[0] == name]

    if d_category is not None:
        filtered_list = [item for item in filtered_list if item[1] == d_category]

    if material is not None:
        filtered_list = [item for item in filtered_list if item[2] == material]

    if min_price is not None:
        filtered_list = [item for item in filtered_list if item[3] >= min_price]

    if max_price is not None:
        filtered_list = [item for item in filtered_list if item[3] <= max_price]

    return filtered_list

glass_data = [
    ["데플로리안 와인잔", "와인잔", 8900, False, 132],
    ["레트로 주름 유리컵", "고블렛", 8000, False, 32],
    ["레터링 스택글라스", "카페유리컵", 6500, False, 232],
    ["내열 플라워 유리컵", "일러스트컵", 18000, True, 92],
    ["킨토 내열 이중 브라운 글라스", "손잡이컵", 23000, True, 182],
]

@app.get("/GlassSearch")
def filter_glass_search(
    name: str = Query(None, description="상품명"),
    category: str = Query(..., description="형태별분류 (예: 와인잔, 고블렛, 손잡이컵, 일러스트컵, 카페유리컵 등)"),
    min_price: float = Query(None, ge=0, description="최소 가격"),
    max_price: float = Query(None, ge=0, description="최대 가격"),
    heatresisting: bool = Query(None, description="내열유리여부"),
):
    filtered_list = glass_data

    if name is not None:
        filtered_list = [item for item in filtered_list if item[0] == name]

    if category is not None:
        filtered_list = [item for item in filtered_list if item[1] == category]

    if min_price is not None:
        filtered_list = [item for item in filtered_list if item[2] >= min_price]

    if max_price is not None:
        filtered_list = [item for item in filtered_list if item[2] <= max_price]

    if heatresisting is not None:
        filtered_list = [item for item in filtered_list if item[3] == heatresisting]

    return filtered_list




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

flights = [
    {
        "id": 1,
        "airline": "대한항공",
        "departure" : "Seoul",
        "destination": "Jeju",
        "departure_time": "2023-06-01 09:00",
        "price": 100000
    },
    {
        "id": 2,
        "airline": "아시아나항공",
        "departure" : "Seoul",
        "destination": "Jeju",
        "departure_time": "2023-06-01 10:00",
        "price": 80000
    },
    {
        "id": 3,
        "airline": "제주항공",
        "departure" : "Seoul",
        "destination": "Jeju",
        "departure_time": "2023-06-01 11:00",
        "price": 50000
    }
]

# 가상의 인터넷 소설 데이터
novels = [
    {"title": "The Legendary Guardian", "author": "Shi Luo Ye", "downloads": 100000, "genre": "Fantasy", "release_year": 2015, "platform": "Webnovel"},
    {"title": "Rebirth of the Thief Who Roamed the World", "author": "Mad Snail", "downloads": 80000, "genre": "Game", "release_year": 2010, "platform": "Webnovel"},
    {"title": "Lord of the Mysteries", "author": "Cuttlefish That Loves Diving", "downloads": 90000, "genre": "Mystery", "release_year": 2017, "platform": "Qidian"},
    {"title": "The King's Avatar", "author": "Butterfly Blue", "downloads": 120000, "genre": "Game", "release_year": 2011, "platform": "Webnovel"},
    {"title": "The Great Ruler", "author": "Tian Can Tu Dou", "downloads": 70000, "genre": "Fantasy", "release_year": 2012, "platform": "Qidian"},
    {"title": "Release That Witch", "author": "Er Mu", "downloads": 95000, "genre": "Fantasy", "release_year": 2014, "platform": "Webnovel"},
    {"title": "The Legendary Mechanic", "author": "Chocolion", "downloads": 85000, "genre": "Game", "release_year": 2016, "platform": "Qidian"},
    {"title": "Martial God Asura", "author": "Kindhearted Bee", "downloads": 110000, "genre": "Fantasy", "release_year": 2013, "platform": "Webnovel"},
    {"title": "I Shall Seal the Heavens", "author": "Er Gen", "downloads": 75000, "genre": "Fantasy", "release_year": 2014, "platform": "Qidian"},
    {"title": "The Great Thief", "author": "Boating Lyrics", "downloads": 85000, "genre": "Game", "release_year": 2015, "platform": "Webnovel"}
]

# 가상의 영화 데이터
movies = [
    {"title": "The Shawshank Redemption", "director": "Frank Darabont", "year": 1994, "genre": "Drama", "rating": 9.3},
    {"title": "The Godfather", "director": "Francis Ford Coppola", "year": 1972, "genre": "Crime", "rating": 9.2},
    {"title": "The Dark Knight", "director": "Christopher Nolan", "year": 2008, "genre": "Action", "rating": 9.0},
    {"title": "Pulp Fiction", "director": "Quentin Tarantino", "year": 1994, "genre": "Crime", "rating": 8.9},
    {"title": "Fight Club", "director": "David Fincher", "year": 1999, "genre": "Drama", "rating": 8.8},
    {"title": "Inception", "director": "Christopher Nolan", "year": 2010, "genre": "Action", "rating": 8.7},
    {"title": "The Matrix", "director": "Lana Wachowski", "year": 1999, "genre": "Action", "rating": 8.7},
    {"title": "Goodfellas", "director": "Martin Scorsese", "year": 1990, "genre": "Crime", "rating": 8.7},
    {"title": "Seven", "director": "David Fincher", "year": 1995, "genre": "Crime", "rating": 8.6},
    {"title": "Interstellar", "director": "Christopher Nolan", "year": 2014, "genre": "Sci-Fi", "rating": 8.6}
]

#가상의 음악 데이터
songs = [
    {"title": "Shape of You", "artist": "Ed Sheeran", "rating": 4.8, "release_date": "2017-01-06", "genre": "Pop"},
    {"title": "Bohemian Rhapsody", "artist": "Queen", "rating": 4.9, "release_date": "1975-10-31", "genre": "Rock"},
    {"title": "Rolling in the Deep", "artist": "Adele", "rating": 4.7, "release_date": "2010-11-29", "genre": "Pop"},
    {"title": "Hotel California", "artist": "Eagles", "rating": 4.9, "release_date": "1977-02-22", "genre": "Rock"},
    {"title": "Imagine", "artist": "John Lennon", "rating": 4.8, "release_date": "1971-10-11", "genre": "Pop"},
    {"title": "Smells Like Teen Spirit", "artist": "Nirvana", "rating": 4.7, "release_date": "1991-09-10", "genre": "Rock"},
    {"title": "Viva la Vida", "artist": "Coldplay", "rating": 4.6, "release_date": "2008-05-25", "genre": "Pop"},
    {"title": "Stairway to Heaven", "artist": "Led Zeppelin", "rating": 4.9, "release_date": "1971-11-08", "genre": "Rock"},
    {"title": "Someone Like You", "artist": "Adele", "rating": 4.7, "release_date": "2011-01-24", "genre": "Pop"},
    {"title": "November Rain", "artist": "Guns N' Roses", "rating": 4.8, "release_date": "1992-02-18", "genre": "Rock"}
]

# 가상의 커피 원두 데이터
coffees = [
    {"name": "Colombian Supremo", "origin": "Colombia", "acidity": 4, "sweetness": 3, "bitterness": 2, "price": 15.99},
    {"name": "Ethiopian Yirgacheffe", "origin": "Ethiopia", "acidity": 5, "sweetness": 4, "bitterness": 1, "price": 17.99},
    {"name": "Costa Rican Tarrazu", "origin": "Costa Rica", "acidity": 3, "sweetness": 3, "bitterness": 3, "price": 14.99},
    {"name": "Guatemalan Antigua", "origin": "Guatemala", "acidity": 4, "sweetness": 2, "bitterness": 4, "price": 16.99},
    {"name": "Kenyan AA", "origin": "Kenya", "acidity": 5, "sweetness": 3, "bitterness": 2, "price": 18.99},
    {"name": "Brazilian Santos", "origin": "Brazil", "acidity": 2, "sweetness": 4, "bitterness": 3, "price": 12.99},
    {"name": "Sumatra Mandheling", "origin": "Indonesia", "acidity": 3, "sweetness": 2, "bitterness": 5, "price": 15.99},
    {"name": "Hawaiian Kona", "origin": "Hawaii", "acidity": 4, "sweetness": 4, "bitterness": 2, "price": 19.99},
    {"name": "Mexican Altura", "origin": "Mexico", "acidity": 3, "sweetness": 3, "bitterness": 3, "price": 13.99},
    {"name": "Tanzanian Peaberry", "origin": "Tanzania", "acidity": 4, "sweetness": 3, "bitterness": 2, "price": 17.99}
]

# 가상의 파스타 가게 메뉴 데이터
menu_items = [
    {"menu_name": "Spaghetti Bolognese", "price": 12.99, "spicy_level": 1, "calories": 800},
    {"menu_name": "Carbonara", "price": 11.99, "spicy_level": 2, "calories": 900},
    {"menu_name": "Arrabbiata", "price": 10.99, "spicy_level": 3, "calories": 750},
    {"menu_name": "Pesto Pasta", "price": 13.99, "spicy_level": 1, "calories": 850},
    {"menu_name": "Alfredo", "price": 12.99, "spicy_level": 1, "calories": 950},
    {"menu_name": "Aglio e Olio", "price": 10.99, "spicy_level": 2, "calories": 700},
    {"menu_name": "Vongole", "price": 14.99, "spicy_level": 1, "calories": 900},
    {"menu_name": "Puttanesca", "price": 11.99, "spicy_level": 3, "calories": 800},
    {"menu_name": "Seafood Linguine", "price": 15.99, "spicy_level": 2, "calories": 1000},
    {"menu_name": "Mushroom Risotto", "price": 12.99, "spicy_level": 1, "calories": 850}
]

# 가상의 옷 상품 데이터
products = [
    {"product_name": "T-Shirt", "price": 15.99, "category": "Clothing", "sale_colors": "blue", "sales": 100, "keywords": "casual"},
    {"product_name": "Jeans", "price": 49.99, "category": "Clothing", "sale_colors": "blue", "sales": 50, "keywords": "denim"},
    {"product_name": "Sneakers", "price": 79.99, "category": "Shoes", "sale_colors": "black", "sales": 80, "keywords": "athletic"},
    {"product_name": "Dress", "price": 39.99, "category": "Clothing", "sale_colors": "red", "sales": 30, "keywords": "formal"},
    {"product_name": "Jacket", "price": 89.99, "category": "Clothing", "sale_colors": "black", "sales": 20, "keywords": "outerwear"}
]

travel_packages = [
    {"destination": "Paris", "duration": "5 days", "price": 1500},
    {"destination": "Tokyo", "duration": "7 days", "price": 2500},
    {"destination": "New York", "duration": "4 days", "price": 1800},
    {"destination": "Rome", "duration": "6 days", "price": 2000},
    {"destination": "Bali", "duration": "10 days", "price": 3000},
    {"destination": "Cairo", "duration": "8 days", "price": 2200},
    {"destination": "Sydney", "duration": "7 days", "price": 2800},
    {"destination": "Cancun", "duration": "5 days", "price": 1700},
    {"destination": "Barcelona", "duration": "6 days", "price": 1900},
    {"destination": "Hawaii", "duration": "9 days", "price": 3200}
]

# 가상의 구직정보 데이터
job_listings = [
    {"company_name": "ABC Company", "salary": 50000, "position": "Software Engineer", "application_deadline": "2023-06-30", "employee_count": 100},
    {"company_name": "XYZ Corporation", "salary": 60000, "position": "Data Analyst", "application_deadline": "2023-07-15", "employee_count": 200},
    {"company_name": "DEF Enterprises", "salary": 55000, "position": "Marketing Specialist", "application_deadline": "2023-06-25", "employee_count": 150},
    {"company_name": "GHI Inc.", "salary": 70000, "position": "Product Manager", "application_deadline": "2023-07-10", "employee_count": 120},
    {"company_name": "JKL Solutions", "salary": 65000, "position": "Sales Representative", "application_deadline": "2023-07-05", "employee_count": 180},
    {"company_name": "MNO Corporation", "salary": 55000, "position": "HR Coordinator", "application_deadline": "2023-07-20", "employee_count": 100},
    {"company_name": "PQR Industries", "salary": 60000, "position": "Operations Manager", "application_deadline": "2023-07-08", "employee_count": 250},
    {"company_name": "STU Technologies", "salary": 70000, "position": "UX/UI Designer", "application_deadline": "2023-06-28", "employee_count": 80},
    {"company_name": "VWX Group", "salary": 55000, "position": "Accountant", "application_deadline": "2023-07-12", "employee_count": 130},
    {"company_name": "YZA Corporation", "salary": 60000, "position": "Customer Service Representative", "application_deadline": "2023-07-18", "employee_count": 150}
]

@app.get("/courses")
async def get_courses(
    id: str = Query(default=None),
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
        filtered_courses = [course for course in filtered_courses if id.lower() in course["id"].lower()]

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

    if 최소학점 is not None:
        # 학점 필터링
        filtered_courses = [course for course in filtered_courses if course["학점"] >= 최소학점]

    return filtered_courses

@app.get("/flights")
async def get_flights(
    id: int = Query(default=None),
    airline: str = Query(default=None),
    departure: str = Query(default=None),
    destination: str = Query(default=None),
    min_price: int = Query(default=None, gt=0),
    max_price: int = Query(default=None, gt=0)
):
    filtered_flights = flights

    if id is not None:
        # id 필터링
        filtered_flights = [flight for flight in filtered_flights if flight["id"] == id]

    if airline is not None:
        # 항공사명 포함 필터링
        filtered_flights = [flight for flight in filtered_flights if airline.lower() in flight["airline"].lower()]

    if departure is not None:
        # 출발지 포함 필터링
        filtered_flights = [flight for flight in filtered_flights if departure.lower() in flight["departure"].lower()]
        
    if destination is not None:
        # 도착지 포함 필터링
        filtered_flights = [flight for flight in filtered_flights if destination.lower() in flight["destination"].lower()]

    if min_price is not None:
        # 최소 가격 필터링
        filtered_flights = [flight for flight in filtered_flights if flight["price"] >= min_price]
        
    if max_price is not None:
        # 최대 가격 필터링
        filtered_flights = [flight for flight in filtered_flights if flight["price"] <= max_price]

    return filtered_flights

@app.get("/movies")
async def get_movies(
    title: str = Query(default=None),
    director: str = Query(default=None),
    genre: str = Query(default=None),
    min_rating: float = Query(default=None, ge=0.0, le=10.0)
):
    filtered_movies = movies

    if title is not None:
        # 제목 필터링
        filtered_movies = [movie for movie in filtered_movies if title.lower() in movie['title'].lower()]

    if director is not None:
        # 감독 필터링
        filtered_movies = [movie for movie in filtered_movies if director.lower() in movie['director'].lower()]

    if genre is not None:
        # 장르 필터링
        filtered_movies = [movie for movie in filtered_movies if genre.lower() == movie['genre'].lower()]

    if min_rating is not None:
        # 최소 평점 필터링
        filtered_movies = [movie for movie in filtered_movies if movie['rating'] >= min_rating]

    return filtered_movies

@app.get("/novels")
async def get_novels(
    title: str = Query(default=None),
    author: str = Query(default=None),
    platform: str = Query(default=None),
    genre: str = Query(default=None),
    min_downloads: int = Query(default=None, ge=0)
):
    filtered_novels = novels

    if title is not None:
        # 제목 필터링
        filtered_novels = [novel for novel in filtered_novels if title.lower() in novel['title'].lower()]

    if author is not None:
        # 작가 필터링
        filtered_novels = [novel for novel in filtered_novels if author.lower() in novel['author'].lower()]

    if platform is not None:
        # 플랫폼 필터링
        filtered_novels = [novel for novel in filtered_novels if platform.lower() == novel['platform'].lower()]

    if genre is not None:
        # 장르 필터링
        filtered_novels = [novel for novel in filtered_novels if genre.lower() == novel['genre'].lower()]

    if min_downloads is not None:
        # 최소 다운로드 필터링
        filtered_novels = [novel for novel in filtered_novels if novel['downloads'] >= min_downloads]

    return filtered_novels

@app.get("/songs")
async def get_songs(
    min_rating: float = Query(default=None, ge=0.0, le=5.0),
    genre: str = Query(default=None),
    title: str = Query(default=None),
    artist: str = Query(default=None),
    release_date: str = Query(default=None),
):
    filtered_songs = songs

    if min_rating is not None:
        # 최소 평점 필터링
        filtered_songs = [song for song in filtered_songs if song['rating'] >= min_rating]

    if genre is not None:
        # 장르 필터링
        filtered_songs = [song for song in filtered_songs if genre.lower() == song['genre'].lower()]

    if title is not None:
        # 제목 필터링
        filtered_songs = [song for song in filtered_songs if title.lower() in song['title'].lower()]

    if artist is not None:
        # 가수 필터링
        filtered_songs = [song for song in filtered_songs if artist.lower() in song['artist'].lower()]

    if release_date is not None:
        # 출시일 필터링
        filtered_songs = [song for song in filtered_songs if release_date == song['release_date']]

    return filtered_songs

@app.get("/coffees")
async def get_coffees(
    origin: str = Query(default=None),
    min_acidity: int = Query(default=None, ge=1, le=5),
    max_acidity: int = Query(default=None, ge=1, le=5),
    min_sweetness: int = Query(default=None, ge=1, le=5),
    max_sweetness: int = Query(default=None, ge=1, le=5),
    min_bitterness: int = Query(default=None, ge=1, le=5),
    max_bitterness: int = Query(default=None, ge=1, le=5),
    max_price: float = Query(default=None, ge=0),
):
    filtered_coffees = coffees

    if origin is not None:
        # 생산지 필터링
        filtered_coffees = [coffee for coffee in filtered_coffees if origin.lower() == coffee['origin'].lower()]

    if min_acidity is not None:
        # 최소 산미 필터링
        filtered_coffees = [coffee for coffee in filtered_coffees if coffee['acidity'] >= min_acidity]

    if max_acidity is not None:
        # 최대 산미 필터링
        filtered_coffees = [coffee for coffee in filtered_coffees if coffee['acidity'] <= max_acidity]

    if min_sweetness is not None:
        # 최소 당도 필터링
        filtered_coffees = [coffee for coffee in filtered_coffees if coffee['sweetness'] >= min_sweetness]

    if max_sweetness is not None:
        # 최대 당도 필터링
        filtered_coffees = [coffee for coffee in filtered_coffees if coffee['sweetness'] <= max_sweetness]

    if min_bitterness is not None:
        # 최소 쓴맛 필터링
        filtered_coffees = [coffee for coffee in filtered_coffees if coffee['bitterness'] >= min_bitterness]

    if max_bitterness is not None:
        # 최대 쓴맛 필터링
        filtered_coffees = [coffee for coffee in filtered_coffees if coffee['bitterness'] <= max_bitterness]

    if max_price is not None:
        # 최대 가격 필터링
        filtered_coffees = [coffee for coffee in filtered_coffees if coffee['price'] <= max_price]

    return filtered_coffees

@app.get("/menu")
async def get_menu(
    menu_name: str = Query(default=None),
    max_price: float = Query(default=None, ge=0),
    min_spicy_level: int = Query(default=None, ge=1, le=5),
    max_spicy_level: int = Query(default=None, ge=1, le=5),
    max_calories: int = Query(default=None, ge=0),
):
    filtered_menu = menu_items

    if menu_name is not None:
        # 메뉴 이름 필터링
        filtered_menu = [item for item in filtered_menu if menu_name.lower() in item['menu_name'].lower()]

    if max_price is not None:
        # 최대 가격 필터링
        filtered_menu = [item for item in filtered_menu if item['price'] <= max_price]

    if min_spicy_level is not None:
        # 최소 맵기 필터링
        filtered_menu = [item for item in filtered_menu if item['spicy_level'] >= min_spicy_level]

    if max_spicy_level is not None:
        # 최대 맵기 필터링
        filtered_menu = [item for item in filtered_menu if item['spicy_level'] <= max_spicy_level]

    if max_calories is not None:
        # 최대 칼로리 필터링
        filtered_menu = [item for item in filtered_menu if item['calories'] <= max_calories]

    return filtered_menu

@app.get("/products")
async def get_products(
    product_name: str = Query(default=None),
    max_price: float = Query(default=None, ge=0),
    category: str = Query(default=None),
    sale_colors: str = Query(default=None),
    min_sales: int = Query(default=None, ge=0),
    keywords: str = Query(default=None),
):
    filtered_products = products

    if product_name is not None:
        # 제품명 필터링
        filtered_products = [product for product in filtered_products if product_name.lower() in product['product_name'].lower()]

    if max_price is not None:
        # 최대 가격 필터링
        filtered_products = [product for product in filtered_products if product['price'] <= max_price]

    if category is not None:
        # 종류 필터링
        filtered_products = [product for product in filtered_products if product['category'].lower() == category.lower()]

    if sale_colors is not None:
        # 판매 색상 필터링
        filtered_products = [product for product in filtered_products if sale_colors.lower() in product['sale_colors'].lower()]

    if min_sales is not None:
        # 최소 판매량 필터링
        filtered_products = [product for product in filtered_products if product['sales'] >= min_sales]

    if keywords is not None:
        # 키워드 필터링
        filtered_products = [product for product in filtered_products if keywords.lower() in product['keywords'].lower()]

    return filtered_products

@app.get("/travel-packages")
async def get_travel_packages(
    destination: str = Query(default=None),
    min_duration: int = Query(default=None, ge=1),
    max_duration: int = Query(default=None, ge=1),
    max_price: int = Query(default=None, ge=0),
):
    filtered_packages = travel_packages

    if destination is not None:
        # 여행지 필터링
        filtered_packages = [package for package in filtered_packages if destination.lower() in package['destination'].lower()]

    if min_duration is not None:
        # 최소 여행기간 필터링
        filtered_packages = [package for package in filtered_packages if int(package['duration'].split()[0]) >= min_duration]

    if max_duration is not None:
        # 최대 여행기간 필터링
        filtered_packages = [package for package in filtered_packages if int(package['duration'].split()[0]) <= max_duration]

    if max_price is not None:
        # 최대 가격 필터링
        filtered_packages = [package for package in filtered_packages if package['price'] <= max_price]

    return filtered_packages

@app.get("/job-listings")
async def get_job_listings(
    company_name: str = Query(default=None),
    min_salary: int = Query(default=None, ge=0),
    position: str = Query(default=None),
    min_employee_count: int = Query(default=None, ge=0),
):
    filtered_listings = job_listings

    if company_name is not None:
        # 회사명 필터링
        filtered_listings = [listing for listing in filtered_listings if company_name.lower() in listing['company_name'].lower()]

    if min_salary is not None:
        # 최소 급여 필터링
        filtered_listings = [listing for listing in filtered_listings if listing['salary'] >= min_salary]

    if position is not None:
        # 구직 포지션 필터링
        filtered_listings = [listing for listing in filtered_listings if position.lower() in listing['position'].lower()]

    if min_employee_count is not None:
        # 최소 직원수 필터링
        filtered_listings = [listing for listing in filtered_listings if listing['employee_count'] >= min_employee_count]

    return filtered_listings

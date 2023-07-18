from fastapi import FastAPI, Query
from typing import List

app = FastAPI()


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
        filtered_reservations = [reservation for reservation in filtered_reservations if reservation[3] == length]
    if designer:
        filtered_reservations = [reservation for reservation in filtered_reservations if reservation[4] == designer]
    if keyword:
        filtered_reservations = [reservation for reservation in filtered_reservations if keyword in reservation[5]]

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
    if category:
        filtered_products = [product for product in filtered_products if product[2] == category]
    if sort:
        filtered_products = [product for product in filtered_products if product[3] == sort]
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
    schedule: str = Query(None, description="스케줄"),
    id: str = Query(None, description="사번"),
    name: str = Query(None, description="이름"),
    phone: str = Query(None, description="전화번호"),
    min_orderYear: int = Query(None, description="최소 연차"),
):
    filtered_schedules = uni_hospital_nurse_schedules

    filtered_schedules = [schedule for schedule in filtered_schedules if schedule[0] == belong]
    if schedule:
        filtered_schedules = [schedule for schedule in filtered_schedules if schedule[1] == schedule]
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
    class_: str = Query(..., description="강습 종류"),
    rental: bool = Query(None, description="장비 대여 여부"),
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
    filtered_diving_pools = [pool for pool in filtered_diving_pools if class_ in pool[4]]
    if rental is not None:
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
    seatId: str = Query(None, description="좌석 번호"),
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
    blogger: str = Query(None, description="블로거 이름"),
    category: str = Query(..., description="카테고리"),
    min_openDate: int = Query(None, description="최소 개설일자"),
    keyword: str = Query(None, description="작성글 제목을 조회하는 키워드"),
):
    filtered_bloggers = blogger_data

    if blogName:
        filtered_bloggers = [blogger for blogger in filtered_bloggers if blogger[0] == blogName]
    if blogger:
        filtered_bloggers = [blogger for blogger in filtered_bloggers if blogger[1] == blogger]
    filtered_bloggers = [blogger for blogger in filtered_bloggers if blogger[2] == category]
    if min_openDate is not None:
        filtered_bloggers = [blogger for blogger in filtered_bloggers if int(blogger[4].split(".")[0]) >= min_openDate]
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

korean_chinese_food_data = [
    ["짜장면",["면","짜장","춘장","돼지고기"],"단맛",1,7500,"수타면을 사용한 짜장입니다."],
    ["짬뽕",["면","오징어","홍합","돼지고기"],"매운맛",1,7500,"불맛이 가득한 짬뽕입니다."],
    ["볶음밥",["밥","양파","계란","돼지고기"],"담백한맛",1,7500,"계란볶음밥. 짜장소스는 없습니다."],
    ["경장육사",["오이","건두부","춘장","돼지고기"],"짭짤한맛",3,25500,"건두부에 볶은 돼지고기를 싸먹는 요리입니다."],
    ["유산슬",["계란","새우","오징어","해삼"],"담백한맛",3,32000,"신선한 해산물을 가득 넣었습니다."]
]

@app.get("/KoreanChineseFood")
def filter_korean_chinese_food(
    menu: str = Query(None, description="메뉴이름"),
    food_stuff: str = Query(..., description="재료"),
    taste: str = Query(None, description="맛"),
    min_amount: int = Query(None, gt=0, description="최소인분"),
    max_amount: int = Query(None, gt=0, description="최대인분"),
    min_price: int = Query(None, gt=0, description="최소가격"),
    max_price: int = Query(None, gt=0, description="최대가격"),
):
    filtered_food = korean_chinese_food_data

    if menu:
        filtered_food = [food for food in filtered_food if food[0] == menu]
    filtered_food = [food for food in filtered_food if all(ingredient in food[1] for ingredient in food_stuff)]
    if taste:
        filtered_food = [food for food in filtered_food if food[2] == taste]
    if min_amount:
        filtered_food = [food for food in filtered_food if food[3] >= min_amount]
    if max_amount:
        filtered_food = [food for food in filtered_food if food[3] <= max_amount]
    if min_price:
        filtered_food = [food for food in filtered_food if food[4] >= min_price]
    if max_price:
        filtered_food = [food for food in filtered_food if food[4] <= max_price]

    return filtered_food

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
        filtered_goods = [goods for goods in filtered_goods if goods[0] == name]
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
    filtered_stores = [store for store in filtered_stores if store[2] == location]
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
    ["코인워시24","서울특별시 동작구 노량진로6길 46",4000,true,"생활용품판매","02-000-0000","24시간"],
    ["워시엔조이","서울특별시 중구 회현동 121-4",3000,true,"무인카페","02-000-0001","24시간"],
    ["빨래터","서울특별시 관악구 청룡동 청룡10길 18",5000,true,"식료품판매","02-000-0002","07:00~23:00"],
    ["코인세탁365","서울특별시 용산구 이촌로18길 21",3000,false,"없음","02-000-0003","24시간"],
    ["코인크린","서울특별시 중구 동호로8길 5",4000,true,"운동화전용 세탁기기 구비","02-000-0004","07:00~22:00"]
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
    filtered_laundries = [laundry for laundry in filtered_laundries if laundry[1] == location]
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
        filtered_hanbok = [h for h in filtered_hanbok if h[1] == location]
    if category:
        filtered_hanbok = [h for h in filtered_hanbok if category in h[2]]
    if rating:
        filtered_hanbok = [h for h in filtered_hanbok if h[4] >= rating]
    if desc:
        filtered_hanbok = [h for h in filtered_hanbok if h[5] == desc]

    return filtered_hanbok

hanbok_rental_data = [
    ["파란마음","파랑",["S","M"],90000,true,"버선"],
    ["초록물결","초록",["L","M"],100000,true,"비녀, 버선"],
    ["성균관","흰색",["S","M","L"],120000,false,"버선"],
    ["꼬까옷","노랑",["S","M"],80000,true,"버선, 허리띠"],
    ["진달래","분홍",["S","M"],70000,false,"버선"]
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
    ["요리조리 초보클래스","도마 제작","인천문화회관",50000,"2023-08-21",true,"우드카빙 도마를 만들고 관리하는 방법을 배웁니다."],
    ["귀여움이 가득한","목각인형 제작","구월산회관",80000,"2023-06-21",true,"수공구로 만드는 목각인형."],
    ["창업준비클래스","목공방 창업 수업","기린문화원",150000,"2023-09-21",true,"목공방 창업을 위한 노하우 클래스."],
    ["전통 소목장","소반 제작","대전문화회관",200000,"2023-08-21",false,"전통 방법으로 소반을 만듭니다."],
    ["원목가구와 짜임","서랍장 제작","청년청",250000,"2023-07-21",true,"중형 목가구와 짜임 수업입니다."]
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
    a_name: str = Query(None, description="저자명"),
    min_price: int = Query(None, ge=0, description="최소 가격"),
    max_price: int = Query(None, ge=0, description="최대 가격"),
    date: str = Query(None, description="펀딩 마감일"),
    desc: str = Query(..., description="설명 (도서 홍보 설명 등)"),
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
        filtered_fundings = [f for f in filtered_fundings if f[5] == desc]

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

nature_education_data = [
    ["건강숲","산행, 체조","백련산",40000,"65세 이상",True,"010-0000-0000"],
    ["노르딕워킹","산행, 걷기코칭","백련산",60000,"일반성인",True,"010-0000-0000"],
    ["양서류교실","숲해설, 물놀이","인산계곡",30000,"유아, 초등, 가족",True,"010-0000-0000"],
    ["숲속보물찾기","숲해설, 자연탐방","인왕어린이공원",20000,"초등",False,"010-0000-0000"],
    ["매미탐험","숲해설, 매미관찰","백련산",40000,"초등, 가족",True,"010-0000-0000"]
]

@app.get("/NatureEducation")
def filter_nature_education(
    name: str = Query(None, description="교육이름"),
    contents: str = Query(..., description="내용"),
    location: str = Query(None, description="장소 (예: 백련산, 인왕계곡 등)"),
    min_price: int = Query(None, gt=0, description="최소 가격"),
    max_price: int = Query(None, gt=0, description="최대 가격"),
    age: str = Query(None, description="교육대상연령 (예: 유아, 초등, 가족 등)"),
    available: bool = Query(None, description="예약가능여부"),
):
    filtered_list = nature_education_data

    if name:
        filtered_list = [l for l in filtered_list if l[0] == name]
    if contents:
        filtered_list = [l for l in filtered_list if l[1] == contents]
    if location:
        filtered_list = [l for l in filtered_list if l[2] == location]
    if min_price is not None:
        filtered_list = [l for l in filtered_list if l[3] >= min_price]
    if max_price is not None:
        filtered_list = [l for l in filtered_list if l[3] <= max_price]
    if age:
        filtered_list = [l for l in filtered_list if l[4] == age]
    if available is not None:
        filtered_list = [l for l in filtered_list if l[5] == available]

    return filtered_list

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

shampoo_data = [
    ["두피스파 샴푸","비듬 감소, 두피 건강","멘솔",12400,750,"소듐라우레스설페이트 등","시원한 쿨링감"],
    ["모이스처 10 샴푸","두피와 모발건조 완화","코튼",15400,680,"소듐라우레스설페이트 등","촉촉함이 그대로 남는"],
    ["자윤 모근강화 샴푸","모근 강화, 지성 두피용","한약재",17800,950,"소듐라우레스설페이트 등","한방 성분으로 모근을 더 건강하게"],
    ["마이크로바이옴 효모 샴푸","두피 가려움 개선","플로럴",29000,400,"프로폴리스 추출물 등","두피 장벽 개선"],
    ["펩타이드 고영양 샴푸","손상모 개선","코코넛",19400,850,"아르간 오일 등","찰랑찰랑한 머릿결로 회복"]
]

@app.get("/ShampooSearch")
def filter_shampoo(
    name: str = Query(None, description="제품명"),
    effect: str = Query(..., description="기능 (예: 비듬 감소, 모근 강화 등)"),
    aroma: str = Query(None, description="향 (예: 코튼, 플로럴 등)"),
    min_price: int = Query(None, description="최소 가격"),
    max_price: int = Query(None, description="최대 가격"),
    size: int = Query(None, description="용량(ml)"),
    component: str = Query(None, description="성분 (예: 프로폴리스, 아르간 오일 등)"),
):
    filtered_list = shampoo_data

    if name:
        filtered_list = [s for s in filtered_list if s[0] == name]
    if effect:
        filtered_list = [s for s in filtered_list if s[1] == effect]
    if aroma:
        filtered_list = [s for s in filtered_list if s[2] == aroma]
    if min_price is not None:
        filtered_list = [s for s in filtered_list if s[3] >= min_price]
    if max_price is not None:
        filtered_list = [s for s in filtered_list if s[3] <= max_price]
    if size is not None:
        filtered_list = [s for s in filtered_list if s[4] == size]
    if component:
        filtered_list = [s for s in filtered_list if s[5] == component]

    return filtered_list

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
    ["초보자","드라세나 마지나타","madagascar dragon tree","백합과","아프리카","없음","폭이 좁고 가는잎"],
    ["전문가","박쥐란","common staghorn fern","고사리과","호주","없음","사슴뿔 모양"],
    ["초보자","개운죽","Sander's dracaena","백합과","아프리카","있음","대나무를 닮았으나 대나무 아님"],
    ["초보자","치자나무","common gardenia","꼭두서니과","아시아","있음","향기가 매우 강함"],
    ["경험자","공작야자","Fish tail palm","야자과","인도네시아","있음","열매색이 빨강색"]
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
        filtered_list = [festival for festival in filtered_list if nation == festival[1]]
    if region:
        filtered_list = [festival for festival in filtered_list if region == festival[2]]
    if contents:
        filtered_list = [festival for festival in filtered_list if contents == festival[3]]
    if month:
        filtered_list = [festival for festival in filtered_list if month == festival[4]]
    if min_congestion:
        filtered_list = [festival for festival in filtered_list if min_congestion <= festival[5]]

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

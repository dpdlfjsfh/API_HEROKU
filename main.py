from fastapi import FastAPI, Query
from typing import List

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
    {"product_name": "T-Shirt", "price": 19.99, "category": "Shirts", "sale_colors": ["Red", "Blue", "White"], "sales": 1000, "keywords": ["casual", "cotton"]},
    {"product_name": "Jeans", "price": 49.99, "category": "Pants", "sale_colors": ["Black", "Blue"], "sales": 500, "keywords": ["denim", "slim fit"]},
    {"product_name": "Dress", "price": 39.99, "category": "Dresses", "sale_colors": ["Pink", "Black"], "sales": 800, "keywords": ["formal", "evening"]},
    {"product_name": "Sweater", "price": 29.99, "category": "Sweaters", "sale_colors": ["Gray", "Navy"], "sales": 300, "keywords": ["wool", "warm"]},
    {"product_name": "Shorts", "price": 24.99, "category": "Shorts", "sale_colors": ["Beige", "Khaki"], "sales": 600, "keywords": ["summer", "casual"]},
    {"product_name": "Blouse", "price": 34.99, "category": "Shirts", "sale_colors": ["White", "Yellow"], "sales": 400, "keywords": ["feminine", "chiffon"]},
    {"product_name": "Jacket", "price": 59.99, "category": "Jackets", "sale_colors": ["Black", "Brown"], "sales": 200, "keywords": ["leather", "outerwear"]},
    {"product_name": "Skirt", "price": 29.99, "category": "Skirts", "sale_colors": ["Navy", "Green"], "sales": 700, "keywords": ["floral", "midi"]},
    {"product_name": "Sweatshirt", "price": 39.99, "category": "Sweaters", "sale_colors": ["Gray", "Black"], "sales": 400, "keywords": ["hoodie", "sporty"]},
    {"product_name": "Coat", "price": 79.99, "category": "Coats", "sale_colors": ["Gray", "Camel"], "sales": 100, "keywords": ["winter", "warm"]}
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

    return filtered_s

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
    sale_colors: List[str] = Query(default=None),
    min_sales: int = Query(default=None, ge=0),
    keywords: List[str] = Query(default=None),
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
        filtered_products = [product for product in filtered_products if set(sale_colors).intersection(set(product['sale_colors']))]

    if min_sales is not None:
        # 최소 판매량 필터링
        filtered_products = [product for product in filtered_products if product['sales'] >= min_sales]

    if keywords is not None:
        # 키워드 필터링
        filtered_products = [product for product in filtered_products if set(keywords).intersection(set(product['keywords']))]

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

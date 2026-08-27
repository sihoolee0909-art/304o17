import streamlit as st
import requests
import random
import urllib.parse
import time

# =========================================================
# 🎨 페이지 설정
# =========================================================

st.set_page_config(
    page_title="🎨 세계의 화가 검색",
    page_icon="🎨",
    layout="wide"
)

# =========================================================
# 🧑‍🎨 화가 40명 데이터
# =========================================================

artists = {
    "빈센트 반 고흐": {
        "국적": "🇳🇱 네덜란드",
        "생몰연도": "1853–1890",
        "작품": [
            ("별이 빛나는 밤", "The Starry Night"),
            ("해바라기", "Sunflowers"),
            ("아를의 침실", "The Bedroom")
        ]
    },

    "레오나르도 다 빈치": {
        "국적": "🇮🇹 이탈리아",
        "생몰연도": "1452–1519",
        "작품": [
            ("모나리자", "Mona Lisa"),
            ("최후의 만찬", "The Last Supper"),
            ("성 안나와 함께 있는 성모자", "The Virgin and Child with Saint Anne")
        ]
    },

    "클로드 모네": {
        "국적": "🇫🇷 프랑스",
        "생몰연도": "1840–1926",
        "작품": [
            ("인상, 해돋이", "Impression, Sunrise"),
            ("수련", "Water Lilies"),
            ("루앙 대성당", "Rouen Cathedral")
        ]
    },

    "파블로 피카소": {
        "국적": "🇪🇸 스페인",
        "생몰연도": "1881–1973",
        "작품": [
            ("게르니카", "Guernica"),
            ("우는 여인", "The Weeping Woman"),
            ("아비뇽의 처녀들", "Les Demoiselles d'Avignon")
        ]
    },

    "살바도르 달리": {
        "국적": "🇪🇸 스페인",
        "생몰연도": "1904–1989",
        "작품": [
            ("기억의 지속", "The Persistence of Memory"),
            ("코끼리", "The Elephants"),
            ("백조가 코끼리가 되는 순간", "Swans Reflecting Elephants")
        ]
    },

    "에드바르 뭉크": {
        "국적": "🇳🇴 노르웨이",
        "생몰연도": "1863–1944",
        "작품": [
            ("절규", "The Scream"),
            ("마돈나", "Madonna"),
            ("키스", "The Kiss")
        ]
    },

    "렘브란트": {
        "국적": "🇳🇱 네덜란드",
        "생몰연도": "1606–1669",
        "작품": [
            ("야경", "The Night Watch"),
            ("돌아온 탕자", "The Return of the Prodigal Son"),
            ("해부학 강의", "The Anatomy Lesson of Dr. Nicolaes Tulp")
        ]
    },

    "미켈란젤로": {
        "국적": "🇮🇹 이탈리아",
        "생몰연도": "1475–1564",
        "작품": [
            ("천지창조", "The Creation of Adam"),
            ("최후의 심판", "The Last Judgment"),
            ("피에타", "Pieta")
        ]
    },

    "라파엘로": {
        "국적": "🇮🇹 이탈리아",
        "생몰연도": "1483–1520",
        "작품": [
            ("아테네 학당", "The School of Athens"),
            ("시스티나의 성모", "Sistine Madonna"),
            ("갈라테이아", "The Triumph of Galatea")
        ]
    },

    "구스타프 클림트": {
        "국적": "🇦🇹 오스트리아",
        "생몰연도": "1862–1918",
        "작품": [
            ("키스", "The Kiss"),
            ("아델레 블로흐바우어의 초상", "Portrait of Adele Bloch-Bauer I"),
            ("유디트", "Judith and the Head of Holofernes")
        ]
    },

    "프리다 칼로": {
        "국적": "🇲🇽 멕시코",
        "생몰연도": "1907–1954",
        "작품": [
            ("두 명의 프리다", "The Two Fridas"),
            ("부러진 기둥", "The Broken Column"),
            ("가시 목걸이와 벌새가 있는 자화상",
             "Self-Portrait with Thorn Necklace and Hummingbird")
        ]
    },

    "앤디 워홀": {
        "국적": "🇺🇸 미국",
        "생몰연도": "1928–1987",
        "작품": [
            ("캠벨 수프 캔", "Campbell's Soup Cans"),
            ("마릴린 딥티크", "Marilyn Diptych"),
            ("8명의 엘비스", "Eight Elvises")
        ]
    },

    "오귀스트 르누아르": {
        "국적": "🇫🇷 프랑스",
        "생몰연도": "1841–1919",
        "작품": [
            ("물랭 드 라 갈레트의 무도회",
             "Dance at Le Moulin de la Galette"),
            ("뱃놀이하는 사람들의 점심",
             "Luncheon of the Boating Party"),
            ("두 자매", "Two Sisters")
        ]
    },

    "폴 세잔": {
        "국적": "🇫🇷 프랑스",
        "생몰연도": "1839–1906",
        "작품": [
            ("사과와 오렌지", "Apples and Oranges"),
            ("생트빅투아르산", "Mont Sainte-Victoire"),
            ("카드놀이하는 사람들", "The Card Players")
        ]
    },

    "폴 고갱": {
        "국적": "🇫🇷 프랑스",
        "생몰연도": "1848–1903",
        "작품": [
            ("우리는 어디서 왔는가", "Where Do We Come From"),
            ("타히티의 여인들", "Tahitian Women"),
            ("신의 날", "Day of the God")
        ]
    },

    "앙리 마티스": {
        "국적": "🇫🇷 프랑스",
        "생몰연도": "1869–1954",
        "작품": [
            ("춤", "The Dance"),
            ("붉은 방", "The Red Room"),
            ("음악", "Music")
        ]
    },

    "조르주 쇠라": {
        "국적": "🇫🇷 프랑스",
        "생몰연도": "1859–1891",
        "작품": [
            ("그랑드자트섬의 일요일 오후",
             "A Sunday Afternoon on the Island of La Grande Jatte"),
            ("아스니에르에서의 물놀이", "Bathers at Asnières"),
            ("서커스", "The Circus")
        ]
    },

    "에드가 드가": {
        "국적": "🇫🇷 프랑스",
        "생몰연도": "1834–1917",
        "작품": [
            ("발레 수업", "The Ballet Class"),
            ("무대 위의 무희", "The Star"),
            ("압생트", "L'Absinthe")
        ]
    },

    "카미유 피사로": {
        "국적": "🇫🇷 프랑스",
        "생몰연도": "1830–1903",
        "작품": [
            ("몽마르트르 거리", "Boulevard Montmartre"),
            ("붉은 지붕", "Red Roofs"),
            ("에라니의 사과나무", "Apple Trees at Eragny")
        ]
    },

    "피트 몬드리안": {
        "국적": "🇳🇱 네덜란드",
        "생몰연도": "1872–1944",
        "작품": [
            ("브로드웨이 부기우기", "Broadway Boogie Woogie"),
            ("빨강 파랑 노랑의 구성", "Composition with Red Blue and Yellow"),
            ("구성", "Composition")
        ]
    },

    "잭슨 폴록": {
        "국적": "🇺🇸 미국",
        "생몰연도": "1912–1956",
        "작품": [
            ("넘버 1", "Number 1"),
            ("라벤더 미스트", "Lavender Mist"),
            ("가을 리듬", "Autumn Rhythm")
        ]
    },

    "마르크 샤갈": {
        "국적": "🇷🇺 러시아",
        "생몰연도": "1887–1985",
        "작품": [
            ("산책", "The Promenade"),
            ("나와 마을", "I and the Village"),
            ("바이올린 연주자", "The Fiddler")
        ]
    },

    "바실리 칸딘스키": {
        "국적": "🇷🇺 러시아",
        "생몰연도": "1866–1944",
        "작품": [
            ("구성 8", "Composition VIII"),
            ("구성 7", "Composition VII"),
            ("노랑 빨강 파랑", "Yellow Red Blue")
        ]
    },

    "에곤 실레": {
        "국적": "🇦🇹 오스트리아",
        "생몰연도": "1890–1918",
        "작품": [
            ("죽음과 소녀", "Death and the Maiden"),
            ("포옹", "The Embrace"),
            ("자화상", "Self-Portrait")
        ]
    },

    "귀스타브 쿠르베": {
        "국적": "🇫🇷 프랑스",
        "생몰연도": "1819–1877",
        "작품": [
            ("돌 깨는 사람들", "The Stone Breakers"),
            ("화가의 작업실", "The Artist's Studio"),
            ("세상의 기원", "The Origin of the World")
        ]
    },

    "아메데오 모딜리아니": {
        "국적": "🇮🇹 이탈리아",
        "생몰연도": "1884–1920",
        "작품": [
            ("잔 에뷔테른", "Jeanne Hebuterne"),
            ("붉은 누드", "Red Nude"),
            ("자화상", "Self-Portrait")
        ]
    },

    "히에로니무스 보스": {
        "국적": "🇳🇱 네덜란드",
        "생몰연도": "1450–1516",
        "작품": [
            ("쾌락의 정원", "The Garden of Earthly Delights"),
            ("최후의 심판", "The Last Judgment"),
            ("성 안토니우스의 유혹", "The Temptation of Saint Anthony")
        ]
    },

    "피터르 브뤼헐": {
        "국적": "🇳🇱 네덜란드",
        "생몰연도": "1525–1569",
        "작품": [
            ("눈 속의 사냥꾼", "The Hunters in the Snow"),
            ("농부의 결혼식", "The Peasant Wedding"),
            ("바벨탑", "The Tower of Babel")
        ]
    },

    "카라바조": {
        "국적": "🇮🇹 이탈리아",
        "생몰연도": "1571–1610",
        "작품": [
            ("성 마태오의 소명", "The Calling of Saint Matthew"),
            ("바쿠스", "Bacchus"),
            ("유디트와 홀로페르네스", "Judith Beheading Holofernes")
        ]
    },

    "디에고 벨라스케스": {
        "국적": "🇪🇸 스페인",
        "생몰연도": "1599–1660",
        "작품": [
            ("시녀들", "Las Meninas"),
            ("교황 인노첸시오 10세", "Portrait of Pope Innocent X"),
            ("브레다의 항복", "The Surrender of Breda")
        ]
    },

    "프란시스코 고야": {
        "국적": "🇪🇸 스페인",
        "생몰연도": "1746–1828",
        "작품": [
            ("1808년 5월 3일", "The Third of May 1808"),
            ("옷 입은 마하", "The Clothed Maja"),
            ("사투르누스", "Saturn Devouring His Son")
        ]
    },

    "외젠 들라크루아": {
        "국적": "🇫🇷 프랑스",
        "생몰연도": "1798–1863",
        "작품": [
            ("민중을 이끄는 자유의 여신",
             "Liberty Leading the People"),
            ("사르다나팔루스의 죽음",
             "The Death of Sardanapalus"),
            ("호랑이 사냥", "Tiger Hunt")
        ]
    },

    "장 프랑수아 밀레": {
        "국적": "🇫🇷 프랑스",
        "생몰연도": "1814–1875",
        "작품": [
            ("이삭 줍는 사람들", "The Gleaners"),
            ("만종", "The Angelus"),
            ("씨 뿌리는 사람", "The Sower")
        ]
    },

    "에두아르 마네": {
        "국적": "🇫🇷 프랑스",
        "생몰연도": "1832–1883",
        "작품": [
            ("풀밭 위의 점심", "Le Dejeuner sur l'herbe"),
            ("올랭피아", "Olympia"),
            ("폴리 베르제르의 술집",
             "A Bar at the Folies-Bergere")
        ]
    },

    "조안 미로": {
        "국적": "🇪🇸 스페인",
        "생몰연도": "1893–1983",
        "작품": [
            ("카탈루냐 풍경", "The Farm"),
            ("별자리", "Constellation"),
            ("여성과 새", "Woman and Bird")
        ]
    },

    "르네 마그리트": {
        "국적": "🇧🇪 벨기에",
        "생몰연도": "1898–1967",
        "작품": [
            ("인간의 아들", "The Son of Man"),
            ("골콩다", "Golconda"),
            ("이미지의 배반", "The Treachery of Images")
        ]
    },

    "조르조 데 키리코": {
        "국적": "🇮🇹 이탈리아",
        "생몰연도": "1888–1978",
        "작품": [
            ("거리의 신비와 우울",
             "Mystery and Melancholy of a Street"),
            ("예언자", "The Prophet"),
            ("사랑의 노래", "The Song of Love")
        ]
    },

    "로이 리히텐슈타인": {
        "국적": "🇺🇸 미국",
        "생몰연도": "1923–1997",
        "작품": [
            ("Whaam!", "Whaam!"),
            ("익사하는 소녀", "Drowning Girl"),
            ("오, 제프", "Oh, Jeff...I Love You, Too...")
        ]
    },

    "장 미셸 바스키아": {
        "국적": "🇺🇸 미국",
        "생몰연도": "1960–1988",
        "작품": [
            ("해골", "Skull"),
            ("무제", "Untitled"),
            ("할리우드 아프리카인", "Hollywood Africans")
        ]
    },

    "조지아 오키프": {
        "국적": "🇺🇸 미국",
        "생몰연도": "1887–1986",
        "작품": [
            ("붉은 칸나", "Red Canna"),
            ("소의 두개골", "Cow's Skull"),
            ("검은 붓꽃", "Black Iris")
        ]
    },

    "구스타브 모로": {
        "국적": "🇫🇷 프랑스",
        "생몰연도": "1826–1898",
        "작품": [
            ("살로메의 춤", "The Apparition"),
            ("오이디푸스와 스핑크스", "Oedipus and the Sphinx"),
            ("유피테르와 세멜레", "Jupiter and Semele")
        ]
    },

    "알브레히트 뒤러": {
        "국적": "🇩🇪 독일",
        "생몰연도": "1471–1528",
        "작품": [
            ("멜랑콜리아 I", "Melencolia I"),
            ("토끼", "Young Hare"),
            ("기도하는 손", "Praying Hands")
        ]
    },

    "산드로 보티첼리": {
        "국적": "🇮🇹 이탈리아",
        "생몰연도": "1445–1510",
        "작품": [
            ("비너스의 탄생", "The Birth of Venus"),
            ("봄", "Primavera"),
            ("동방박사의 경배", "Adoration of the Magi")
        ]
    }
}

# =========================================================
# 🖼️ Wikimedia Commons 이미지 검색
# =========================================================

@st.cache_data(ttl=86400)
def get_image_url(search_text):

    url = "https://commons.wikimedia.org/w/api.php"

    params = {
        "action": "query",
        "format": "json",
        "generator": "search",
        "gsrsearch": search_text,
        "gsrnamespace": 6,
        "gsrlimit": 1,
        "prop": "imageinfo",
        "iiprop": "url"
    }

    try:
        response = requests.get(
            url,
            params=params,
            timeout=10
        )

        data = response.json()

        pages = data.get("query", {}).get("pages", {})

        for page in pages.values():
            imageinfo = page.get("imageinfo", [])

            if imageinfo:
                return imageinfo[0]["url"]

    except Exception:
        return None

    return None


# =========================================================
# 🎨 모든 작품 이미지 준비
# =========================================================

@st.cache_data(ttl=86400)
def get_all_images():

    images = []

    for artist_name, artist in artists.items():

        for korean, english in artist["작품"]:

            image = get_image_url(
                english + " " + artist_name
            )

            if image:
                images.append({
                    "화가": artist_name,
                    "작품": korean,
                    "이미지": image
                })

    return images


# =========================================================
# 🌈 랜덤 배경
# =========================================================

all_images = get_all_images()

if all_images:

    # 현재 시간에 따라 10초마다 다른 이미지
    background_index = int(time.time() // 10) % len(all_images)

    background = all_images[background_index]

    background_url = background["이미지"]

    st.markdown(
        f"""
        <style>

        .stApp {{
            background:
                linear-gradient(
                    rgba(0,0,0,0.58),
                    rgba(0,0,0,0.58)
                ),
                url("{background_url}");

            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}

        .main-title {{
            text-align: center;
            color: white;
            font-size: 55px;
            font-weight: bold;
            text-shadow: 3px 3px 10px black;
        }}

        .subtitle {{
            text-align: center;
            color: white;
            font-size: 20px;
            text-shadow: 2px 2px 5px black;
        }}

        .artist-box {{
            background-color: rgba(255,255,255,0.92);
            padding: 25px;
            border-radius: 20px;
            margin-top: 20px;
        }}

        </style>
        """,
        unsafe_allow_html=True
    )

# =========================================================
# 🎨 제목
# =========================================================

st.markdown(
    '<div class="main-title">🎨 세계의 화가 검색</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">🖌️ 화가의 이름을 검색하고 대표 작품을 만나보세요!</div>',
    unsafe_allow_html=True
)

st.write("")

# =========================================================
# 🔎 검색
# =========================================================

search = st.text_input(
    "🔎 화가 이름을 검색하세요",
    placeholder="예: 빈센트 반 고흐"
)

# =========================================================
# 🧑‍🎨 검색 결과
# =========================================================

if search:

    # 정확한 이름 검색
    if search in artists:

        artist = artists[search]

        st.markdown(
            '<div class="artist-box">',
            unsafe_allow_html=True
        )

        st.success(f"🎉 {search} 화가를 찾았습니다!")

        st.header(f"🎨 {search}")

        col1, col2 = st.columns(2)

        with col1:
            st.write(f"🌍 **국적:** {artist['국적']}")

        with col2:
            st.write(f"📅 **생몰연도:** {artist['생몰연도']}")

        st.divider()

        st.subheader("🖼️ 대표 작품")

        cols = st.columns(3)

        for i, (korean, english) in enumerate(artist["작품"]):

            image = get_image_url(
                english + " " + search
            )

            with cols[i]:

                if image:
                    st.image(
                        image,
                        caption=f"🎨 {korean}",
                        use_container_width=True
                    )
                else:
                    st.write(f"🖼️ **{korean}**")

        st.markdown(
            '</div>',
            unsafe_allow_html=True
        )

    else:

        st.error("😢 해당 화가를 찾을 수 없습니다.")

        # 부분 검색
        results = [
            name for name in artists
            if search.lower() in name.lower()
        ]

        if results:

            st.info("🔎 혹시 이 화가를 찾으시나요?")

            for name in results:
                st.write(f"🎨 {name}")

        else:

            st.warning("💡 아래 화가 중 한 명을 검색해 보세요!")

            cols = st.columns(4)

            for i, name in enumerate(artists):

                cols[i % 4].write(
                    f"🖌️ {name}"
                )

# =========================================================
# 🏠 검색하지 않았을 때
# =========================================================

else:

    st.info(
        "👆 위 검색창에 화가 이름을 입력해 보세요!"
    )

    st.subheader("🌟 검색할 수 있는 화가 40명")

    cols = st.columns(4)

    for i, name in enumerate(artists):

        cols[i % 4].write(
            f"🎨 {name}"
        )

    st.divider()

    if all_images:

        st.caption(
            f"🖼️ 현재 배경: "
            f"{background['화가']} - {background['작품']} "
            f" | 🔄 10초마다 변경"
        )

# =========================================================
# ⏱️ 10초마다 자동 새로고침
# =========================================================

time.sleep(10)
st.rerun()

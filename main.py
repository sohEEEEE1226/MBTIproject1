import streamlit as st
import random
import time
 
st.set_page_config(
    page_title="✨ MBTI 포켓몬 매칭 ✨",
    page_icon="🎮",
    layout="centered"
)
 
# ─────────────────────────────────────────────
# 데이터 정의
# ─────────────────────────────────────────────
 
MBTI_POKEMON = {
    "INTJ": {
        "pokemon": "리자몽",
        "english": "Charizard",
        "number": "006",
        "emoji": "🔥",
        "reason": "전략적이고 독립적인 당신! 리자몽처럼 강한 의지와 뛰어난 지략으로 목표를 향해 불꽃처럼 돌진해요.",
        "traits": ["🧠 전략가", "🎯 목표 지향", "🦅 독립적", "💡 통찰력"],
        "color": "#FF6B35",
        "bg_color": "#FFF3EE",
        "move": "화염방사",
        "type": "불꽃/비행",
        "sprite_id": 6,
    },
    "INTP": {
        "pokemon": "뮤츠",
        "english": "Mewtwo",
        "number": "150",
        "emoji": "🧬",
        "reason": "끝없는 지적 호기심의 소유자! 뮤츠처럼 세상의 진리를 탐구하며 독자적인 사고의 세계를 구축해요.",
        "traits": ["🔬 분석가", "💭 사색가", "📚 지식 탐구", "🌀 창의적 사고"],
        "color": "#7B68EE",
        "bg_color": "#F0EEFF",
        "move": "사이코키네시스",
        "type": "에스퍼",
        "sprite_id": 150,
    },
    "ENTJ": {
        "pokemon": "갸라도스",
        "english": "Gyarados",
        "number": "130",
        "emoji": "🌊",
        "reason": "타고난 리더십과 강인한 의지! 갸라도스처럼 역경을 딛고 일어나 모든 것을 압도하는 카리스마를 가졌어요.",
        "traits": ["👑 리더", "💪 강인함", "🎯 결단력", "🔥 카리스마"],
        "color": "#1A6BB5",
        "bg_color": "#EEF5FF",
        "move": "하이드로펌프",
        "type": "물/비행",
        "sprite_id": 130,
    },
    "ENTP": {
        "pokemon": "팬텀",
        "english": "Gengar",
        "number": "094",
        "emoji": "👻",
        "reason": "재치 넘치는 아이디어 뱅크! 팬텀처럼 예상치 못한 곳에서 나타나 모두를 깜짝 놀라게 하는 매력이 있어요.",
        "traits": ["💡 아이디어맨", "😏 재치있음", "🎭 도전적", "🌪️ 에너지 넘침"],
        "color": "#6B3FA0",
        "bg_color": "#F5EEFF",
        "move": "나이트헤드",
        "type": "고스트/독",
        "sprite_id": 94,
    },
    "INFJ": {
        "pokemon": "루기아",
        "english": "Lugia",
        "number": "249",
        "emoji": "🌙",
        "reason": "깊은 통찰력과 따뜻한 마음씨! 루기아처럼 조용하지만 강력한 존재감으로 주변을 평화롭게 만들어요.",
        "traits": ["🔮 통찰력", "💙 공감 능력", "🕊️ 평화로움", "✨ 이상주의"],
        "color": "#4A90D9",
        "bg_color": "#EEF8FF",
        "move": "에어로블라스트",
        "type": "에스퍼/비행",
        "sprite_id": 249,
    },
    "INFP": {
        "pokemon": "이브이",
        "english": "Eevee",
        "number": "133",
        "emoji": "🌸",
        "reason": "무한한 가능성과 따뜻한 감수성! 이브이처럼 어떤 모습으로든 변화하며 자신만의 길을 찾아가는 특별한 존재예요.",
        "traits": ["🎨 창의적", "💕 감수성 풍부", "🌱 성장 지향", "🦋 자유로움"],
        "color": "#E8956D",
        "bg_color": "#FFF5F0",
        "move": "아이언테일",
        "type": "노말",
        "sprite_id": 133,
    },
    "ENFJ": {
        "pokemon": "피카츄",
        "english": "Pikachu",
        "number": "025",
        "emoji": "⚡",
        "reason": "사람들에게 활력과 긍정 에너지를 주는 당신! 피카츄처럼 모두의 마음을 전기처럼 찌릿하게 만드는 매력을 가졌어요.",
        "traits": ["🌟 카리스마", "💛 따뜻함", "🤝 소통 능력", "⚡ 에너지"],
        "color": "#FFD700",
        "bg_color": "#FFFDE7",
        "move": "10만볼트",
        "type": "전기",
        "sprite_id": 25,
    },
    "ENFP": {
        "pokemon": "뮤",
        "english": "Mew",
        "number": "151",
        "emoji": "🌈",
        "reason": "자유로운 영혼과 무한한 상상력! 뮤처럼 모든 기술을 배울 수 있는 잠재력과 장난기 넘치는 매력으로 세상을 즐겨요.",
        "traits": ["🌈 자유분방", "✨ 상상력", "😊 밝은 에너지", "💫 다재다능"],
        "color": "#FF69B4",
        "bg_color": "#FFF0F8",
        "move": "변환",
        "type": "에스퍼",
        "sprite_id": 151,
    },
    "ISTJ": {
        "pokemon": "거북왕",
        "english": "Blastoise",
        "number": "009",
        "emoji": "🛡️",
        "reason": "신뢰할 수 있는 든든한 존재! 거북왕처럼 강인한 방어력과 책임감으로 소중한 것들을 지켜내요.",
        "traits": ["📋 책임감", "🏛️ 안정적", "🛡️ 신뢰감", "⚙️ 체계적"],
        "color": "#2E86AB",
        "bg_color": "#EEF8FF",
        "move": "하이드로캐논",
        "type": "물",
        "sprite_id": 9,
    },
    "ISFJ": {
        "pokemon": "푸린",
        "english": "Jigglypuff",
        "number": "039",
        "emoji": "🎵",
        "reason": "따뜻한 배려심과 헌신적인 사랑! 푸린처럼 노래로 모두를 편안하게 해주며 소중한 사람들을 위해 최선을 다해요.",
        "traits": ["💗 배려심", "🎵 상냥함", "🏠 가정적", "🤲 헌신적"],
        "color": "#FF8FAB",
        "bg_color": "#FFF0F5",
        "move": "잠자기노래",
        "type": "노말/페어리",
        "sprite_id": 39,
    },
    "ESTJ": {
        "pokemon": "괴력몬",
        "english": "Machamp",
        "number": "068",
        "emoji": "💪",
        "reason": "강력한 실행력과 조직력! 괴력몬처럼 네 팔로 모든 일을 동시에 처리하는 뛰어난 관리 능력과 리더십을 가졌어요.",
        "traits": ["📊 조직적", "💪 실행력", "👔 규율", "🏆 성취 지향"],
        "color": "#D4A017",
        "bg_color": "#FFF8E7",
        "move": "크로스촙",
        "type": "격투",
        "sprite_id": 68,
    },
    "ESFJ": {
        "pokemon": "찌리리공",
        "english": "Togekiss",
        "number": "468",
        "emoji": "🕊️",
        "reason": "주변을 행복으로 가득 채우는 당신! 찌리리공처럼 행복의 씨앗을 뿌리며 모두가 웃을 수 있는 환경을 만들어요.",
        "traits": ["🤗 사교적", "💝 친화력", "🌟 긍정적", "🕊️ 평화 사랑"],
        "color": "#58C4DD",
        "bg_color": "#EEF9FF",
        "move": "에어슬래시",
        "type": "노말/비행",
        "sprite_id": 468,
    },
    "ISTP": {
        "pokemon": "마기라스",
        "english": "Tyranitar",
        "number": "248",
        "emoji": "🦖",
        "reason": "냉철하고 실용적인 문제 해결사! 마기라스처럼 강인한 독립심과 예리한 분석력으로 어떤 도전도 거뜬히 이겨내요.",
        "traits": ["🔧 실용적", "🧊 냉철함", "🎯 분석적", "🦖 독립적"],
        "color": "#5C7A5C",
        "bg_color": "#F0F8F0",
        "move": "스톤에지",
        "type": "바위/악",
        "sprite_id": 248,
    },
    "ISFP": {
        "pokemon": "이상해꽃",
        "english": "Venusaur",
        "number": "003",
        "emoji": "🌺",
        "reason": "자연과 함께하는 평온한 예술가! 이상해꽃처럼 꽃을 피워내는 고요한 아름다움과 따뜻한 감성을 가진 특별한 존재예요.",
        "traits": ["🎨 예술적", "🌿 자연친화", "💚 온화함", "🌸 감성적"],
        "color": "#3D9970",
        "bg_color": "#F0FFF8",
        "move": "솔라빔",
        "type": "풀/독",
        "sprite_id": 3,
    },
    "ESTP": {
        "pokemon": "잠만보",
        "english": "Snorlax",
        "number": "143",
        "emoji": "😄",
        "reason": "현실적이고 즉흥적인 행동파! 잠만보처럼 자신만의 페이스로 유유자적하면서도 필요할 때는 강력한 힘을 발휘해요.",
        "traits": ["⚡ 행동파", "😎 현실주의", "🎲 즉흥적", "💥 강력함"],
        "color": "#6AAF84",
        "bg_color": "#F0FFF5",
        "move": "기가임팩트",
        "type": "노말",
        "sprite_id": 143,
    },
    "ESFP": {
        "pokemon": "파이리",
        "english": "Charmander",
        "number": "004",
        "emoji": "🔥",
        "reason": "누구와도 친해지는 사교의 달인! 파이리처럼 밝고 따뜻한 에너지로 주변을 환하게 밝히며 삶을 즐기는 행복 바이러스예요.",
        "traits": ["🎉 사교적", "😄 활발함", "❤️ 열정적", "🌟 낙천적"],
        "color": "#FF8C42",
        "bg_color": "#FFF5EE",
        "move": "화염방사",
        "type": "불꽃",
        "sprite_id": 4,
    },
}
 
MBTI_TYPES = ["INTJ", "INTP", "ENTJ", "ENTP",
              "INFJ", "INFP", "ENFJ", "ENFP",
              "ISTJ", "ISFJ", "ESTJ", "ESFJ",
              "ISTP", "ISFP", "ESTP", "ESFP"]
 
# ─────────────────────────────────────────────
# CSS 스타일
# ─────────────────────────────────────────────
 
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700;800;900&family=Jua&display=swap');
 
* { font-family: 'Nunito', sans-serif; }
 
.stApp {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%);
    min-height: 100vh;
}
 
.main-title {
    text-align: center;
    font-size: 3rem;
    font-weight: 900;
    color: white;
    text-shadow: 3px 3px 0px rgba(0,0,0,0.2), 0 0 30px rgba(255,255,255,0.5);
    margin-bottom: 0.3rem;
    animation: titleFloat 3s ease-in-out infinite;
    letter-spacing: -1px;
}
 
@keyframes titleFloat {
    0%, 100% { transform: translateY(0px); }
    50% { transform: translateY(-8px); }
}
 
.subtitle {
    text-align: center;
    font-size: 1.1rem;
    color: rgba(255,255,255,0.9);
    margin-bottom: 2rem;
    font-weight: 600;
}
 
.card {
    background: white;
    border-radius: 24px;
    padding: 2rem;
    box-shadow: 0 20px 60px rgba(0,0,0,0.15), 0 0 0 1px rgba(255,255,255,0.5);
    margin-bottom: 1.5rem;
    animation: cardIn 0.5s ease-out;
}
 
@keyframes cardIn {
    from { opacity: 0; transform: translateY(30px) scale(0.95); }
    to { opacity: 1; transform: translateY(0) scale(1); }
}
 
.pokemon-card {
    border-radius: 28px;
    padding: 2rem;
    text-align: center;
    position: relative;
    overflow: hidden;
    box-shadow: 0 25px 70px rgba(0,0,0,0.2);
    animation: cardIn 0.6s ease-out;
}
 
.pokemon-card::before {
    content: '';
    position: absolute;
    top: -50%;
    right: -30%;
    width: 300px;
    height: 300px;
    border-radius: 50%;
    background: rgba(255,255,255,0.15);
    pointer-events: none;
}
 
.pokemon-card::after {
    content: '';
    position: absolute;
    bottom: -40%;
    left: -20%;
    width: 250px;
    height: 250px;
    border-radius: 50%;
    background: rgba(255,255,255,0.1);
    pointer-events: none;
}
 
.pokemon-name {
    font-size: 2.2rem;
    font-weight: 900;
    margin: 0;
    text-shadow: 2px 2px 8px rgba(0,0,0,0.2);
}
 
.pokemon-number {
    font-size: 1rem;
    opacity: 0.7;
    font-weight: 700;
    letter-spacing: 2px;
}
 
.trait-badge {
    display: inline-block;
    background: rgba(255,255,255,0.9);
    border-radius: 50px;
    padding: 6px 16px;
    margin: 4px;
    font-size: 0.85rem;
    font-weight: 700;
    box-shadow: 0 3px 10px rgba(0,0,0,0.1);
    color: #333;
}
 
.stat-box {
    background: rgba(255,255,255,0.85);
    border-radius: 16px;
    padding: 12px 20px;
    margin: 8px 0;
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-weight: 700;
}
 
.floating-emoji {
    font-size: 1.5rem;
    animation: floatEmoji 2s ease-in-out infinite;
    display: inline-block;
}
 
@keyframes floatEmoji {
    0%, 100% { transform: translateY(0) rotate(0deg); }
    33% { transform: translateY(-10px) rotate(5deg); }
    66% { transform: translateY(-5px) rotate(-5deg); }
}
 
.stSelectbox > div > div {
    border-radius: 16px !important;
    border: 3px solid rgba(118, 75, 162, 0.3) !important;
    font-size: 1rem !important;
    font-weight: 700 !important;
    padding: 8px 16px !important;
    background: white !important;
}
 
.stSelectbox > div > div:focus-within {
    border-color: #764ba2 !important;
    box-shadow: 0 0 0 4px rgba(118, 75, 162, 0.2) !important;
}
 
.stButton > button {
    background: linear-gradient(135deg, #667eea, #764ba2) !important;
    color: white !important;
    border: none !important;
    border-radius: 50px !important;
    padding: 14px 40px !important;
    font-size: 1.1rem !important;
    font-weight: 800 !important;
    width: 100% !important;
    cursor: pointer !important;
    box-shadow: 0 8px 25px rgba(102, 126, 234, 0.5) !important;
    transition: all 0.3s ease !important;
    letter-spacing: 0.5px !important;
}
 
.stButton > button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 12px 35px rgba(102, 126, 234, 0.7) !important;
}
 
.confetti-emoji {
    font-size: 2rem;
    animation: spin 1s ease-in-out;
}
 
@keyframes spin {
    0% { transform: rotate(0deg) scale(0); opacity: 0; }
    50% { transform: rotate(180deg) scale(1.3); }
    100% { transform: rotate(360deg) scale(1); opacity: 1; }
}
 
.shimmer-text {
    background: linear-gradient(90deg, #667eea, #f093fb, #764ba2, #667eea);
    background-size: 200% auto;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    animation: shimmer 3s linear infinite;
    font-weight: 900;
}
 
@keyframes shimmer {
    to { background-position: 200% center; }
}
 
.divider {
    border: none;
    height: 2px;
    background: linear-gradient(90deg, transparent, rgba(118,75,162,0.3), transparent);
    margin: 1rem 0;
}
 
.reason-box {
    background: linear-gradient(135deg, rgba(255,255,255,0.9), rgba(255,255,255,0.7));
    border-left: 4px solid;
    border-radius: 12px;
    padding: 16px 20px;
    margin: 1rem 0;
    font-weight: 600;
    font-size: 1rem;
    line-height: 1.6;
    color: #333;
}
 
.mbti-grid-title {
    text-align: center;
    color: white;
    font-size: 1.3rem;
    font-weight: 800;
    margin-bottom: 1rem;
    text-shadow: 1px 1px 3px rgba(0,0,0,0.2);
}
 
.info-banner {
    background: rgba(255,255,255,0.2);
    backdrop-filter: blur(10px);
    border-radius: 16px;
    padding: 12px 20px;
    text-align: center;
    color: white;
    font-weight: 700;
    margin-bottom: 1.5rem;
    border: 1px solid rgba(255,255,255,0.3);
}
 
</style>
""", unsafe_allow_html=True)
 
 
# ─────────────────────────────────────────────
# 헤더
# ─────────────────────────────────────────────
 
st.markdown('<div class="main-title">✨ MBTI 포켓몬 매칭 ✨</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">🔮 나와 닮은 포켓몬은 누구일까? 지금 바로 알아봐요! 🎮</div>', unsafe_allow_html=True)
 
# 랜덤 이모지 배너
emojis = ["⚡", "🌊", "🔥", "🌿", "💫", "🎯", "🌈", "💜"]
banner_text = "  ".join(emojis * 3)
st.markdown(f'<div class="info-banner">{banner_text}</div>', unsafe_allow_html=True)
 
# ─────────────────────────────────────────────
# MBTI 선택 카드
# ─────────────────────────────────────────────
 
st.markdown("""
<div class="card">
    <h3 style="text-align:center; color:#764ba2; font-weight:900; font-size:1.4rem; margin-bottom:0.3rem;">
        🧩 내 MBTI를 선택해줘!
    </h3>
    <p style="text-align:center; color:#888; font-size:0.9rem; margin-bottom:1rem;">
        16가지 유형 중에서 나에게 맞는 유형을 골라봐요 💭
    </p>
</div>
""", unsafe_allow_html=True)
 
selected_mbti = st.selectbox(
    "MBTI 유형 선택",
    ["👆 유형을 선택해주세요!"] + MBTI_TYPES,
    label_visibility="collapsed"
)
 
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    match_button = st.button("🎰 포켓몬 매칭 시작!", use_container_width=True)
 
# ─────────────────────────────────────────────
# 결과 표시
# ─────────────────────────────────────────────
 
if match_button and selected_mbti != "👆 유형을 선택해주세요!":
    
    # 로딩 애니메이션
    with st.spinner(""):
        loading_placeholder = st.empty()
        loading_messages = [
            "🔮 포켓몬 세계를 탐색하는 중...",
            "⚡ 당신의 에너지를 분석하는 중...",
            "✨ 완벽한 포켓몬을 찾았어요!"
        ]
        for msg in loading_messages:
            loading_placeholder.markdown(
                f'<div style="text-align:center; color:white; font-size:1.2rem; font-weight:700; padding:20px;">{msg}</div>',
                unsafe_allow_html=True
            )
            time.sleep(0.6)
        loading_placeholder.empty()
 
    data = MBTI_POKEMON[selected_mbti]
    sprite_url = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/{data['sprite_id']}.png"
    home_sprite_url = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{data['sprite_id']}.gif"
 
    # 🎉 등장 이모지 효과
    confetti_cols = st.columns(7)
    celebrate_emojis = ["🎉", "⭐", "🎊", "💥", "🌟", "🎈", "✨"]
    for i, col in enumerate(confetti_cols):
        col.markdown(f'<div class="confetti-emoji" style="text-align:center;">{celebrate_emojis[i]}</div>', unsafe_allow_html=True)
 
    st.markdown("<br>", unsafe_allow_html=True)
 
    # 메인 포켓몬 카드
    card_style = f"background: linear-gradient(135deg, {data['color']}22, {data['color']}44); border: 3px solid {data['color']}66;"
    
    st.markdown(f"""
    <div class="pokemon-card" style="{card_style}">
        <div class="pokemon-number" style="color:{data['color']};">NO. #{data['number']}</div>
        <img src="{sprite_url}" 
             style="width:220px; height:220px; object-fit:contain; 
                    filter: drop-shadow(0 15px 30px {data['color']}88);
                    animation: bounce 1s ease-in-out infinite alternate;"
             onerror="this.src='https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{data['sprite_id']}.png'">
        <div style="margin-top:-10px;">
            <span class="floating-emoji">{data['emoji']}</span>
            <h2 class="pokemon-name" style="color:{data['color']}; display:inline; margin: 0 12px;">
                {data['pokemon']}
            </h2>
            <span class="floating-emoji">{data['emoji']}</span>
        </div>
        <p style="color:#666; font-size:0.9rem; font-weight:700; margin:4px 0 12px;">
            {data['english']}
        </p>
        <div>
            {''.join([f'<span class="trait-badge">{t}</span>' for t in data['traits']])}
        </div>
    </div>
    
    <style>
    @keyframes bounce {{
        from {{ transform: translateY(0) scale(1); }}
        to {{ transform: translateY(-12px) scale(1.03); }}
    }}
    </style>
    """, unsafe_allow_html=True)
 
    st.markdown("<br>", unsafe_allow_html=True)
 
    # MBTI 매칭 이유
    st.markdown(f"""
    <div class="card">
        <h4 style="color:{data['color']}; font-weight:900; margin-bottom:0.5rem;">
            💡 {selected_mbti}와 {data['pokemon']}이 닮은 이유
        </h4>
        <div class="reason-box" style="border-color:{data['color']};">
            {data['reason']}
        </div>
    </div>
    """, unsafe_allow_html=True)
 
    # 포켓몬 스탯 정보
    st.markdown(f"""
    <div class="card">
        <h4 style="color:#764ba2; font-weight:900; margin-bottom:1rem; text-align:center;">
            📋 포켓몬 정보
        </h4>
        <div class="stat-box">
            <span style="color:#666;">🏷️ 타입</span>
            <span style="color:{data['color']}; font-weight:800;">{data['type']}</span>
        </div>
        <div class="stat-box">
            <span style="color:#666;">⚔️ 대표 기술</span>
            <span style="color:{data['color']}; font-weight:800;">{data['move']}</span>
        </div>
        <div class="stat-box">
            <span style="color:#666;">🎯 매칭 MBTI</span>
            <span style="color:{data['color']}; font-weight:800;">{selected_mbti}</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
 
    # 공유 문구
    st.markdown(f"""
    <div style="text-align:center; margin-top:1rem; padding:20px; 
                background:rgba(255,255,255,0.2); border-radius:20px;
                backdrop-filter:blur(10px); border:1px solid rgba(255,255,255,0.4);">
        <p style="color:white; font-size:1.1rem; font-weight:800; margin:0;">
            ✨ {selected_mbti}인 당신의 포켓몬 파트너는
        </p>
        <p style="color:white; font-size:1.8rem; font-weight:900; margin:4px 0;">
            {data['emoji']} {data['pokemon']} {data['emoji']}
        </p>
        <p style="color:rgba(255,255,255,0.8); font-size:0.85rem; font-weight:600; margin:0;">
            친구에게 공유해서 파트너 포켓몬을 비교해봐요! 🎮
        </p>
    </div>
    """, unsafe_allow_html=True)
 
elif match_button and selected_mbti == "👆 유형을 선택해주세요!":
    st.markdown("""
    <div style="text-align:center; padding:20px; background:rgba(255,255,255,0.9); 
                border-radius:16px; margin-top:1rem;">
        <p style="font-size:1.2rem; color:#764ba2; font-weight:800;">
            😅 먼저 MBTI 유형을 선택해주세요!
        </p>
    </div>
    """, unsafe_allow_html=True)
 
# ─────────────────────────────────────────────
# 전체 MBTI 목록 (접이식)
# ─────────────────────────────────────────────
 
st.markdown("<br>", unsafe_allow_html=True)
 
with st.expander("🗂️ 모든 MBTI 포켓몬 보기"):
    cols = st.columns(4)
    for i, mbti in enumerate(MBTI_TYPES):
        p = MBTI_POKEMON[mbti]
        with cols[i % 4]:
            sprite_sm = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{p['sprite_id']}.png"
            st.markdown(f"""
            <div style="text-align:center; background:white; border-radius:16px; 
                        padding:12px 8px; margin-bottom:12px;
                        box-shadow:0 4px 15px rgba(0,0,0,0.1);
                        border-top:3px solid {p['color']};">
                <img src="{sprite_sm}" style="width:60px; height:60px; object-fit:contain;">
                <p style="font-weight:800; color:{p['color']}; font-size:0.8rem; margin:4px 0 0;">{mbti}</p>
                <p style="font-weight:700; color:#333; font-size:0.75rem; margin:0;">{p['pokemon']} {p['emoji']}</p>
            </div>
            """, unsafe_allow_html=True)
 
# 푸터
st.markdown("""
<div style="text-align:center; margin-top:2rem; color:rgba(255,255,255,0.7); font-size:0.85rem; font-weight:600;">
    💜 포켓몬 이미지 출처: PokéAPI • Made with Streamlit 🎈
</div>
""", unsafe_allow_html=True)

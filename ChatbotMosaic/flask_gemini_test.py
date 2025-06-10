from flask import Flask, request
from flask_cors import CORS
import google.generativeai as genai

GOOGLE_API_KEY = "AIzaSyAQVeCbpIjCaIE6JQb2FNupWIuatvA5OF4"
genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel("models/gemini-1.5-flash")

app = Flask(__name__)
CORS(app)

@app.route('/')
def gemini_test():
    question = request.args.get("question", "").strip()

    if not question:
        return "❗ 질문을 입력해주세요. 예: ?question=모임 추천", 400

    # 1️⃣ 고정 응답
    if any(kw in question for kw in ["너는 누구", "정체", "챗봇", "누구세요", "소개"]):
        return "저는 스토리모자이크 전용 챗봇입니다. 무엇이든 물어보세요!"

    # 2️⃣ 플랫폼 관련 질문
    platform_keywords = ["모임", "가입", "후기", "리뷰", "스토리", "참여"]
    if any(kw in question for kw in platform_keywords):
        prompt = [
            "당신은 '스토리모자이크' 플랫폼에 탑재된 전용 챗봇입니다. 플랫폼 관련 질문에만 응답하세요.",
            f"질문: {question}"
        ]
    else:
        # 3️⃣ 일반 질문
        prompt = [
            "당신은 '스토리모자이크'라는 커뮤니티 플랫폼의 챗봇입니다. 문화, 사회, 다문화 관련 일반적인 질문에도 응답해 주세요.",
            f"질문: {question}"
        ]

    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        print("[Gemini 오류]", e)
        return "⚠️ 챗봇 처리 중 오류가 발생했습니다.", 500

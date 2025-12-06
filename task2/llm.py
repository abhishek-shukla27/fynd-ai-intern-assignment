import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-pro")

def analyze_review(review, rating):
    prompt = f"""
You are a customer support AI.

Customer rating: {rating}
Customer review: "{review}"

Generate the following:
1. A polite response to the customer
2. A one-line summary of the feedback
3. A recommended action for the business

Return the output in this exact format:

Response:
<text>

Summary:
<text>

Action:
<text>
"""

    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return "AI service unavailable"

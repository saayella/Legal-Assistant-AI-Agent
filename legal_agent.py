from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_sueme_prompt(accused, situation, country):
    return f"""
You are a legal expert AI named SueMe. Your job is to analyze legal disputes and estimate possible compensation outcomes. Be direct and concise.

Accused Party: {accused}
Situation: {situation}
Country: {country}

Please respond with:
Short answer : YES OR NO
1. What kind of legal issue this is (e.g. employment law, defamation, personal injury, etc.)
2. Whether the person has a case worth pursuing.
3. The estimated compensation range in local currency, based on legal precedent or typical settlements in {country}.
4. Suggested next step(s).
"""

def call_openai(prompt):
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a legal reasoning assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content

def run_sueme():
    print("\n===== SUE ME — LEGAL COMPENSATION ESTIMATOR =====")
    accused = input("Who is the person you're thinking of suing? ")
    situation = input("Describe what happened: ")
    country = input("What country did this happen in? ")

    prompt = generate_sueme_prompt(accused, situation, country)
    result = call_openai(prompt)

    print("\n📢 SueMe says...\n")
    print(result)

if __name__ == "__main__":
    run_sueme()

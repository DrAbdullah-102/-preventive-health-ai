print("=== Advanced Health AI Chatbot ===\n")

# نظام الأمراض والنقاط
score = {
    "flu": 0,
    "migraine": 0,
    "gastritis": 0
}

# إدخال المستخدم
user_input = input("Describe your symptoms: ").lower()

# تحليل أولي (NLP بسيط)
if "fever" in user_input:
    score["flu"] += 2

if "cough" in user_input:
    score["flu"] += 2

if "fatigue" in user_input:
    score["flu"] += 1

if "headache" in user_input:
    score["migraine"] += 2

if "nausea" in user_input:
    score["migraine"] += 2
    score["gastritis"] += 1

if "stomach" in user_input or "pain" in user_input:
    score["gastritis"] += 3


# أسئلة متابعة ذكية (Adaptive)
print("\n--- Follow-up questions ---")

if score["flu"] > 0:
    q = input("Do you have chills? (yes/no): ").lower()
    if q == "yes":
        score["flu"] += 1

if score["migraine"] > 0:
    q = input("Are you sensitive to light? (yes/no): ").lower()
    if q == "yes":
        score["migraine"] += 1

if score["gastritis"] > 0:
    q = input("Did you eat spicy or heavy food recently? (yes/no): ").lower()
    if q == "yes":
        score["gastritis"] += 1


# تحديد النتيجة
diagnosis = max(score, key=score.get)

print("\n=== Result ===")

if diagnosis == "flu":
    print("Most likely: Viral infection (Flu)")
    print("Advice:")
    print("- Rest and sleep")
    print("- Drink plenty of fluids")
    print("- Monitor temperature")

elif diagnosis == "migraine":
    print("Most likely: Migraine")
    print("Advice:")
    print("- Rest in a dark quiet room")
    print("- Stay hydrated")
    print("- Avoid stress and screens")

elif diagnosis == "gastritis":
    print("Most likely: Gastritis")
    print("Advice:")
    print("- Avoid spicy and heavy food")
    print("- Eat light meals")
    print("- Monitor symptoms")

# عرض كل النقاط (للاحتراف)
print("\n--- Debug Info (Scores) ---")
for disease, value in score.items():
    print(f"{disease}: {value}")

print("\nNote: This is not a medical diagnosis. Consult a doctor if needed.")

print("=== Health AI Chatbot ===")

score = {
    "flu": 0,
    "migraine": 0,
    "gastritis": 0
}

# سؤال 1
fever = input("Do you have fever? (yes/no): ").lower()
if fever == "yes":
    score["flu"] += 2

# سؤال 2
cough = input("Do you have cough? (yes/no): ").lower()
if cough == "yes":
    score["flu"] += 2

# سؤال 3
headache = input("Do you have headache? (yes/no): ").lower()
if headache == "yes":
    score["migraine"] += 2
    score["flu"] += 1

# سؤال 4
nausea = input("Do you feel nausea? (yes/no): ").lower()
if nausea == "yes":
    score["migraine"] += 2
    score["gastritis"] += 1

# سؤال 5
stomach = input("Do you have stomach pain? (yes/no): ").lower()
if stomach == "yes":
    score["gastritis"] += 3

# تحديد أعلى احتمال
diagnosis = max(score, key=score.get)

print("\n=== Result ===")

if diagnosis == "flu":
    print("Most likely: Viral infection (Flu)")
    print("Advice: Rest, fluids, monitor temperature")

elif diagnosis == "migraine":
    print("Most likely: Migraine")
    print("Advice: Rest in dark room, hydration")

elif diagnosis == "gastritis":
    print("Most likely: Gastritis")
    print("Advice: Avoid spicy food, eat light meals")

print("\nNote: This is not a medical diagnosis. Consult a doctor if needed.")

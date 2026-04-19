print("=== Health AI Companion ===")

symptoms = input("Enter your symptoms: ").lower()

if "fever" in symptoms and "cough" in symptoms:
    print("Possible: Viral infection")
    print("Advice: Rest and drink fluids")

elif "headache" in symptoms:
    print("Possible: Tension headache")
    print("Advice: Rest and reduce stress")

elif "stomach" in symptoms:
    print("Possible: Digestive issue")
    print("Advice: Avoid heavy food and monitor symptoms")

else:
    print("Not enough data")
    print("Advice: Consult a doctor if needed")

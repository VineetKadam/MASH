from orchestrator.orchestrator import run_diagnosis

symptoms = input("Enter patient symptoms: ")

result = run_diagnosis(symptoms)

print(result)
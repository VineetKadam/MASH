from rag.domain_retriever import retrieve_domain_knowledge

symptoms = "chest pain and shortness of breath"

print("Cardiology knowledge:\n")
print(retrieve_domain_knowledge(symptoms, "cardiology"))

print("\nNeurology knowledge:\n")
print(retrieve_domain_knowledge(symptoms, "neurology"))

print("\nPulmonology knowledge:\n")
print(retrieve_domain_knowledge(symptoms, "pulmonology"))
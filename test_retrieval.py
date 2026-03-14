from rag.retrieve import retrieve_medical_knowledge

query = "chest pain and shortness of breath"

results = retrieve_medical_knowledge(query)

print("Retrieved Medical Knowledge:\n")
print(results)
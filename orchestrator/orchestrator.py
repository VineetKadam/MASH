from agents.cardiology_agent import cardiology_agent
from agents.neurology_agent import neurology_agent
from agents.pulmonology_agent import pulmonology_agent
from llm.gemini_client import ask_gemini


def run_diagnosis(symptoms):

    print("\nCollecting medical knowledge...\n")

    cardio = cardiology_agent(symptoms)
    neuro = neurology_agent(symptoms)
    pulmo = pulmonology_agent(symptoms)

    prompt = f"""
You are a senior medical diagnostician coordinating multiple specialist AI agents.

Clinical Reasoning Guidelines:

1. Prioritize common and benign conditions before considering rare or life-threatening diseases.
2. Only suggest severe or emergency diagnoses if the symptoms strongly support them.
3. Avoid alarming conclusions when the evidence is weak or incomplete.
4. Use specialist knowledge from the agents to determine likelihood and relevance.
5. If symptoms are mild, isolated, or nonspecific, favor common explanations.
6. Reserve HIGH urgency only for situations where symptoms clearly indicate possible emergency conditions.
7. Use MODERATE urgency when symptoms require medical evaluation but are not immediately life-threatening.
8. Use LOW urgency when symptoms are mild and likely benign.
9. If specialist agents disagree, weigh their confidence and relevance before deciding.
10. The final diagnosis should reflect the most plausible explanation given the evidence retrieved from the agents.

Patient symptoms:
{symptoms}

Specialist knowledge retrieved:

Cardiology Agent Knowledge:
{cardio}

Neurology Agent Knowledge:
{neuro}

Pulmonology Agent Knowledge:
{pulmo}

Generate a SHORT structured diagnosis.

Rules:
- Keep the output concise.
- Credit the agent whose knowledge supports the diagnosis.
- Include a confidence score (0.0–1.0).

Output format exactly:

Most Probable Diagnosis:
<diagnosis> (Source: <Agent Name>, Confidence: <score>)

Alternative Diagnoses:
<diagnosis> (Source: <Agent Name>, Confidence: <score>)
<diagnosis> (Source: <Agent Name>, Confidence: <score>)

Recommended Tests:
<test>
<test>
<test>

Urgency Level:
Low / Moderate / High
"""

    result = ask_gemini(prompt)

    return f"""
===============================
AI MEDICAL DIAGNOSTIC SUMMARY
===============================

{result}
"""
# agents/usecase.py
import os
import re
from langchain_groq import ChatGroq

# Create Groq client
llm = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model_name="llama3-70b-8192",
    temperature=0.7,
)

def generate_usecases(context: str) -> list[dict]:
    prompt = f"""
You are an AI strategist assigned to generate practical AI/GenAI use cases.

Company / Industry Context:
{context}

Instructions:
- Analyze industry trends based on reports and insights from sources like McKinsey, Deloitte, Nexocode.
- Generate **EXACTLY 5** use cases.
- Each use case must have:
    1. **Title**: 2-6 words, bolded (**like this**)
    2. **One-line Benefit**: Summarize value
    3. **Source**: At least one citation in parentheses at end.

- Format the response as **a numbered Markdown list** exactly like this:

1. **[Use Case Title]**: [One-line benefit] (Source: [Reference])
2. **[Use Case Title]**: [One-line benefit] (Source: [Reference])
... and so on.

Return only the list. No extra text.
"""
    result = llm.invoke(prompt)
    result_content = result.content   # ✅ Extract plain text
    
    pattern = r"\d+\.\s+\*\*(.+?)\*\*:\s+(.+?)\s+\(Source:\s*(.+?)\)"
    out = []
    for title, desc, src in re.findall(pattern, result_content):
        out.append({
            "title": title.strip(),
            "description": desc.strip(),
            "source": src.strip()
        })
    
    return out

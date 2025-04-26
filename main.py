# main.py
import dotenv
dotenv.load_dotenv()

from pathlib import Path
from agents.research import run_research
from agents.usecase import generate_usecases
from agents.resources import collect_resources

def build_proposal(target: str) -> str:
    info = run_research(target)
    usecases = generate_usecases(info["summary"])
    md_lines = [f"# AI / GenAI Proposal for **{target}**\n",
                "## 1  Industry & Company Snapshot\n",
                info["summary"], "\n",
                "## 2  Recommended Use Cases\n"]
    for i, uc in enumerate(usecases, 1):
        md_lines.append(f"### {i}. {uc['title']}\n")
        md_lines.append(f"{uc['description']}  \n*Source:* {uc['source']}\n")
        links = collect_resources(uc["title"])
        if links:
            md_lines.append("**Starter datasets / repos:**")
            for title, url in links:
                md_lines.append(f"- [{title}]({url})")
        md_lines.append("")
    return "\n".join(md_lines)

if __name__ == "__main__":
    company = input("Enter company or industry: ").strip()
    report = build_proposal(company)
    out_path = Path("proposal.md")
    out_path.write_text(report, encoding="utf-8")
    print(f"\n✅  Proposal saved to {out_path.resolve()}")

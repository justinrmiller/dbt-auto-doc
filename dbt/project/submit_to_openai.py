import os
import typer
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
from typing import Optional

app = typer.Typer()

# You must set your OpenAI API key

PROMPT_HEADER = """You are an expert data engineer. Given a set of dbt model files and seed CSVs, generate a comprehensive summary document describing the DBT setup. Your summary should include:

1. A high-level **overview** of the structure (staging, marts, seeds).
2. A **description of each seed file** and what kind of data it contains.
3. A **table summarizing staging models**, their sources, and key fields extracted.
4. A **description of each mart model**, the joins it performs, and any calculated fields.
5. A **data lineage diagram** in text format (ASCII or pseudo-graph).
6. A brief **conclusion** highlighting good practices or architectural choices.

Use clear headings, structured tables, and readable prose. Make the summary business-friendly while still detailed enough for technical audiences.

---

Here are the files:
"""

def collect_files(base_dir: str, suffixes: tuple) -> list:
    result = []
    for root, _, files in os.walk(base_dir):
        for file in files:
            if file.endswith(suffixes):
                file_path = os.path.join(root, file)
                result.append(file_path)
    return result

@app.command()
def submit_summary(
    models: str = typer.Option("models", help="Path to your models directory"),
    seeds: str = typer.Option("seeds", help="Path to your seeds directory"),
    output: Optional[str] = typer.Option("output.md", help="Path to save the generated summary"),
    model: str = typer.Option("gpt-4o", help="OpenAI model to use (e.g., gpt-4, gpt-3.5-turbo)")
):
    if not os.path.isdir(models) or not os.path.isdir(seeds):
        typer.echo("❌ Both models and seeds directories must exist.")
        raise typer.Exit(code=1)

    sql_files = collect_files(models, (".sql",))
    csv_files = collect_files(seeds, (".csv",))

    all_files = sql_files + csv_files
    if not all_files:
        typer.echo("⚠️ No SQL or CSV files found.")
        raise typer.Exit(code=0)

    prompt = PROMPT_HEADER.strip() + "\n\n"
    for file_path in sorted(all_files):
        rel_path = os.path.relpath(file_path)
        prompt += f"File: {rel_path}\n" + ("-" * 80) + "\n"
        with open(file_path, "r", encoding="utf-8") as f:
            prompt += f.read().strip() + "\n"
        prompt += ("-" * 80) + "\n\n"

    typer.echo("📡 Submitting prompt to OpenAI...")
    try:
        response = client.chat.completions.create(model=model,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.0)
        content = response.choices[0].message.content.strip()
        with open(output, "w", encoding="utf-8") as f_out:
            f_out.write(content)
        typer.echo(f"✅ Summary written to {output}")
    except Exception as e:
        typer.echo(f"❌ Failed to get response from OpenAI: {e}")
        raise typer.Exit(code=1)

if __name__ == "__main__":
    app()

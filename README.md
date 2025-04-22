# 📘 dbt-auto-doc

Automatically generate **rich, business-readable documentation** for your [dbt](https://www.getdbt.com/) project using OpenAI's GPT-4o—fully integrated into your GitHub Actions workflow.

Every time you open a PR, your dbt models and seed files are analyzed and documented by an LLM. The result? Clean, contextual markdown docs committed directly to your branch as `output.md`.

---

## 🚀 Features

- ✨ **LLM-Powered Documentation**: Uses GPT-4o to generate human-friendly documentation from dbt models and seed files.
- 🔄 **CI/CD Integration**: Seamlessly hooks into your GitHub Actions pipeline—no manual steps required.
- 🗂️ **Auto-Summarized Structure**: Includes model overviews, joins, sources, seed file descriptions, and more.
- 🧠 **Business + Technical Alignment**: Summaries are accessible to analysts, engineers, and stakeholders alike.
- ✅ **Zero Maintenance**: Docs update on every PR—ensuring they never go stale.

---

## 🧰 Tech Stack

- **dbt** – Data transformation framework  
- **OpenAI GPT-4o API** – LLM inference engine  
- **GitHub Actions** – CI/CD pipeline integration  
- **Typer** – Command-line interface for local runs

---

## 📸 Example Output

The generated `output.md` includes:

- Overview of your dbt DAG (staging, marts, seeds)
- Description of each seed file and its contents
- Table of staging models, sources, and fields
- Detailed descriptions of mart models and joins
- ASCII data lineage diagram
- Best practices and architectural notes

👉 [See PR Example](https://github.com/justinrmiller/dbt-auto-doc/pull/2)

---

## ⚙️ Setup

### 1. Prerequisites

- A working dbt project (with `models/` and `seeds/`)
- [OpenAI API key](https://platform.openai.com/account/api-keys)
- Add `OPENAI_API_KEY` as a GitHub Secret

### 2. Add the Script

Copy `generate_with_openai.py` into your dbt repo.

This script:
- Collects all `.sql` model files and `.csv` seed files
- Constructs a prompt
- Calls OpenAI's API
- Writes the response to `output.md`

### 3. GitHub Action

Add the workflow file (or reuse `dbt.yml` in this repo).  
It will:

1. Set up Python + dbt
2. Spin up Postgres
3. Run `dbt seed` + `dbt run`
4. Call the OpenAI script
5. Commit `output.md` back to your PR

> ⚠️ Ensure your workflow has **Read and Write** permissions set in GitHub Actions settings.

---

## 💡 Prompt Logic

The prompt sent to GPT-4o requests:

- Overview of staging/mart layers
- Descriptions of each seed file
- Table of staging models and sources
- Explanation of marts, joins, calculated fields
- Lineage diagram (text-based)
- Conclusion with architectural highlights

This ensures both **breadth and depth** in the documentation.

---

## 📦 Local Development

You can also run the script locally with:

```bash
pip install openai typer
python generate_with_openai.py --models path/to/models --seeds path/to/seeds --output output.md
```

---

## 🧪 Future Ideas

- Post documentation as PR comments
- Send summaries to Slack or Teams
- Add quality gates that require updated docs
- Embed rendered markdown in GitHub Pages

---

## 📚 References

- [dbt Documentation](https://docs.getdbt.com/docs/build)
- [OpenAI API](https://platform.openai.com/docs/)
- [GitHub Actions](https://docs.github.com/en/actions)
- [Typer CLI](https://typer.tiangolo.com)

---

## 🙌 Contributing

Want to improve the prompt, enhance the workflow, or add new output formats? PRs are welcome!

---

## 🧠 Why This Matters

Keeping dbt docs current is often overlooked. This repo brings **LLM automation** to your CI/CD, ensuring docs stay fresh and relevant with **zero manual effort**.

Say goodbye to outdated READMEs and stale wiki pages.

---

### ⭐️ Give it a star if you find it useful!

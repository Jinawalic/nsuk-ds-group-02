# 🤖 AI-use statement

**Group:** Group 02

## 1. Tools used
- [ ] ChatGPT  - [x] Google Gemini  - [ ] Microsoft Copilot  - [ ] GitHub Copilot  - [ ] Claude  - [ ] Meta AI  - [ ] Other: ______
- [ ] We did not use any AI tools.

## 2. What we used AI for
| Part / file | Member | What we asked the AI (summary or exact prompt) | How we used the answer |
|---|---|---|---|
| Part 1–2 (`notebooks/group_project.ipynb`) | Jinawa Titus Torhile (Data lead) | Clarify `pandas` cleaning logic for text-encoded numbers, sentinel `-999` values, and Git branch/merge synchronization | Verified row counts (`2,436` raw → `2,360` clean) and executed the cleaning pipeline in our notebook |
| Part 3 (`notebooks/group_project.ipynb`) | Maji Friday (Visualisation lead) | Review formatting and labels for multi-panel seaborn/matplotlib figures (`fig1_yield_by_seed_and_staking.png`) | Applied clean axis titles, units, and 300-dpi export settings after inspecting plotted values against group summaries |
| Part 4–5 (`notebooks/group_project.ipynb`) | Chidume Chinwe Augustina (Statistics lead) | Format APA reporting for Welch's $t$-test, $\chi^2$ test, and multivariable OLS regression output | Structured the statistical write-up and cross-checked every coefficient, confidence interval, and $p$-value against `results/ols_coefficients.csv` |
| Part 6 (`notebooks/group_project.ipynb`) | Ezra Isaac (ML lead) | Explain leakage-free scikit-learn `Pipeline` cross-validation and permutation importance interpretation | Confirmed our 5-fold CV comparison (`results/table3_model_comparison_cv.csv`) and hold-out test metrics (`models/model_card.json`) |
| Part 8 (`app/streamlit_app.py`) | Tudi James (App lead) | Step-by-step guidance completing TODOs 1–8 and fixing a Python indentation / `NameError` bug before Streamlit Cloud deployment | Applied the corrected indentation, tested all three app tabs locally and live at `group02project.streamlit.app` |
| Part 9 (`report/GROUP_REPORT.md`, `CONTRIBUTIONS.md`) | All members | Organize and polish our notebook outputs, tables, and project documentation into the final report template | Reviewed every section, inserted our exact notebook numbers, and approved the final text as a team |

## 3. How we checked the AI's output
- We ran **Restart & Run All** on `notebooks/group_project.ipynb` from top to bottom to verify that every data cleaning step, statistical test, figure, and ML pipeline executed without errors and passed all automated `✅` checks.
- We cross-checked every single number in `report/GROUP_REPORT.md` directly against our notebook cell outputs, `results/table1_descriptives_by_staking.csv`, `results/ols_coefficients.csv`, `results/table3_model_comparison_cv.csv`, and `models/model_card.json` (confirming $N = 2,360$, staking difference $= 1.63\text{ t/ha}$, OLS adjusted $R^2 = 0.599$, and test Linear Regression $R^2 = 0.586$, $\text{MAE} = 1.42\text{ t/ha}$).
- We tested `app/streamlit_app.py` locally (`localhost:8501`) and on Streamlit Community Cloud (`https://group02project.streamlit.app`) across all three tabs to verify predictions, charts, and model card metrics rendered accurately.

## 4. What we did NOT use AI for / what we did not share
- We did not upload or paste the raw or cleaned CSV datasets (`yam_yield_raw.csv` or `yam_yield_clean.csv`) into any AI tool—we only shared column names, code snippets, and aggregated summary outputs.
- All data cleaning decisions, statistical modeling runs, model selection, GitHub commits, and live Streamlit deployment were executed directly by Group 02 members.
- We verified that no fabricated citations or external references were introduced anywhere in the report.

## 5. Declaration
We confirm this statement is accurate, that we checked all AI-generated content, and that we take responsibility for everything in this repository.

| Member | Agree (type your name) |
|---|---|
| Member 1 | Jinawa Titus Torhile |
| Member 2 | Maji Friday |
| Member 3 | Chidume Chinwe Augustina |
| Member 4 | Ezra Isaac |
| Member 5 | Tudi James |
# 👥 Contributions

**Group:** Group ___

**Step 5 (first commit):** each member fills in **only their own row** (Name, GitHub username, Role) and pushes it.
**Before submission:** each member updates their **What I did** column. Be specific, e.g. *"Parts 1–2: wrote the
cleaning code for LGAs, Yes/No and months; wrote report section 2; fixed the merge conflict on 20 Nov."*

| # | Name | GitHub username | Role | What I did |
|---|---|---|---|---|
| 1 |Jinawa Titus Torhile| @Jinawalic | Coordinator + Data lead (Parts 1–2) | Set up Group 02 GitHub repo and branch/PR coordination; audited 2,436 raw records and wrote Parts 1–2 cleaning code (LGAs, Yes/No, gender, months, `-999` codes, text-encoded numbers, and leaky column exclusion) producing `data/processed/yam_yield_clean.csv` (2,360 farms); drafted Section 2 of `report/GROUP_REPORT.md` and `docs/AI_USE_STATEMENT.md`.|
| 2 |Maji Friday | @friday-mj |member+ Visualisation lead (Parts 3 and 7) |Cloned repo and completed Part 3 EDA and Part 7 publication figures in `figures/` (`yam_yield_distribution.png`, `yam_yield_by_lga.png`, `yam_yield_by_staking.png`, `extension_yield.png`, and `fig1_yield_by_seed_and_staking.png`); drafted Section 3 of `report/GROUP_REPORT.md`. |
| 3 |Chidume Chinwe Augustina | @ChinweChidume86 | Statistics lead (Parts 4–5) | Conducted Part 4 hypothesis tests (H1 staking Welch's $t$-test, H2 cooperative × credit $\chi^2$ test, H3 gender $t$-test) and saved `results/table1_descriptives_by_staking.csv`; fitted the Part 5 multivariable OLS regression (`results/ols_coefficients.csv`, `fig2_regression_coefficients.png`); drafted Sections 4 and 5 of `report/GROUP_REPORT.md`.|
| 4 |Ezra Isaac | @exraisaac| Machine-learning lead (Part 6) |Built the Part 6 leakage-free 5-fold CV and 80/20 train/test pipelines across four models (`results/table3_model_comparison_cv.csv`), ran the data leakage experiment, exported `models/yam_yield_model.joblib`, `models/model_card.json`, `fig3_predicted_vs_actual.png`, and `fig4_feature_importance.png`; drafted Section 6 of `report/GROUP_REPORT.md`. |
| 5 |Tudi James | @Tudi22 | App lead (Parts 8–9) |Completed `app/streamlit_app.py` (TODOs 1–8), verified live deployment at `https://group02project.streamlit.app`, and drafted the Abstract, Introduction, Streamlit App, and Conclusion sections of `report/GROUP_REPORT.md`. |
| 5 |Rebecca Nkiruka Umeh | @ | Assist |Cloned repository, assisted with data/report review, and verified reproducibility checks across notebook outputs and documentation. |

## Meeting log *(optional, but helps if there are disagreements later)*
| Date | Who attended | What we agreed |
|---|---|---|
| 11 Nov 2026 | All group members | Created `nsuk-ds-group-02` repository, assigned Parts 1–9 roles, and pushed initial `CONTRIBUTIONS.md` rows. |
| 17 Nov 2026 | All group members | Reviewed and merged Parts 1–3 data cleaning and EDA outputs (`2,360` clean farms). |
| 22 Nov 2026 | All group members | Completed Parts 4–7 statistical inference, OLS regression, ML pipelines, and saved model card. |
| 24 Nov 2026 | All group members | Completed `app/streamlit_app.py` (`group02project.streamlit.app`), finalized `report/GROUP_REPORT.md` and `docs/AI_USE_STATEMENT.md`, and verified full notebook execution. |

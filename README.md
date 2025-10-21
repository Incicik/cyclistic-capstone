# Cyclistic Bike-Share Capstone — Fast Track

(Explanation: This repo is a minimal, ready-to-run scaffold to finish the Cyclistic case quickly while still hitting hiring signals.)

## Deliverables Checklist (print this and tick ✓)
- [ ] `notebooks/01_prepare_process_analyze.ipynb` runs end-to-end
- [ ] `data/processed/cyclistic_clean.parquet` saved
- [ ] 4–6 charts exported to `figures/` (PNG) with decision-oriented titles
- [ ] `docs/executive_summary.md` completed (1 page: 3 insights → 3 actions → 3 metrics)
- [ ] `docs/recommendations_and_experiment.md` completed (A/B plan + expected impact)
- [ ] Portfolio page (Quarto/Markdown/Medium/Notion) published with links to notebook and figures

## Data
(Explanation: Use the official Divvy/Cyclistic monthly CSVs; place the 12 CSVs into `data/raw/`.)

## How to run
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
jupyter lab  # or jupyter notebook
```
Open `notebooks/01_prepare_process_analyze.ipynb` and run all cells. (Explanation: The notebook includes clear markers for each phase: Prepare → Process → Analyze → Share → Act.)

## Figures to produce (target 6)
1. (Decision) **Who rides when?** — median ride duration by weekday × member type
2. (Decision) **Seasonality** — rides per month × member type
3. (Decision) **Where to target** — top 15 casual hotspots (starts) vs top member stations
4. (Decision) **Device mix** — rideable_type distribution × member type
5. (Decision) **Conversion funnel** — casual share by weekday/weekend and by hour
6. (Decision) **Offer sizing** — potential reach if we target top casual hotspots

(Explanation: Each figure title is phrased as a stakeholder question/decision to make the story obvious.)

## Output files
- `data/processed/cyclistic_clean.parquet` (clean dataset with engineered features)
- `data/processed/summary_tables.xlsx` (key summary tabs for quick reference)
- `figures/*.png` (exported visuals, ready for portfolio page)

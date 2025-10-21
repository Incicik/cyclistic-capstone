# Cyclistic Bike-Share Capstone — Fast Track
**Target windows:** Weekends 11:00–16:00; Weekdays 16:00–18:00  
**Traffic:** ~235 eligible exposures/day (≈120 weekday, ≈518 weekend)  
**Power:** n≈9,799 per arm → ~84 days at current scope

**Live site:** https://incicik.github.io/cyclistic-capstone/  
**Executive summary:** [docs/executive_summary.md](docs/executive_summary.md)  
**Analysis notebook (HTML):** [docs/01_prepare_process_analyze.html](docs/01_prepare_process_analyze.html)  
**Recommendations & A/B plan:** [docs/recommendations_and_experiment.md](docs/recommendations_and_experiment.md)

## Deliverables Checklist (print this and tick ✓)
- [ ] `notebooks/01_prepare_process_analyze.ipynb` runs end-to-end
- [ ] `data/processed/cyclistic_clean.parquet` saved
- [ ] 4–6 charts exported to `figures/` (PNG) with decision-oriented titles
- [ ] `docs/executive_summary.md` completed (1 page: 3 insights → 3 actions → 3 metrics)
- [ ] `docs/recommendations_and_experiment.md` completed (A/B plan + expected impact)
- [ ] Portfolio page (Quarto/Markdown/Medium/Notion) published with links to notebook and figures

## Data
- Source: Divvy/Cyclistic monthly trip data (public release).
- Setup: place **12 monthly CSVs** into `data/raw/` (not tracked by Git).
- Output: the notebook builds a cleaned dataset → `data/processed/cyclistic_clean.parquet`.


## How to run
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
jupyter lab  # or jupyter notebook
```
Open `notebooks/01_prepare_process_analyze.ipynb` and run all cells.

## Figures to produce (target 6)
1. (Decision) **Who rides when?** — median ride duration by weekday × member type
2. (Decision) **Seasonality** — rides per month × member type
3. (Decision) **Where to target** — top 15 casual hotspots (starts) vs top member stations
4. (Decision) **Device mix** — rideable_type distribution × member type
5. (Decision) **Conversion funnel** — casual share by weekday/weekend and by hour
6. (Decision) **Offer sizing** — potential reach if we target top casual hotspots


## Output files
- `data/processed/cyclistic_clean.parquet` (clean dataset with engineered features)
- `data/processed/summary_tables.xlsx` (key summary tabs for quick reference)
- `figures/*.png` (exported visuals, ready for portfolio page)
  

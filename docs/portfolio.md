# Cyclistic Bike-Share — Portfolio Case Study



## Ask — Business Task
Convert more **casual riders → annual members** to improve predictable revenue.

## Prepare & Process — Data
12 months of Divvy ride data (public course dataset). Cleaned and engineered: `ride_length_min`, `day_of_week`, `month`, `hour`, filters for outliers.

## Analyze — Findings (with visuals)
![Median ride duration by weekday × member type](../figures/fig1_median_duration_weekday.png)
![Rides per month × member type (seasonality)](../figures/fig2_rides_per_month.png)
![Top 15 casual hotspots](../figures/fig3_top_casual_hotspots.png)
![Rideable type distribution × member type](../figures/fig4_device_mix.png)
![Casual share by hour (weekend vs weekday)](../figures/fig5_casual_share_by_hour.png)



## Share — Executive Summary (paste your auto-generated draft here)
>

## Act — Recommendations & Experiment Plan
- Weekend Day Pass → Annual Offer at top hotspots.
- Summer Weekly Pass with 14-day upgrade credit.
- On-dock prompts during weekend afternoons.
(See `docs/recommendations_and_experiment.md` for A/B design and rollout.)

## Appendix — Reproducibility
- Notebook: `notebooks/01_prepare_process_analyze.ipynb`
- Clean data: `data/processed/cyclistic_clean.parquet`
- Summary tables: `data/processed/summary_tables.xlsx`

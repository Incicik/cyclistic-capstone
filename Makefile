
# (Explanation: Simple automation for common tasks. Use `make <target>` below.)

.PHONY: help placeholders build clean

help: ## (Explanation: Show available targets)
	@echo "Available targets:"
	@grep -E '^[a-zA-Z_-]+:.*?##' Makefile | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-12s\033[0m %s\n", $$1, $$2}'

placeholders: ## (Explanation: Generate placeholder PNGs under ./figures before real analysis)
	python -m src.make_placeholder_figures

build: ## (Explanation: Execute the analysis notebook end-to-end and generate real figures/tables)
	python -m jupyter nbconvert --to notebook --execute notebooks/01_prepare_process_analyze.ipynb --output 01_prepare_process_analyze.ipynb --output-dir notebooks


clean: ## (Explanation: Remove processed outputs and figures)
	rm -f data/processed/*.parquet data/processed/*.xlsx
	rm -f figures/*.png

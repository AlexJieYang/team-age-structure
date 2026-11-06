# team-age-structure

Analysis and figures for team age, age diversity, citation impact, interdisciplinarity, and disruption.

## Environment

Use Python 3.11 or 3.12. Install the declared Python dependencies from the repository root:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

On Windows, activate with `.venv\Scripts\Activate.ps1`. Select the same environment in JupyterLab. 

R scripts require R 4.3 or later and packages `fixest`, `data.table`, `dplyr`, and `jsonlite`:

```r
install.packages(c("fixest", "data.table", "dplyr", "jsonlite"))
```

## Inputs and outputs

Set `data_dir` and `output_dir` in `config.json`, or use the `PROJECT_DATA_DIR` and `PROJECT_OUTPUT_DIR` environment variables. Relative directories resolve from the repository root. `PROJECT_CONFIG` selects another JSON configuration file. `DATA.md` describes the data fields and units used by the analyses.

Generated figures are stored under `outputs/<notebook>/`; R tables use `outputs/tables/`. Set `PROJECT_OUTPUT_DIR` to choose another output directory. Start notebooks and R scripts with the repository root as the working directory. Output directories are created when needed.

Bootstrap figures default to 10,000 resamples and seed 1. `BOOTSTRAP_RESAMPLES` (minimum 1,000) and `RANDOM_SEED` configure these values. Bootstrap calculations use bounded batches where supported.

## Workflow

1. Set the data directory for the prepared paper-level analysis tables.
2. Open `fig 1 S2.ipynb`, `fig 2.ipynb`, `fig 3.ipynb`, or `fig 4.ipynb` from the repository root and run their cells in order. Each notebook is independent.
3. Run `Rscript "Fixeft reg 1.R"` for the regression tables. The figures read `Paper.csv.zip`; regressions read the separately prepared `paperforReg.csv`.

## Source validation

```bash
python scripts/check_sources.py
```

This command parses Python sources, notebook cell sources, and JSON without executing research code or loading research data. The GitHub workflow performs the same static checks. Notebooks are stored with empty outputs and no execution counts.

## Citation and reuse

Use `CITATION.cff` for the software repository and cite the associated research publication separately. 

The code and repository documentation are licensed under MIT; see `LICENSE`.
Third-party datasets, external map data, and research publications retain their original rights and terms; the software license does not grant rights to those materials.

## Research context

# team-age-structure
team age structure
Unveiling the dynamics of team age structure and its impact on scientific innovation
Alex J. Yang 1, Huimin Xu3, Ying Ding 3,4 and Meijun Liu 2

1 School of Information Management, Nanjing University, Nanjing (China).
2 Institute for Global Public Policy, Fudan University, Shanghai (China)
3 School of Information, University of Texas at Austin, Austin, TX (The United States)
4 Department of Population Health, Dell Medical School, University of Texas at Austin (The United States)

Abstract
In the dynamic landscape of contemporary scientific research characterized by increasing collaboration, this study, leveraging a comprehensive dataset spanning six decades and encompassing 16 diverse fields with 30 million journal papers, conducts the first large-scale analysis of age structure within scientific teams. Our findings illuminate a consistent upward trajectory in the average team age over time, coupled with a concurrent decline in team age diversity. Examining their intricate relationships with scientific impact, we unveil intriguing inverted-U associations between team age, team age diversity, and scientific impact. This underscores the optimal performance of moderately aged and diverse teams in terms of team impact. Additionally, our research uncovers a U-shaped relationship between team age, team age diversity, and disruption, emphasizing the disruptive potential of extreme team age patterns. Importantly, these discerned patterns hold robustly across various fields and team sizes, offering valuable insights for strategically composing scientific teams and enhancing their productivity in the collaborative landscape of scientific research.

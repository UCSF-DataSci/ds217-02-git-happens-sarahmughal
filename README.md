# DataSci Week 2 Integration Project - Sarah Mughal

## project overview
this project demonstrates integration of git workflows, CLI automation, and python data processing.

## project structure
```
datasci-week02-integration/
├── README.md
├── tips.md
├── .github
├── .gitignore
├── requirements.txt
├── setup_project.sh
├── src/
│   ├── data_analysis.py
│   └── data_analysis_functions.py
├── data/
│   ├── students.csv
└── output/
    └── analysis_report.txt

```

## features
- **project scaffold**: automated project setup with `setup_project.sh`
- **data processing**: python scripts for student grade analysis
- **git workflow**: feature branch development and merging

## usage
1. run `./setup_project.sh` to create project structure
2. execute `python src/data_analysis.py` for basic analysis
3. run `python src/data_analysis_functions.py` for advanced analysis

## git workflow
| branch | purpose | status |
|--------|---------|--------|
| main | production code | active |
| feature/project-scaffold | CLI automation | merged |
| feature/data-processing | python analysis | merged |
```

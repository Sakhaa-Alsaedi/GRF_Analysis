# Genetic Risk Factor Analysis Tutorial

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![Jupyter Notebook](https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=flat&logo=jupyter&logoColor=white)](https://jupyter.org/)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/yourusername/covid19-genetic-risk-analysis/blob/main/notebooks/COVID19_Genetic_Risk_Analysis_Tutorial.ipynb)

A comprehensive computational workflow for analyzing genetic risk variants associated with severe COVID-19 outcomes, based on the research methodology from:

> **"Computational network analysis of host genetic risk variants of severe COVID-19"**  
> *Alsaedi, S.B., Mineta, K., Gao, X., Gojobori, T. (2023). Human Genomics 17, 17.*  
> DOI: [10.1186/s40246-023-00454-y](https://doi.org/10.1186/s40246-023-00454-y)

## Overview

This tutorial provides hands-on experience with computational methods for genetic risk analysis, including:

- **Data curation and annotation** of genetic variants
- **Functional enrichment analysis** of risk genes
- **Protein-protein interaction network** construction and analysis
- **Pathway analysis and disease mapping**

Perfect for students, researchers, and bioinformaticians interested in COVID-19 genetics, network biology, and computational genomics.

## Repository Structure

```
covid19-genetic-risk-analysis/
├── notebooks/
│   └── COVID19_Genetic_Risk_Analysis_Tutorial.ipynb  # Main tutorial
├── data/
│   ├── covid19_genetic_risk_variants.csv             # Sample dataset (109 variants)
│   └── covid19_gene_summary.csv                      # Gene-level summary
├── scripts/
│   ├── create_synthetic_dataset.py                   # Data generation script
│   └── test_tutorial.py                              # Validation script
├── docs/
│   ├── methodology.md                                 # Detailed methodology
│   └── troubleshooting.md                            # Common issues and solutions
├── images/
│   └── workflow_diagram.png                          # Analysis workflow diagram
├── README.md                                          # This file
├── requirements.txt                                   # Python dependencies
├── LICENSE                                            # MIT License
└── .gitignore                                         # Git ignore file
```

## Quick Start

### Option 1: Google Colab (Recommended)

1. **Click the "Open in Colab" badge above** or [click here](https://colab.research.google.com/github/yourusername/covid19-genetic-risk-analysis/blob/main/notebooks/COVID19_Genetic_Risk_Analysis_Tutorial.ipynb)
2. **Run all cells** - packages will be installed automatically
3. **Follow the tutorial** - no local setup required!

### Option 2: Local Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/covid19-genetic-risk-analysis.git
   cd covid19-genetic-risk-analysis
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Launch Jupyter:**
   ```bash
   jupyter notebook notebooks/COVID19_Genetic_Risk_Analysis_Tutorial.ipynb
   ```

## Analysis Workflow

The tutorial follows a four-phase computational workflow:

### Phase 1: Data Curation and Annotation
- Load and preprocess genetic variant data
- Perform exploratory data analysis
- Quality control and data validation

### Phase 2: Functional Enrichment Analysis
- Gene-level statistical analysis
- Pathway enrichment identification
- Biological process categorization

### Phase 3: Molecular Network Construction
- Build protein-protein interaction networks
- Analyze network topology and centrality
- Detect functional communities
- Identify hub genes

### Phase 4: Pathway Analysis and Disease Mapping
- Map disease-gene associations
- Analyze pathway-disease correlations
- Calculate genetic risk scores
- Interpret biological significance

## Key Features

### Comprehensive Analysis
- **109 genetic variants** analysis (matching original study)
- **Multiple pathway categories**: Immune response, inflammation, viral entry, coagulation
- **Network metrics**: Centrality, clustering, community detection
- **Risk scoring**: Multi-factor genetic risk assessment

### Rich Visualizations
- Interactive network plots with Plotly
- Pathway enrichment heatmaps
- Statistical distribution plots
- Community structure visualization

### Educational Content
- Step-by-step explanations
- Biological interpretation of results
- Best practices for genetic analysis
- Troubleshooting guides

## Technical Requirements

### Python Packages
```
pandas>=1.3.0
numpy>=1.21.0
matplotlib>=3.4.0
seaborn>=0.11.0
plotly>=5.0.0
networkx>=2.6.0
scipy>=1.7.0
scikit-learn>=1.0.0
```

### System Requirements
- **Python:** 3.7 or higher
- **Memory:** 4GB+ RAM recommended
- **Storage:** 100MB for repository
- **Internet:** Required for package installation

## Learning Objectives

After completing this tutorial, you will be able to:

✅ **Load and preprocess** genetic variant datasets  
✅ **Perform functional enrichment** analysis using pathway databases  
✅ **Construct and analyze** protein-protein interaction networks  
✅ **Identify hub genes** and functional communities  
✅ **Calculate genetic risk scores** for disease susceptibility  
✅ **Interpret results** in the context of COVID-19 pathogenesis  

## 🔍 Dataset Information

### Synthetic Dataset Features
- **109 genetic variants** (rs IDs, chromosomal locations, P-values)
- **60 unique genes** from COVID-19 literature
- **Multiple populations**: European, East Asian, Mixed ancestry
- **Disease associations**: Severe COVID-19, ARDS, thrombosis, etc.

### Real Data Integration
The tutorial is designed to work with real data from:
- **COVID-19 Host Genetics Initiative**
- **UK Biobank**
- **Published GWAS studies**

Simply replace the synthetic data loading section with your real dataset!

## Contributing

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) for details.

### Ways to Contribute
- Report bugs or issues
- Suggest new features or analyses
- Improve documentation
- Add real datasets
- Enhance visualizations

## Documentation

- **[Methodology](docs/methodology.md)**: Detailed explanation of computational methods
- **[Troubleshooting](docs/troubleshooting.md)**: Common issues and solutions
- **[API Reference](docs/api_reference.md)**: Function documentation

## Citation

If you use this tutorial in your research or teaching, please cite:

```bibtex
@article{alsaedi2023computational,
  title={Computational network analysis of host genetic risk variants of severe COVID-19},
  author={Alsaedi, Sakhaa B and Mineta, Katsuhiko and Gao, Xin and Gojobori, Takashi},
  journal={Human Genomics},
  volume={17},
  number={1},
  pages={17},
  year={2023},
  publisher={BioMed Central},
  doi={10.1186/s40246-023-00454-y}
}
```

## 🔗 Related Resources

### Databases and Tools
- **[STRING Database](https://string-db.org/)** - Protein-protein interactions
- **[g:Profiler](https://biit.cs.ut.ee/gprofiler/)** - Functional enrichment analysis
- **[COVID-19 HGI](https://www.covid19hg.org/)** - Host genetics data
- **[GTEx Portal](https://gtexportal.org/)** - Gene expression data

### Additional Reading
- **[COVID-19 Host Genetics Initiative](https://www.nature.com/articles/s41586-021-03767-x)** - Nature 2021
- **[Genetic mechanisms of critical illness](https://www.nature.com/articles/s41586-020-03065-y)** - Nature 2021
- **[Inborn errors of type I IFN immunity](https://science.sciencemag.org/content/370/6515/eabd4570)** - Science 2020

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Original Research Team**: Alsaedi, S.B., Mineta, K., Gao, X., Gojobori, T.
- **COVID-19 Host Genetics Initiative** for foundational research
- **Open source community** for excellent Python packages
- **Contributors** who help improve this tutorial

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/yourusername/covid19-genetic-risk-analysis/issues)
- **Discussions**: [GitHub Discussions](https://github.com/yourusername/covid19-genetic-risk-analysis/discussions)
- **Email**: sakhaa.alsaedi@kaust.edu.sa, Sakhaa@deepcares.net

---

⭐ **Star this repository** if you find it useful!

📢 **Share with colleagues** interested in COVID-19 genetics and computational biology!


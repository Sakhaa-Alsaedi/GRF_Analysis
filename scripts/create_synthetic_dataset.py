import pandas as pd
import numpy as np
import random

# Set random seed for reproducibility
np.random.seed(42)
random.seed(42)

# Define lists of realistic genetic data
chromosomes = [f"chr{i}" for i in range(1, 23)] + ["chrX", "chrY"]
functional_consequences = [
    "missense_variant", "synonymous_variant", "intron_variant", 
    "upstream_gene_variant", "downstream_gene_variant", "3_prime_UTR_variant",
    "5_prime_UTR_variant", "splice_region_variant", "regulatory_region_variant"
]

# COVID-19 related genes from literature
covid_genes = [
    "ACE2", "TMPRSS2", "IFNAR2", "TYK2", "OAS1", "OAS2", "OAS3", "IFIH1",
    "IRF7", "IRF3", "STAT1", "STAT2", "IL6", "IL1B", "TNF", "CCL2",
    "CXCL10", "IFNG", "IL10", "IL4", "IL13", "CD14", "TLR3", "TLR7",
    "TLR8", "MYD88", "IRAK4", "IRF8", "NLRP3", "CASP1", "IL18",
    "HMGB1", "S100A8", "S100A9", "LCN2", "RETN", "ADIPOQ", "LEP",
    "CRP", "SAA1", "APOE", "LDLR", "PCSK9", "ANGPT2", "VWF",
    "F8", "SERPINE1", "PLAT", "PLG", "FGB", "FGA", "FGG",
    "PROC", "PROS1", "THBD", "EPCR", "TFPI", "AT3", "PC"
]

# Related diseases
related_diseases = [
    "Severe COVID-19", "Respiratory failure", "ARDS", "Pneumonia",
    "Thrombosis", "Cardiovascular disease", "Diabetes", "Hypertension",
    "Immune deficiency", "Inflammatory response", "Cytokine storm",
    "Sepsis", "Multi-organ failure", "Coagulopathy"
]

# Generate synthetic dataset
def generate_covid_risk_variants(n_variants=109):
    data = []
    
    for i in range(n_variants):
        # Generate rs ID
        rs_id = f"rs{random.randint(1000000, 99999999)}"
        
        # Generate chromosomal location
        chromosome = random.choice(chromosomes)
        position = random.randint(1000000, 200000000)
        location = f"{chromosome}:{position}"
        
        # Generate functional consequence
        consequence = random.choice(functional_consequences)
        
        # Select host gene
        host_gene = random.choice(covid_genes)
        
        # Generate P value (significant variants)
        p_value = np.random.uniform(1e-8, 5e-5)
        
        # Select related disease
        disease = random.choice(related_diseases)
        
        # Generate additional features
        allele_freq = np.random.uniform(0.01, 0.5)
        odds_ratio = np.random.uniform(1.1, 3.5)
        
        data.append({
            'rs_id': rs_id,
            'chromosome': chromosome,
            'position': position,
            'chromosomal_location': location,
            'functional_consequence': consequence,
            'host_gene': host_gene,
            'p_value': p_value,
            'allele_frequency': allele_freq,
            'odds_ratio': odds_ratio,
            'related_disease': disease,
            'study_population': random.choice(['European', 'East Asian', 'Mixed', 'Middle Eastern']),
            'sample_size': random.randint(500, 50000)
        })
    
    return pd.DataFrame(data)

# Generate the dataset
covid_variants_df = generate_covid_risk_variants()

# Save to CSV
covid_variants_df.to_csv('/home/ubuntu/covid19_genetic_risk_variants.csv', index=False)

print(f"Generated dataset with {len(covid_variants_df)} variants")
print(f"Number of unique genes: {covid_variants_df['host_gene'].nunique()}")
print(f"Dataset saved to: /home/ubuntu/covid19_genetic_risk_variants.csv")

# Display first few rows
print("\nFirst 5 rows of the dataset:")
print(covid_variants_df.head())

# Generate gene-level summary
gene_summary = covid_variants_df.groupby('host_gene').agg({
    'rs_id': 'count',
    'p_value': 'min',
    'odds_ratio': 'mean',
    'related_disease': lambda x: ', '.join(x.unique()[:3])
}).rename(columns={'rs_id': 'variant_count'})

gene_summary.to_csv('/home/ubuntu/covid19_gene_summary.csv')
print(f"\nGene summary saved to: /home/ubuntu/covid19_gene_summary.csv")


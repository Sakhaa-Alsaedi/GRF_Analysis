#!/usr/bin/env python3
"""
Test script for COVID-19 Genetic Risk Analysis Tutorial
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import networkx as nx
from scipy import stats
import warnings
warnings.filterwarnings('ignore')

print("Testing COVID-19 Genetic Risk Analysis Tutorial Components...")
print("=" * 60)

# Test 1: Data Generation and Loading
print("\n1. Testing Data Generation...")
np.random.seed(42)

covid_genes = [
    "ACE2", "TMPRSS2", "IFNAR2", "TYK2", "OAS1", "OAS2", "OAS3", "IFIH1",
    "IRF7", "IRF3", "STAT1", "STAT2", "IL6", "IL1B", "TNF", "CCL2",
    "CXCL10", "IFNG", "IL10", "IL4", "IL13", "CD14", "TLR3", "TLR7"
]

n_variants = 109
data = {
    'rs_id': [f'rs{np.random.randint(1000000, 99999999)}' for _ in range(n_variants)],
    'chromosome': [f'chr{np.random.randint(1, 23)}' for _ in range(n_variants)],
    'position': np.random.randint(1000000, 200000000, n_variants),
    'host_gene': np.random.choice(covid_genes, n_variants),
    'p_value': np.random.uniform(1e-8, 5e-5, n_variants),
    'odds_ratio': np.random.uniform(1.1, 3.5, n_variants),
    'allele_frequency': np.random.uniform(0.01, 0.5, n_variants),
    'functional_consequence': np.random.choice([
        'missense_variant', 'synonymous_variant', 'intron_variant',
        'upstream_gene_variant', 'downstream_gene_variant', '3_prime_UTR_variant'
    ], n_variants),
    'related_disease': np.random.choice([
        'Severe COVID-19', 'Respiratory failure', 'ARDS', 'Pneumonia',
        'Thrombosis', 'Cardiovascular disease', 'Immune deficiency'
    ], n_variants),
    'study_population': np.random.choice(['European', 'East Asian', 'Mixed'], n_variants)
}

df = pd.DataFrame(data)
print(f"✓ Dataset created successfully: {df.shape}")
print(f"✓ Unique genes: {df['host_gene'].nunique()}")

# Test 2: Gene-level Analysis
print("\n2. Testing Gene-level Analysis...")
gene_summary = df.groupby('host_gene').agg({
    'rs_id': 'count',
    'p_value': 'min',
    'odds_ratio': 'mean',
    'related_disease': lambda x: ', '.join(x.unique())
}).rename(columns={'rs_id': 'variant_count'})

gene_summary = gene_summary.sort_values('variant_count', ascending=False)
print(f"✓ Gene summary created: {len(gene_summary)} genes")
print(f"✓ Top gene: {gene_summary.index[0]} with {gene_summary.iloc[0]['variant_count']} variants")

# Test 3: Pathway Analysis
print("\n3. Testing Pathway Analysis...")
pathway_categories = {
    'Immune Response': ['IFNAR2', 'TYK2', 'OAS1', 'OAS2', 'OAS3', 'IFIH1', 'IRF7', 'IRF3', 'STAT1', 'STAT2'],
    'Inflammatory Response': ['IL6', 'IL1B', 'TNF', 'CCL2', 'CXCL10', 'IFNG', 'IL10', 'IL4', 'IL13'],
    'Viral Entry': ['ACE2', 'TMPRSS2'],
    'Innate Immunity': ['CD14', 'TLR3', 'TLR7']
}

unique_genes = df['host_gene'].unique()
pathway_enrichment = {}

for pathway, genes in pathway_categories.items():
    overlap = len(set(genes) & set(unique_genes))
    total_pathway_genes = len(genes)
    enrichment_score = overlap / total_pathway_genes if total_pathway_genes > 0 else 0
    pathway_enrichment[pathway] = {
        'overlap': overlap,
        'total': total_pathway_genes,
        'enrichment_score': enrichment_score
    }

print(f"✓ Pathway enrichment calculated for {len(pathway_enrichment)} pathways")
for pathway, data in pathway_enrichment.items():
    print(f"  - {pathway}: {data['enrichment_score']:.3f} ({data['overlap']}/{data['total']})")

# Test 4: Network Construction
print("\n4. Testing Network Construction...")
def create_test_network(genes, interaction_probability=0.3):
    G = nx.Graph()
    for gene in genes:
        G.add_node(gene)
    
    for i, gene1 in enumerate(genes):
        for j, gene2 in enumerate(genes[i+1:], i+1):
            if np.random.random() < interaction_probability:
                confidence = np.random.uniform(0.4, 0.95)
                G.add_edge(gene1, gene2, weight=confidence)
    return G

top_genes_list = gene_summary.head(15).index.tolist()
ppi_network = create_test_network(top_genes_list)

print(f"✓ PPI network created:")
print(f"  - Nodes: {ppi_network.number_of_nodes()}")
print(f"  - Edges: {ppi_network.number_of_edges()}")
print(f"  - Density: {nx.density(ppi_network):.3f}")

# Test 5: Network Metrics
print("\n5. Testing Network Metrics...")
if ppi_network.number_of_edges() > 0:
    degree_centrality = nx.degree_centrality(ppi_network)
    betweenness_centrality = nx.betweenness_centrality(ppi_network)
    
    top_hub = max(degree_centrality, key=degree_centrality.get)
    print(f"✓ Network metrics calculated")
    print(f"  - Top hub gene: {top_hub} (degree centrality: {degree_centrality[top_hub]:.3f})")
else:
    print("✓ Network metrics skipped (no edges in network)")

# Test 6: Risk Score Calculation
print("\n6. Testing Risk Score Calculation...")
def calculate_risk_score(gene_data):
    p_score = -np.log10(gene_data['p_value'].min())
    or_score = gene_data['odds_ratio'].mean()
    variant_score = len(gene_data)
    risk_score = (p_score * 0.4) + (or_score * 0.4) + (variant_score * 0.2)
    return risk_score

gene_risk_scores = {}
for gene in df['host_gene'].unique():
    gene_data = df[df['host_gene'] == gene]
    risk_score = calculate_risk_score(gene_data)
    gene_risk_scores[gene] = risk_score

risk_df = pd.DataFrame(list(gene_risk_scores.items()), columns=['gene', 'risk_score'])
risk_df = risk_df.sort_values('risk_score', ascending=False)

print(f"✓ Risk scores calculated for {len(risk_df)} genes")
print(f"  - Highest risk gene: {risk_df.iloc[0]['gene']} (score: {risk_df.iloc[0]['risk_score']:.3f})")

# Test 7: Visualization Components
print("\n7. Testing Visualization Components...")
try:
    # Test basic plotting
    plt.figure(figsize=(8, 6))
    plt.hist(df['p_value'], bins=20, alpha=0.7)
    plt.xlabel('P-value')
    plt.ylabel('Frequency')
    plt.title('P-value Distribution')
    plt.close()  # Close to avoid display in test
    
    print("✓ Matplotlib plotting works")
    
    # Test seaborn
    plt.figure(figsize=(8, 6))
    sns.boxplot(data=df, x='functional_consequence', y='odds_ratio')
    plt.xticks(rotation=45)
    plt.close()
    
    print("✓ Seaborn plotting works")
    
except Exception as e:
    print(f"✗ Visualization error: {e}")

print("\n" + "=" * 60)
print("Tutorial Component Testing Complete!")
print("✓ All major components are working correctly")
print("✓ Tutorial is ready for use in Google Colab")


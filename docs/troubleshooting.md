# Troubleshooting Guide

## Common Issues and Solutions

### Installation Issues

#### 1. Package Installation Errors

**Problem**: `pip install` fails with permission errors
```bash
ERROR: Could not install packages due to an EnvironmentError: [Errno 13] Permission denied
```

**Solutions**:
```bash
# Option 1: Use --user flag
pip install --user -r requirements.txt

# Option 2: Use virtual environment (recommended)
python -m venv covid19_env
source covid19_env/bin/activate  # On Windows: covid19_env\Scripts\activate
pip install -r requirements.txt

# Option 3: Use conda
conda create -n covid19_env python=3.8
conda activate covid19_env
pip install -r requirements.txt
```

#### 2. NetworkX Installation Issues

**Problem**: NetworkX fails to install or import
```python
ModuleNotFoundError: No module named 'networkx'
```

**Solutions**:
```bash
# Try different installation methods
pip install networkx
# or
conda install networkx
# or
pip install networkx --upgrade
```

#### 3. Plotly Display Issues

**Problem**: Plotly plots not displaying in Jupyter
```python
# Plots appear blank or don't render
```

**Solutions**:
```python
# Install Jupyter extensions
pip install "notebook>=5.3" "ipywidgets>=7.2"

# Enable extensions
jupyter nbextension enable --py widgetsnbextension

# For JupyterLab
pip install jupyterlab "ipywidgets>=7.5"
jupyter labextension install jupyterlab-plotly

# Alternative: Use static plots
import plotly.io as pio
pio.renderers.default = "png"  # or "svg", "pdf"
```

### Google Colab Issues

#### 1. File Upload Problems

**Problem**: Cannot upload CSV files to Colab
```python
FileNotFoundError: [Errno 2] No such file or directory: 'data.csv'
```

**Solutions**:
```python
# Method 1: Use file upload widget
from google.colab import files
uploaded = files.upload()

# Method 2: Mount Google Drive
from google.colab import drive
drive.mount('/content/drive')
# Then access files from /content/drive/MyDrive/

# Method 3: Download from URL
import pandas as pd
url = "https://raw.githubusercontent.com/username/repo/main/data/file.csv"
df = pd.read_csv(url)
```

#### 2. Runtime Disconnection

**Problem**: Colab runtime disconnects during long computations
```
Your session crashed after using all available RAM
```

**Solutions**:
```python
# Reduce dataset size
df_sample = df.sample(n=1000)  # Use smaller sample

# Clear variables periodically
del large_variable
import gc
gc.collect()

# Use Colab Pro for more RAM
# Or process data in chunks
```

#### 3. Package Version Conflicts

**Problem**: Package versions incompatible in Colab
```python
ImportError: cannot import name 'something' from 'package'
```

**Solutions**:
```python
# Check versions
import package_name
print(package_name.__version__)

# Force reinstall specific version
!pip install package_name==1.2.3 --force-reinstall

# Restart runtime after installation
# Runtime -> Restart runtime
```

### Data Issues

#### 1. CSV Loading Errors

**Problem**: Pandas cannot read CSV file
```python
UnicodeDecodeError: 'utf-8' codec can't decode byte
```

**Solutions**:
```python
# Try different encodings
df = pd.read_csv('file.csv', encoding='latin-1')
# or
df = pd.read_csv('file.csv', encoding='cp1252')

# Handle malformed lines
df = pd.read_csv('file.csv', error_bad_lines=False, warn_bad_lines=True)

# Specify separator if needed
df = pd.read_csv('file.csv', sep=';')  # or '\t' for tab-separated
```

#### 2. Missing Data Handling

**Problem**: Analysis fails due to missing values
```python
ValueError: Input contains NaN, infinity or a value too large
```

**Solutions**:
```python
# Check for missing values
print(df.isnull().sum())

# Remove rows with missing values
df_clean = df.dropna()

# Fill missing values
df['column'] = df['column'].fillna(df['column'].mean())  # numerical
df['column'] = df['column'].fillna('Unknown')  # categorical

# Remove infinite values
df = df.replace([np.inf, -np.inf], np.nan).dropna()
```

#### 3. Data Type Issues

**Problem**: Incorrect data types causing analysis errors
```python
TypeError: unsupported operand type(s) for /: 'str' and 'int'
```

**Solutions**:
```python
# Check data types
print(df.dtypes)

# Convert data types
df['p_value'] = pd.to_numeric(df['p_value'], errors='coerce')
df['chromosome'] = df['chromosome'].astype('category')

# Handle scientific notation
df['p_value'] = df['p_value'].apply(lambda x: float(x) if isinstance(x, str) else x)
```

### Network Analysis Issues

#### 1. Empty Networks

**Problem**: Network has no edges
```python
NetworkXError: Graph has no edges
```

**Solutions**:
```python
# Check if network has edges
if G.number_of_edges() == 0:
    print("Network is empty - adjusting parameters")
    
# Lower interaction threshold
interaction_threshold = 0.1  # instead of 0.9

# Add edges manually if needed
G.add_edge('gene1', 'gene2', weight=0.5)

# Check input data
print(f"Number of genes: {len(gene_list)}")
print(f"Gene list: {gene_list}")
```

#### 2. Memory Issues with Large Networks

**Problem**: Out of memory errors with large networks
```python
MemoryError: Unable to allocate array
```

**Solutions**:
```python
# Reduce network size
top_genes = gene_summary.head(50)  # Use fewer genes

# Use sparse matrices
import scipy.sparse as sp
adjacency_sparse = nx.adjacency_matrix(G, format='csr')

# Process in chunks
def process_network_chunks(genes, chunk_size=20):
    for i in range(0, len(genes), chunk_size):
        chunk = genes[i:i+chunk_size]
        # Process chunk
        yield chunk
```

#### 3. Centrality Calculation Errors

**Problem**: Centrality measures fail for disconnected graphs
```python
NetworkXError: Graph not connected
```

**Solutions**:
```python
# Check connectivity
if not nx.is_connected(G):
    # Get largest connected component
    largest_cc = max(nx.connected_components(G), key=len)
    G_connected = G.subgraph(largest_cc).copy()
    
# Use appropriate centrality measures
if nx.is_connected(G):
    centrality = nx.betweenness_centrality(G)
else:
    centrality = nx.degree_centrality(G)  # Works for disconnected graphs
```

### Visualization Issues

#### 1. Matplotlib Backend Problems

**Problem**: Plots not displaying
```python
UserWarning: Matplotlib is currently using agg, which is a non-GUI backend
```

**Solutions**:
```python
# Set backend explicitly
import matplotlib
matplotlib.use('TkAgg')  # or 'Qt5Agg'
import matplotlib.pyplot as plt

# For Jupyter notebooks
%matplotlib inline
# or
%matplotlib widget

# Force display
plt.show()
```

#### 2. Font Issues

**Problem**: Missing fonts or encoding errors in plots
```python
UserWarning: Glyph missing from current font
```

**Solutions**:
```python
# Set font explicitly
plt.rcParams['font.family'] = 'DejaVu Sans'

# For special characters
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']

# Clear font cache
import matplotlib.font_manager
matplotlib.font_manager._rebuild()
```

#### 3. Plot Size and Layout Issues

**Problem**: Plots too small or overlapping elements
```python
# Labels cut off or overlapping
```

**Solutions**:
```python
# Adjust figure size
plt.figure(figsize=(12, 8))

# Adjust layout
plt.tight_layout()

# Adjust margins
plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)

# Rotate labels
plt.xticks(rotation=45, ha='right')

# Use constrained layout
fig, ax = plt.subplots(constrained_layout=True)
```

### Performance Issues

#### 1. Slow Network Analysis

**Problem**: Network calculations taking too long
```python
# Code runs for hours without completing
```

**Solutions**:
```python
# Use approximate algorithms
centrality = nx.degree_centrality(G)  # Faster than betweenness

# Parallel processing
from multiprocessing import Pool
import networkx as nx

def calculate_centrality_parallel(G):
    # Use parallel algorithms where available
    return nx.betweenness_centrality(G, k=100)  # Sample nodes

# Reduce precision
centrality = {node: round(cent, 3) for node, cent in centrality.items()}
```

#### 2. Memory Optimization

**Problem**: High memory usage
```python
# Process uses too much RAM
```

**Solutions**:
```python
# Use generators instead of lists
gene_pairs = ((g1, g2) for g1 in genes for g2 in genes if g1 != g2)

# Delete unused variables
del large_dataframe
import gc
gc.collect()

# Use data types efficiently
df['category'] = df['category'].astype('category')  # Save memory
df['small_int'] = df['small_int'].astype('int8')   # Use smaller int types
```

## Getting Help

### 1. Check Documentation
- Read the methodology document
- Review function docstrings
- Check package documentation

### 2. Search Issues
- GitHub Issues page
- Stack Overflow
- Package-specific forums

### 3. Create Minimal Example
```python
# When reporting issues, provide minimal reproducible example
import pandas as pd
import networkx as nx

# Minimal data
data = {'gene': ['A', 'B'], 'value': [1, 2]}
df = pd.DataFrame(data)

# Minimal code that fails
# ... your problematic code here ...
```

### 4. Include System Information
```python
import sys
import pandas as pd
import networkx as nx

print(f"Python version: {sys.version}")
print(f"Pandas version: {pd.__version__}")
print(f"NetworkX version: {nx.__version__}")
```

## Best Practices

### 1. Environment Management
- Always use virtual environments
- Pin package versions in requirements.txt
- Document your environment setup

### 2. Data Validation
- Always check data types and ranges
- Validate input parameters
- Handle edge cases gracefully

### 3. Error Handling
```python
try:
    result = risky_operation()
except SpecificError as e:
    print(f"Expected error occurred: {e}")
    # Handle gracefully
except Exception as e:
    print(f"Unexpected error: {e}")
    # Log and investigate
```

### 4. Testing
- Test with small datasets first
- Validate results against known examples
- Use unit tests for custom functions

Remember: Most issues can be resolved by carefully reading error messages and checking the documentation!


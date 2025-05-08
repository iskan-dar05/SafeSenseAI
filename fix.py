import nbformat

path = "SafeSensAI.ipynb"  # adjust if different
nb = nbformat.read(path, as_version=4)

# Fix: Remove invalid 'widgets' metadata
if 'widgets' in nb['metadata']:
    print("Removing corrupted widgets metadata...")
    del nb['metadata']['widgets']

nbformat.write(nb, path)
print(f"✅ Fixed notebook saved at: {path}")

#!/bin/bash
echo "setting up project environment..."

# create directories
mkdir -p src data output
echo "directories created"

# create .gitignore
cat > .gitignore << 'EOF'
# python
__pycache__/
*.pyc
.venv/

# mac os files
.DS_store
EOF
echo ".gitignore created"

# create requirements.txt
cat > requirements.txt << 'EOF'
# no external packages required
pytest>=7.0.0
EOF
echo "requirements.txt created"

# create sample students.csv
cat > data/students.csv << 'EOF'
name,age,grade,subject
Alice,15,85,Math
Bella,14,90,Science
Carlos,16,78,History
Dina,15,92,English
Emil,16,88,Math
Fatima,14,76,Science
Henry,15,84,History
Isla,16,95,Math
EOF
echo "students.csv created"

# create python template for basic analysis
cat > src/data_analysis.py << 'EOF'
# data_analysis.py
# TODO: add basic data analysis code here

def main():
    # TODO: implement program logic
    pass

if __name__ == "__main__":
    main()
EOF

# create python template for advanced analysis
cat > src/data_analysis_functions.py << 'EOF'
# data_analysis_functions.py
# TODO: add advanced data analysis code here

def main():
    # TODO: implement program logic
    pass

if __name__ == "__main__":
    main()
EOF

echo "setup_project.sh complete!"

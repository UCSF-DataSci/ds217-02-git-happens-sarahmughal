#!/bin/bash
echo "set up project environment"

# create directories
mkdir -p src data output
echo "directories created"

# create .gitignore
cat > .gitignore << 'EOF'
__pycache__/
*.pyc
EOF
echo ".gitignore created"

# create requirements.txt
cat > requirements.txt << 'EOF'
# core python packages (built-in, no external dependencies required)
# testing framework: pytest>=7.0.0
EOF
echo "requirements.txt created"

# create sample students.csv
cat > data/students.csv << 'EOF'
name,age,grade,subject
alex,15,85,math
bella,14,90,science
carlos,16,78,history
dina,15,92,english
emil,16,88,math
fatima,14,76,science
henry,15,84,history
isla,16,95,math
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

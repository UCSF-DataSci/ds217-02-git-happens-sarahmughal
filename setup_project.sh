#!/bin/bash
echo "set up project environment"

# create directories
mkdir -p src data output
echo "create directories"

# create .gitignore
cat > .gitignore <<EOL
__pycache__/
*.pyc
output/
EOL
echo "create .gitignore"

# create requirements.txt
cat > requirements.txt <<EOL
# no external packages required
EOL
echo "create requirements.txt"

# create sample students.csv (8+ records)
cat > data/students.csv <<EOL
name,age,grade,subject
george,15,85,math
hannah,14,90,science
ian,16,78,history
jane,15,92,english
gal,16,88,math
ariel,14,76,science
kathy,15,84,history
leo,16,95,math
EOL
echo "create students.csv"

# create Python template files
cat > src/data_analysis.py <<EOL
# data_analysis.py
# TODO: implement main entry point

def main():
    # TODO: implement program logic
    pass

if __name__ == "__main__":
    main()
EOL

cat > src/data_analysis_functions.py <<EOL
# data_analysis_functions.py
# TODO: add helper functions here
EOL

echo "python template files created"
echo "project environment setup complete!"

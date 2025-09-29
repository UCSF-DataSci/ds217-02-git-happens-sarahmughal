#!/bin/bash
echo "set up project environment"

# create directories
mkdir -p src data output
echo "create directories"

# create sample students.csv (8+)
cat > data/students.csv <<EOL
name,age,grade,subject
alex,15,85,math
bella,14,90,science
carlos,16,78,history
dina,15,92,english
emil,16,88,math
fatima,14,76,science
henry,15,84,history
isla,16,95,math
EOL
echo "create students.csv"

# create python template files
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

echo "setup_project.sh complete!"